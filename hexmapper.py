"""Script to generate cool colour patterns over a hex grid."""

import sys
import json
import math

parameterSourceFile = "./parameters.json"

def main():
    """Main entry point of script."""
    param = loadParameters(parameterSourceFile)
    hexArray, yMax, xMax = genArray(**param)    
    colourMap = gencolourMap(yMax, param['colours'])
    hexArray = [ colourMap(point) for point in hexArray]
    # GENERATE AN SVG FROM ARRAY INPUTS
    pass

def loadParameters(parameterSource):
    """Pulls in config file and returns a queriable python dictionary."""
    try:
        with open(parameterSource, 'r') as paramFile:
            paramDict = json.load(paramFile)
    except OSError:
        print("Failed to parse parameters file.")
    return paramDict

def genArray(width, height, hexWidth, alternateRows, **kwargs):
    """Creates an array of hex origins and colour assignments."""
    outArray = []
    for row in range(height):
        rowOffset =0
        if alternateRows == "in" and height%2 == 0:
            rowOffset = 1
        for piece in range(width - rowOffset):
            outArray.append((piece*hexWidth+((row % 2)*hexWidth/2), row*hexWidth/1.73205, 0))
    yMax = outArray[-1][1]
    xMax = outArray[-1][0]
    print("Max position: ({},{})".format(xMax, yMax))
    return outArray, yMax, xMax

def gencolourMap( yMax, colArray ):
    """Massive cheat just for the moment, thanks Griff!"""
    def colourMap(point):
        colourIndex = math.floor((len(colArray)-1)*(point[1] / yMax)) 
        outPoint = (point[0], point[1], colourIndex)
        return outPoint
    return colourMap

def generateSVG():
    """outputs a .csv file of the mapped hex tiles"""
    pass

if __name__ == '__main__':
    sys.exit(main())