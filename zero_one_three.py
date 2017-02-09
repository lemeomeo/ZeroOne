#!usr/bin/env python
import sys, base64
code=str(sys.argv)
print base64.b64decode(code)