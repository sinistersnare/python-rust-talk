from ctypes import Structure, CDLL, c_double, pointer, POINTER

class POINT(Structure):
	_fields_ = [("x", c_double), ("y", c_double)]

rlib = CDLL("points.dll")

rlib.point_new.restype = POINTER(POINT)
rlib.point_new.argtypes = [c_double, c_double]

rlib.point_origin.restype = POINTER(POINT)
rlib.point_origin.argtypes = []

rlib.point_distance.restype = c_double
rlib.point_distance.argtypes = [POINTER(POINT), POINTER(POINT)]

rlib.point_x.restype = c_double
rlib.point_x.argtypes = [POINTER(POINT)]

rlib.point_y.restype = c_double
rlib.point_y.argtypes = [POINTER(POINT)]

a = rlib.point_new(c_double(1.0), c_double(3.5))
b = rlib.point_origin()

dist = rlib.point_distance(a, b)

print("distance: {}".format(dist))
