import random
num=random.randint(1,100)
print('You will guess a random number from 1 to 100')
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("You will get multiple guess")
print("LET'S PLAY!")

guesses= [0]

while True:
    guess = int(input('Guess a number'))
    if guess<1 or guess>100:
        print("Out of bound! Try again")
        continue

    if guess == num:
        print(f'Congratulation, You have guessed correctly! in your {len(guesses)}th attempt')
        break
    guesses.append(guess)
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('Warmer!')
        else:
            print('Colder!')
    else:
        if abs(num-guess) <= 10:
            print('Warm!')
        else:
            print('Cold!')
