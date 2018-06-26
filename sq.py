

1(a).a=2
b=5
c=4
x=a*a+b*b+c*c
print(x)
print(pow(x,0.5))

output:

45
6.708203932499369

(b). x=2
y=5
a=10
c=x*x*x+y*y-(pow(x*y,0.5))/2*a
print(c)

output:
17.188611699158102

2.Error in this code: 
a=10
if a==10: ---->  (error invalid syntax)
    print("a is equal to 10")
else:
    print("a is not equal to 10")

output:
  a is equal to 10


3.output of the following code:

     for j in range(1,11):
          for i in range(1,11):
              print("%3d"%(j*i)),end="")
              print()


output:
    1 2 3 4 56 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50 
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100





4.Fibonacci Series:


numfib=20
n1 = 0

n2 = 1

count = 0

while count<numfib:
    print(n1)
    a=n1+n2
    n1=n2
    n2=a
    count += 1


output:

0
1
1
2
3
5
8
13
21
34
89
144
233
377
610
687
1597
2584
4181


5. Largest Among Three Numbers:

 a1 = 5
a2 = 10
a3 = 6
if (a1 >= a2) and (a1 >= a3):
   largest = a1
elif (a2 >= a1) and (a2 >= a3):
   largest = a2
else:
   largest = a3
print("The biggest number between","is",largest)

output:

 The  biggest number between is 10
