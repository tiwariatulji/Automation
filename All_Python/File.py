# # TYPE OF FILES.
# # There are 2 types of files:
# # 1.
# # Text files (.txt, .c, etc)
# # 2.
# # Binary files (.jpg, .dat, etc)
# # Python has a lot of functions for reading, updating, and deleting files. OPENING A FILE
# # Python has an open() function for opening files. It takes 2 parameters: filename and mode. # open("filename", "mode of opening(read mode by default)") open("this.txt", "r")

f = open("C:/Study/All_Python/file.txt")
data = f.read()
print(data)
f.close()


# Why This Happens
# In Python, backslashes (\) are used to introduce escape sequences (e.g., \n for newline, \t for tab).

# When you write C:\Study\All_Python\Newfile.txt, Python interprets \S, \A, and \N as escape sequences, which are invalid.

# word = "Donkey"

# with open("C:\\Study\\All_Python\\Newfile.txt", "r") as f:
#     content = f.read()
#     print(content)

# contentNew = content.replace(word,"######")


# with open ("C:\\Study\\All_Python\\Newfile.txt","w") as f:
#     f.write(contentNew)    


# Words = ["Donkey","Bad","ganda"]

# with open("C:\\Study\\All_Python\\Newfile.txt","r"):
#      content = f.read()

# for word in Words:
#      content = content.replace(word,"#" * len(word))     

# with open("C:\\Study\\All_Python\\Newfile.txt","w") as f:
#      f.write(content)