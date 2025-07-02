def cmd_init(argv):
    """init command is handled by this function."""
    if(len(argv) == 0):
        print("A description is required.")
        return
    print(f"Snake initialized {argv[0]}.")