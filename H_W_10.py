# Подключитесь к API НБУ (описание API - https://old.bank.gov.ua/doccatalog/document?id=72819047),
# получите текущий курс валют и верните в таком виде:
# "дата создания запроса"
# 1 - "название ввалюты1" - - "курс"
# 2 - "название ввалюты2" - - "курс"
# 3 - "название ввалюты3" - - "курс"
# так все валюты, которые придут

from pprint import pprint
from _datetime import datetime
import requests
res = requests.get("https://bank.gov.ua/NBU_Exchange/exchange?json")
spisok = res.json()
print("Время запроса", datetime.now())
def Key_dic():
    count = 0
    while count < len(spisok):
        for dik in spisok:
            if "CurrencyCodeL" and "Amount" in dik:
                count += 1
                res = f"{dik['CurrencyCodeL'], dik['Amount']}"
                print(count, res)
            else:
                return TypeError
pprint(Key_dic())


# class Connection():
#
#     def __init__(self, url, **kwargs):
#         self.url = url
#         self.kwargs = kwargs
#         self.res = None
#
#     def req_get(self):
#         try:
#             self.res = requests.get(self.url)
#         except:
#             return
#
#     def parse_resp(self):
#         if not self.res:
#             return
#         if self.res.statuse_code == 200:
#             pass
#         else:
#             #todo: do smth
#             pass
#
#     def prep_answer(self,res):
#         if not self.res:
#             self.total = {}
#
# req = Connection("https://bank.gov.ua/NBU_Exchange/exchange?json")
# res = req.req_get()
# print(req)
