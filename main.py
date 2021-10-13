#!/usr/bin/env python
# first line to maek life easiier for unix suers
"""Pure Python Raytracer by Joao Kalva and totally not an youtube guy"""
import argparse
import importlib
import os
from multiprocessing import cpu_count

from engine import RenderEngine
from scene import Scene

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (without .py extension. E.g. examples.twoballs)")
    parser.add_argument("-p", "--processes", action="store", type=int, dest="processes", default=0, help="Number of processes (default = 0)")
    args = parser.parse_args()
    if args.processes == 0:
        process_count = cpu_count()
    else:
        process_count = args.processes
    mod = importlib.import_module(args.scene)
    
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()
    
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))    
    with open(mod.RENDERED_IMG, "w") as img_fileobj:
        engine.render_multiprocess(scene, process_count, img_fileobj)

if __name__ == "__main__":
    main()