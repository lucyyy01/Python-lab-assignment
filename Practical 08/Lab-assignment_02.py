source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

src = open(source, "r")
dest = open(destination, "w")

for line in src:
    if not line.strip().startswith("#"):
        dest.write(line)

src.close()
dest.close()

print("\nSource File Content:")
src = open(source, "r")
print(src.read())
src.close()

print("\nDestination File Content (without comments):")
dest = open(destination, "r")
print(dest.read())
dest.close()
