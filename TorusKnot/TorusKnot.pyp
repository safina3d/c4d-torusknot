"""
  author  : Safina3D
  version : 1.0.0
  website : https://safina3d.blogspot.com
"""


import os
import c4d
from c4d import plugins, bitmaps, Vector, SplineObject
from math import cos, sin, pi


class TorusKnot (plugins.ObjectData):

    def __init__ (self):
        self.SetOptimizeCache(True)

    def Init(self, node):
        # Parameter initialization
        self.InitAttr(node, float, [c4d.KNOT_RANGE_MIN])
        self.InitAttr(node, float, [c4d.KNOT_RANGE_MAX])
        self.InitAttr(node, float, [c4d.KNOT_STEP])

        self.InitAttr(node, float, [c4d.KNOT_PARAM_R0])
        self.InitAttr(node, float, [c4d.KNOT_PARAM_R1])
        self.InitAttr(node, float, [c4d.KNOT_PARAM_N])

        self.InitAttr(node, bool, [c4d.KNOT_CUBIC_INTERPOLATION])
        self.InitAttr(node, bool, [c4d.KNOT_CLOSE_SPLINE])

        self.InitAttr(node, str, [c4d.KNOT_POINT_COUNT])

        # Set default values
        node[c4d.KNOT_RANGE_MIN] = 0.0
        node[c4d.KNOT_RANGE_MAX] = 2.0
        node[c4d.KNOT_STEP] = 0.1
        node[c4d.KNOT_PARAM_R0] = 200.0
        node[c4d.KNOT_PARAM_R1] = 0.0
        node[c4d.KNOT_PARAM_N] = 1.0
        node[c4d.KNOT_CUBIC_INTERPOLATION] = False
        node[c4d.KNOT_CLOSE_SPLINE] = True
        node[c4d.KNOT_POINT_COUNT] = '0'

        return True

    def GetVirtualObjects(self, op, hh):
        # Retreive UI data values
        range_min = op[c4d.KNOT_RANGE_MIN] * pi
        range_max = op[c4d.KNOT_RANGE_MAX] * pi
        step = op[c4d.KNOT_STEP] * pi
        R = op[c4d.KNOT_PARAM_R0]
        r = op[c4d.KNOT_PARAM_R1]
        n = op[c4d.KNOT_PARAM_N]
        is_cubic = op[c4d.KNOT_CUBIC_INTERPOLATION]

        # Calculate all points' position
        points = []
        t = range_min
        while t < range_max:
            c = R + r * cos(n * t)
            x = c * cos(t)
            y = c * sin(t)
            z = r * sin(n * t)

            points.append(Vector(x, y, z))
            t += step

        # Spline initialization
        point_count = len(points)
        spline_type = c4d.SPLINETYPE_CUBIC if is_cubic else c4d.SPLINETYPE_LINEAR
        spline = SplineObject(point_count, spline_type)

        if spline is None: return

        # Update spline points
        for index, point in enumerate(points):
            spline.SetPoint(index, point)

        # Update UI point count
        op[c4d.KNOT_POINT_COUNT] = str(point_count)

        # Close the spline if needed
        spline[c4d.SPLINEOBJECT_CLOSED] = op[c4d.KNOT_CLOSE_SPLINE]

        # Send update message
        spline.Message(c4d.MSG_UPDATE)

        return spline


if __name__ == "__main__":
    # Load the plugin icon
    icon_absolute_path = os.path.join(os.path.dirname(__file__), 'res/icons', 'knot.png')
    plugin_icon = bitmaps.BaseBitmap()
    plugin_icon.InitWith(icon_absolute_path)

    # Register the plugin
    plugins.RegisterObjectPlugin(
        id = 1053564,
        str = 'Torus Knot',
        g =  TorusKnot,
        description = 'Oknot',
        info = c4d.OBJECT_GENERATOR | c4d.OBJECT_ISSPLINE,
        icon = plugin_icon
    )
