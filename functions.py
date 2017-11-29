def printme(str):
  """This will print"""
  print(str)
  return

printme("Hello, World!!")

def me(name, age=18):
  print(name, age)
  return

me("Takkar")

def something(var1, *vartuple):
  print(var1)
  for e in vartuple:
    print(e)
  return

something(1, 2, 3, 4)

sum = lambda arg1, arg2: arg1 + arg2

print(sum(10, 2))
