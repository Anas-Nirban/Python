# print(type(1))
# print(type(1.0))
# print(type(complex(8, 2)))
# print(type("Anas"))
# print(type(True))
# print(type([1, 2, 3]))
# print(type({1, 'a'}))
# print(type({1: 'An'}))
# print(type((1, 2, 3)))
# print(3**3)

# a = int(input('Enter No. 1: '))

# b = int(input('Enter No. 2: '))

# if(a>=0 & b>=0):
#     print("Addition of",a,"and", b,"is",a+b)
#     print("Subtraction of",a,"and", b,"is",a-b)
#     print("Multiplication of",a,"and", b,"is",a*b)
#     print("Division of",a,"and", b,"is",a//b)
#     print("Modulus of",a,"and", b,"is",a%b)
#     print("Exponential of",a,"and", b,"is",a**b)

# a = 'harry'

# print(a[ -4:-2])

# years = int(input("Enter no. of years"))


# if (years>5):
#     salary = int(input("Enter your salary"))
#     salary = salary * 0.5
#     print(salary*0.5)
# else:
#     print("your experience is low")


# quantity = int(input("Enter your quantity"))
# net_price = quantity * 100
# if (quantity>10):
#     total_price = net_price - .1*net_price
#     print(total_price)


# marks = int(input("Enter your marks: "))

# if(marks>80):
#     print("Grade A")
# elif (marks<80 | marks>60):
#     print("Grade B")
# else:
#     print("fail")

# num1 = int(input("Enter a positive num: "))

# num2 = int(input("Enter a negative num: "))

# print("Num one was", abs(num1))
# print("Num two was", abs(num2))

# classes_held = int(input("Enter no. of classes held"))
# classes_attended = int(input("Enter no. of classes attended"))

# total_percentage = classes_attended / classes_held * 100

# print(total_percentage)
# if(total_percentage > 75):
#     health = input("Do you have a medical cause: Y or N")
#     if(health == "y"):
#         print("Student not allowed")
#     else:
#         print("student allowed")
# else:
#     print("student is not allowed")

# import time

# timestamp = time.strftime("%H : %M : %S")
# print(timestamp)

# if(int(time.strftime("%H"))>=12):
#     print("good afternoon")
# elif(int(time.strftime("%H"))>5 and int(time.strftime("%H"))<9):
#     print("Good evening")
# else:
#     print("Good night")

# def weekday(day):
#     match day:
#         case 1: return "Sunday"
#         case 2: return "Monday"
#         case 3: return "Tuesday"
#         case 4: return "Wednesday"
#         case 5: return "Thursday"
#         case 6: return "Friday"
#         case 7: return "Saturday"
#         case _: return "Sunday"
    
    
# day = int(input("Enter the no. for day"))
# day_ = weekday(day)
# print(day_)

# n = int(input("Enter No. "))
# sum = 0

# for i in range(2, 20, 2):
#     print(i+1)

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for number in numbers:
#     if number>500:
#         break
#     if number>150:
#         continue
#     if(number%5==0):
#         print(number)

# num = 75869

# count = 0

# while num!=0:
#     num = num//10

#     count = count + 1

# print(count)

# list1 = [12, 20, 30, 40, 50]

# size = len(list1)-1

# for i in range(size, -1, -1):
#     print(list1[i])
# new_l = reversed(list1)

# for item in new_l:
#     print(item)
    
# for j in range(-10, 0, 1):
#     print(j)

# for i in range(5):
#     print(i)
# else:
#     print("Done")

# fib0 = 0
# fib1 = 1

# n = int(input("enter range: "))

# if n == 0:
#     print("0")
# elif(n==1):
#     print("1")
# elif(n>1):
#     for i in range(n):
#         print(fib0)
#         res = fib0+fib1
#         fib0 = fib1
#         fib1 = res

# f = int(input("Enter range for fact: "))
# fact  = 1
# if(f == 0):
#     print(0)
# elif(f == 1):
#     print(1)
# else:
#     for i in range(1, f+1):
#         fact = fact * i
#     print(fact)

# i = 1234
# j = reversed(i)
# print(i.reverse())

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for i in my_list[1::2]:
#         print(i)

# num = int(input("Enter No. for cube"))

# cube = 0
# for i in range(1, num+1):
#     cube = i * i * i
#     print(cube)

# row = int(input("Enter no. of rows"))

# for i in range(0,5+1):
#     for j in range(row-i,0, -1):
#         print('*', end='')
#     print("")

# row = 5
# for i in range(0, row):
#     print(i)

# for j in range(row, 0, -1):
#     print(j)

54321
4321
321
21
1

# row = int(input("Enter rows: "))

# for i in range(0, row+1):
#     for j in range(row-i,0, -1):
#         print(j, end="")
#     print("")

# mult = int(input("Enter no. "))
# i=1
# while(True):
#     if mult == 24:
#         print(mult*i)
#         i = i + 1

# num = int(input("Enter no. for factorial"))
# fact = 1

# if(num == 0):
#     print (0)
# else:
#     while(num>=1):
#         fact = fact * num
#         num=num-1
#     print(fact)


# sm = 0
# while(True):
#     sm = (input("Enter input: "))
#     print("Do you want to quit")
#     sm = sm+1
#     if(sm == 'q'):
#         break
# print(sm)

# num = 10
# n = 0
# while(num>=1):
#     if(num % 2 == 0):
#         n = n + num
#     num=num-1

# print (n)

# low = int(input("enter lower range"))
# high = int(input("Enter high num"))

# for i in range (low+1, high):
#     if (i % 2 == 0):
#         print(i)

# num = 0
# while(num<20):
#     num = num + 1
#     print(num)

# num = 1
# while(num<20):
#     num = num + 2
#     print(num)

# num = 105

# while(num>=7):
#     print(num)
#     num = num - 7

num = int(input("enter no. "))

i = 1
while(i<=10):
    print(num , 'x', i, '=', num*1)
    i=i+1