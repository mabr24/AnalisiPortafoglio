import os
import pandas as pd

workfolder = os.getcwd()
path = workfolder + "\Proposta_Portafoglio.xlsx"

df = pd.read_excel(path, sheetname="Foglio1")

print(df)


# Leggi i file excel dalle cartelle predefinite
# Uniscili in un unico dataframe
# Applica i cambiamenti dal file override
