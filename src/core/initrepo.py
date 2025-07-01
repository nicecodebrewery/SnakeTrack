import os
from utils.filehandler import read_file,append_file,write_file

def init(reponame):
    """This function creates an empty repository and nothing more"""
    try:
        os.mkdir(reponame)
        os.mkdir(os.path.join(reponame,'.snake'))
        for name in ['objects','refs','refs/heads']:
            os.mkdir(os.path.join(reponame,'.snake',name))
        write_file(os.path.join(reponame,'.snake','HEAD'),'ref: refs/heads/master')
        print(f'Snake initialized empty repository: {reponame}')
    except FileExistsError:
        print("\033[31mRepo already there. Don't fool snake.\033[0m")
    except PermissionError:
        print("\033[31mSnake don't have permission to write here. make sure the land is not wet.\033[0m")
    except:
        print(f"\033[31mFailed to initialize empty repository {reponame}\033[0m")