numfib=10
n1 = 0

n2 = 1

count = 0

while count<numfib:
    print(n1)
    a=n1+n2
    n1=n2
    n2=a
    count += 1