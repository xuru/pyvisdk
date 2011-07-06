import os.path
import sys

# make sure that we are pulling in the right module for testing...
here = os.path.expanduser(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(here, ".."))
