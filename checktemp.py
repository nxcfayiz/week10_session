import mytemp as t
c=int(input("enter your temp in C and we will provide the FH temp"))

print(c, "celcius is equivalent to",t.celTofeh(c))

f=int(input("enter your temp in fh and we will provide the C temp"))
print(f,"celcius is equivalent to",t.fehTocel(c))
