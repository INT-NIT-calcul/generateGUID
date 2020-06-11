#!/usr/bin/python
import sys
from generateGUID import generate_GUID, generate_GUID2


if len(sys.argv) > 1:

    if len(sys.argv) == 5:
        guid=generate_GUID2(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
        print(guid)
        sys.exit(0)
    elif len(sys.argv) == 2:
        key = sys.argv[1]
        guid=generate_GUID(key)
        print(guid)
        sys.exit(0)
    else:
        print("mauvais nombre d'arguments: {}".format(len(sys.argv)))

sys.exit(-1)
