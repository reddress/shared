from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

import sys
obj = Uppercase(open('streams.py'), sys.stdout)
obj.process()
