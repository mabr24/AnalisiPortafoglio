from zeep import Client
from sys import argv
from Modules.config import Config

my_path = argv[0]
my_root_folder = my_path.split("01_ScaricaDatiBarra.py")[0]
config_path = my_root_folder+"\Config.toml"
config = Config(config_path)
wsdl_path = my_root_folder+"\\Resources\\bdt.wsdl"
client = Client(wsdl_path)
#login = client.service.Login(config.user, config.clientid, config.password)
#FilterType = client.get_type("ns0:FilterType")
#help(FilterType)
#filterType = FilterType("PortfolioTree")
#myFilters = client.service.GetFilters(filterType)
#print(myFilters)
PortfolioTree = client.get_type("ns0:PortfolioTree")
myPftree = PortfolioTree()
myPftree.TreeName = "defaultExportSetTree"
print(myPftree)
