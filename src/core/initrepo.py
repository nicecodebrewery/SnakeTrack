import os
from utils.filehandler import read_file,append_file,write_file

def init(reponame):
    """This function creates an empty repository and nothing more"""
    try:
        os.mkdir(reponame)
        os.mkdir(os.path.join(reponame,'.git'))
        for name in ['objects','refs','refs/heads']:
            os.mkdir(os.path.join(reponame,'.git',name))
        write_file(os.path.join(reponame,'.git','HEAD'),b'ref: refs/heads/master')
        print(f'initialized empty repository: {reponame}')
    except:
        print(f"Failed to initialize empty repository {reponame}")