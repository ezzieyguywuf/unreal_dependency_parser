from dataclasses import dataclass
import xml.etree.ElementTree as ET

@dataclass
class FileData:
    filepath: str

@dataclass
class PackData:
    hash: str
    remotePath: str
    compressedSize: int
    size: int

@dataclass
class BlobData:
    hash: str
    size: int
    offset: int

@dataclass
class FilePathData:
    filePath: str
    isExecutable: bool

# Expects a filename, which will contain the xml data. No error-handling is
# currently incorporated - so make sure it's an actual xml file
def parseFile(fname: str) -> ET.ElementTree:
    print("trying to parse {}".format(fname))
    return ET.parse(fname)

def generateHashMap(treeRoot: ET.Element):
    out = {}
    for child in treeRoot.find('Files').findall('File'):
        fpath = child.attrib['Name']
        fhash = child.attrib['Hash']
        out[fhash] = FileData(fpath)
    return out
