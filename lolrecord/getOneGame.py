# coding:utf-8
import time
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'Connection': 'Keep-Alive'

            }

    url = url.format(gameId)
    res = requests.get(url, headers = headers)
    #print res.text
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

def get_all_game(gids):

    gameids.sort()
    gameids.reverse()

    res = []
    for gid in gameids:
        try:
            res.append(getGameInfo(gid))
        except:
            print "eeeeeeeeeeeeeeeerror"
            time.sleep(0.5)
            continue
        time.sleep(0.5)

    write_games(res)

def write_games(res):
    with open('gamesInfo.txt', 'w') as f:
        for j in res:
            f.write(json.dumps(j)+"\n")

def loadids():
    gids =[]
    with open('gameids.txt') as f:
        for line in f:
            gids.append(int(line.strip()))
    return gids;
    
if __name__ == '__main__':
    #gameids = [3923257969, 3923330122, 3946956970, 3947024964, 3949075785, 3949287769, 3949422019, 3950411125, 3953015900, 3955072694, 3971532645, 3978245610, 3978274691, 3979303809, 3979363234, 3979843242, 3979897320, 3979936505, 3980004018, 3980217989, 3980406333, 3980465082, 3980490647, 3981755053, 3982933219, 3983009837, 3984117989, 3984181587, 3985262855, 3985288243, 3985336146, 3986410471, 3986464671, 3986521395, 3986562783, 3986592450, 3986628164, 3986776582, 3986802839, 3986819841, 3986829280, 3986966370, 3986966961, 3987347172, 3987380678, 3987420152, 3987446167, 3987475842, 3987568564, 3987606793, 3987691950, 3988198489, 3988302349, 3988379325, 3988402575, 3988403665, 3988416552, 3988465750, 3988503212, 3988515788, 3988591088, 3988990434, 3989063481, 3989103103, 3989230594, 3990201209, 3990240015, 3991325074, 3991436045, 3991507999, 3991589252, 3991630342, 3991677143, 3992340114, 3992415924, 3992523006, 3992643639, 3992850382, 3992887550, 3993946520, 3993974727, 3994027573, 3994099437, 3994152149, 3994156138, 3994159415, 3994186861, 3994192594, 3995016398, 3995086913, 3995163280, 3995233116, 3995324871, 3995350251, 3995432547, 3995475684, 3995501214, 3995504708, 3995510322, 3995516732, 3995552119, 3995631829, 3995650876, 3995659802, 3995692522, 3995695427, 3995721430, 3995736461, 3995750045, 3995801564, 3995846634, 3996104115, 3996299398, 3996377875, 3996458086, 3996527221, 3996543615, 3996549232, 3996572043, 3996590075, 3996591687, 3996616349]
    #gameids = [3991325074]
    gameids = loadids()
    print gameids
    get_all_game(gameids)
