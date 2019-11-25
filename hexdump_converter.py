import filecmp
import sys


def clean(string):
    # List of redundant characters
    to_remove = ["\n"]
    chars = list(string)
    for char in to_remove:
        # Remove the char from our list if it exists
        if chars.__contains__(char):
            chars.remove(char)
    # Join each char on a blank string and switch to lowercase
    return "".join(chars).lower()


def convert(input_file):
    name = input_file.split(".")
    output_file = "{}.{}-expanded.{}".format(name[0]+"2", name[1], name[2])

    try:
        reader = open(input_file, "r", encoding="UTF-8")
        input_lines = []
        output_lines = []

        for line in reader:
            line = clean(line)
            input_lines.append(line)
        cur_line = get_address(input_lines[0])
        end = get_address(input_lines[len(input_lines)-1])
        i = 0
        data_length = 2*(len(input_lines[0].split(" "))-1)

        while cur_line < end:
            if input_lines[i] == "*":
                repetitions = get_address(input_lines[i+1])-get_address(input_lines[i-1])
                repetitions = int(repetitions / data_length)-1
                for rep in range(repetitions):
                    #if rep != 0:
                    new_adress = get_address(input_lines[i-1])+((rep+1)*data_length)
                    data_list = input_lines[i-1].split(" ")
                    address_length = len(list(data_list[0]))
                    data_list[0] = convert_decimal_hex(new_adress, address_length)
                    new_line = " ".join(data_list)
                    output_lines.append(new_line)
                cur_line = get_address(input_lines[i+1])
                i += 1
            else:
                output_lines.append(input_lines[i])
                cur_line = get_address(input_lines[i])
                i += 1

        output_lines.append(input_lines[len(input_lines)-1])
        writer = open(output_file, "w")

        for line in output_lines:
            writer.writelines(line+"\n")

        writer.close()
        reader.close()


    except IOError:
        print("Error while reading file")


def get_address(tot_string):
    return convert_hex_decimal(tot_string.split(" ")[0])

def convert_hex_decimal(hex_string):
    return int(hex_string, 16)

def convert_decimal_hex(number, address_length):
    value = str(hex(number))
    char_arr = list(value)
    char_arr.remove("x")

    while len(char_arr) < address_length:
        char_arr.insert(0, "0")
    return "".join(char_arr)

def main(arg):
    convert(arg)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(sys.argv[1])
        main(sys.argv[1])
        convert("in/test.bin.hex")
        try:
            #testing only
            print("Are the files equal?: {}".format(filecmp.cmp("in/test.bin-expanded.hex", "in/test2.bin-expanded.hex")))
        except FileExistsError:
            print("Could not find testfiles")
    else:
        print("please specify hex-file")
