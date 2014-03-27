import os, sys

def init():
    if sys.platform == 'win32':
        os.chdir("c:/users/heitor/desktop/emacs-24.3/bin/shared/python/mandarinrhymes/")
    else:
        os.chdir("/home/mandarinpandarin/rhymes/rhymes/rhymeapp")
