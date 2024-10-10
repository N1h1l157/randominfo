import json
import random


def get_city_coordinates(filename='./data/city_region.json'):
    # JSON 数据字符串（假设已从文件city_region.json读取到）
    with open(filename, 'r', encoding='utf-8') as f:
        json_data = f.read()

    # 转换为Python字典
    data = json.loads(json_data)

    # 随机选择一个省份
    province = random.choice(data['districts'])

    # 随机选择一个城市
    while True:
        try:
            # 验证城市列表是否不为空
            city = random.choice(province['districts'])
            break
        except IndexError:
            # 如果城市列表为空，则选择另一个省份
            province = random.choice(data['districts'])

    # 如果该城市包含了自己的地区，则选择其中一个地区并打印相关信息
    if 'districts' in city and city['districts']:
        district = random.choice(city['districts'])
        # print(f"{province['name']} {city['name']} {district['name']}")
        # print(f"{district['center']['longitude']} {district['center']['latitude']}")
        return f"{province['name']} {city['name']} {district['name']}", f"{district['center']['longitude']} {district['center']['latitude']}"

    # 如果该城市没有自己的地区，则直接打印省名和城市信息
    else:
        # print(f"{province['name']} {city['name']}")
        # print(f"{city['center']['longitude']} {city['center']['latitude']}")
        return f"{province['name']} {city['name']}", f"{city['center']['longitude']} {city['center']['latitude']}"


if __name__ == "__main__":
    city, coordinates = get_city_coordinates('../data/city_region.json')
    print(f"城市：{city}")
    print(f"经纬度：{coordinates}")
