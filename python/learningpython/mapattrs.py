# p. 1004

import pprint
def trace(x, label='', end='\n'):
    print(label + pprint.pformat(x) + end)

def filterdictvals(d, v):
    """
    remove entries with value v from dict d
    """
    return {K: V2 for (K, V2) in d.items() if V2 != v}

def invertdict(d):
    """
    swap keys and values (grouped by values)
    """
    def keysof(v):
        return sorted(k for k in d.keys() if d[k] == v)
    return {v: keysof(v) for v in set(d.values())}

def dflr(cls):
    """
    classic depth-first left to right order
    """
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here

def inheritance(instance):
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)

def mapattrs(instance, withobject=False, bysource=False):
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__:
                attr2obj[attr] = obj
                break

    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)

def test():
    print('new style in 3.x')
    class A: attr1 = 1
    class B(A): attr2 = 2
    class C(A): attr1 = 3
    class D(B, C): pass
    i = D()
    print("py=> %s" % i.attr1)
    trace(inheritance(i), 'INH\n')
    trace(mapattrs(i), 'attrs\n')
    trace(mapattrs(i, bysource=True), 'objs\n')

def testslots():
    class A(object): __slots__ = ['a', 'b']; x = 1; y = 2
    class B(A): __slots__ = ['b', 'c']
    class C(A): x = 2
    class D(B, C):
        z = 3
        def __init__(self): self.name = "Bob"

    I = D()
    trace(mapattrs(I, bysource = True))

testslots()
