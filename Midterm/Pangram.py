N = int(input())
word = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

if len(set(word.lower())) == 26:
    print("YES")
else:
    print("NO")