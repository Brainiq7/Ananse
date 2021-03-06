#!/usr/bin/env python
from __future__ import unicode_literals

# Execute with
# $ python ananse_dl/__main__.py (2.6+)
# $ python -m ananse_dl          (2.7+)

import sys

if __package__ is None and not hasattr(sys, "frozen"):
    # direct call of __main__.py
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(os.path.dirname(path)))

import ananse_dl

if __name__ == '__main__':
    ananse_dl.main()
