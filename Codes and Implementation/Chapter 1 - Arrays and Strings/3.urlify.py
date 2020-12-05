'''
Replace white space with %20
level: easy
'''


inp=input("Enter the url: ")
print((inp.strip()).replace(" ","%20"))

'''
string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string.strip())
> xoxo love xoxo

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))
> lov

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))
>   xoxo love xoxo 

string = 'android is awesome'
print(string.strip('an'))
> droid is awesome