'''
Checking if the string is rotation or not
level: easy
'''
def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return(tmp)
 

str0=input("Enter the first string: ")
str1 = input("Enter the second string: ")

cout=0
for i in range(len(str1)):
    if(leftrotate(str1, i)==str0):
        print("Is Rotation")
        cout=1
        break

if cout==0:
    print("Not a Rotation")