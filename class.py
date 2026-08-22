''''''
#value="Raj"
#value=12.87
#print(value)
#print(type(value))
'''
'''
#a,b,c="Bhanupriya",87,82
#print(a,b,c)
#a,b,c=3,4
#print(a,b,c)
'''
a=b=c=d=84
print(a,b,c,d)
'''
'''
a=7
print("First assigned value:",a)
a=19.7
print("variable is re-initialised,now the value is:",a)
print(type(a))
'''
'''
emp_id=12
name='Manya'
salary=50000.80
print("My employee ID is:",emp_id)
print("My name is:",name)
print("My salary is:",salary)

print("emp_id type is:",type(emp_id))
print(type(name))
print(type(salary)
'''
'''
a=3E2
b=4E2
c=5E2
print(a)
print(b)
print(c)
print(type(a))
'''
'''
a=2+5j
b=4-5.5j
c=2+10.5j
print(a)
print(b)
print(c)
print()
print(a+b)
print(b+c)
print(c+a)
'''
'''
a=True
b=False
print(a)
print(b)
print()
print(a+a)
print(a+b)
'''
'''
#a=None
#print(a)
#print(type(a))
'''
'''
x=[10,20,30,40]
y=bytes(x)
print(type(y))
'''
#x=[10,300,180]
#y=bytes(x)
'''
x=[10,40,100,30]
y=bytes(x)
y[0]=20
'''
'''
l1=range(5) #0-4
l2=range(2,7) #2-6
l3=range(2,10,2) #2,4,6,8
print(l1)
print(l2)
print(l3)
print(type(l3))
for x in l3:
    print(x)
    '''
'''
a=5.9
n=str(a)
print(n)
print(type(n)
'''
'''
a="YUG"
n=int(a)
print(n)
print(type(n))
'''
'''
a=""
a=bool(a)
print(type(a))
print(a*10*2)
'''
'''
a=None
print(a)
print(type(a))
'''
'''
x=[10,20,30,40,50]
y=bytes(x)
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])
'''
""" x=[10,20,30,40,50]
y=bytes(x)
for a in y:
    print(a)
 """
""" x=[340,40,7,19]
y=bytes(x) """
""" x=[10,20]
y=bytes(x)
x[0]=90
 """
'''a=range(10,2,-2)
print(a)
for x in a:
    print(x)'''
'''a=-89 #any number is true except 0 or none 
a="Amit" #String is true except empty string
print(bool(a)+3)'''

""" a=5
print("123"+a) """
""" a=5
print(str(a)+"123")
print(a+int("123")) """
""" a=5
n=float(a)
print(n)
print(type(n)) """
""" a=5.9
n=int(a)
print(n)
print(type(n)) """
""" b=6
c=str(b)
print(c)
print(type(c)) """ 
""" a=10
b=30
c=-5
d=(a if a<b else b)+30 """
""" a=10
b=20
c=-5
d=(a if a<c else c) if a<b else (b if b<c else c) """
a=20
b=12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)