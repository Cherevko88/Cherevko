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

class Connection:

    def __init__(self, url, **kwargs):
        self.url = url
        self.kwargs = kwargs

    def req_get(self):
        res = None
        try:
            res = requests.get(self.url)
        except:
            pass
        return res

    def parse_resp(self):
        resp = self.req_get()
        if not resp:
            return
        if requests.get(self.url).status_code == 200:
            try:
                resp.json()
            except:
                pass
            else:
                return resp.json()

    def prep_answer(self):
        spisok = self.parse_resp()
        count = 0
        print("Время запроса", datetime.now())
        while count < len(spisok):
            for dik in spisok:
                if "CurrencyCodeL" and "Amount" in dik:
                    count += 1
                    res = f"{dik['CurrencyCodeL'], dik['Amount']}"
                    print(count, res)
                else:
                    raise TypeError

req = Connection("https://bank.gov.ua/NBU_Exchange/exchange?json")
pprint(req.prep_answer())



