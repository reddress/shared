# from . import importer3

from pkg.eggs import aardvark as a, bison as b
import imp

imp.reload(pkg.eggs)
a
b
