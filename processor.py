import gzip
import hashlib
import os
import os.path
import shutil

TARGET_DIR = "output"

def processPaths(blob, blobData):
    for path in blob.paths:
        dirname = os.path.join(TARGET_DIR, os.path.dirname(path.filePath))
        targetPath = os.path.join(TARGET_DIR, path.filePath)
        # This will create the directory if it doesn't exist
        os.makedirs(dirname, exist_ok=True)
        with open(targetPath, 'wb') as outfile:
            outfile.write(blobData)
        if path.isExecutable:
            # first, get the current mode
            st = os.stat(targetPathpath.filePath)
            # add executable
            os.chmod(targetPath, st.st_mode | stat.S_IEXEC)

        print("    saved to: " + path.filePath)

def processBlobs(pack, data):
    for blob in pack.blobs:
        blobData = data[blob.offset:blob.offset + blob.size]
        blobHash = hashlib.sha1(blobData)

        if blob.hash == blobHash.hexdigest():
            processPaths(blob, blobData)
        else:
            print("    BLOB HASH DOES NOT MATCH. DOING NOTHING")
            print("    (blob hash = {})".format(blobHash))

def processPack(pack, req):
        data = gzip.decompress(req.content)
        check_hash = hashlib.sha1(data)
        if pack.hash == check_hash.hexdigest():
            processBlobs(pack, data)
        else:
            print("PACK HASH DOES NOT MATCH. DOING NOTHING.")
