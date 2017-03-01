from browser import document

def square(x):
    return x * x;

def compute(event):
    inpt = int(document['inpt'].value)
    result = square(inpt)
    document['result'].value += str(result) + "\n"
    
document['compute'].bind("click", compute)
