from src.core.snakerepo import repo_create

def cmd_init(argv):
    """init command is handled by this function."""
    if(len(argv) == 0):
        print("A path is required.")
        return
    repo_create(argv[0])
    print(f"Snake initialized {argv[0]}.")