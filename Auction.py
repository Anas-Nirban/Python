#HINT: You can call clear() to clear the output in the console.
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

any_bidders = True

bidder_list = {}
while(any_bidders):
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
  bidder_list[name] = bid
  if bidders == "no":
    any_bidders = False
  os.system('cls')

for keys in bidder_list:
  bid = bidder_list[keys]
  if bid > bidder_list[keys]:
    bidder_list[keys] = bid

print(logo)
print("The winner is " + keys + " with a bid of $" + str(bidder_list[keys]))
