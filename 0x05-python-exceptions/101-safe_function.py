#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except Exception as t:
        print("Exception: {}".format(t), file=sys.stderr)
        return None
