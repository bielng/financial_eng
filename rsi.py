import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

import yfinance as yf
print(yf.__version__)

df = yf.download("SPY", start="2000-01-01", end="2020-01-01")