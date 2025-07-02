from src.core.snakerepo import repo_find
from src.objects.snakeobject import object_read
import sys

def cmd_dog_file(argv):
    if len(argv) < 2:
        print(f"Snake bite. Insufficient arguments")
        return
    type = argv[0]
    if type not in ['blob','commit','tree','tag']:
        print(f"Snake confused. Chose a valid type ['blob','commit','tree','tag']")
        return
    object = argv[1]
    repo = repo_find()
    dog_file(repo,object,fmt=type.encode())

def dog_file(repo,obj,fmt=None):
    obj = object_read(repo, object_find(repo,obj,fmt=fmt))
    sys.stdout.buffer.write(obj.serialize())

def object_find(repo, name, fmt=None, follow=True):
    return name