out_file = open("output.csv", "r+")
# contents = out_file.read()
# print(contents)

books = []

for line in out_file:  # go through each line (how many lines)
    # line = out_file.readline()  # reads line
    line_list = line.split(",")  # creates list from string
    line_list[-1] = line_list[-1].strip()  # removes \n
    books.append(line_list)  # makes list of lists

# find out how to remove everything after reading
# set formatting so its less retarded
print(books)
out_file.truncate(1)
print(books, file=out_file)
print(out_file.name)
out_file.truncate(1)
out_file.close()
