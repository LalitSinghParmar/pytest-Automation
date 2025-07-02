import os

def config_exists():
    return os.path.exists("/etc/myapp/config.yaml")
