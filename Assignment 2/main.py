# Formula of volumes are imported from volumes.py file
import volumes

def formatInput(textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine

# Prompt the user to enter their desired shape
count = 0
if __name__ == '__main__':
    my_list = []
    while (True):
        shape_choice = formatInput(input("Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): "))
    # Program will exit if user enters quit or q
        if shape_choice in ["quit", "q"]:
            if count == 0:
                print('Output: No shapes entered')
                quit()
            break
    # If input is not valid; error message is printed and prompts user to enter a valid input
        while formatInput(shape_choice) not in ['quit', 'q', 'cube', 'c', 'pyramid', 'p', 'ellipsoid', 'e']:
            shape_choice = input("Invalid input: Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): ")

    # Code will then prompt user to enter values for a cube; if user inputs cubes
        count = count + 1
        if shape_choice in ["cube", "c"]:
            cube_length = input('Enter length of side for the cube: ')
            # Code calls for the function of a cube
            volume = volumes.volume_of_cube(cube_length)
            print('The volume of a cube with side', cube_length, 'is: ', volume)
            # Value and shape is saved to my_list
            my_list.append(('cube', volume))

        # Code will then prompt user to enter values for a pyramid; if user inputs pyramid
        elif shape_choice in ["pyramid", "p"]:
            pyramid_base = input('Enter the base of the pyramid: ')
            pyramid_height = input('Enter the height of the pyramid:')
            # Code calls for the function of a pyramid
            volume = volumes.volume_of_pyramid(pyramid_base, pyramid_height)
            print('The volume of a pyramid with base', pyramid_base, 'and height', pyramid_height, 'is: ', volume)
            # Value and shape is saved to my_list
            my_list.append(('pyramid', volume))

        # Code will now prompt user to enter values for an ellipsoid; if user inputs ellipsoid
        elif shape_choice in ["ellipsoid", "e"]:
            radius1 = input('Enter the first radius: ')
            radius2 = input('Enter the second radius: ')
            radius3 = input('Enter the third radius: ')
            # Code calls for the function of an ellipsoid
            volume = volumes.volume_of_ellipsoid(radius1, radius2, radius3)
            print('The volume of an ellipsoid with radii', radius1, 'and', radius2, 'and', radius3, 'is: ', volume)
            # Value and shape is saved to my_list
            my_list.append(('ellipsoid', volume))

    # Saved shape and respective value will be sorted from smallest to largest volume
    length = len(my_list)
    my_list.sort(key=lambda my_list: my_list[1])
    print('Output: Volumes of shapes entered in sorted order: ')
    length = len(my_list)
    i = 0
    while i < length:
        print(my_list[i][0], my_list[i][1])
        i = i + 1

