from collections import defaultdict

count_dict = defaultdict(int)

with open('sample_strain_out', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line_list = line.split('\t')
        line_info = line_list[0] + "\t" + line_list[1]
        count_dict[line_info] += int(line_list[2])


for line in count_dict:
    print(line, count_dict[line])
