def calc(expression):
    try:
        res = expression.split('+')
        result = []
        for i in range(len(res)):
            result.append(int(res[i]))
        return sum(result)
    except:
        pass
