def isPerOfPalindrome(stringA):
    Letters = {}
    #arranging the words so we can get the count
    #{'r': 2, 'a': 2, 'c': 2, 'e': 1}
    for char in stringA:
        if char in Letters:
            Letters[char] += 1
            print(Letters)
        else:
            Letters[char] = 1
    odd = 0
    #ckecking the 
    for count in Letters.values():
        if count%2 > 0:
            odd += 1
            if odd > 1:
                return False
    return True

    
print (isPerOfPalindrome('racecar'))
print (isPerOfPalindrome('recar'))
print (isPerOfPalindrome('rcecar'))
print (isPerOfPalindrome('rr'))
print (isPerOfPalindrome(''))