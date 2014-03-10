import types
from imp import reload

def status(module):
    print('reloading '+module.__name__)

def tryreload(module):
    try:
        reload(module)
    except:
        print('failed module reload %s' % module)

def transitive_reload(module, visited):
    if not module in visited:
        status(module)
        tryreload(module)
        visited[module] = True
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

def tester(reloader, modname):
    import importlib, sys
    if len(sys.argv) > 1: modname = sys.argv[1]
    module = importlib.import_module(modname)
    reloader(module)

if __name__ == '__main__':
    tester(reload_all, 'reloadall')

