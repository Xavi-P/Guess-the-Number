import random as rd

magic_number= rd.randint(1,10)
# print(magic_number)

guess=int(input("what is your guess?:"))
if guess == magic_number:
  print("your right")
else:
  print("your dumb")
while guess != magic_number:
  guess=int(input("try again:"))
  if guess==magic_number:
    print("your right")
  else:
    print("your dumb")
