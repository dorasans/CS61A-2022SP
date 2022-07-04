def count(s,value):
    total = 0
    for element in s:
        if element==value:
            total+=1
    return total
print(count([1,2,2,1],1))
def mySum(L):
    if L==[]:
        return 0
    else:
        return L[0]+mySum(L[1:])
print(mySum([1,2,3,4]))

def reverse(s):
    if len(s)==1:
        return s
    else:
        return reverse(s[1:])+s[0]
print(reverse('string'))
