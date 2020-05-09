    # 1. Методом строк очистить текст от знаков препинания;
t = open('text_l3.txt', encoding='utf-8')  # открываем файл с текстом и декодируем
text = t.read()  # считать из файла в текстовую переменную
str = text
symbol_list = ['.', ',', '!', '?', '-', ' ', ':', ';', '(', ')', '«', '»', '..', '—', "'",'"','\n']
for a in range(len(symbol_list)):
    str = str.replace(symbol_list[a], ' ')
print(str)
    # 2. Сформировать list со словами (split);
text_list = str.split()
print(text_list)
    # 3. Привести все слова к нижнему регистру (map);
text_list = list(map(lambda x : x.lower(), text_list))
print(text_list)
    # 4. Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
text_dict = {a:text_list.count(a) for a in text_list}
print(text_dict)
    # 5. Вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set);
sort_list = list(text_dict.items())
sort_list.sort(key = lambda i: i[1], reverse = True)
print('5 наиболее часто встречающихся слов:')
print(sort_list[:5])
text_set = set(text_list)
print('Kоличество разных слов в тексте:')
print(len(text_set))