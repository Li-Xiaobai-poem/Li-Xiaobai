# -*- coding: utf-8 -*-


'''
@author 王博学
@date 2021/07/08
依据输入的关键字和类型判断诗词押韵
'''
import re
from rhyme_init_sc import get_sheet

useTC = False

ping_shui_rhymes = get_sheet()
print("----------------")


def get_rhyme(keyword):
    rhyme_judgement = ['0', '0']
    for i in ping_shui_rhymes:
        if i.chineseChar == keyword:
            rhyme_judgement = i.getDescript()
            if not i.isPolyphone:
                break
    return rhyme_judgement


def get_tone(rhy):
    """
    依据字所在的韵部，返回当前字的平仄
    """
    if rhy[0] == '上声' or rhy[0] == '去声' or rhy[0] == '入声':
        return '仄'
    else:
        return '平'


def poem_analyse(content):
    sentences = [sentence for sentence in re.split("[，。？！]", content) if sentence != ""]
    judge = True
    for i in range(len(sentences) - 3):  # 让诗句不为最后两句
        if not judge:  # 判断诗句押韵是否有误，有误则直接跳出循环，无误则继续循环，直到整首诗都判定押韵
            break
        else:
            if i % 2 == 1:  # 判断诗句是否为偶数句
                if get_tone(get_rhyme(sentences[i][len(sentences[i]) - 1])[0]) == '平':  # 判断偶数句韵脚是否为平，不同为False
                    judge = get_rhyme(sentences[i][len(sentences[i]) - 1]) == \
                            get_rhyme(sentences[i + 2][len(sentences[i + 2]) - 1])  # 为平则判断韵脚是否相同，相同为True
                else:
                    judge = False
            else:
                if i == 0:  # 判断诗句是否为首句，首句可入偶数诗韵脚，也可不入韵
                    if get_tone(get_rhyme(sentences[0][len(sentences[0]) - 1])[0]) == '平':
                        judge = get_rhyme(sentences[0][len([0]) - 1]) == \
                                get_rhyme(sentences[i][len(sentences[i]) - 1])  # 首句诗为平时，韵脚应入韵
                else:  # 不为首句时判断奇数句诗韵脚是否为仄，为仄返回True，
                    judge = get_tone(get_rhyme(sentences[i][len(sentences[i]) - 1])[0]) == '仄'
    return judge



