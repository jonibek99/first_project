f=open('ali.txt','r').readlines() 
 
a=open('familya.txt','r').readlines()

for c,d in zip(a,f):
    print(d,c)