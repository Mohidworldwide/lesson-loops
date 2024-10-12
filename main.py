# # #activity 1


# # # word="mohid"

# # # for char in word:
# # #     print (char)


# # # for i in range (0,10):
# # #     print (i)

# # #activity 2


# # number=int(input("enter number for table"))

# # for i in range (1,11):
# #     print (number,"x",i,"=",number*i)

# #activity 3

# number=sum(range(1,11))
# print (number)

#activity 4

number=int(input("enter number to be checked prime or not"))
flag=False

if number >1 :
    for i in range (2,number):
        if (number % i==0):
            flag=True
            break

if flag :
    print ("number is not prime",number)
else :
    print ("number is a prime number",number)
