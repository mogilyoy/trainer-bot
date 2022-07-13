from fuzzywuzzy import fuzz

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
 