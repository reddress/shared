# p. 691 imports are assignments, not special compile-time declarations.
# imports may appear in if tests, in function defs, trys, etc.

import importer5

importer5.importer3.small.x

import pkg.spam

# p. 742 quiz
"""
1. identify dir as package, and run init code when imported
2. use as keyword
3. packages
4. absolute imports
5. . is relative import and can only be used as package
6. directory not having init, can span many physical directories

# use if __name__ == '__main__':
# to modify behavior if run as program or if imported

"""
p. 777 quiz
1. will not get imported by from * statement
2. it is being run as a program
3. importlib.import_module
4. not as robust, can alter order of imports
5. o no wai
"""
