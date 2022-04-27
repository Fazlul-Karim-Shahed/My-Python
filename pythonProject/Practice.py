'''color= {
    'R' + 'G' : 'B',
    'G' + 'R' : 'B',
    'B' + 'R' : 'G',
    'R' + 'B' : 'G',
    'B' + 'G' : 'R',
    'G' + 'B' : 'R',
    'R' + 'R' : 'R',
    'G' + 'G' : 'G',
    'B' + 'B' : 'B',
}'''


line = int(input())


for i in range(line):
    y = int(input())
    x = input()

    if x[0] == 'R':
        max = x.count('R')
        print(len(x)-max)


    elif x[0]=='G':

        max = x.count('G')
        print(len(x) - max)


    elif x[0]=='B':
        max = x.count('B')
        print(len(x) - max)

