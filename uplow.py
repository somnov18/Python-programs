def up_low(s):
    d={'lower':0,'upper':0}
    for i in s:
        if i.isupper():
            d['upper'] += 1
        elif i.islower():
            d['lower'] += 1
        else:
            pass
    print(f"no. of upper case characters: {d['upper']}")
    print(f"no. of lower case characters: {d['lower']}")

s = input("enter a string")
up_low(s)