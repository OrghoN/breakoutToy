from collections import namedtuple

#Define Data Structures
Point = namedtuple('Point', ['x', 'y'])
Ball = namedtuple('Ball', ['center', 'radius', 'color', 'velocity', 'graphical'])
Brick = namedtuple('Brick', ['topLeft', 'bottomRight', 'color', 'health', 'graphical'])
Paddle = namedtuple('Paddle', ['topLeft', 'bottomRight', 'color', 'graphical'])
