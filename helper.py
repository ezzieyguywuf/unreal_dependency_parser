import xml.etree.ElementTree as ET

# Expects a filename, which will contain the xml data. No error-handling is
# currently incorporated - so make sure it's an actual xml file
def parseFile(fname: str) -> ET:
    print("trying to parse {}".format(fname))
    return ET.parse(fname)
