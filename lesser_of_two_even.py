def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
        
a=int(input("enter first no.:"))
b=int(input("enter second no.:"))
lesser_of_two_evens(a,b)