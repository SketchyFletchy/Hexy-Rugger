"""Script to generate cool colour patterns over a hex grid."""

import sys
import json
import math
import random
import cairocffi as cairo

parameterSourceFile = "./parameters.json"

def main():
    """Main entry point of script."""
    param = loadParameters(parameterSourceFile)
    hexArray, yMax, xMax = genArray(**param)    
    colourMap = gencolourMap(yMax, param['colours'])
    svgHexDraw = genSVG(param['windowWidth'], param['windowHeight'])
    hexArray = [ colourMap(point, param['scatter']) for point in hexArray]
    [ svgHexDraw(point, param['hexHeight'], param['colours']) for point in hexArray ]

def loadParameters(parameterSource):
    """Pulls in config file and returns a queriable python dictionary."""
    try:
        with open(parameterSource, 'r') as paramFile:
            paramDict = json.load(paramFile)
    except OSError:
        print("Failed to parse parameters file.")
    return paramDict

def genArray(width, height, hexHeight, alternateRows, **kwargs):
    """Creates an array of hex origins and colour assignments."""
    outArray = []
    for row in range(height):
        xStep = hexHeight*math.sqrt(3)/2
        rowOffset =0
        if alternateRows == "in" and height%2 == 0:
            rowOffset = 1
        for piece in range(width - rowOffset):
            outArray.append((piece*xStep+((row % 2)*xStep/2), row*hexHeight*3/4, 0))
    yMax = outArray[-1][1]
    xMax = outArray[-1][0]
    return outArray, yMax, xMax

def gencolourMap( yMax, colArray ):
    """Massive cheat just for the moment, thanks Griff!"""
    def colourMap(point, scatterVal):
        colourNormal = (point[1] / yMax)+random.gauss(0, scatterVal)
        colourIndex = quantiseNormalToIndex( colourNormal, (len(colArray))) 
        outPoint = (point[0], point[1], colourIndex)
        return outPoint
    return colourMap

def quantiseNormalToIndex(normalVal, steps):
    """Return zero referenced index value by quantising input normal value."""
    level = math.floor(normalVal * steps)
    if level >= (steps-1):
        level = steps-1
    elif level <= 0:
        level = 0
    return level

def genSVG(height, width):
    """Outputs a .SVG file of the mapped hex tiles"""
    surface = cairo.SVGSurface("outputs/latest.svg", width, height)
    surface.set_document_unit(cairo.SVG_UNIT_MM)
    ctxt = cairo.Context(surface)
    ctxt.translate(10,10)
    def drawHex(point, hexHeight, colours):
        verts = [
            (point[0], point[1]+hexHeight/2),
            (point[0]+math.sqrt(3)*hexHeight/4, point[1]+hexHeight/4),
            (point[0]+math.sqrt(3)*hexHeight/4, point[1]-hexHeight/4),
            (point[0], point[1]-hexHeight/2),
            (point[0]-math.sqrt(3)*hexHeight/4, point[1]-hexHeight/4),
            (point[0]-math.sqrt(3)*hexHeight/4, point[1]+hexHeight/4)
        ]
        for coord in verts:
            ctxt.line_to(coord[0],coord[1])
        ctxt.close_path()
        ctxt.set_source_rgb(0,0,0)
        ctxt.set_line_width(1)
        ctxt.stroke_preserve()
        ctxt.set_source_rgb(*colours[point[2]])
        ctxt.fill()
    return drawHex

if __name__ == '__main__':
    sys.exit(main())