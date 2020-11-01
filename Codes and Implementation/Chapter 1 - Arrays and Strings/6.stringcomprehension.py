'''
Print the number of occurance of the alphabet
'''

def compress(string):
    if string == '':
        return ''
    current = string[0]
    result = ''
    count = 0
    string = string + ' '
    for i in range (0, len(string)):
        if current == string[i]:
            count +=1
        else: 
            result += current+str(count)
            count = 1
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
