import os
import pandas as pd
import numpy as np
from matplotlib import pyplot  as plt
print(*[filename.split(".")[0] for filename in os.listdir("./opinions")],sep="\n")

product_code = input('Podaj kod produktu: ')

opinions = pd.read_json(f'./opinions/{product_code}.json')
opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",",",")))

#wyliczenie podstawowych statystyk
opinions_count = opinions.opinion_id.count()
#opinions_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
stars_avg = opinions.stars.mean().round(2)
print(f'''Dla produktu o kodzie {product_code}
pobrano {opinions_count} opinii/opinię.
Dla {pros_count} opinii podano listę zalet,
a dla {cons_count} podano listę wad.
Średnia ocena productu wynosi {stars_avg}.''')

#histogram częstośco poszczególnych ocen
stars=  opinions.stars.values_counts()
print(stars)
stars.plot.bar()
plt.show()