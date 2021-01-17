#coding:utf-8
import requests
import json
import config
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')


cookie = config.appcookie

def get_gameids_by_uid(uid, start):

    url = "https://mlol.qt.qq.com:443/go/battle_info/get_battle_list"
    #url = url.format(uid)

    header = {

            'User-Agent': 'QTL/8.5.3.10608 Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
            'cookie': cookie,
            'Host': 'mlol.qt.qq.com',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive'
            }

    data = {
            "target_uuid":uid,
            "start_idx":start,
            "self_uuid":"1c00dc77-7913-4ffe-b2a0-b6c6b7cbd7dd",
            "area_id":6,
            "search_type":0 
            }
    #print url, header
    res = requests.post(url, headers = header, data = json.dumps(data))
    # print res.text
    
    j = json.loads(res.text)


    games = j['data']['player_battle_brief_list']
    gameids = set()
    for game in games:
        gameId = game['game_id']
        gameids.add(gameId)

    # print gameids
    print uid, "对应的gameid个数", len(gameids)
    return gameids


def get_all_gameids():

    allids = set()
    uids = config.appuids
    for uid in uids:
        print uid
        allids = allids.union(get_gameids_by_uid(uid, 0))
        time.sleep(1)
        allids = allids.union(get_gameids_by_uid(uid, 10))
        time.sleep(1)
        allids = allids.union(get_gameids_by_uid(uid, 30))
        time.sleep(1)


    allids = list(allids)
    allids.sort()
    print allids
    print "一共的games id 个数：" + str(len(allids))
    write_id(allids)

def write_id(l):
    with open('gameids.txt', 'w') as f:
        for one in l:
            f.write(str(one)+'\n')

if __name__ == "__main__":
    get_all_gameids()
