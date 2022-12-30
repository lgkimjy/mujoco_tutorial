import mujoco as mj
from mujoco.glfw import glfw
import numpy as np
import os
from robot import Robot

simend = 5

def main():

    glfw.init()
    window = glfw.create_window(1200, 900, "Demo", None, None)
    # sim = Sim(xml_path='../models/robots/agility_cassie/scene.xml', window=window)
    robot = Robot(config='../models/robots/agility_cassie/scene.xml', simrate=60.0, window=window)
    
    glfw.make_context_current(window)
    glfw.swap_interval(1)

    mj.mjv_defaultCamera(robot.sim.cam)
    mj.mjv_defaultOption(robot.sim.opt)
    context = mj.MjrContext(robot.sim.model, mj.mjtFontScale.mjFONTSCALE_150.value)

    glfw.set_key_callback(window, robot.sim.keyboard)
    glfw.set_cursor_pos_callback(window, robot.sim.mouse_move)
    glfw.set_mouse_button_callback(window, robot.sim.mouse_button)
    glfw.set_scroll_callback(window, robot.sim.scroll)

    while not glfw.window_should_close(robot.sim.window):
        time_prev = robot.sim.data.time

        while (robot.sim.data.time - time_prev < 1.0/robot.simrate):
            mj.mj_step(robot.sim.model, robot.sim.data)

        if (robot.sim.data.time >= simend):
            break;

        # get framebuffer viewport
        viewport_width, viewport_height = glfw.get_framebuffer_size(window)
        viewport = mj.MjrRect(0, 0, viewport_width, viewport_height)

        if(True):
            print('cam.azimuth =', robot.sim.cam.azimuth,';','cam.elevation =',robot.sim.cam.elevation,';','cam.distance = ',robot.sim.cam.distance)
            print('cam.lookat =np.array([',robot.sim.cam.lookat[0],',',robot.sim.cam.lookat[1],',',robot.sim.cam.lookat[2],'])')

        # Update scene and render
        mj.mjv_updateScene(robot.sim.model, robot.sim.data, robot.sim.opt, None, robot.sim.cam, mj.mjtCatBit.mjCAT_ALL.value, robot.sim.scene)
        mj.mjr_render(viewport, robot.sim.scene, context)

        # swap OpenGL buffers && process pending GUI events, call GLFW callbacks
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()