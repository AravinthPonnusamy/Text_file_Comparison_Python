import datetime

print(datetime.datetime.now())
with open('a.txt','r') as file2:
    with open('b.txt','r') as file1:
        difference = set(file1).difference(file2)
difference.discard('\n')

with open('difference.txt','w') as file_out:
    for line in difference:
        file_out.write(line+"\n")

print(datetime.datetime.now())