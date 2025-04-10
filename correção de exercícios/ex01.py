#range(3,153,3)

l=[]
i=1
while i<= 150:
    if i%3==0:
        l.append(i)
    i+=1

i=0 
while i<len(l):
    print(l[i])
    i+=1

