# coding:utf-8
import requests
import json
import config

import sys
reload(sys)
sys.setdefaultencoding('utf8')

cookie = config.cookie
def getGameInfo(gameId):
    # gameId = "3992850382"
    #gameId = "3987691951"
    url = "https://lol.sw.game.qq.com/lol/api/?c=Battle&a=combatGains&areaId=6&gameId={}&r1=combatGains"
    headers = {'cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
            }

    url = url.format(gameId)
    res = requests.get(url, headers = headers)
    # print res.text[18:]
    j = json.loads(res.text[18:])
    particpiants = j['msg']['participants']

    starttime = j['msg']['gameInfo']['gameCreationTime']
    for own in particpiants:
        username = own['summonerName']
        uid = own['originalAccountId']
        status = own['stats']
        win = status['win']
        kills = status['kills']
        assists = status['assists']
        deaths = status['deaths']
        reslist = [username, uid, win, kills, assists, deaths]
        print '\t'.join([str(x) for x in reslist])
    print "\n\n\n"
    return j

def get_all_game():
    gameids = [3985288243, 3987568564, 3987691950, 3988416552, 3988465750, 3988990434, 3992850382, 3992887550, 3993946520, 3993974727, 3994027573, 3994099437, 3995163280, 3995233116, 3995324871, 3995350251, 3995432547, 3995475684, 3995501214, 3995504708, 3995510322, 3995516732, 3995552119, 3995631829, 3995650876, 3995659802, 3995692522, 3995695427, 3995721430, 3995736461, 3995750045, 3995801564, 3995846634, 3996104115, 3996299398, 3996377875, 3996458086]
    gameids.sort()
    gameids.reverse()

    res = []
    for gid in gameids:
        res.append(getGameInfo(gid))

    write_games(res)

def write_games(res):
    with open('gamesInfo.txt', 'w') as f:
        for j in res:
            f.write(json.dumps(j)+"\n")
    
if __name__ == '__main__':
    get_all_game()
