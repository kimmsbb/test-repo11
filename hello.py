x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
answer=False
for i in range(y):
    for j in range(x):
        if b[i]==a[j]:
            c=1
            for z in range(y):
                if b[i+z]==a[j+z]:
                    c+=1
            if c==y:
                answer=True
                break
        if answer:
            break
    if answer:
        break
if answer:
    print("Yes")
else:
    print("No")
                