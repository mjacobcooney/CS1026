# this file has three functions that are used to compute the volume for the given shape.

# for pi
import cmath


# cube volume formula as a function
def cubeVolume(a):
    return int(a) ** 3


# pyramid volume formula as a function
def pyramidVolume(base, height):
    return ((1 / 3 * int(base)) ** 2) * int(height)


# ellipsoid volume formula as a function
def ellipsoidVolume(r1, r2, r3):
    return (4 / 3 * cmath.pi) * int(r1) * int(r2) * int(r3)
