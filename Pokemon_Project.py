import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

df = pd.read_csv("pokemon_data.csv")
print(df)

type_count = df["Type1"].value_counts(ascending=True)

graph1 = plt.barh(type_count.index, type_count.values, color = "skyblue",
                                              edgecolor = "Black")

plt.title("Number of Pokemon by primary type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()
plt.savefig("graph1.png")
plt.show()

categories = np.array(type_count.index)
values = np.array(type_count.values)
plt.figure(figsize=(6,6))
graph2 =plt.pie(values, labels= categories,
                shadow = True,
                startangle = 90)

plt.title("Number of Pokemon by primary type")

plt.tight_layout()

plt.savefig("graph2.png")
plt.show()