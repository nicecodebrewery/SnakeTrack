import os

class GitRepository(object):
    """A git repository"""

    worktree = None
    snakerepo = None
    conf = None

    def __init__(self,path,force = False):
        self.worktree = path
        self.snakerepo = os.path.join
        