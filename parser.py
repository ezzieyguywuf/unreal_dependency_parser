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

def generateParseDict(treeRoot: ET.Element):
    """Returns a dictionary containing the hierarchical parsed data

       The hierarchy is Pack→Blob→FilePath

       A Pack is some sort of archive stored on the Epic servers. Each Pack
       contains one or more Blobs

       A Blob is an actual file. It will be located in one or more FilePath's

       I FilePath is an actual location on disk.
    """
    out = {}
    return out
