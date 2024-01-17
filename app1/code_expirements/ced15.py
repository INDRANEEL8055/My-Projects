import glob #The glob module, which is short for global, is a function
            # that's used to search for files that match a specific file pattern or name.
            # It can be used to search CSV files and for text in files.

myfiles = glob.glob("../*.txt")

for filepath in myfiles:
    with open(filepath, "r") as file:
        print (file.read().upper())

