

from . import base62_encode, base62_decode, Geoid, make_classes
import sys

class AcsGeoid(Geoid):

    sl = None
    fmt = None

    class_map = {}
    sl_map = {}
    name_map = {}

    sl_width = 3
    width_pos = 1
    sl_format = '{sl:0>3d}00US' # The '00' bit is for the geo component, always 00 in our use.
    elem_format = '{{{}:0{}d}}'
    sl_regex = '(?P<sl>.{3})00US'
    elem_regex = '(?P<{}>.{{{}}})'
    encode = lambda x: int(x)
    decode = lambda x: int(x)

    @classmethod
    def class_factory(cls, name):
        def __init__(self, *args, **kwargs):
            cls.__init__(self, *args, **kwargs)

        return type(name, (cls,), {"__init__": __init__})

    def summarize(self):
        """Convert all of the values to their max values. This form is used to represent the summary level"""

        s = str(self.allval())

        return self.parse(s[:7] + ''.join(['9'] * len(s[7:])))


make_classes(AcsGeoid, sys.modules[__name__])