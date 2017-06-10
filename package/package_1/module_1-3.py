import sys
import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('../package')

print sys.path

sys.path.pop()

print sys.path