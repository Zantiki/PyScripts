

def analyse(filename):
    file = None
    sentence_lengths = []
    blank_spaces = []
    word_dict = dict()
    line_counter = 0
    word_counter = 0
    prev_line = ""

    try:
        file = open(filename, "r", encoding="utf8")
        words_in_line = []
        file_size = sum(1 for line in file)
        file.close()
        file = open(filename, "r", encoding="utf8")
        for line in file:

            if find_paragraph(line, prev_line):
                blank_spaces.append(line_counter)
            line.upper()

            if line != "\n":
                words_in_line = line.split(" ")
                sentence_lengths.append(len(words_in_line))
                for word in words_in_line:
                    word_dict.update({word: word_dict.setdefault(word, 0)+1})
                prev_line = line
                line_counter += 1

        file.close()
        avg_length_line = get_avg_length_line(sentence_lengths)
        avg_length_paragraph = get_avg_length_paragraph(blank_spaces, line_counter)
        percentage_different = get_different(sum(sentence_lengths), word_dict)
        easy_diff = get_diff_easy(word_dict)

        return "1: Average line length {}, 2: % of difficult words {}% , " \
               "3: % of easy words {}%, 4: % of different words {}%, 5: Average length of each paragraph {}"\
            .format(avg_length_line, easy_diff[0], easy_diff[1], percentage_different, avg_length_paragraph)
    except FileNotFoundError:
        return "File does not exist"


def get_avg_length_line(line_list):
    total = sum(line_list)
    list_length = len(line_list)
    return round(total / list_length)


def get_different(tot_words, word_dictionary):
    unique_words = len(word_dictionary)
    return round(unique_words / tot_words, 2)*100


def get_diff_easy(word_dictionary):
    avg_frequency = sum(word_dictionary.values()) / len(word_dictionary)
    total_words = len(word_dictionary)
    diff_count = 0
    easy_count = 0
    for value in word_dictionary.values():
        if value <= 0.25 * avg_frequency:
            diff_count += 1

        elif value >= 1.5 * avg_frequency:
            easy_count += 1
    return round(diff_count/total_words, 2)*100, round(easy_count/total_words, 2)*100


def get_avg_length_paragraph(paragraph_list, total_lines):
    paragraph_lengths = []
    next_index = 0
    current_index = 0

    while current_index < len(paragraph_list)-1:
        if paragraph_list[current_index] != 0 or paragraph_list[current_index] != total_lines-1:
            next_index = current_index + 1
            paragraph_lengths.append(paragraph_list[next_index]-paragraph_list[current_index])
            current_index += 1

    total_paragraphs = len(paragraph_list) +1
    if total_paragraphs != 0:
        return round(total_lines / total_paragraphs, 2)
    else:
        return 1


def find_paragraph(line, prev_line):
    if (line == "\n" and prev_line.find("\n") != -1) or prev_line == "\n":
        return True
    return False


print(analyse("sorttest.txt"))



