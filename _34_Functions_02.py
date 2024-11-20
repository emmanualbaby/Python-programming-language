

def fsum(a,b,c):
  return (a+b+c)


def oe(n):
  if n%2==0:
    return ("even")
  else:
    return ("odd")

#odd add 1
#evn add 100
#sep fun

def o(n):
  return n+1

def e(n):
  return n+100


b=20

x=fsum(10,b,401)
print(x)

v=oe(x)
print(v)


if v=="even":
  # w=e(x)
  # print(w)
  print(e(x))
else:
  # w=o(x)
  # print(w)
  print(o(x))


print(oe(677))











