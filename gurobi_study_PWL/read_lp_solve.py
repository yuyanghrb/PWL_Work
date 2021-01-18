#%%

import os
import math
import time
import itertools
import numpy as np
import pandas as pd
from gurobipy import *
from gurobipy import Model, quicksum, GRB
import gurobipy as gp


#%% 

# Create model on Gurobi
# model = gp.read('model_1.lp')

model = gp.read('QCP_400_40_1_80_80_1.lp')
# not working with previous LP files.
# %%
