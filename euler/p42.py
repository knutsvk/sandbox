def triangle_numbers(max_value):
    ret = [1]
    while ret[-1] < max_value:
        ret.append(ret[-1] + len(ret) + 1)
    return ret


def value(word):
    return sum([ord(char)-64 for char in word])


if __name__ == "__main__": 
    words = [word.replace("\"", "").replace("\n", "") for word in open("p42.in").readline().split(',')]
    values = [value(word) for word in words]
    triangles = triangle_numbers(max(values))
    print(sum([value in triangles for value in values]))
