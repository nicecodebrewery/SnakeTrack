import os
import configparser

class GitRepository(object):
    """A git repository"""

    worktree = None
    snakedir = None
    conf = None

    def __init__(self,path,force = False):
        self.worktree = path
        self.snakedir = os.path.join(path,".snake")

        if not (force or os.path.isdir(self.snakedir)):
            raise Exception("Not a git repository")
        
        self.conf = configparser.ConfigParser()
        cf = repo_file(self,"config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing.")
        
        if not force:
            vers = int(self.conf.get("core","repositoryformatversion"))
            if vers != 0:
                raise Exception(f"Unsupported version {vers}")


def repo_path(repo,*path):
        """Compute path under repo's snakedir"""
        return os.path.join(repo.snakedir,*path)
    
def repo_file(repo,*path,mkdir=False):
        """Same as repo_path, but create dirname(*path) if absent.  For
        example, repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create
        .git/refs/remotes/origin."""
        if len(path) == 0:
             return None
        if repo_dir(repo,*path[1:],mkdir=mkdir):
            return repo_path(repo,*path)
    
def repo_dir(repo, *path, mkdir=False):
        """Same as repo_path, but mkdir *path if absent if mkdir."""

        path = repo_path(repo, *path)

        if os.path.exists(path):
            if (os.path.isdir(path)):
                return path
            else:
                raise Exception(f"Not a directory {path}")

        if mkdir:
            os.makedirs(path)
            return path
        else:
            return None    

def repo_create(path):
    """Creates a repository"""

    repo = GitRepository(path,force=True)

    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception(f"{path} is not a directory.")
        if os.path.exists(repo.snakedir) and os.listdir(repo.snakedir):
            raise Exception(f"Snake is already there in {path}")
    else:
        os.makedirs(repo.worktree)

    assert repo_dir(repo,"branches",mkdir=True)
    assert repo_dir(repo,"objects",mkdir=True)
    assert repo_dir(repo,"refs","tags",mkdir=True)
    assert repo_dir(repo,"refs","heads",mkdir=True)

    with open(repo_file(repo,"description"),"w") as f:
         f.write("An unnamed snake is here. Name this repo by editing this file.\n")

    with open(repo_file(repo,"HEAD"),"w") as f:
         f.write("ref: refs/heads/master\n")
    
    with open(repo_file(repo,"config"),"w") as f:
         config = repo_default_conf()
         config.write(f)
    return repo

def repo_default_conf():
     ret = configparser.ConfigParser()

     ret.add_section("core")
     ret.set("core","repositoryformatversion","0")
     ret.set("core","filemode","false")
     ret.set("core","bare","false")    

     return ret


     