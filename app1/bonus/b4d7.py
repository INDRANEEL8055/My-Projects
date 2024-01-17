filenames = ["1.doc","1.report","1.presentatoion"]

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

print(filenames)