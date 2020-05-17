def lone_sum(a, b, c):
    return 0 if (a==b and b==c) else a+b+c if (a!=b and a!=c and b!=c) else a if (b==c) else b if (a==c) else c if (a==b) else 0