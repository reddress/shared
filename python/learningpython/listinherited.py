class ListInherited:
    """
    use dir() to collect instance attrs and names inherited
    """
    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\t%s' % attr
            else:
                result += '\n\t%s=%s' % (attr, getattr(self, attr))
        return result

    def __attrnames2(self, indent=" "*4):
        result = "unders%s\n%s%%s\nOthers%s\n" % ('-'*72, indent, '-'*72)
        unders = []
        for attr in dir(self):
            if attr[:2] == "__" and attr[-2:] == "__":
                unders.append(attr)
            else:
                display = str(getattr(self,attr))[:75-(len(indent) + len(attr))]
                result += "%s%s=%s\n" % (indent, attr, display)
        return result % ", ".join(unders)

    def __str__(self):
        return "<instance of %s, addr %s \n%s>" % (
            self.__class__.__name__,
            id(self),
            self.__attrnames2())
import testmixin
testmixin.tester(ListInherited)
