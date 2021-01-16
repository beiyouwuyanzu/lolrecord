import requests
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')


uid = "4006324864"
url = "https://lol.sw.game.qq.com/lol/api/?c=Battle&a=matchList&areaId=6&accountId={}&queueId=70,72,73,75,76,78,96,98,100,300,310,313,317,318,325,400,420,430,450,460,600,610,940,950,960,980,990,420,440,470,83,800,810,820,830,840,850&r1=matchList"
url = url.format(uid)

header = {
        'Referer': 'https://lol.qq.com/space/game_info.shtml',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        'cookie': 'tvfe_boss_uuid=a3fd2c426ef14455; ue_uid=75f3396c0983742d2f7360e284cd0390; RK=UAvj4TJqd7; ts_uid=3394960024; pgv_pvi=7898544128; o_cookie=1035628914; pgv_pvid=7383762540; ptcz=20951b80f91035c238b1966f3978fcbe22123cc2895e56019a29f70f3d06727b; pac_uid=1_1035628914; ue_uk=16d2cc594bb061290e306ede8d12eeb5; LW_pid=fed0b1e3213a119cdd06c3af6d28e051; ue_ts=1537581100; ue_skey=5dbc27e7e0847ef6d4daacf1f6d57ec3; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221686e3ef28648b-05e3f9cd2d58e7-9393265-1327104-1686e3ef28743c%22%2C%22%24device_id%22%3A%221686e3ef28648b-05e3f9cd2d58e7-9393265-1327104-1686e3ef28743c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; ied_qq=o1035628914; uin_cookie=o1035628914; XWINDEXGREY=0; eas_sid=01t5h8K2O6G4i4w5C1W6H9z6j4; PTTuserFirstTime=1585267200000; iip=0; ts_refer=xui.ptlogin2.qq.com/cgi-bin/xlogin; LW_uid=0185t9V8C6P8x3P1c4Q6t4G3F9; LW_sid=t1U5N9S8S6u8a3C2g083O5P3O0; ptui_loginuin=1035628914; gpmtips_data_his=%5B%7B%22id%22%3A%22308095%22%2C%22valid%22%3A1586532196%7D%2C%7B%22id%22%3A%22326935%22%2C%22valid%22%3A1610273668%7D%5D; PTTosSysFirstTime=1609027200000; PTTosFirstTime=1609027200000; weekloop=53-0-0-3; uin=o1035628914; isActDate=18642; PTTactFirstTime=1610668800000; LOLWebSet_AreaBindInfo_1035628914=%257B%2522areaid%2522%253A%25226%2522%252C%2522areaname%2522%253A%2522%25E5%25BE%25B7%25E7%258E%259B%25E8%25A5%25BF%25E4%25BA%259A%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221035628914%2522%252C%2522rolename%2522%253A%2522%25E4%25B8%258D%25E4%25B8%25A2%25E8%25B7%2591%25E8%25BD%25A6%25E4%25B8%25A8%25E5%25B0%258F%25E5%25AD%25A6%25E7%2594%259F%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1035628914%257C6%257C1035628914*%257C%257C%257C%257C%2525E4%2525B8%25258D%2525E4%2525B8%2525A2%2525E8%2525B7%252591%2525E8%2525BD%2525A6%2525E4%2525B8%2525A8%2525E5%2525B0%25258F%2525E5%2525AD%2525A6%2525E7%252594%25259F*%257C%257C%257C1610718954%257C%2522%252C%2522md5str%2522%253A%2522AEC6C82F590AFB90B59C6B942DDAEC66%2522%252C%2522roleareaid%2522%253A%25226%2522%252C%2522sPartition%2522%253A%25226%2522%257D; isHostDate=18643; pgv_info=ssid=s8535682136; _qpsvr_localtk=0.3069003065056002; gpmtips_cfg=%7B%22iSendApi%22%3A0%2C%22iShowCount%22%3A0%2C%22iOnlineCount%22%3A0%2C%22iSendOneCount%22%3A0%2C%22iShowAllCount%22%3A0%2C%22iHomeCount%22%3A0%7D; skey=@KgUUpMMYb; IED_LOG_INFO2=userUin%3D1035628914%26nickName%3Dohh%26nickname%3Dohh%26userLoginTime%3D1610769858%26logtype%3Dqq%26loginType%3Dqq%26uin%3D1035628914; isOsSysDate=18643; isOsDate=18643; tokenParams=%3Fe_code%3D507042; lolqqcomrouteLine=space_space_a20200608eternals_index-tool_index-page_space_space; ts_last=lol.qq.com/space/game_info.shtml'
        }

res = requests.get(url, headers = header)
#print res.text
j = json.loads(res.text[16:])

games = j['msg']['games']
gameids = []
for game in games:
    gameId = game['gameId']
    gameids.append(gameId)

print gameids
print len(gameids)

