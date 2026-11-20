try:
    f = open("source.txt", "r")
    data = f.read()
    f.close()
    f = open("destination.txt", "w")
    f.write(data)
    f.close()
    print("File copied successfully")
except FileNotFoundError:
    print("Source file does not exist")