from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt
import seaborn as sbs


def are_similar(s1, s2):
    if fuzz.ratio(s1, s2) >= 67:
        print(1)
        return True
    if fuzz.token_sort_ratio(s1, s2) > 75:
        print(2)
        return True
    return False


def similar_rating(s1, s2):
    a = fuzz.ratio(s1, s2)
    b = fuzz.token_sort_ratio(s1, s2)
    c = fuzz.WRatio(s1, s2)
    return round((a + b + c)/3, 3)

def find_closest(s1: str, lst: list):
    a = 0
    b = ''
    for el in lst:
        if a < similar_rating(s1, el.strip()):
            a = similar_rating(s1, el.strip())
            b = el.strip()
    return a, b


def build_graph(lst):
    if len(lst) > 30: 
        lst = lst[-30:]
    sbs.set_style("whitegrid")
    sbs.lineplot(x = list(range(1, len(lst) + 1)), y = lst, legend='full')
    plt.savefig('images/graph.png')  

