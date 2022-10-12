# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



    #     if num!= 0:
    #         num = num//10
    #         cnt = cnt + 1
    # print(cnt)
    # # 1. Write    a    program    to    find    all    factors    of    a    number
    # num = int(input("please enter a number"))
    # for i in range(1,num+1):
    #     if num % i ==0:
    #         print(f"{i} is a factor of {num}")

    # # 2 Using while loop Write a program to find  factorial 10
    # num = int(input("enter a number"))
    # i = 1
    # while num >= 1:
    #     i = i * num
    #     num = num - 1
    # print(i)
            #or
    # product =1
    # for i in range(1,11):
    #     product = product* i
    # print(product)

    # # 3.Challenge 3 : print all prime numbers between 1 and 100
    # for number in range(1, 100 + 1):
    #     if number > 1:
    #         for i in range(2, number):
    #             if number % i == 0:
    #                 break
    #         else:
    #             print(number)

    # # 4.Challenge 4 : Write a function that can calculate HCF of 2 numbers
    ##num1= 15
    #num2=30
    # def find_factors(num1, num2):
    #     for i in range(1, num1 + 1):
    #         if num1 % i == 0 and num2 % i == 0:
    #             hcf = i
    #     print(hcf)
    # # 5.Challenge 5 : write a function that can find total digits in a natural number

    # num = 125
    # cnt = 0
    # while True:
    #     if num != 0:
    #         num = num // 10
    #         cnt = cnt + 1
    # print(cnt)
    # # 6 write a large element in the list
    # list=[23,3,56,3,10]
    # max=list[0]
    # for i in list:
    #     if i >max:
    #         max=i
    # print(max)

    # # 7.count of the list without count method
    # mylist=[1,9,99,85,85,30,22,10,85] # output num =85 and count is 3
    # num=85
    # count=0
    # for i in mylist:
    #     if i==num:
    #         count= count+1
    # print(f"Total numbers {num} of mylist is :{count}")

    # # 8. create dict using without zip method
    # list1=["India","Lanka","Nepal","UK"]
    # list2=["Delhi","Colombo","Kathmandu"]
    # mydict = {}
    # for i in range(len(list1)):
    #     mydict[list1[i]]=list2[i]
    # print(mydict)

    # #9 lambda
    # # give the input and print square of the output
    # x = lambda a: a*a
    # print(x(3))

    # sequence=[2,5,7]
    # result=filter(lambda x: True if x%2==0 else False,sequence)
    # print(list(result))

    # # max number
    # from functools import  reduce
    # mylist=[1,22,300,14,555,6]
    # def maxlist(num1,num2):
    #     if num1>num2:
    #         return num1
    #     else:
    #         return num2
    # result= reduce(maxlist,mylist)
    # print(result)
    # result = reduce(lambda num1,num2:num1 if num1>num2 else num2,mylist)
    # print(result)





# # 4.Challenge 4 : Write a function that can calculate HCF of 2 numbers
#num1= 15
#num2=30
# def find_factors(num1,num2):
#     for i in range(1,num1+1):
#         if num1%i==0 and num2%i==0:
#             hcf=i
#     print(hcf)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #def add(*args,**kwargs):

    # find_factors(15,17)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
