def calc(expression):
    res = expression.split('+')
    result = []
    for i in range(len(res)):
        result.append(float(res[i]))
    return sum(result)
