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
---'   ____)____
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
while(True):
    user_input = int(input("Enter 0, 1 or 2: "))

    li = [rock, paper, scissors]

    print(li[user_input])

    pc = random.randint(0, 2)

    print(li[pc])
    if(user_input == pc):
        print ("draw")
    elif(user_input == 0 and pc == 1):
        print("PC wins")
    elif(user_input == 0 and pc == 2):
        print("user wins")
    elif(user_input == 1 and pc == 0):
        print("user wins")
    elif(user_input == 1 and pc == 2):
        print("pc wins")
    elif(user_input == 2 and pc == 0):
        print("pc wins")
    else:
        print("user wins")


