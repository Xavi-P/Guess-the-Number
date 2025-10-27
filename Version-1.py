import random as rd

magic_number= rd.randint(6,7)
# print(magic_number)

guess=int(input("what is your guess?"))
if guess == magic_number:
  print("your right")
else:
  print("your dumb")
