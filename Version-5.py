import random as rd
numbers=[]
magic_number= rd.randint(1,100)
# print(magic_number)

guess=int(input("what is your guess?:"))
counter=6

while guess != magic_number and counter > 0 :
  counter-=1
  numbers.append(guess)
  print("your already guessed  %s " % (numbers))
  if magic_number<guess:
    print("try a lower number")
  if magic_number>guess:
      print("try a higher number")
  print("you have %d guesses left" % (counter))
  if counter==0:
    print("gameover")
  else:
    guess=int(input("try again:"))
  
if guess==magic_number:
    print("you win!")
