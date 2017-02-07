#! /usr/bin/python

# variables and affect values
a=12  # Integer
b=10.5 # float
c='string' # string
print(a)
print(b)
print(c)

# control flow if-else
print(20*"-")
print("IF-else begins here")
print(20*"-")
if a==10:
	print("a:10")
elif a==11:
	print("a :11")
else:
	print("a: not recognized!")
print(20*"-")
print("If-else ends here")
print(20*"-")

# control flow while
while a>=0:
	print(a)
	a=a-1
# loops : for
print(20*"-")
print("For begins here")
print(20*"-")

for i in range(10):
	print(i)
print(20*"-")
print("For is finished")
print(20*"-")


# strings
print(20*"-")
print("Strings begins here")
print(20*"-")
s="hello world"
print(s)
j=""
for i in s:
	j=j+i
	print(j)
j=""
for i in range(len(s)):
	j=j+s[i]
	print(j)
## slice
print("slice")
print(s[-1])


print(20*"-")
print("string is finished")
print(20*"-")










