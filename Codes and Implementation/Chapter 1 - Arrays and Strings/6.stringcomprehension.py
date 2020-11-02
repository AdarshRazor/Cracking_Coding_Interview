'''
Print the number of occurance of the alphabet
level: easy
'''

def compress(string):
    if string == '':
        return ''
    #setting the first alphabet in the current
    current = string[0]
    result = ''
    count = 0
    string = string + ' '
    #itterating from 1 to end of the string
    for i in range (0, len(string)):
        #if the string match then increase the count
        #
        if current == string[i]:
            count +=1
        #if not then store the current string and the number in the result
        else: 
            result += current+str(count)
            count = 1
        #increase the current char with the i everytime
        current = string[i]
    return result

inp=input("Enter the strings: ")

'''
print (compress('ab'))
print (compress('a'))
print (compress(''))
print (compress('aaabbbcbabababababababababaxxxxxxxxxxxxxxxxxxxx'))
'''

print (compress(inp))
