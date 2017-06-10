import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import module_2
import module_3

# from .. import module_2
# from .. import module_3

module_2.func_2()
module_3.func_3()

sys.path.pop()