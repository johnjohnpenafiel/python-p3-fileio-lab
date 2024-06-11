def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w", encoding= "UTF-8") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a", encoding= "UTF-8") as file:
        file.write(append_content)


def read_file(file_name):
    with open(f"{file_name}.txt", "r", encoding= "UTF-8") as file:
       content = file.read()
       return content

write_file("./Test", "testing to see if this works and I create a new folder")
append_file("./Test", "Hello")
append_file("./Test", "Goodbye")
append_file("./Test", "Next line\n")
append_file("./Test", "Is this going to the next line?")
append_file("./Test", "\nSo if I want this on the next line I have to use the /n first")

print(read_file("./Test"))