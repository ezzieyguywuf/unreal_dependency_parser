from dataclasses import dataclass,field
from collections import defaultdict
import xml.etree.ElementTree as ET

@dataclass
class FileData:
    filepath: str

@dataclass
class FilePathData:
    filePath: str
    isExecutable: bool

@dataclass
class BlobData:
    hash: str
    size: int
    offset: int
    paths: list[FilePathData] = field(default_factory=list)

@dataclass
class PackData:
    hash: str
    remotePath: str
    compressedSize: int
    size: int
    blobs: list[BlobData] = field(default_factory=list)

# Expects a filename, which will contain the xml data. No error-handling is
# currently incorporated - so make sure it's an actual xml file
def parseFile(fname: str) -> ET.ElementTree:
    print("trying to parse {}".format(fname))
    return ET.parse(fname)

def generateParsedData(treeRoot: ET.Element):
    """Returns a list Pack objects containing hierarchical data needed for fetching

       The hierarchy is Pack → Blob → FilePath

       A Pack is some sort of archive stored on the Epic servers. Each Pack
       contains one or more Blobs

       A Blob is an actual file. It will be located in one or more FilePath's

       I FilePath is an actual location on disk.
    """
    pathDict = defaultdict(list)
    blobDict = defaultdict(list)

    for path in treeRoot.find("Files").findall("File"):
        filePath = path.attrib['Name']
        hash = path.attrib['Hash']
        isExecutable = False
        if 'IsExecutable' in path.attrib.keys():
            if 't' == path.attrib['IsExecutable'].lower()[0]:
                isExecutable = True
        pathDict[hash].append(
            FilePathData(filePath, isExecutable)
        )

    for blob in treeRoot.find("Blobs").findall("Blob"):
        blobHash = blob.attrib['Hash']
        blobSize = blob.attrib['Size']
        blobOffset = blob.attrib['PackOffset']
        packHash = blob.attrib['PackHash']
        paths = pathDict[blobHash]
        blobDict[packHash].append(
            BlobData(blobHash, blobSize, blobOffset, paths)
        )

    packs = []
    for pack in treeRoot.find("Packs").findall("Pack"):
        packHash = pack.attrib['Hash']
        packSize = pack.attrib['Size']
        packCompressedSize = pack.attrib['CompressedSize']
        remotePath = pack.attrib['RemotePath']
        blobs = blobDict[packHash]
        packs.append(
            PackData(packHash, remotePath, packCompressedSize, packSize, blobs)
        )

    return packs
