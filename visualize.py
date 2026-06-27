import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/housing.csv")

plt.scatter(data["Area"], data["Price"])

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")

plt.show()