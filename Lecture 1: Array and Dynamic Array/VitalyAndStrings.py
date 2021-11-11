a=list(input())
b=input()
i=len(a)-1

while a[i] == 'z':
  a[i]='a'
  i-=1

a[i]=chr(ord(a[i])+1)
a=''.join(a)
if a>=b:
  print('No such string')
else:
  print(a)
