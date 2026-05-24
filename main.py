import random
secret_number = str(random.randint(0,9))
print("Welcome to number guessing name")
print("I have chosen a number between 0 and 9")
print("Try to get it. you will keep on try stil you get it right\n")



while True:
  guess_input = input("Enter yor guess between 0 and 9")
  if guess_input == secret_number:
    print("Congratulation you guessed it right")
    print(f"The number was : {secret_number}")
    break
  else:
    print("Please try it a again")
