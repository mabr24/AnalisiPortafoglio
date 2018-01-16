import subprocess
from sys import argv, exc_info
import toml
from subprocess import Popen, PIPE

try:
    my_path = argv[0]
    config_path = my_path.split("\InstallFiles")[0]+"\Config.toml"
    toml_file = open(config_path, "r")
    toml_string = toml_file.read()
    config = toml.loads(toml_string)
    username = config["barra_credentials"]["username"]
    password = config["barra_credentials"]["password"]
    owner = config["barra_config"]["owner"]
    barra_path = config["barra_config"]["dataconnect_path"]

    if (len(argv) < 2):
        print("Not enough parameters!")
        print("Usage: .\\UploadBarraPositions.py <TemplateImportPositions_path>")
        exit()

    path = argv[1]
    print("Received path: "+path)

    print("Uploading...")
    proc = subprocess.check_output([barra_path,
                                    '-u', username,
                                    '-p', password,
                                    '-c', 'q4b33vhnbs',
                                    '-f', 'name="'+path+'";datatransform="BarraOne Positions(xls)";effectivedate="LATEST_FINALIZED_DATE";owner="'+owner+'"'],
                                    bufsize=1)

    print(proc)

    print("Done!")
    print("Premi ENTER per continuare...")
    input()

except Exception as e:
    print("An error has occurred: "+str(e)+"\n")
    print(exc_info()[0])
    print("Press ENTER to continue...")
    input()
