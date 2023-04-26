#1
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
txt1= fname[::-1]
txt2= lname[::-1]
print ( txt2 + " " + txt1)

#2
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

#3

#4
# pi = 3.1415926535897931
# r= 6.0
# V= 4.0/3.0*pi* r**3
# print('The volume of the sphere is: ',V)

#5
# b = int(input("Input the base : "))
# h = int(input("Input the height : "))
# area = b*h/2
# print("area = ", area)

#6
# n=5
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')
# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

#7
# word = input("Input a word to reverse: ")
# for char in range(len(word) - 1, -1, -1):
#   print(word[char], end="")
# print("\n")

#8
# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x,end=' ')
# print("\n")

#9
# x,y=0,1
# while y<50:
#     print(y)
#     x,y = y,x+y

#10
# s = input("Input a string: ")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)