#!/root/.virtualenvs/blog/bin/python
import difflib
from os import listdir
from os.path import isfile, join
path="/root/blog"
new_doc = ''
compared_list, new = [], []

#check current files
for file in listdir(path):
        if isfile(join(path,file)):
                compared_list.append(file)

#compare files
with open('list.txt', 'r') as saved_list:
        read_data = [line.rstrip() for line in saved_list]
saved_list.close()

#remove duplicatess

for x in compared_list:
        if x not in read_data:
                new.append(x)

#adicionar novos ao index
#call whoosh?

#append to txt

with open('list.txt', 'a') as save:
        for x in new:
                save.write(x + '\n')
saved_list.close()
