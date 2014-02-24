#! /usr/bin/python


a=[1,2,3]
for i in range(0,3):
  print a[i]

print "second array"
ls=[[9,7,8],[4,5,6]]

i=0
b=0
while i<2:
    b=0
    for b in range(0,3):
	print ls[i][b] 
    print "i = ",i
    print "b =  ",b
    i =i+1
    print "i= ",i
    


