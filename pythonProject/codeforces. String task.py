string = str(input())  #string input from user
z = string.lower()
lenth = len(z)    #finfing the lenth of string

# if consonant then print them
for i in z:
    if i=='b' or i=='c'or i=='d' or i=='f'or i=='g' or i=='h'or i=='j' or i=='k'or i=='l' or i=='m'or i=='n' or i=='p'or  i == 'q' or i == 'r' or i=='s' or i=='t'or i=='v' or i=='w'or i=='x'or  i=='z':
        print(f".{i}",end="")