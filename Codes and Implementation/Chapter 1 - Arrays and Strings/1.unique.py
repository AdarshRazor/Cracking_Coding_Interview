'''
Check all the strings are unique or not
'''

def uniqueornot(inp):
    unassign = []
    for i in inp:
        if i in unassign:
            return (print("\nNot Unique !\n"))
        else:
            unassign.append(i)
    return (print("\nUnique !\n"))

inp = input("\nEnter the String: ")

uniqueornot(inp)