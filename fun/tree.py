

print("Give height of tree:")
h=int(input())
print("Give the symbol of the tree:")
c=input()
for i in range(h):
    print((h-i)*" "+(2*i+1)*c)
