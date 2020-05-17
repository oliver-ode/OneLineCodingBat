def no_teen_sum(a, b, c):
    return(a if (a<13 or a>19 or a==15 or a==16) else 0) + (b if (b<13 or b>19 or b==15 or b==16) else 0) + (c if (c<13 or c>19 or c==15 or c==16) else 0)