def count_code(str):
    return sum([1 if str[i]=="c" and str[i+1]=="o" and str[i+3]=="e" else 0 for i in range(len(str) - 3)])