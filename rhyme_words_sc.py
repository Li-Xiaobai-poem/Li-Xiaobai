# -*- coding: utf-8 -*-

# rhyme_words.py

import rhyme_sheet_sc as rhyme_sheet

'''
@author 王博学
@data 2021/07/07
初始化平水韵，调用方法返回字的声部和韵脚
'''
class rhyme_word:
    chineseChar = ""
    polyDescript = ""
    mainTypeIndex = 0
    isPolyphone = False
    secondTypeIndex = 0

    def __bool__(self):
        return not self.chineseChar == ""

    def __str__(self):
        return self.getDescript()

    def __init__(self, ChineseChar, MainTypeIndex, secondTypeIndex, PolyDescript="__DEFAULT__"):
        self.chineseChar = ChineseChar
        self.mainTypeIndex = MainTypeIndex
        self.secondTypeIndex = secondTypeIndex
        if PolyDescript == "__DEFAULT__":
            self.isPolyphone = False
        else:
            self.isPolyphone = True
            self.polyDescript = PolyDescript

    def __cmp__(self, str):
        return self.chineseChar == str

    def getDescript(self):
        if self.isPolyphone:
            return [rhyme_sheet.mainTypeEnum[self.mainTypeIndex] ,rhyme_sheet.secondTypeEnum[self.mainTypeIndex][self.secondTypeIndex]]
        else:
            return [rhyme_sheet.mainTypeEnum[self.mainTypeIndex] , rhyme_sheet.secondTypeEnum[self.mainTypeIndex][self.secondTypeIndex]]

    def isPing(self):
        return self.mainTypeIndex < 2