import importlib

import sys
import os

sub_dir_1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(sub_dir_1)

from config.configuracion import *

print(sub_dir_1)




#
