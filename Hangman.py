import random
print("Welcome to hangman")
play = "Y"
answers = ["PYTHON", "RUBY", "JAVASCRIPT", "JAVA", "COBOL", "SWIFT", "KOTLIN"]
j = 0
k = 0
while play == "Y":
    input_x = []
    m = random.randint(0,7)
    answers_h = answers[m]
    print("Pick letter #{}" .format(j+1))
    input_x = input_x.append(input())
    print(answers_h)
    list_1 = list(answers_h)
    print(list_1)
    while k <= len(list_1):
        if input_x[j] == list_1[k]:
            print("You guessed one right")
            k += 10
        if k == len(list_1):
            print("Guess Agian")
        else:
            k += 1
        print("Guess {} was {}" .format(j, input_x[j]))
    j += 1
    play = input("Play agian (y/n)")
    print(input_x)


