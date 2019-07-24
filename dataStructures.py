from collections import namedtuple

#Define Data Structures
Point = namedtuple('Point', ['x', 'y'])
Ball = namedtuple('Ball', ['center', 'radius', 'color', 'velocity'])
Brick = namedtuple('Brick', ['topLeft', 'bottomRight', 'color', 'health'])
Paddle = namedtuple('Paddle', ['topLeft', 'bottomRight', 'color'])
