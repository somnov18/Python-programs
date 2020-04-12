def unique_list(lt):
    unique=[]
    for i in lt:
        if i not in unique:
            unique.append(i)
    return unique

def lst():

    lst = []
    n = int(input("Enter no. of elements in the list:"))
    for i in range(0,n):
        ele = int(input())
        lst.append(ele)
    return (lst)


lt = lst()
print("Unique list is:")
final = unique_list(lt)
print(final)