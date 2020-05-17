def last2(str):
    return sum(str[-2:len(str)]==str[i:i+2] for i in range(len(str)-2))