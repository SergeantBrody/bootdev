
def count_words(book):
    total = len(book.split())
    return total

def count_characters(book):
    my_dict = {}
    book = book.lower()
    for character in book:
        my_dict[character] = 0 
    for character in book:
        my_dict[character] += 1 
    return my_dict

def sort_on(items):
    return items["num"]

def report(dic):
    print("--------- Character Count -------")
    list_of_dics = []
    for key, value in dic.items():
        new_dic = {}
        new_dic["char"] = key
        new_dic["num"] = value
        list_of_dics.append(new_dic)

    list_of_dics.sort(reverse=True, key=sort_on)

    for dic in list_of_dics:
        dic_values = dic.values()
        if list(dic_values)[0].isalpha():
            print(f"{list(dic_values)[0]}: {list(dic_values)[1]}")
    
    print("============= END ===============")

