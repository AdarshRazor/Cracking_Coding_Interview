'''
Check if one edit or not
level: easy
'''

def isDistanceLessThanTwo(stringA, stringB):
    #take lenth of both
    lenA = len(stringA)
    lenB = len(stringB)
    dis = 0
    #if difference of length is more than 1 then its changed
    if abs(lenA-lenB)>1:
        return False
    #if both are equal then obvio its true#
    #
    #also have else condition 
    #
    if stringA == stringB:return True
    #if length is equal then check  for the wordings
    if lenA == lenB:
        for i in range(0,lenA):
            #if wording are chaged then increase dis and if its more than 1 then its changed
            if stringA[i]!=stringB[i]:
                dis += 1
                if dis > 1:
                    return False
        return True
    #if len is not equal then move forward
    else:
        #if len of A is greater than B than longest string is A or else its B
        if lenA > lenB:
            shortS = stringB
            longS = stringA
        else:
            shortS = stringA
            longS = stringB
        #editing every char and matching to check 
        for i in range(0,len(longS)):
            temp = longS[:i] + longS[i+1:]
            if temp == shortS:
                return True
            return False
            
print (isDistanceLessThanTwo('aaa', 'aaaa'))
print (isDistanceLessThanTwo('aaa', 'aaaaa'))
print (isDistanceLessThanTwo('aaa', 'aabb'))
print (isDistanceLessThanTwo('aaa', 'bbbb'))
print (isDistanceLessThanTwo('', ''))
print (isDistanceLessThanTwo('aaaa', 'aaba'))
print (isDistanceLessThanTwo('aaaa', 'babb'))