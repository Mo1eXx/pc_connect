import re

my_list = {}

with open('all_pc.txt', 'r') as file:
    content = file.read()
    list_content = re.split('\n', content)

    for i in list_content:
        pc_name = re.split(': ', str(i))
        my_list[pc_name[0]] = pc_name[-1]

print(my_list)
