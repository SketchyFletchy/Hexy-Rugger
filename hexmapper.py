"""Script to generate cool colour patterns over a hex grid."""

import sys
import json

parameterSourceFile = "./parameters.json"


def main():
    """Main entry point of script."""
    param = loadParameters(parameterSourceFile)
    hexArray = genArray(param["width"], param["height"], param["hexWidth"], param["alternateRows"])
    hexArray = colourMap()
    pass

def loadParameters(parameterSource):
    """Pulls in config file and returns a queriable python dictionary."""
    try:
        with open(parameterSource, 'r') as paramFile:
            paramDict = json.load(paramFile)
    except OSError:
        print("Failed to parse parameters file.")
    return paramDict

def genArray(width, height, hexWidth, alternateRows):
    """Creates an array of hex origins and colour assignments."""
    outArray = []
    for row in range(height):
        rowOffset =0
        if alternateRows == "in" and height%2 == 0:
            rowOffset = 1
        for piece in range(width - rowOffset):
            outArray.append((piece*hexWidth+((row % 2)*hexWidth/2), row*hexWidth/1.73205, 0, 0, 0))
    return outArray

def colourMap (angle, scatter)

def generateSVG():
    """outputs a .csv file of the mapped hex tiles"""
    pass

if __name__ == '__main__':
    sys.exit(main())