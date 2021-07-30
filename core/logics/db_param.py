# encoding: utf-8
# author TurboChang

from faker import Faker
from datetime import timedelta, datetime
import datetime
import threading

def db_cost(start_time):
    """
    记录数据库操作耗时
    """
    stop_time = datetime.datetime.now()
    ms = (stop_time - start_time)
    print(str(ms.total_seconds())+'s')

fake = Faker('zh_CN')

class PtDataGen():

    def __init__(self, num):
        self.num = num
        self.data_list = []
        self.array = []

    def fake_data(self):
        pt_profile = fake.profile()
        col1 = f"{fake.pyint(15000,17000):05}"
        col2 = f"{fake.pyint(200,350):05}"
        col3 = pt_profile['name']
        col4 = pt_profile['sex']
        col5 = fake.pyint(15,50)
        col6 = fake.past_datetime(start_date="-30d",tzinfo=None)
        col7 = fake.past_datetime(start_date=col6+timedelta(days=1),tzinfo=None)
        return col1, col2, col3, col4, col5, col6, col7

    def get_datas(self):
        for row in range(0, self.num):
            self.data_list.append(self.fake_data())
        return self.data_list

def thds(thd):
    f = PtDataGen(100)
    data = f.get_datas()
    thread = [threading.Thread(target=data) for i in range(thd)]
    for t in thread:
        t.start()
    for t in thread:
        t.join()

if __name__ == '__main__':
    print(thds(5))



