# https://qiita.com/164kondo/items/eec4d1d8fd7648217935
# https://docs.gspread.org/en/latest/user-guide.html#opening-a-spreadsheet

import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

class recorder:
    worksheet = None
    sheet_data = []

    def __init__(self, jsonf, key):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
        gc = gspread.authorize(credentials)
        self.worksheet = gc.open_by_key(key).sheet1

    def get_length(self):
        return 1

    def add_row(self, array, point = 0):
        target = self.worksheet.row_values(point)
        print(target)
        return 0

