def calc(expression):
    res = list(expression)
    while '-' in res:            
        i = res.index('-')
        res[i] = '+-'
    res = ''.join(res).split('+')
    
    result = []
    for j in range(len(res)):
        result.append(float(res[j]))
    return round(sum(result), 6)
