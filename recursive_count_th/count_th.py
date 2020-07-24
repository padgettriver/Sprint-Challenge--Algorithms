'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if len(word) < 2:                          #base case cany be 'th' if its less then 2 characters
        return 0 
    
    if word[:2] == 'th':                      #looks for 'th' in index
        return count_th(word[1:]) + 1          #move indexes
    else:
        return count_th(word[1:])               #remoe first index