# https://qiita.com/164kondo/items/eec4d1d8fd7648217935
# https://docs.gspread.org/en/latest/user-guide.html#opening-a-spreadsheet

import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

# 文字と数字の足し算を行う
def add_char(char, number):
    return chr(ord(char)+number)

# セルの番号を変換する
# CELL(1,1)-CELL(10,10)→'A1:J:10'
def convert_cellguige(x0, y0, x1, y1):
    return add_char('A', x0-1)+str(y0)+':'+add_char('A', x1-1)+str(y1)

class recorder:
    worksheet = None
    sheet_data = []

    def __init__(self, jsonf, key):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
        gc = gspread.authorize(credentials)
        self.worksheet = gc.open_by_key(key).sheet1
        self.sheet_data = self.worksheet.get_all_values()

    def get_length(self):
        return len(self.sheet_data)

    def add_row(self, array, strnize):
        # 挿入するデータ数がシートのデータ数と同じか
        if (len(self.sheet_data[0]) > 0 and len(array) != len(self.sheet_data[0])):
            return -1

        # 挿入するデータを全て文字列に変換する
        print(strnize)
        if (strnize == True):
            array = [str(i) for i in array]
            print(array)

        self.sheet_data.append(array)
        return 0

    def update(self):
        cellguid = convert_cellguige(1, 1, len(self.sheet_data[0]), len(self.sheet_data))
        self.worksheet.update(cellguid, self.sheet_data)
        return 0

