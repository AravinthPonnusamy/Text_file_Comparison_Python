import os
file_name = '100MB.txt'
with open(file_name,'a') as file_out:
    i = 1
    #30000000 - 1.5 GB 
    #3000000 - 130 MB 
    while i < 30000000:
        asd = "line "+ str(i) + " : This is an auto generated text"
        file_out.write(asd+"\n")
        i = i + 1

file_stats = os.stat(file_name)
print (f'complete - The file size is : {file_stats.st_size/(1024*1024)} MB')