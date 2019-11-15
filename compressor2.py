import filecmp
import struct
import os

def longest_str(search, look_ahead):
    # Keep track of the length of search and buffer
    ls = len(search)
    llh = len(look_ahead)


    # Handle edge cases
    if (ls == 0):
        return (0, 0, look_ahead[0])

    if (llh) == 0:
        return (-1, -1, -1)

    best_length = 0
    best_offset = 0

    # Set the entire window
    buf1 = search + look_ahead

    # Points to the beginning of lhbuffer
    search_pointer = ls

   # Search for the longest common substring of bytes
    for i in range(0, ls):
        # Loop through each element in search
        length = 0
        # Increment the length while the byte sequence in the search and lhbuffer match
        while buf1[i + length] == buf1[search_pointer + length]:
            length = length + 1

            # Reached end of window
            if search_pointer + length == len(buf1):
                length = length - 1
                break
            # Break if repeating sequence leaks into lhbuffer
            if i + length >= search_pointer:
                break
        # Check if there is any improvent to best_length in this iteration of the loop and make the necessary changes
        if length > best_length:
            best_offset = i
            best_length = length
    # Return the index, length of the best result and the char following the lookahead-buffer
    return (best_offset, best_length, buf1[search_pointer + best_length])


def compress(name):

    # Max size of search
    MAXSEARCH = 3000

    # Max size of look-ahead buffer
    MAXLH = 1000

    # Open the file we want to write the compression to
    f = open(name, "rb")
    input = f.read()

    # Reformat the file-type
    compressed_name = name.split(".")
    compressed_name[1] = "bin"
    compressed_name = compressed_name[0]+"."+compressed_name[1]
    out = open(compressed_name, "wb")

    # Pointer for search
    searchiterator = 0


    #Pointer for position of the buffer start
    lhiterator = 0

    # While buffer-pointer has not reached end, do encoding.
    while lhiterator < len(input):
        # Set position in our data
        search = input[searchiterator:lhiterator]
        look_ahead = input[lhiterator:lhiterator + MAXLH]

        # Get position, length and next char outside of repeating sequence.
        (offset, length, char) = longest_str(search, look_ahead)

        # Pack the triple as one short and two unsigned chars(represented as ints?) and one short
        ol_bytes = struct.pack("hBB", offset, length, char)
        # Write the encoded data to the file
        out.write(ol_bytes)

        # Move the window (search and lookahead) forwards
        lhiterator = lhiterator + length + 1
        searchiterator = lhiterator - MAXSEARCH

        # Make sure the searchpointer never goes below zero
        if searchiterator < 0:
            searchiterator = 0

    f.close()
    out.close()


def decode(name, f_type):

    MAX_SEARCH = 3000

    # Reformat the file, read the data and open the our decoded variant
    file = open(name, "rb")
    input = file.read()
    name_list = name.split(".")
    out = open(name_list[0] + "_decoded." + f_type, "wb")

    # The array for decoded bytes that we wish to append to our decoded file
    read = bytearray()

    # Keeps track of our byte position
    i = 0
    # Count the amount of decoded touples for debugging purposes
    totalTups = 0
    # Loop through every single byte
    while i < len(input):
        # Unpack the tuple for every 4 bytes
        # unPack the tuple as one short and two unsigned chars(represented as ints?) and one short
        (offset, length, next_byte) = struct.unpack("hBB", input[i:i + 4])

        # Incremet the tups counter
        totalTups += 1

        # Increment out bytepointer by 4
        i = i + 4
        # Take care of cases where the offset or length of repeating sequence is 0.
        if (offset == 0) and (length == 0):
            read.append(next_byte)


        else:
            # iterator represents the beginning of the window
            iterator = len(read) - MAX_SEARCH
            if iterator < 0:
                iterator = offset
            else:
                # Shift to the repeating sequence
                iterator += offset
                # Write the repeating sequence
            for pointer in range(length):
                # Append the repeats to file
                read.append(read[iterator + pointer])
            # Add the next char in the buffer to the data.
            read.append(next_byte)

    # Write the entire decode to our output file.
    out.write(read)

    # The size of the decoded file
    print("size of decoded file: {} bytes".format(len(read)))
    # The size of the encoded file
    print("size of encoded file: {} bytes".format(i))
    # The total amount of encoded tuples
    print("Total amount of tuples inside encoded file: {}".format(totalTups))
    print("Percentage saved {}%".format(100-round(i*100/len(read))))
    file.close()
    out.close()


if __name__ == '__main__':
    print("Compressing")
    compress("in/opg12.txt")

    print("Decompressing")
    decode("in/opg12.bin", "txt")
    print("Are the files equal?: {}".format(filecmp.cmp("in/opg12.txt", "in/opg12_decoded.txt")))