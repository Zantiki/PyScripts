

def lexi_greater(string1, string2):
    """
    Function for determining whether or not a string has a greater
    lexicographic order.
    :param string1: the string we wish to compare with string1
    :param string2: the string we wish to compare with string2
    :return True/False: Indicating a difference in lexicographic value.
    """
    # Iterate through the chars in each string until we can return a lexicographic difference.
    for c1, c2 in zip(string1, string2):
        if c1 == c2:
            continue
        if c1 > c2:
            return True
        else:
            return False


def compare_strings(string1, string2):
    """
    Function for determining whether or not string1 should be replaced with string2
    :param string1: the string we wish to compare with string2
    :param string2: the string we wish to compare with string1
    :return True/False: a boolean value indicating a difference in size or lexicographic value
    """
    item1 = list(string1)
    item2 = list(string2)
    # If the strings are of equal length we compare them lexicographically
    if len(item1) == len(item2):
        return lexi_greater(item1, item2)
    else:
        if len(item1) > len(item2):
            return True
        else:
            return False


def insertion_sort(string_list):
    """
    Simple insertion sort function for sorting a list of strings
    :param string_list: The list we wish to sort
    """
    j = 1
    while j < len(string_list):
        swap = string_list[j]
        # Increment/define our inner(i)/outer(j) loop indexes.
        i = j - 1
        j += 1
        # Loop that swaps the list elements if string_list[i] is greater than string_list[j]
        while i >= 0 and compare_strings(string_list[i], swap):
            # Move the i element one place up
            string_list[i + 1] = string_list[i]
            i -= 1
        # Set the old i element to the one we wanted to swap with
        string_list[i + 1] = swap


def create_list(filename):
    """
    Method for reading a list of strings from a file and generate
    a list based on said strings. The file needs to be an absolute path
    or in the current directory.
    :param filename: the name of the file we wish to "scan"
    :return gen_list: the list of strings generated from the file provided.
    """
    gen_list = []
    try:
        file = open(filename, "r")
        text = file.readlines()
        # The text has one line, and we separate the line into words, these words will be our strings.
        if len(text) == 1:
            # Remove newline symbols from the line
            gen_list = text[0].replace("\n", "").split(" ")
            return gen_list
        # The text has several lines, and we use the lines as our strings.
        else:
            for line in text:
                gen_list.append(line.replace("\n", ""))
            return gen_list
    except FileNotFoundError:
        print("File Not Found")


def run(filename):
    """Function for creating a list, printing it, sorting it
    and finally print the sorted result """
    gen_list = create_list(filename)
    if gen_list is None:
        print("Cannot find file")
    else:
        print("\n---Generated list---")
        print(gen_list)
        print("\n---Sorted list---")
        insertion_sort(gen_list)
        print(gen_list)


name = input("The file you wish to sort: ")
run(name)







