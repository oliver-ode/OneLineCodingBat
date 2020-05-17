def string_splosion(str):
    return(lambda : "".join(str[0:i]for i in range(len(str)+1)))()