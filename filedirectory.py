import os

path = "C:\\Users\kevinskeen\Desktop"
dir_list = os.listdir(path)

print("Files and directories in  " , path )

#print(dir_list)
for entry in dir_list:
    print(entry)


#print out list of files in the directory
