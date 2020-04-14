files = ['large-file-01.csv', 
         'myscript.py',
         'large-file-02.csv',
         'small-01.csv',
         'small-02.csv']

large_files = []
small_files = []
other_files = []





temp_string = files[0]

# print(temp_string)


print(temp_string.startswith('large'))

large_indicator = 'large-'
small_indicator = 'small-'

for file in files:
    if file.startswith(large_indicator):
        large_files.append(file)
    elif file.startswith(small_indicator):
        small_files.append(file)
    else:
        other_files.append(file)

print('large_files:', large_files)
print('small_files:', small_files)
print('other_files:', other_files)