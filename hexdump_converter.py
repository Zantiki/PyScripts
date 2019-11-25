
def convert(input_file):
    name = input_file.split(".")
    output_file = "{}.{}-expanded.{}".format(name[0], name[1], name[2])

    try:
        reader = open(name, "r", encoding="UTF-8")
        input_lines = []
        output_lines = []

        for line in reader:
            input_lines.append(line)

        end = get_address(input_lines[len(input_lines)-1])
        cur_line = get_address(input_lines[0])
        i = 0

        while cur_line < end:
            if input_lines[i] == "*":
                repetitions = get_address(input_lines[i+1])-get_address(input_lines[i-1])
                for rep in range(repetitions):
                    new_adress = get_address(input_lines[i-1])+rep
                    data_list = input_lines[i-1].split(" ")
                    data_list[0] = new_adress
                    new_line = data_list.join(" ")
                    output_lines.append(new_line)
                cur_line = get_address(input_lines[i+1])
                i += 1
            else:
                output_lines.append(input_lines[i])
                cur_line = get_address(input_lines[i])
                i += 1


        writer = output_file.open(output_file, "w")

        for lines in output_lines:
            writer.write(line)

        writer.close()
        reader.close()


    except IOError:
        print("Error while reading file")






def get_address(tot_string):
    return convert_hex_decimal(tot_string.split(" ")[0])

def convert_hex_decimal(hex_string):
    return int(hex_string, 16)

def convert_decimal_hex(number):
    return hex(number)











if __name__ == '__main__':
    print("Are the files equal?: {}".format(filecmp.cmp("in/opg12.txt", "in/opg12_decoded.txt")))