num=10
while num>0:
    print(f"*" * num)
    num-=1
num=1
while num<10:
    print(f"*" * num)
    num+=1
num=10
while num>0:
    print(f"*" * num)
    num-=1
    
rows=10
i=1
while i<=rows:
    print(" " * (rows-i) + "*" * (2*i-1))
    i+=1
    
while i>=1:
    print(" " * (rows-i) + "*" * (2*i-1))
    i-=1