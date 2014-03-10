x = 1
def nester():
    x = 2
    print(x)
    class C:
        x = 3
        print(x)
        def method1(self):
            print("method 1 x", x)
            print("method 1 self.x", self.x)
        def method2(self):
            x = 4
            print("method 2 x", x)
            self.x = 5
            print("method 2 self.x", self.x)
    j = C()
    j.method1()
    j.method2()

print(x)
nester()
print('-'*30)

class Super:
    def hello(self):
        self.data1 = 'super hello'
class Sub(Super):
    def hola(self):
        self.data2 = 'sub hola'

x = Sub()
x.__dict__
x.__class__
Sub.__bases__
Super.__bases__

Super.b = 2
y = Super()
y.b
x.__dict__
x.hello()
x.hola()
x.__dict__
Sub.__dict__
Super.__dict__
