class Me:
  
  meCount = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Me.meCount += 1
  
  def displayName(self):
    print(self.name)

  def displayAge(self):
    print(self.age)

iam = Me("Takkar", 18)
iam.age = 19
iam.displayAge()

print(hasattr(iam, 'name'))
print(getattr(iam, "name"))
# setattr()
# delattr()

print(Me.meCount)

iam2 = Me("Faiyaz", 18)
iam3 = Me("F", 18)

print(Me.meCount)
print(Me.__name__)
