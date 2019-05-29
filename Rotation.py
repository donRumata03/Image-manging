import math

def rotate(origin, point, angle):
 ox, oy = origin
 px, py = point
 qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
 qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
 return qx, qy