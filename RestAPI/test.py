#1

# user_list=[{'name':'Bhaskar','age':28},{'name':'Sirisha','age':26}]
# user_list[0].update({'name':'Bhaskar','age':27})
# print(user_list)


# #2
# recipes=[
#     {
#         'id': 1,
#         'name': 'Salad',
#         'description': 'This is a lovely Greek salad recipe.'
#     },
#     {
#         'id': 2,
#         'name': 'Rava Masala Dosa',
#         'description': 'This is recipe for Rava Masala Dosa.'
#     }
#         ]
#
# print(recipes[0].items)


# for key,value in recipes.items():
#     print(key,value)


# /recipes   GET  to get all recipes
# /recipes/<id> GET to get matching id



# Guess the number game
# 1. Allow user to guess the number in 7 chances
# 2. If the number guessed by user is greater or smaller than the number generated notify user about it .
# 3.  If the user is able to guess the number correctly you need to congratulate the user and and you need to tell in
#      how many attempt the user cracked it
#   Congratulations !!! You cracked the number in 4 attempts
# 4. If the user is not able to crack the number , you need to say all chances exhausted.

import random
gennum = random.randint(1,100)
print(gennum)
#user_input = int(input("Enter the number between 1 to 100: "))
cnt =1
for itemchance in range(1,3):
    #print(itemchance)
    user_input = int(input("Enter the number between 1 to 100: "))
    if gennum==user_input:
        success= "Congratulations !!! You cracked the number in {0} attempts".format(itemchance)
        print(success)
        break
    else:
        print(itemchance)
        if itemchance == 7:
            exceeded = "Oh !!! Your all chances {0} attempts exhausted,Actual number is {1}  ".format(itemchance,gennum)
            break
        else:
            if gennum > user_input:
                print("please enter greater number")
            else:
                print("please enter lessor number")
# else:
#     exceeded = "Oh !!! Your all chances {0} attempts exhausted,Actual number is {1}  ".format(itemchance,gennum)
#     print(exceeded)





