filenames = ["1.eat.txt","2.sleep.txt","3.dance.txt"]
for filename in filenames:
    filename=filename.replace('.','-',1)
    print(filename)