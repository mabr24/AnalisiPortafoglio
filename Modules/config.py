import toml

class Config:

    username = None
    password = None
    owner = None
    barra_path = None
    clientid = None

    def __init__(self, config_path):
        toml_file = open(config_path, "r")
        toml_string = toml_file.read()
        config = toml.loads(toml_string)
        self.username = config["barra_credentials"]["username"]
        self.clientid = config["barra_credentials"]["clientid"]
        self.password = config["barra_credentials"]["password"]
        self.owner = config["barra_config"]["owner"]
        self.barra_path = config["barra_config"]["dataconnect_path"]
