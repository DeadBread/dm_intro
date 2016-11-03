#coding=utf8

import numpy as np
from string import maketrans
import math

def transformer(strings):    

    #генерируем множество слов
    words = set()
    
    tr1 = ',.?!'
    tr2 = '    '
    trtable = maketrans(tr1,tr2)
    
    splited_strings = []
    
    for string in strings:
        
        tmp = string.translate(trtable)
        tmp2 = tmp.split()
        
        splited_strings.append(tmp2)
        
        words.update(set(tmp2))
        
    #создаем массив соответствующей размерности
    res = np.zeros((len(splited_strings),len(words)))
    
    #считаем tf
    for i, string in enumerate(splited_strings):
        for j, word in enumerate(sorted(words)):
            res[i,j] = string.count(word)
            res[i,j] /= len(string)
            
    #считаем idf и кладем его в матрицу
    for j, word in enumerate(sorted(words)):
        tmp = 0.0
        for string in splited_strings:
            if word in string:
                tmp += 1.0
        for i in range(len(splited_strings)):
            res[i, j] *= math.log10((len(splited_strings) / tmp))
    
    #чтобы не менять весь код верну траспонированную матрицу, удобнее для просмотра
    return res.transpose()
        
print transformer(['aaaa bbb sss dd.', 'dd? aaaa iii dd', 'rrrr rrrr sss rrrr!'])

