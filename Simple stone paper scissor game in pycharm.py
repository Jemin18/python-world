import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What do you choose? Type 0 for rock,1 for paper or 2 for scissors.\n"))
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)
if user>2 or user<0:
    print("You entered invalid number.You lose.")


com = [rock,paper,scissors]
machine_choice = random.randint(0,len(com)-1)
a = com[machine_choice]
print(f"Computer chose:\n{a}")

if user == 0 and machine_choice==1:
    print("You lose.")
elif user == 1 and machine_choice==0:
    print("You won.")

if user == 1 and machine_choice==2:
    print("You lose.")
elif user == 2 and machine_choice==1:
    print("You won.")

if user == 2 and machine_choice==0:
    print("You lose.")
elif user == 0 and machine_choice==2:
    print("You won.")

if user == machine_choice:
    print("Match drawn.")




