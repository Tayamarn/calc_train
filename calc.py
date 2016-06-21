def calc(expression):
    try:
        res = expression.split('+')
        result = []
        for i in range(len(res)):
            result.append(float(res[i]))
        return sum(result)
    except ValueError:
        pass
