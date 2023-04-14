
name1=input("enter the name1=")
name2=input("enter he name2=")

for i in name1:
    for j in name2:
        if i==j:
            name1=name1.replace(i,"",1)
            name2=name2.replace(j,"",1)
            break
print(name1,name2)
count=len(name1+name2)
print(count)

if count>0:
    list1=["friends","lovers","affection","marriage","enemies","siblings"]
    while len(list1)>1:
        c=count%len(list1)
        y=c-1
        if y>=0:
            left=list1[:y]
            right=list1[y+1:]
            list1=right+left
        else:
            list1=list1[:len(list1)-1]
    print("relationship is:",list1[0])
else:
    print("differnt relationship")
