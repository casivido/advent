import re
from helpers import loadFileByLine;

sections = loadFileByLine('inputs/day4_1.txt')

overlap_counter = 0
for section in sections:
    [section1_start, section1_end, section2_start, section2_end] = list(map(lambda x: int(x), re.search(r"(\d*)-(\d*),(\d*)-(\d*)", section).groups()))

    # check if section 1 ends are within 2, then if 2 is fully within 1
    section1_starts_within_2 = section1_start >= section2_start and section1_start <= section2_end
    section1_ends_within_2 = section1_end >= section2_start and section1_end <= section2_end
    section2_starts_within_1 = section2_start >= section1_start and section2_start <= section1_end
    if section1_starts_within_2 or section1_ends_within_2 or section2_starts_within_1:
        overlap_counter += 1

print(overlap_counter)