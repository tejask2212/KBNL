def printinbox(message):
    length = len(message)
    x = ("+" + "-"* (length-7) + "+")
    y = ("         | " + message + " |")
    z = ("+" + "-"* (length-7) + "+")
    print(x.center(150))
    print(y.center(150))
    print(z.center(150))

def color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

questions = [
             ["Capital of India?", "1.Mumbai", "2.Delhi", "3.Pune", "4.Goa"],
             ["Largest continent?","1.Africa", "2.Asia", "3.Europe", "4.America"],
             ["Smallest planet in our solar system?","1.Earth", "2.Mars", "3.Mercury", "4.Venus"],
             ["Fastest land animal?","1.Cheetah", "2.Lion", "3.Tiger", "4.Leopard"],
             ["Tallest mountain in the world?","1.K2", "2.Kangchenjunga", "3.Everest", "4.Lhotse"],
             ["Deepest ocean?","1.Atlantic", "2.Indian", "3.Arctic", "4.Pacific"],
             ["Largest mammal?","1.Elephant", "2.Blue Whale", "3.Great White Shark", "4.Giraffe"]]
answers = [2, 2, 3, 1, 3, 4, 2]
money = [1000, 2000, 5000, 10000, 20000, 50000, 100000]

total_money = 0

printinbox(color("Welcome to Kaun Banega Nakli Lakhpati (KBNL)", 35))
print("\n\n")
name = input(color("Enter your name ", 34))
print("\n")

for i in range(len(questions)):
    if i in {2,5,6}:
     print(color("CONFIRM MONEY QUESTION (CMQ)", 34))

    print((f"Question for Rs.{money[i]}"))
    question = questions[i]
    print(color(question[0], 33))
    print(color(f"{question[1]}             {question[2]}", 33))
    print(color(f"{question[3]}             {question[4]}", 33))
    a = int(input("Enter correct answer or 0 to Quit: "))
    if a == answers[i]:
        print(color(f"Correct answer! You have won {money[i]}.\n\n", 32))
        if i == 2:
            total_money = 5000
        elif i == 5:
            total_money = 50000
        elif i == 6:
            total_money = 100000
            printinbox(color(f"Congratulation {name}, you are now Nakli Lakhpati", 36))
    elif a == 0:
        print(color("You have quit the game", 36))
        break
    else:
        correct_option = questions[i][answers[i]]
        print(color(f"Opps!!! Wrong answer. The correct answer is {correct_option}.", 31))
        break

print(color(f"\nTotal money won: {total_money}", 32))