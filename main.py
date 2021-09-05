#!/usr/bin/env python
# first line to maek life easiier for unix suers
"""Pure Python Raytracer by Joao Kalva and totally not an youtube guy"""
import argparse
import importlib
import os

from engine import RenderEngine
from scene import Scene

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (with .py extension)")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)
    
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))    
    with open(mod.RENDERED_IMG, "w") as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()