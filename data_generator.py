#!/usr/bin/python3
import csv
import json
import random
import radar


# read json file to get level3 address
def jsonreader():
    return json.loads(open('./src/level3.json', 'r', encoding='utf-8').read())


# read txt file to get level4 address
def txtreader():
    return open('./src/level4.txt', 'r', encoding='utf-8').readlines()


__address_list = jsonreader()

__level4_list = txtreader()

__level4_temp = []

province = random.choice(__address_list[:-3])


def generate():
    city = random.choice(province['regionEntitys'])
    county = random.choice(city['regionEntitys'][1:])
    for item in __level4_list:
        if item[0:6] == county['code']:
            __level4_temp.append(item[13:])
    town = random.choice(__level4_temp).replace('\n', '')
    number = str(random.randint(1, 100)).zfill(3) + "号"
    room = str(random.randint(1, 999)).zfill(3) + "室"
    return [province['region'], city['region'], county['region'], town, number + room]


header = ['fault_id', 'fault_type', 'fault_1', 'fault_2',
          'province', 'city', 'county', 'town', 'detail', 'fault_time']

with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    f1 = ['业务不能使用', '业务使用部分功能出现异常', '其他错误提示', '其他问题']
    f2 = ['铜缆接入方式', 'FTTH光纤接入方式', 'FTTB+LAN', 'FTTO']
    datas = []
    for i in range(1001):
        address = generate()
        t = radar.random_datetime("2021-01-01T00:00:00", "2021-12-31T23:59:59")
        data = [i, '普通故障', random.choice(f1), random.choice(f2), address[0], address[1], address[2], address[3],
                address[4], t]
        datas.append(data)
    writer.writerows(datas)

file.close()
