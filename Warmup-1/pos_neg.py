def pos_neg(a, b, negative):
    return (negative and abs(a)!=a and abs(b)!=b) or (not negative and abs(a)!=a and abs(b)==b) or (not negative and abs(a)==a and abs(b)!=b)