def write_file(file,content):
    """This writes to a file. Uses the default python API"""
    with open(file,"w") as f:
        f.write(content)
        f.close()

def append_file(file,content):
    """This appends to a file"""
    with open(file,"a") as f:
        f.write(content)
        f.close()

def read_file(file):
    """This reads from a file"""
    with open(file,"r") as f:
        value = f.read()
        f.close()
        return value
