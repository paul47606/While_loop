# Even numbers
# enter = int(input("Enter your number: "))
# num = 2
# while num <= enter:
#     print(num)
#     num = num + 2
# --------------------------------------------------------------------------------------------
# Odd numbers
# enter = int(input("Enter your number: "))
# num = 1
# while num <= enter:
#     print(num)
#     num = num + 2
# --------------------------------------------------------------------------------------------
# natural number
# num = 1
# while num <=10:
#     print(num)
#     num = num + 1
# --------------------------------------------------------------------------------------------
# whole number
# num = 0
# while num <=10:
#     print(num)
#     num = num + 1
# --------------------------------------------------------------------------------------------
# square numbers
# num = 1 # init
# print("Number\t\tSqures")
# while num <= 100: # condition
#     print(f"{num}\t\t\t\t{num**2}") #condition
#     num = num + 1
# --------------------------------------------------------------------------------------------
# number series
# num = 10
# while num <= 300:
#     print(num)
#     num = num + 10
# --------------------------------------------------------------------------------------------
# while loop 105, 98, 91,.................7.
# num = 105
# while num >= 7:
#     print(num)
#     num = num - 7
# --------------------------------------------------------------------------------------------
# even number that fall b\t two numbers (exclusive both numberas)
#
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 1st number: "))
# if num1 > num2:
#     while num1 > num2:
#         if num2 % 2 == 0:
#             print(num2)
#         num2 = num2 + 1
# else:
#     while num1 < num2:
#         if num1 % 2 == 0:
#             print(num1)
#         num1 = num1 + 1
# --------------------------------------------------------------------------------------------
# check primer number or not
# num1 = int(input("Enter number: "))
# k = 0
# if num1 == 0 or num1 == 1:
#     print("Not a prime number")
#
# else:
#     i = 2
#     while i < num1:
#         if num1 % i == 0:
#             k = k + 1
#         i = i + 1
#     if k == 0:
#         print(num1, "is the prime number")
#     else:
#         print(num1, "si not prime number")
# --------------------------------------------------------------------------------------------
# sum of digits numbers - read more
# num1 = int(input("Enter number: "))
# r = 0
# s = 0
# while num1 != 0:
#     r = num1 % 10
#     s = s + r
#     num1 = num1 // 10
# print("sum of the digits are: ", s)
# --------------------------------------------------------------------------------------------
# reverse tne number
# num1 = int(input("Enter number: "))
# r = 0
# r_num = 0
# while num1 != 0:
#     r = num1 % 10
#     r_num = r_num * 10 + r
#     num1 = num1 // 10
# print("Reverse number is:", r_num)
# --------------------------------------------------------------------------------------------
# number to words
# num1 = input("Enter number: ")
# L1 = list(num1)
# L = len(L1)
# i = 0
# n = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN",
#      8:"EIGHT", 9:"NINE"}
# while i < L:
#     print(n [int (L1 [i] ) ], end=" " )
#     i = i + 1
# --------------------------------------------------------------------------------------------
# num avg
# s = 0
# i = 0
# while i < 10:
#     num = int(input("Enter Number: "))
#     s = s + num
#     i = i + 1
# print("Avg is: ", s/10)
# --------------------------------------------------------------------------------------------
