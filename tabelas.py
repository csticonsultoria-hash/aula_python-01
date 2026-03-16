import pandas as pd
url = "https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o"

table = pd.read_html(url)

df = table[0]

print(df.head())