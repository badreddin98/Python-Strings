# Task 1: Input Length Validator:
first = input("What is your first name?")
last = input("What is your last name?")

checkFirst = len(first)
checkLast = len(last)

if checkFirst < 2:
  print("ERROR, the first name has to be 2 charactors or more.")
else:
  print(checkFirst)

if checkLast < 2:
  print("ERROR, the last name has to be 2 charactors or more.")
else:
  print(checkLast)