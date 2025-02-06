import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv(r'C:\Users\Devid Hidayat\Documents\Pelatihan Data Analyst\Project\project 5\epa-sea-level.csv')

plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color='blue', label="Data Asli")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()
plt.show()

x = df["Year"]
y = df["CSIRO Adjusted Sea Level"]

slope, intercept, r_value, p_value, std_err = linregress(x, y)

x_pred = np.arange(1880, 2051)
y_pred = slope * x_pred + intercept

plt.scatter(x, y, color='blue', label="Data Asli")
plt.plot(x_pred, y_pred, color='red', label="Tren 1880-2050")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()
plt.show()

df_recent = df[df["Year"] >= 2000]

x_recent = df_recent["Year"]
y_recent = df_recent["CSIRO Adjusted Sea Level"]

slope_recent, intercept_recent, r_value, p_value, std_err = linregress(x_recent, y_recent)

x_pred_recent = np.arange(2000, 2051) 
y_pred_recent = slope_recent * x_pred_recent + intercept_recent

plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color='blue', label="Data Asli") 
plt.plot(x_pred, y_pred, color='red', label="Tren 1880-2050") 
plt.plot(x_pred_recent, y_pred_recent, color='green', linestyle="dashed", label="Tren 2000-2050")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()

plt.savefig('sea_level_plot.png')
def draw_plot():
    return plt.gcf()