from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from engine import RenderEngine
from light import Light
from material import Material, ChequeredMaterial

WIDTH = 320
HEIGHT = 200
RENDERED_IMG = "2balls.ppm"
CAMERA = Vector(0, -0.35, -1)
OBJECTS = [
    # Ground Plane
    Sphere(Point(0, 10000.5, 1), 10000.0, ChequeredMaterial(color1 = Color.from_hex("#420500"), color2 = Color.from_hex("#e6b87d"), ambient = 0.2, reflection = 0.2)),
    # Blue Ball
    Sphere(Point(0.75, -0.1, 1.0), 0.6, Material(Color.from_hex("#0000FF"))),
    # Pink Ball
    Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#803980")))
]
LIGHTS = [
    Light(Point(1.5, -0.5, -10.0), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0.0), Color.from_hex("#E6E6E6"))]
