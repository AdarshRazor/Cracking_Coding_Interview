'''
Check the permutation of both strings
level: easy
'''

from collections import Counter

def isPermutation(stringA, stringB):
  if (Counter(stringA) == Counter(stringB)):
    print(stringA,"and",stringB,"are permutation of each other")
  else:
    print(stringA,"and",stringB,"are NOT permutation of each other")


print (isPermutation('abc','cba'))
print (isPermutation('abc','bca'))
print (isPermutation('abc','bcaa'))
print (isPermutation('abc','bcax'))
print (isPermutation('abc','b'))