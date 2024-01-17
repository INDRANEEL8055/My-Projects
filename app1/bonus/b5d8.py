#  create a file of your journal whenever you update it
date = input("enter the todays date:- " )
mood = input("hows your mood from 1 - 10 :- ")
thoughts = input("Let your thoughts flow :- \n")

with open(f"..\journal\{date}.txt", "w") as file:
    file.write(mood+2*"\n")
    file.write(thoughts)