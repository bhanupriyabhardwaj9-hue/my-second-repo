""" from sys import argv """

'''
#value="Raj"
#value=12.87
#print(value)
#print(type(value))
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

""" a=20
b=12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b) """

""" val=(12 or 5)-3
print(val)
x=0 or 4
y=5 or 7
print(x,y)
a=not 5
b=not 0
print(a,b) """

""" a=10
b=20
a+=30
b-=10
print(a,b) """

""" a=10
print(a)
print(-a) """

""" text="Welcome to Python Programming"
print("Welcome" in text)
print("python" in text)
print("Programming" in text)
print("hello" not in text)"""

""" a=19
b=19
print(id(a))
print(id(b))
print(a is b) """

""" name=input("Enter your name:")
print("Your name is:",name) """

""" a=input("Num 1:")
b=input("Num 2:")
c=float(a)+float(b)
print(c) """

""" principle=float(input("enter p:"))
rate=float(input("enter r:"))
years=int(input("enter y:"))
simple_interest=(principle*rate*years)/100
print("The simple interest is:",simple_interest) """
""" a=eval("10+10")
print(a)
print(10>=10)
b=eval("10*10")
print(b) """

""" val=eval(input("Enter Expression:"))
print(val)
print(type(val)) """

""" a=eval(input("Num 1-"))
b=eval(input("Num 2-"))
c=a+b
print(c)
 """
""" a=eval(argv[1])
b=eval(argv[2])
c=a+b
print(c) """
""" print("abc") """
""" 
print(argv[2])
 """
""" a=eval(argv[1])
b=eval(argv[2])
c=a+b
print(c) 
print("The Length of values:", len(argv)) """

""" str1="Priya's Diary"
str2='Priya said,"I am a good girl"'
print(str1)
print(str2)
 """
""" c="" +34-4
print(c) """
""" c=bool("") +34-4
print(c) """
""" c=bool("dsjkj") +34-4
print(c) """

""" s1="Python"
print(s1[0])
print(s1[len(s1)-1])
print(s1[-1])
print(s1[-len(s1)])
for x in range (len(s1)):
    print(s1[x])
for x in range (-len(s1),0):
    print(s1[x])
for s in s1:
    print(s) """

""" s1="Python in GLA CL2" 
print(s1)
print(s1[::])
print(s1[13:9:-1])
print(s1[10:-4:])
print(s1[-5:9:-1])
print(s1[-5:9:])
print(s1[-50:90:])
print(s1[-100]) """

""" name="Bhavya"
print(name)
print(name[0])
name[0]="X" """

""" a="Python"
b="Programming"
c=a+b
print(c) """
""" a="Python"
b=4 #Always multiply string with a whole number
print(a*b) """

""" print("p" in "python")
print("z" in "python")
print("on" in "python")
print("pa" in "python")
print("y" not in "apple") """
""" s1="abcd"
s2="abcdefg"
print(s1==s2)
if(s1==s2):
    print("Both are same")
else:
    print("Not same") """

""" s1=input("Enter string 1:")
s2=input("Enter string 2:")
output=print("same") if s1==s2 else print("Not same")
print(output)
 """
""" s1=input("Enter string 1:")
s2=input("Enter string 2:")
output="same" if s1==s2 else "Not same"
print(output) """

""" s1=" Amit Singh "
print(len(s1.strip())) """
""" s1="python is a programming language. Python is easy to learn. Python is used in AI and ML"
print(s1.find("Python"))
print(s1.index("Python"))
print(s1.rfind("Python"))

output="Yes" if s1.find("Python")!=-1 else "No"
print(output)
output="Yes" if "Python" in s1 else "No
print(output)
 """
""" s1="python is a programming language. Python is easy to learn. Python is used in AI and ML"
print(id(s1))
s2=s1.count("Python")
print(id(s1))
print(s2)
for i in s1:
    print(i,s1.count(i)) if s1.count(i)>15 else None """

""" s1="Priya Nishu Eshika Durgesh"
s2=s1.split()
print(s1, type(s1))
print(s2, type(s2))
for item in s2:
    print(item,s1.count(item)) """
""" dob=input("Enter Date of Birth(DD/MM/YYYY)")
#year=dob.split("/")
year=dob[dob.rfind("/")+1:]
print(year) """

""" l1=["22","11","2026"]
s1="-".join(l1)
print(s1)
print(type(s1)) """

""" x="Python"
y=""
z=x.split()
for i in z:
    y=y+x[::2]
 print(y.strip()) """

""" str1=input("Enter a string:")
sub=""
for i in str1.split():
    sub+=i[::2]+" "
print(sub.strip()) """

""" str1="The quick brown fox jumps over the lazy dog"
sub="fox"
print(str1.count(sub)) """

""" str1=input("Enter a string")
sub=""
for i in str1:
  if str1.count(i)>1 and i not in sub:
    sub+=f"{i}{str1.count(i)}"
print(sub.strip()) """

""" str1=input("Enter'#' and '*' as many times you want:")
for i in str1:
    if str1.count("#")==str1.count("*"):
        print("0")
    elif str1.count("#")>str1.count("*"):
        print("1")
    elif str1.count("#")<str1.count("*"):
        print("-1") """

""" str1="PROGRAMMING"
sub=""
for i in str1.split():
    sub+=i[::2]+" " + i[::3]+" "
print(sub.strip()) """

""" x=int(input("Enter a number:"))
if x<0:
    print("The number is a negative number")
else:
    print("the number is a positive number") """

""" user_name='rahul'
x=input("Enter a name: ")
if user_name==x:
    print("The name is valid")
else:
    print("The name is invalid") """

""" a=eval(input("Enter the marks of english"))
b=eval(input("Enter the marks of Hindi/Telugu"))
c=eval(input("Enter the marks of Maths"))
d=eval(input("Enter the marks of Science"))
e=eval(input("Enter the marks of Geography"))
f=eval(input("Enter the marks of History"))
sum=(a+b+c+d+e+f)
print("The sum is: ",sum)
avg=sum/6
print("the average is: ",avg)

if avg>=90:
    print("Ramu's grade is:A+")
    print("RAMU HAS PASSED")
elif avg>=89 and avg<90:
    print("Ramu's grade is:A")
    print("RAMU HAS PASSED")
elif avg>=79 and avg<89:
    print("Ramu's grade is:B+")
    print("RAMU HAS PASSED")
elif avg>=69 and avg<79: 
    print("Ramu's grade is:B")
    print("RAMU HAS PASSED")
elif avg>=45 and avg<69: 
    print("Ramu's grade is:C")
    print("RAMU HAS PASSED")
elif avg>=33 and avg<44: 
    print("Ramu's grade is:D")
    print("RAMU HAS PASSED")
else:
    print("RAMU HAS FAILED") """

""" val=3.789
s="%.2d"%val
print(s) """

""" items_cost=[10,20,30]
gst=2
for x in items_cost:
    print(x+gst) """

""" for x in range(1,5):
    print(x) """

""" x=[10,20,30,"Python"]
for i in x:
    print(i) """

""" x="python"
for ch in x:
    print(ch) """

""" item_cost=[10,20,30]
sum=0
for x in item_cost:
    sum=sum+x
print(sum) """

x=input("Enter a number")
num=0
for ch in x:
    y=num+int(x)
print(y)