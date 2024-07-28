from pprint import pprint


def custom_write(file_name, strings):
    file_txt = open(file_name, 'a', encoding='utf-8')
    dict_ = {}
    strings_counter = 1
    for i in strings:
        dict_[(strings_counter, file_txt.tell())] = i
        file_txt.write(i + '\n')
        strings_counter += 1
    file_txt.close()
    return dict_


# list_ = ['file.txt', '123', 'qwe', 'wsfqeg']
# print(custom_write('file.txt', list_))

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
