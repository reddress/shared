"""
p. 939

Superclass that takes an input and output stream, sending data that is
modified by a converter.
"""

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        # raise error if subclass does not define it
        assert False, 'converter must be defined'

