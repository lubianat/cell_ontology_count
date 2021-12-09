from bs4 import BeautifulSoup, SoupStrainer
import requests
import pandas as pd
import json

url = "https://bioportal.bioontology.org/ontologies/CL"
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data)

table = soup.find("table", id="ontology_versions")

df = pd.read_html(str(table))[0]

df["id"] = list(range(88, -1, -1))
df["id"] = df["id"].astype("string")

with open("../results/result.json") as f:
    data = json.loads(f.read())

print(data)

df["id"]
df["counts"] = df["id"].map(data).fillna("unknown")
df["counts"] = pd.to_numeric(df["counts"], errors="coerce")


df["Released"] = pd.to_datetime(
    df["Released"], infer_datetime_format=True, errors="coerce"
)

df = df.dropna()

print(df.tail())

import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x="Released", y="counts", data=df)
plt.xticks(rotation=15)
plt.title("CL classes mentioned per release")
plt.savefig("../results/classes_per_release.png", format="png")
