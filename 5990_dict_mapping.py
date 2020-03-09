import os
from tqdm import tqdm
import data.keys.keys_5990 as keys


def load_data(_path):
    res_dict = dict()
    with open(_path, 'r', encoding='utf-8') as f:
        data_line = f.readlines()
        for i in data_line:
            data = i.strip().split(' ')
            res_dict[data[0]] = data[1:]
    return res_dict


def write_data1(_path, _dict):
    with open(_path, 'w', encoding='utf-8') as f:
        for k, v in _dict.items():
            temp_list = [k]
            mapping = [dictKeys[i] for i in v]
            temp_list += mapping
            result = ' '.join(temp_list)
            f.write(u"{}\n".format(result))


def write_data2(_path, _dict):
    key_1 = keys.alphabet_capital[:]
    key_2 = characters
    key_3 = keys.alphabet_capital_characters[1:] + u'卍'
    key_4 = keys.alphabet_special_attributes[1:] + u'卍'
    key_5 = keys.alphabet_symbol_1[1:] + u'卍'
    key_6 = keys.alphabet_symbol_2[1:] + u'卍'
    key_7 = keys.alphabet_num[1:] + u'卍'
    with open(_path, 'w', encoding='utf-8') as f:
        for k, v in _dict.items():
            temp_list = [k]
            res_type = judge_word(v, key_1, key_2, key_3, key_4, key_5, key_6, key_7)
            temp_list += res_type
            result = ' '.join(temp_list)
            f.write(u"{}\n".format(result))


def judge_word(_word_list, _k1, _k2, _k3, _k4, _k5, _k6, _k7):
    temp_list = list()
    for _word in _word_list:
        if is_alphabet(_word):
            temp_list.append('1')
        elif is_number(_word):
            temp_list.append('7')
        elif _word in _k3:
            temp_list.append('3')
        elif _word in _k4:
            temp_list.append('4')
        elif is_chinese(_word):
            temp_list.append('2')
        elif _word in _k5:
            temp_list.append('5')
        else:
            temp_list.append('6')
    return temp_list


# 判断一个unicode是否是汉字
def is_chinese(uchar):
    if '\u4e00' <= uchar <= '\u9fff':
        return True
    else:
        return False


# 判断一个unicode是否是数字
def is_number(uchar):
    if '\u0030' <= uchar <= '\u0039':  # 0-9：\u0030-\u0039
        return True
    else:
        return False


# 判断一个unicode是否是英文字母
def is_alphabet(uchar):
    if ('\u0041' <= uchar <= '\u005a') or ('\u0061' <= uchar <= '\u007a'):  # A-Z：\u0041-\u005a  a-z ：\u0061-\u007a
        return True
    else:
        return False


if __name__ == '__main__':
    pathTrain = 'D:/UMPAY/Project/Coding/Tool_Project/data/keys/data_train.txt'
    pathTest = 'D:/UMPAY/Project/Coding/Tool_Project/data/keys/data_test.txt'
    # load data
    dictTrain = load_data(pathTrain)
    dictTest = load_data(pathTest)
    # load key
    characters = keys.alphabet[1:] + u'卍'
    dictKeys = dict(zip([str(i) for i in range(1, len(characters) + 1)], characters))
    write_data1('D:/UMPAY/Project/Coding/Tool_Project/data/keys/data_train_chinese.txt', dictTrain)
    write_data1('D:/UMPAY/Project/Coding/Tool_Project/data/keys/data_test_chinese.txt', dictTest)

    pathTrain2 = 'D:/UMPAY/Project/Coding/Tool_Project/data/keys/data_train_chinese.txt'
    pathTest2 = 'D:/UMPAY/Project/Coding/Tool_Project/data/keys/data_test_chinese.txt'
    # load data
    dictTrain2 = load_data(pathTrain2)
    dictTest2 = load_data(pathTest2)
    write_data2('D:/UMPAY/Project/Coding/Tool_Project/data/keys/data_train_7.txt', dictTrain2)
    write_data2('D:/UMPAY/Project/Coding/Tool_Project/data/keys/data_test_7.txt', dictTest2)
