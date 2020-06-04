import random
attempt = "yes"
tries = 5
rand_num = random.randint(1,10)
print(f'I\'m thinking of a number between 1 and 10. You have {tries} guesses left.')

while (attempt != "no" and tries > 0):
    guess = int(input('What\'s the number? '))
    if guess == rand_num:
        print('You got it!')
        attempt = "no"
    if guess > rand_num:
        tries -= 1
        print(f'Your guess is too high! You have {tries} guesses left')
        attempt = input("Try again? (yes/no) ")
    if guess < rand_num:
        tries -= 1
        print(f'Your guess is too low! You have {tries} guesses left')
        attempt = input("Try again? (yes/no) ")

if tries == 0:
    print('You have run out of attempts!')