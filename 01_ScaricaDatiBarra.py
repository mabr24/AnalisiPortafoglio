
from zeep import Client

USER = "mbrazzelli"
CLIENTID = "q4b33vhnbs"
PW = "Barra2018"


client = Client('./bdti.wsdl')
login = client.service.Login(USER, CLIENTID, PW)
#FilterType = client.get_type("ns0:FilterType")
#help(FilterType)
#filterType = FilterType("PortfolioTree")
#myFilters = client.service.GetFilters(filterType)
#print(myFilters)


import os
import pandas as pd

workfolder = os.getcwd()
path = workfolder + "\Proposta_Portafoglio.xlsx"

df = pd.read_excel(path, sheetname="Foglio1")

print(df)
