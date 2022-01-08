import json

Config = None


def LoadConfig():
    global Config
    with open("token.json", "r", encoding="utf-8") as config_file:
        Config = json.loads(config_file.read())

def get(index, default=None):
    global Config
    return Config.get(index, default)