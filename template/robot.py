#!/usr/bin/env python3

import mujoco as mj
import numpy as np
import math
import os
from mujoco.glfw import glfw
from sim import Sim

class Robot:
    
    def __init__(self, config=False, simrate=60, window=False):
        self.config = config
        self.window = window
        self.sim = Sim(self.config, self.window)
        self.simrate = simrate

    def step_simulation(self):
        pass

    def debug(self):
        print(self.sim.ctrl[0])