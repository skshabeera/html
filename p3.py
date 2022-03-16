# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5
i=5
while i>=1:
    c=5
    j=0
    while j<i:
        print(c,end =" ")
        c-=1
        j+=1
    i-=1
    print()

i=1
while i>=5:
    j=1
    while j>=i:
        print(i,end=" ")
        j=j+1
    i=i-1
    print()

