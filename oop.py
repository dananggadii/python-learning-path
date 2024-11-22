class MySelf:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Nama saya {self.name} dan umur {self.age}"
  
  def myfunc(self):
    return f"Perkenalkan saya {self.name}"



p1 = MySelf('Danang', 19)
print(p1)
print(p1.myfunc())

