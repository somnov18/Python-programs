def spy_game(nums):
    spyno=[0,0,7,'x']
    for i in nums:
        if i == spyno[0]:
            spyno.pop(0)
    return len(spyno) == 1

def lst():

    lst =[]
    n= int(input("Enter no. of values to be inserted in the list:"))
    print("Ënter elements:")
    for i in range(0,n):
        ele = int(input())
        lst.append(ele)
    return (lst)

nums = lst()
spy_game(nums)
