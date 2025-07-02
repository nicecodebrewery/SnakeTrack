from src.core.snakerepo import repo_file
import os
import zlib
import hashlib

class SnakeObject(object):
    def __init__(self,data=None):
        if data != None:
            self.deserialize(data)
        else:
            self.init()

    def serialize(self,repo):
        """Implement in subclass"""
        raise Exception("Method is not implemented : serialize()")
    
    def deserialize(self,repo):
        """Implement in subclass"""
        raise Exception("Method is not implemented : deserialize()")
    
    def init(self):
        pass

def object_read(repo,sha):
    """Read object sha from repo"""
    path = repo_file(repo,"objects",sha[0:2],sha[2:])

    if not os.path.isfile(path):
        return None
    
    with open(path,"rb") as f:
        raw = zlib.decompress(f.read())
        x = raw.find(b' ')
        fmt = raw[0:x]

        y = raw.find(b'\x00',x)
        size = int(raw[x:y].decode("ascii"))

        if size != len(raw) - y - 1:
            raise Exception(f"Snake traped.Malformated object {sha} : bad length")
        
        match fmt:
            case b'commit' : c=SnakeCommit
            case b'tree' : c=SnakeTree
            case b'tag' : c=SnakeTag
            case b'blob' : c=SnakeBlob
            case _ : raise Exception(f"Snake confused. Unknown type {fmt.decode("ascii")} for object {sha}")
        
        return c(raw[y+1:])
        
def object_write(obj,repo=None):
    data = obj.serialize()
    result = obj.fmt + b' ' + str(len(data)).encode() + b'\x00' + data
    sha = hashlib.sha1(result).hexdigest()

    if repo:
        path = repo_file(repo,"objects",sha[0:2],sha[2:],mkdir=True)

        if not os.path.exists(path):
            with open(path,"wb") as f:
                f.write(zlib.compress(result))
        
        return sha

