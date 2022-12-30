import mujoco as mj
from mujoco.glfw import glfw
import numpy as np
import os

class Sim:

    def __init__(self, xml_path, window):
        self.model = mj.MjModel.from_xml_path(xml_path)  # MuJoCo model
        self.data = mj.MjData(self.model)                     # MuJoCo data
        self.cam = mj.MjvCamera()                        # Abstract camera
        self.opt = mj.MjvOption()                        # visualization options

        self.window = window
        self.scene = mj.MjvScene(self.model, maxgeom=10000)

        self.lastx = 0
        self.lasty = 0
        self.button_left = False
        self.button_middle = False
        self.button_right = False

    def keyboard(self, window, key, scancode, act, mods):
        if act == glfw.PRESS and key == glfw.KEY_BACKSPACE:
            mj.mj_resetDataKeyframe(self.model, self.data, 0)
            mj.mj_forward(self.model, self.data)

    def mouse_move(self, window, xpos, ypos):
        dx = xpos - self.lastx
        dy = ypos - self.lasty
        self.lastx = xpos
        self.lasty = ypos

        # no buttons down: nothing to do
        if (not self.button_left) and (not self.button_middle) and (not self.button_right):
            return

        # get current window size
        width, height = glfw.get_window_size(self.window)

        # get shift key state
        PRESS_LEFT_SHIFT = glfw.get_key(self.window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS
        PRESS_RIGHT_SHIFT = glfw.get_key(self.window, glfw.KEY_RIGHT_SHIFT) == glfw.PRESS
        self.mod_shift = (PRESS_LEFT_SHIFT or PRESS_RIGHT_SHIFT)

        # determine action based on mouse button
        if self.button_right:
            if self.mod_shift:
                self.action = mj.mjtMouse.mjMOUSE_MOVE_H
            else:
                self.action = mj.mjtMouse.mjMOUSE_MOVE_V
        elif self.button_left:
            if self.mod_shift:
                self.action = mj.mjtMouse.mjMOUSE_ROTATE_H
            else:
                self.action = mj.mjtMouse.mjMOUSE_ROTATE_V
        else:
            self.action = mj.mjtMouse.mjMOUSE_ZOOM

        mj.mjv_moveCamera(self.model, self.action, dx/height, dy/height, self.scene, self.cam)

    def mouse_button(self, window, button, act, mods):
        self.button_left = (glfw.get_mouse_button(self.window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS)
        self.button_middle = (glfw.get_mouse_button(self.window, glfw.MOUSE_BUTTON_MIDDLE) == glfw.PRESS)
        self.button_right = (glfw.get_mouse_button(self.window, glfw.MOUSE_BUTTON_RIGHT) == glfw.PRESS)
        # update mouse position
        glfw.get_cursor_pos(self.window)

    def scroll(self, window, xoffset, yoffset):
        self.action = mj.mjtMouse.mjMOUSE_ZOOM
        mj.mjv_moveCamera(self.model, self.action, 0.0, -0.05 * yoffset, self.scene, self.cam)