def sort_on(items):
    return items["num"]

text = "Ala ma kota !!!!"
text = text.lower()
dic = {}
for letter in text:
    if letter.isalpha():
        dic[letter] = 0
for letter in text:
    if letter.isalpha():
        dic[letter] += 1


print(dic)

def report(dic):
    list_of_dics = []
    for key, value in dic.items():
        new_dic = {}
        new_dic["char"] = key
        new_dic["num"] = value
        list_of_dics.append(new_dic)

    list_of_dics.sort(reverse=True, key=sort_on)

    for dic in list_of_dics:
        dic_values = dic.values()
        print(f"{list(dic_values)[0]}: {list(dic_values)[1]}")
    print("============= END ===============")


