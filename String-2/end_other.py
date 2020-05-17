def end_other(a, b):
    return a.lower()==b.lower()[-1*len(a):len(b)] or b.lower()==a.lower()[-1*len(b):len(a)]