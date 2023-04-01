def calc():
    a = input()
    l = input()
    result = ""
    for i in l:
        if i == result:
            return "No"
        result = i

    return "Yes"

print(calc())