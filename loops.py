def index_of_by_index(word, list, index):
    indice = -1
    liston = []
    for item in list[index::]:
        if item != word:
            liston.append(item)
        elif item == word:
            indice = len(liston) + index 
            break
    return indice


def index_of_empty(list):
    indice = -1
    liston = []
    for item in list:
        if item != "":
            liston.append(item)
        elif item == "":
            indice = len(liston) 
            break
    return indice


def index_of(word, list):
    indice = -1
    liston = []
    for item in list:
        if item != word:
            liston.append(item)
        elif item == word:
            indice = len(liston) 
            break
    return indice



def put(word, list):
    a = 0
    if "" not in list:
        return -1
    else:
        for item in list:
            a += 1
            if item == "":
                list.insert(a, word)
                del list[a-1]
                break
        return a - 1


def remove(word, list):
    a = 0
    for item in list:
        if item == word: 
            list[index_of(word,list)] = ""
            a += 1
    return a
