#coding:utf-8
import requests
import json
import config
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')


cookie = config.cookie

def get_gameids_by_uid(uid):

    url = "https://lol.sw.game.qq.com/lol/api/?c=Battle&a=matchList&areaId=6&accountId={}&queueId=70,72,73,75,76,78,96,98,100,300,310,313,317,318,325,400,420,430,450,460,600,610,940,950,960,980,990,420,440,470,83,800,810,820,830,840,850&r1=matchList"
    url = url.format(uid)

    header = {

            'Referer': 'https://lol.qq.com/space/game_info.shtml',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
            'cookie': cookie
            }

    print url, header
    res = requests.get(url, headers = header)
    print res.text
    j = json.loads(res.text[16:])

    games = j['msg']['games']
    gameids = set()
    for game in games:
        gameId = game['gameId']
        gameids.add(gameId)

    #print gameids
    print uid, "对应的gameid个数", len(gameids)
    return gameids


def get_all_gameids():

    allids = set()
    uids = config.uids
    for uid in uids:
        print uid
        allids = allids.union(get_gameids_by_uid(uid))
        time.sleep(1)


    allids = list(allids)
    allids.sort()
    print "一共的games id 个数：" + str(len(allids))

if __name__ == "__main__":
    get_all_gameids()
