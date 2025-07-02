from snakeobject import SnakeObject

class SnakeBlob(SnakeObject):
    fmt=b'blob'

    def serialize(self):
        return self.blobdata
    def deserialize(self,data):
        self.blobdata = data

    
