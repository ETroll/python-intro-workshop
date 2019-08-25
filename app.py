

if __name__ == "__main__":
    file : str = "hello.txt"

    # Overwrite the file if it exists
    with open(file, "w+") as fileobj:
        fileobj.write("Hello world\n")

    with open(file, "r") as fileobj:
        print(fileobj.readlines())

    # Append to file
    with open(file, "a") as fileobj:
        fileobj.write("Hello again\n")

    # Read all lines as a list
    with open(file, "r") as fileobj:
        print(fileobj.readlines())

    # Read line by line
    with open(file, "r") as fileobj:
        for line in fileobj:
            print(line)