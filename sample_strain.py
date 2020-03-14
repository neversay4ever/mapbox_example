from collections import defaultdict

sample_dict = defaultdict(list)
strain_dict = defaultdict(list)

with open('sample', 'r') as sample_file:
    sample_lines = sample_file.readlines()
    for line in sample_lines:
        line = line.strip()
        line_str = line.split("\t")
        sample_dict[line_str[2]] = line

with open('strain', 'r') as strain_file:
    strain_lines = strain_file.readlines()
    for line in strain_lines:
        line = line.strip()
        gut_id = line.split("\t")[0]
        if gut_id in sample_dict:
            print(line, sample_dict[gut_id], sep="\t")
