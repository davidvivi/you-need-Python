# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
import requests
import os

# 武器URL地址
weapon_url = "http://gamehelper.gm825.com/wzry/equip/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
# 英雄列表URL地址
heros_url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"

# 英雄出装URL
hero_url = "http://gamehelper.gm825.com/wzry/hero/detail?hero_id={}&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"

headers = {
    'Accept-Charset': 'UTF-8',
    'Accept-Encoding': 'gzip,deflate',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Host': 'gamehelper.gm825.com'
}


# 下载王者荣耀英雄图片
def hero_imgs_download(url, header):
    # 获取文本.text 获取图片 .content
    req = requests.get(url=url, headers=header).json()
    print("一共有%d个英雄" % len(req['list']))
    hero_images_path = 'hero_images'
    hero_list = req['list']
    for each_hero in hero_list:
        hero_photo_url = each_hero['cover']
        hero_name = each_hero['name'] + '.jpg'
        filename = hero_images_path + '/' + hero_name
        print("正在下载 %s的图片" % each_hero['name'])
        if hero_images_path not in os.listdir():
            os.makedirs(hero_images_path)
        # 下载图片
        urlretrieve(url=hero_photo_url, filename=filename)


# 打印所有英雄的名字和ID
def hero_list(url, header):
    print('*' * 100)
    print('\t\t\t\t欢迎使用《王者荣耀》出装小助手！')
    print('*' * 100)
    req = requests.get(url=url, headers=header).json()
    flag = 0
    hero_list = req['list']
    for each_hero in hero_list:
        flag += 1
        # 为end传递一个\t，这样print函数不会在字符串末尾添加一个换行符，而是添加一个\t
        print("%s的ID为:%s" % (each_hero['name'], each_hero['hero_id']), end='\t\t')
        if flag == 3:
            # 先不加end  在加end 看效果
            print('\n', end='')
            flag = 0


# 根据equip_id查询武器名字和价格
# weapon_info - 存储所有武器的字典
def seek_weapon(equip_id, weapon_info):
    for each_weapon in weapon_info:
        if each_weapon['equip_id'] == str(equip_id):
            weapon_name = each_weapon['name']
            weapon_price = each_weapon['price']
            return weapon_name, weapon_price


# 获取武器信息
def hero_weapon(url, header):
    req = requests.get(url=url, headers=header).json()
    weapon_info_list = req['list']
    return weapon_info_list


# 获取并打印出装信息
# weapon_info  所有武器的字典
def hero_info(hero_id, url, header, weapon_info):
    req = requests.get(url=url.format(hero_id), headers=header).json()
    if req['error_code'] == 2:
        print("sorry,您输入的id有误,%s!" % (req['error_msg']))
    else:
        print("\n历史上的%s:\n %s" % (req['info']['name'], req['info']['history_intro']))
        for each_equip_choice in req['info']['equip_choice']:
            print('\n%s:%s' % (each_equip_choice['title'], each_equip_choice['description']))
            flag = 0
            total_price = 0
            for each_weapon in each_equip_choice['list']:
                flag += 1
                weapon = seek_weapon(each_weapon['equip_id'], weapon_info)
                weapon_name = weapon[0]
                weapon_price = weapon[1]
                print('%s:%s' % (weapon_name, weapon_price), end='\t')
                if flag == 3:
                    print('\n', end='')
                    flag = 0
                total_price += int(weapon_price)
            print("神装套件共计:%d" % total_price)


hero_list(url=heros_url, header=headers)
weapon_info = hero_weapon(weapon_url, headers)

hero_id = int(input('\n请输入你要查询的英雄ID?'))

hero_info(hero_id=hero_id, url=hero_url, header=headers, weapon_info=weapon_info)
