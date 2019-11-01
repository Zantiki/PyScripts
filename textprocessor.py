from pathlib import Path
import os


def search(filename):
    """
    Method to search the current working directory for a file with a given filename
    :param filename: the name of the file you want to look for
    :return: returns: the path of the file if it exists
    """
    # Get the path of the current working directory
    if Path(filename).exists():
        return Path(filename)

    p = Path(os.getcwd())

    # Walk the directory tree
    for root, dirs, files in os.walk(p):
        # Check if a given file exists within a directory.
        # Strictly speaking not necessary, since we can just check each file in the tree,
        # but it shows usage of the path object.
        for directory in dirs:
            # Generate and test the path
            q = Path(root) / Path(directory) / filename
            if q.exists():
                return q
    return


def clean(string):
    """
    Method that removes redundant chars from a given string
    :param string: The string to clean.
    :return: a cleaned String.
    """
    # List of redundant characters
    to_remove = [",", ".", ":", ";", "\n", "(", ")", "?", " "]
    chars = list(string)
    for char in to_remove:
        # Remove the char from our list if it exists
        if chars.__contains__(char):
            chars.remove(char)
    # Join each char on a blank string and switch to lowercase
    return "".join(chars).lower()


def get_words_line(filename, search_word):
    """
    Generate a list of every line an instance of a given search word is present.
    :param filename: the name of the file you want to "scan"
    :param search_word: the word you want to "scan" for
    :return lines_where_found: returns a list of integers referring to the a line where the word was found
    """
    path = search(filename)
    lines_where_found = []
    # Index to keep an overview of what line we are referring to
    i = 0
    print("file@: {}".format(path))
    if path is not None:
        file = open(path, "r", encoding="utf8")
        for line in file:
            words = line.split(" ")
            i += 1
            for word in words:
                word = clean(word)
                if word == search_word:
                    # Append the line-index if the word is found there
                    lines_where_found.append(i)
        file.close()
    return lines_where_found


def get_word_freqs(filename):
    """
    Returns a dictionary of all the words in a given file and their frequencies
    :param filename: the file you wish to generate the dictionary from.
    :return dictionary:  a dictionary where the individual words are the keys and frequencies the value
    """
    path = search(filename)
    # An empty dictionary
    dictionary = dict()
    print("file@: {} ".format(path))
    if path is not None:
        file = open(path, "r", encoding="utf8")
        for line in file:
            # Separate our lines on every blank-space
            words = line.split(" ")
            # Iterate through each word in our line and clean them
            for word in words:
                word = clean(word)
                if word != "":
                    # Add the word to our dictionary and increment its value if it already exists
                    dictionary.update({word: dictionary.setdefault(word, 0)+1})
        file.close()
    return dictionary


print("----Find the frequency of a certain word----")

input_filename = input("The file you want to scan (Has to be somewhere within current working directory or an absolute path): ")
key = input("The word you want to find the frequency of: ")

# Generate a dictionary
word_dictionary = get_word_freqs(input_filename)

# get_word_freqs returned None so the file does not exist.
if not word_dictionary:
    print("Dictionary is None, file does not exist")
# Print the key and its value if it exists
elif key.lower() in word_dictionary:
    to_print = "key '{}', value '{}'".format(key, word_dictionary[key])
    print(to_print)
else:
    print("Word is not present in document, please try something else")

print("\n----Find the number of lines a word is present in----")

input_filename = input("The file you want to scan (Has to be somewhere within current working directory or an absolute path): ")
input_word = input("The word you want to find each line for: ")

# Generate our list
test_list = get_words_line(input_filename, input_word.lower())
y = 0

# Count the amount of lines the word exists in.
for line_element in test_list:
    y += 1
to_print_two = "The word '{}' is present in {} lines".format(input_word, y)

# Print the list findings.
print(to_print_two)
