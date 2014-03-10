# p. 809

class rec: pass

rec.name = 'Bob'
rec.age = 30

x = rec()
y = rec()

rec.name
x.name
rec.name = "joe"

y.name
y.name = "Sarah"

rec.__dict__

def f(obj):
    print("f")

rec.f = f
y.f()
