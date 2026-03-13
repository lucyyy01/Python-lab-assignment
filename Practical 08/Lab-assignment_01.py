file1 = open("F:\\coding\\Python lab assignment\\Practical 08\\input.txt", "r")
content = file1.read()
file1.close()

file2 = open("F:\\coding\\Python lab assignment\\Practical 08\\output.txt", "w")
file2.write(content.upper())
file2.close()

print("File copied in uppercase successfully")

