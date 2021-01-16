#coding:utf-8
import requests
import json
import config
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')


cookie = config.cookie

def get_gameids_by_uid(uid, start):

    url = "https://mlol.qt.qq.com:443/go/battle_info/get_battle_list"
    #url = url.format(uid)

    header = {

            'User-Agent': 'QTL/8.5.3.10608 Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
            'cookie': 'clientType=9; l_uin=o1035628914; uin=o1035628914; p_uin=o1035628914; p_skey=6XQ1ID-wfrCRd4i4BWb9dOa9iOPr4uz8y9MvgqLA4jM_; uin=o1035628914; skey=MN7GYXePeI; userId=1c00dc77-7913-4ffe-b2a0-b6c6b7cbd7dd; accountType=1; tid=EC6248906A83EAF25CD228EB7E09515303CF022084AB9941EACD3B1B30448AE2BC44F503315CEDB63D2552036347D127B38A7B702123B5A37AD4D0A8343E20709C9EE37D025AC29CB1A954AABD35220FCA3BB17B7CC669E8E0149771EA87496890CE60B2BF983F5AC67984486289FE0EA754FBA11E20D0A5E8CCC9836FBDC33AB469F5C0C22C331BD36461E6B70959A6C70A896CA5B7CA01ABF00A448FCBEF2B;',
            'Host': 'mlol.qt.qq.com',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive'
            }

    data = {
            "target_uuid":uid,
            "start_idx":0,
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
