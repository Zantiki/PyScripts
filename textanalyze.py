

def analyse(filename):
    """
    A method for analysing a text-file, see return-statement for more details
    :param filename: the name of the file you wish analyse
    :return: A string with the data found
    """
    # Lists and variables keeping track of the values.
    sentence_lengths = []
    # Add the first line to out blank_spaces list
    blank_spaces = [0]
    word_dict = dict()
    line_counter = 0

    try:
        # Open the file to readonly
        file = open(filename, "r", encoding="utf8")
        # Iterate through the lines in the file.
        for line in file:

            # If we reach a lonely newline, we know we are dealing with a paragraph
            if line == "\n":
                blank_spaces.append(line_counter)

            if line != "\n":
                line = clean(line)
                # Seperate a line into words, and append the total amount of words.
                words_in_line = line.split(" ")
                sentence_lengths.append(len(words_in_line))
                for word in words_in_line:
                    # Update the dictionary and increment the value if need be.
                    word_dict.update({word: word_dict.setdefault(word, 0)+1})
                # Only increment the counter if the line is not a linebreak
                line_counter += 1

        # Push the final line-index to blank-spaces as we assume this is a paragraph
        # This would also take care of the problem with a single paragraph text.
        blank_spaces.append(line_counter)
        file.close()
        # Create variables based on the functions for clarity
        avg_length_line = get_avg_length_line(sentence_lengths)
        avg_length_paragraph = get_avg_length_paragraph(blank_spaces)
        percentage_different = get_different(sum(sentence_lengths), word_dict)
        easy_diff = get_diff_easy(word_dict)

        return "1: Average line length {}, 2: % of difficult words {}% , " \
               "3: % of easy words {}%, 4: % of different words {}%, 5: Average length of each paragraph {}"\
            .format(avg_length_line, easy_diff[0], easy_diff[1], percentage_different, avg_length_paragraph)
    except FileNotFoundError:
        return "File does not exist"


def get_avg_length_line(line_list):
    # The average length of a line is the total amount of words over the total amount of lines
    total = sum(line_list)
    return round(total / len(line_list))


def get_different(tot_words, word_dictionary):
    # We subtract one because we want a file containing 1 word to return 0%
    unique_words = len(word_dictionary)-1
    return round(unique_words / tot_words, 2)*100


def get_diff_easy(word_dictionary):
    # Find the average frequency of of every word
    avg_frequency = sum(word_dictionary.values()) / len(word_dictionary)
    total_words = len(word_dictionary)
    diff_count = 0
    easy_count = 0
    for value in word_dictionary.values():
        # If the value is 1/4 of the average add it to the difficult ones
        if value <= 0.25 * avg_frequency:
            diff_count += 1

        # If the value is 6/4 of the average add it to the easy ones
        elif value >= 1.5 * avg_frequency:
            easy_count += 1
    return round(diff_count/total_words, 2)*100, round(easy_count/total_words, 2)*100


def clean(string):
    # List of redundant characters
    to_remove = [",", ".", ":", ";", "\n", "(", ")", "?", " "]
    chars = list(string)
    for char in to_remove:
        # Remove the char from our list if it exists
        if chars.__contains__(char):
            chars.remove(char)
    # Join each char on a blank string and switch to lowercase
    return "".join(chars).lower()


def get_avg_length_paragraph(paragraph_list):
    paragraph_lengths = []
    current_index = 0
    next_index = 1

    # Append the difference between the lines with linebreaks in between
    while next_index < len(paragraph_list):
        paragraph_lengths.append(paragraph_list[next_index]-paragraph_list[current_index])
        current_index += 1
        next_index += 1

    # Subtract 1 to adjust for the total amount of linebreaks
    total_paragraphs = len(paragraph_list)-1
    if total_paragraphs != 0:
        return round((sum(paragraph_lengths)) / total_paragraphs, 2)
    else:
        return 1


def main():
    print(analyse("sorttest.txt"))


if __name__ == "__main__":
    main()




