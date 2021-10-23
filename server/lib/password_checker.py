import Levenshtein
import setup

def password_checker(pw):
    lev_dist = Levenshtein.distance(str(pw), str(setup.AUTHORIXATION))
    divider = len(str(pw)) if len(str(pw)) > len(str(setup.AUTHORIXATION)) else len(str(setup.AUTHORIXATION))
    lev_dist = lev_dist / divider

    print(lev_dist)
    if ((1 - lev_dist) == 1.0):
        return True
    else:
        return False