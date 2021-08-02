# Ensure that the program is able to receive both upper and lowercase; robust to whitespace

def formatInput(textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine
# Volume of a cube is calculated and returned
def volume_of_cube(cube_length):
    cube_volume = int(cube_length) * int(cube_length) * int(cube_length)
    return cube_volume

# Volume of a pyramid is calculated and returned
def volume_of_pyramid(pyramid_base, pyramid_height):
    pyramid_volume = (int(pyramid_base) * int(pyramid_base) / 3) * int(pyramid_height)
    return pyramid_volume

# Volume of a ellipsoid is calculated and returned
def volume_of_ellipsoid(radius1, radius2, radius3):
    pi_val = 3.141599265
    ellipsoid_volume = (4/3 * pi_val) * int(radius1) * int(radius2) * int(radius3)
    return ellipsoid_volume
