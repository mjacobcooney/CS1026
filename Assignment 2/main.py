##
# This program takes user input and computes the volume for three different shapes and exports the list to a file

# Import functions from volume.py and summarize.py
import volume
import summarize

outfile = open("output.txt", "w")

# valid input options
validInputOptions = ["cube", "c", "pyramid", "p", "ellipsoid", "e"]
madeInput = False
selection = ''
# lists
cubeList = []
ellipsoidList = []
pyramidList = []


# Prior given code to format inputs
def formatInput(textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine


testCaseNum = input("Please enter the test case number:")
while not madeInput:
    # prompt for shape name
    selection = input("Enter shape (quit or q to terminate): cube, pyramid, ellipsoid,:\n")
    # format input
    selection = formatInput(selection)
    # if selection is valid
    if validInputOptions.__contains__(selection):
        if selection == "cube" or selection == "c":
            # prompt for dimensions
            a = input("Enter the dimensions of the cube: \n")
            # get cube volume formula
            cubeVolume = volume.cubeVolume(a)
            # add to list
            cubeList.append(cubeVolume)
        elif selection == "pyramid" or selection == "p":
            # prompt for dimensions
            base, height = input("Enter the two values of pyramid base and height (separated by space): \n").split()
            # get pyramid volume formula
            pyramidVolume = volume.pyramidVolume(base, height)
            # add to list
            pyramidList.append(pyramidVolume)
        elif selection == "ellipsoid" or selection == "e":
            # prompt for dimensions
            r1, r2, r3 = input("Enter the three values of ellipsoid radii (separated by space): \n").split()
            # get ellipsoid volume formula
            ellipsoidVolume = volume.ellipsoidVolume(r1, r2, r3)
            # add to list
            ellipsoidList.append(ellipsoidVolume)
    elif selection == "quit" or selection == "q":
        madeInput = True
        # ensures correct statment is printed if no calculations entered
        if len(cubeList + pyramidList + ellipsoidList) == 0:
            print("You have reached the end of your session.\nYou did not perform and volume calculations.")
        else:
            # sorts the list from smallest to largest
            cubeList.sort(reverse=False)
            pyramidList.sort(reverse=False)
            ellipsoidList.sort(reverse=False)
            # title text for the table of printed values
            print("You have reached the end of your session.\n")
            print("The volumes calculated for each shape are:\n")
            # if there are values in the specific shape's list print them rounded to 3 decimal places
            if len(cubeList) > 0:
                for shape in cubeList:
                    round(shape, 3)
                print("Cube: ", *cubeList)
            # if not values entered print no shapes entered
            else:
                print("Cube: No shapes entered")
            # if there are values in the specific shape's list print them rounded to 3 decimal places
            if len(pyramidList) > 0:
                for shape in pyramidList:
                    round(shape, 3)
                print("Pyramid: ", *pyramidList)
            # if not values entered print no shapes entered
            else:
                print("Pyramid: No shapes entered")
            # if there are values in the specific shape's list print them rounded to 3 decimal places
            if len(ellipsoidList) > 0:
                for shape in ellipsoidList:
                    round(shape, 3)
                print("Ellipsoid: ", *ellipsoidList)
            # if not values entered print no shapes entered
            else:
                print("Ellipsoid: No shapes entered")
            summarize.summarize(cubeList, pyramidList, ellipsoidList, testCaseNum)
    # prompt use for valid input if selection is not a valid input option
    else:
        print("Please select valid input")

outfile.close()
