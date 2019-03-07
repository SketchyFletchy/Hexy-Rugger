"""Script to generate cool colour patterns over a hex grid."""

import sys
import json

parameterSourceFile = "./parameters.json"


def main():
    """Main entry point of script."""
    param = loadParameters(parameterSourceFile)

    pass

def loadParameters(parameterSource):
    """Pulls in parameters from parameters.json config file and returns a queriable python dictionary."""
    try:
        with open(parameterSource, 'r') as paramFile:
            paramDict = json.load(paramFile)
    except OSError:
        print("Failed to parse parameters file.")
    return paramDict

def genArray(width, height):
    """Creates an array of hex origins and colour assignments."""
    for 

def generateSVG():
    """outputs a .csv file of the mapped hex tiles"""
    pass



if __name__ == '__main__':
    sys.exit(main())