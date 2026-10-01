import pandas as pd
import yfinance as yf
import numpy as np
import sys
TICKER = ["AAPL", "MSFT", "KO", "SAP.DE", "VOW3.DE"] #zu prüfenden aktien
KAUF = {"KGV":(12,40,20),"KBV":(1,6,10), "EKRendite%":(25,5,15),"Marge%": (20, 2, 12),          #Aufbau Kennzahl: bsp. KGV(gut,schlecht,gewichtung)
        "Wachstum%": (15, -5, 13), "Schulden%": (30, 200, 15),
        "Liquiditaet": (2, 0.8, 5), "Dividende%": (4, 0, 10)}                                   #Kennzahlen in dictionaries damit die aktien einen richtwert
                                                                                                #für  gute Werte haben
RISIKO = {"Beta": (0.5, 2, 25), "Schwankung%": (12, 65, 30), "MaxVerlust%": (-10, -70, 20),
          "Schulden%": (25, 250, 15), "Mrd": (150, 2, 10)}


