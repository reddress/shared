"""
generic lister mixin tester
"""
import importlib

def tester(listerclass, sept=False):
    class Super:
        __slots__ = ['dataSuper']
        def __init__(self):
            self.data1 = 'spam'
        def ham(self):
            pass

    class Sub(Super, listerclass):
        __slots__ = ['dataSub']
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42
        def spam(self):
            pass

    instance = Sub()
    print(instance)
    if sept: print("-" * 77)

def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    listerclass = getattr(modobject, classname)
    tester(listerclass, sept)

testByNames('listinstance', 'ListInstance', True)
# testByNames('listinherited', 'ListInherited', True)
# testByNames('listtree', 'ListTree', False)
