from helpers import loadFileByLine;

input = loadFileByLine("inputs/day7_1.txt")

root = {}
root['/'] = {
    '_type': 'dir',
    '..': root
}
current_directory = root

for line in input:
    args = line.split(' ')

    if args[1] == 'ls':
        continue
    elif args[1] == 'cd':
        dir_name = args[2]
        current_directory = current_directory[dir_name]
    elif args[0] == 'dir':
        dir_name = args[1]
        current_directory[dir_name] = {
            '_type': 'dir',
            '..': current_directory
        }
    else:
        file_name = args[1]
        size = args[0]
        current_directory[file_name] = {
            '_type': 'file',
            '_size': size
        }

ignored_files = ['..', '_type', '_size']
def addSizes(curDir):
    mySize = 0
    for name, file in curDir.items():
        if name in ignored_files:
            continue
        elif file['_type'] == 'file':
            mySize += int(file['_size'])
        elif file['_type'] == 'dir':
            mySize += addSizes(file)
    curDir['_size'] = mySize
    return mySize

total_used = addSizes(root)

total_storage = 70000000
total_needed = 30000000
min_amount_to_free = total_used + total_needed - total_storage

current_smallest_possible_dir_size = total_used

def traverseDir(dir):
    global current_smallest_possible_dir_size
    for name, file in dir.items():
        if name in ignored_files:
            continue
        elif file['_type'] == 'dir':
            traverseDir(file)
            if file['_size'] > min_amount_to_free and file['_size'] < current_smallest_possible_dir_size:
                current_smallest_possible_dir_size = file['_size']

traverseDir(root)



print(current_smallest_possible_dir_size)
print('done')