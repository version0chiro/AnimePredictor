import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn import neighbors,datasets
import pickle
import joblib
import sys


anime = pd.read_csv('Anime.csv')

anime.isnull().sum()

anime.loc[(anime["genre"]=="Hentai") & (anime["episodes"]=="Unknown"),"episodes"]="1"
anime.loc[(anime["type"]=="OVA") & (anime["episodes"]=="Unknown"),"episodes"]="1"
anime.loc[(anime["type"]=="Movie") & (anime["episodes"]=="Unknown"),"episodes"]="1"

known_animes = {"Naruto: Shippuuden":500, "One Piece":784,"Detective Conan":854, "Dragon Ball Super":86,
                "Crayon Shin chan":942, "Yu Gi Oh Arc V":148,"Shingeki no Kyojin Season 2":25,
                "Boku no Hero Academia 2nd Season":25,"Little Witch Academia TV":25}

for k,v in known_animes.items():
    anime.loc[anime["name"]==k,"episodes"] = v

anime["episodes"] = anime["episodes"].map(lambda x:np.nan if x =="Unknown" else x)


anime["episodes"].fillna(anime["episodes"].median(),inplace = True)

pd.get_dummies(anime[["type"]]).head()

anime["rating"] = anime["rating"].astype(float)
anime["rating"].fillna(anime["rating"].median(),inplace = True)
anime["members"] = anime["members"].astype(float)

anime_features = pd.concat([anime["genre"].str.get_dummies(sep=","),pd.get_dummies(anime[["type"]]),anime[["rating"]],anime[["members"]],anime["episodes"]],axis=1)
anime["name"] = anime["name"].map(lambda name:re.sub('[^A-Za-z0-9]+'," ",name))
anime_features.head()

from sklearn.preprocessing import MinMaxScaler

min_max_scaler = MinMaxScaler()
anime_features = min_max_scaler.fit_transform(anime_features)

anime_features1=np.round(anime_features,2)

from sklearn.neighbors import NearestNeighbors

nbrs = NearestNeighbors(n_neighbors=6,algorithm='ball_tree').fit(anime_features)

distance,indices = nbrs.kneighbors(anime_features)

# joblib.dump([anime,indices],"joblib.sav")
# with open('animeTrain.pickle','wb') as f:
#     pickle.dump([anime,indices],f)
def get_index_from_name(name):
    return anime[anime["name"]==name].index.tolist()[0]

all_anime_names = list(anime.name.values)

def get_id_from_partial_name(partial):
    for name in all_anime_names:
        if partial in name:
            print(name,all_anime_names.index(name))

def print_similar_animes(query=None,id=None):
    if id:
        for id in indices[id][1:]:
            print(anime.iloc[id]["name"])
    if query:
        found_id = get_index_from_name(query)
        for id in indices[found_id][1:]:
            print(anime.iloc[id]["name"])
