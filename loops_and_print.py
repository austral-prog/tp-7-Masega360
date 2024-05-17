def enumerate_list(list):
    colors = []
    if list != []:
        a = -1
        for item in list:
            if item != "":
                a += 1
                colors.append(f"{a}. {item}")
    return colors


def enumerate_backwards(list):
    colors = []
    if list != []:
        a = -1
        for item in list:
            if item != "":
                a += 1
                item = item[::-1]
                colors.append(f"{a}. {item}")
    return colors
