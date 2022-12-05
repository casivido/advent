import re
from helpers import loadFileByLine;

sections = loadFileByLine('inputs/day4_1.txt')

overlap_counter = 0
for section in sections:
    [section1_start, section1_end, section2_start, section2_end] = list(map(lambda x: int(x), re.search(r"(\d*)-(\d*),(\d*)-(\d*)", section).groups()))

    section1_within_2 = section1_start >= section2_start and section1_end <= section2_end
    section2_within1 = section2_start >= section1_start and section2_end <= section1_end
    if section1_within_2 or section2_within1:
        overlap_counter += 1

print(overlap_counter)