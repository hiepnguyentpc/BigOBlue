no = int(input())
li1 =['+','-','*','^','/']
for i in range(no):
    z=""
    arr = list(input())
    opr=[]
    var=[]
    for j in arr:
        if j=='(':
            continue
        elif j not in li1 and j!=')':
            z = z+j
        elif j in li1:
            opr.append(j)
        elif j==')':
            z = z+opr.pop()
    print(z)