with open("text.txt", "r") as read_file:
    with open("text_copy.txt", "w") as write_file:
        for line in read_file:
            write_file.write(line)

"""#opening files
with open("text.txt") as f:
    size_to_read = 100

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)







    for line in f:
        print(line, end='')
    """