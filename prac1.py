file1=open("myfile.txt","w")

file1.write("Hello\n")
file1.writelines("This is my first PP practical")
file1.close() #change file access modes

file1=open("myfile.txt","r+")

print("output of Read  function is ")
print(file1.read())

file1.seek(0)

print("output of the readine function is ")
print(file1.readline())

file1.seek(0)

#showing difference btwn read and readline
print("Output of read(4) function is ")
print(file1.read(4))

file1 .seek(0)
#readlines function
print("output the readlines function is ")
print(file1.readlines())
file1.close

