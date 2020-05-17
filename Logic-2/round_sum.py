def round_sum(a, b, c):
    return (a+(10-a%10) if a%10>=5 else a-(a%10)) + (b+(10-b%10) if b%10>=5 else b-(b%10)) + (c+(10-c%10) if c%10>=5 else c-(c%10))