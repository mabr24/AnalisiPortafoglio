import os
import pandas as pd

from bloomberg import *

def main():
    portfolios = ["GASMCAD LX Equity"]
    bloomberg = Bloomberg()
    bloomberg.login()
    results = [bloomberg.getData(p) for p in portfolios]
    # Equivalent to map(bloomberg.getBloombergData, portfolios)
    print(results[0])


if __name__ == "__main__":
    main()



# Scarica i dati da Bloomberg
# Calcoli vari
