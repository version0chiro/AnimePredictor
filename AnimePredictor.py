import pickle
import sys
import joblib

# with open("public/animeTrain.pickle",'rb') as f:
#     anime,indices=pickle.load(f)

anime,indices = joblib.load("joblib.sav")


def get_index_from_name(name):
    return anime[anime["name"]==name].index.tolist()[0]



all_anime_names = list(anime.name.values)


def print_similar_animes(query=None,id=None):
    if id:
        for id in indices[id][1:]:
            print(anime.iloc[id]["name"])
    if query:
        found_id = get_index_from_name(query)
        for id in indices[found_id][1:]:
            print(anime.iloc[id]["name"])


print_similar_animes(sys.argv[1])