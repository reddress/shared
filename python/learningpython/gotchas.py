# p. 507 loop in closures, need to add default argument
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)  # i=i is the default argument
    return acts

acts = makeActions()
acts[2](2)
acts[3](2)

# p. 658
# default arguments retain objects between calls
def saver(x=[]):
    x.append(2)
    print(x)

saver([3])  # default not used
saver()     # default used
saver()     # result grows with each call

# to prevent this behavior, set default inside function body.
def saver(x=None):
    if x is None:
        x = []
    x.append(1)
    print(x)
saver([1])
saver()

def counter(x=[0]):
    x[0] += 1
    print(x)

counter()

# import __main__ to access global

x = 99
def selector():
    import __main__
    print(__main__.x)
    x = 88
    print(x)
selector()
