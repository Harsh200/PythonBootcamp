# variable hold data
name = "Harsh Kumar Saxena"
print("name")
print(name)
c = 10
d = 10.0
print(c)
print(d)
# now we are assigning multiple variable at once
aa,bb,cc,dd=3,"hello",222,123
print(aa)
print(bb)
print(cc)
print(dd)
# Now we declare variable as global,by default a variable is local
x = "Harsh"
print(x)
y=123456
z=666
def f():
    global x
    x=x*2
    print(x)
    print(z)


f()

print(y)


