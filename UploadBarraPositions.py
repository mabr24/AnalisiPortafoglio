import subprocess
from sys import argv, exc_info
from subprocess import Popen, PIPE
from Modules.config import Config

try:
    my_path = argv[0]
    config_path = my_path.split("\\UploadBarraPositions.py")[0]+"\Config.toml"
    config = Config(config_path)

    if (len(argv) < 2):
        print("Not enough parameters!")
        print("Usage: .\\UploadBarraPositions.py <TemplateImportPositions_path>")
        exit()

    path = argv[1]
    print("Received path: "+path)

    print("Uploading...")
    proc = subprocess.check_output([config.barra_path,
                                    '-u', config.username,
                                    '-p', config.password,
                                    '-c', 'q4b33vhnbs',
                                    '-f', 'name="'+path+'";datatransform="BarraOne Positions(xls)";effectivedate="LATEST_FINALIZED_DATE";owner="'+config.owner+'"'],
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
