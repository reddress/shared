"""
module doc
words go here
"""

spam = 30

def square(x):
    """
    fun def
    can we haz liver?
    """
    return x ** 2

class Employee:
    "class doc"
    pass

print(square(4))
print(square.__doc__)

# p. 466 quiz
# 1. multi-line and for it to be available to pydoc
# 2. help, __doc__, pydoc
# 3. dir(obj)
# 4. running pydoc gui or top-level browser in -b mode
# 5. pirate moar
