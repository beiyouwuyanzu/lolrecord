# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json



class Game:

    def __init__(self, j):
        self.users = []
        self.load_game(j)
        self.starttime = 0

    def load_game(self, j):
        j = json.loads(j)
        self.starttime = j['msg']['gameInfo']['gameCreationTime']
        particpiants = j['msg']['participants']
        for own in particpiants:
            user = UserPerGame()
            user.name = own['summonerName']
            user.aid = own['originalAccountId']
            status =  own['stats']
            user.win = status['win']
            user.kills =  status['kills']
            user.assists = status['assists']
            user.deaths =  status['deaths']
            self.users.append(user)

class UserPerGame:
    
    def __init__(self):
        self.name = ""
        self.aid = ""
        self.win = ""
        self.kills = 0
        self.assists = 0
        self.deaths = 0

    def tostring(self):
        res = [self.name, self.aid, self.win, self.kills, self.assists, self.deaths]
        return '\t'.join([str(x) for x in res])



class Person:


    def __init__(self, name):

        self.mp = {
            "jx": "2938141271",
            "wyq": "4006324864",
            "lv": "2955059434",
            "wz": "4017428073",
            "ds": "4007245078",
            "jj": "4006370018",
            "gm": "4030697601"
        }
        self.aid = self.mp[name]
        self.name = name
        self.games = []

    def add(self, pergame):
        self.games.append(pergame)

    def getnum(self):
        return len(self.games)

    def winrate(self):
        if not self.games:
            return 0

        return len([x for x in self.games if x.win == "Win"])*1.0/(len(self.games))

    def maxkill(self):
        return max([x.kills for x in self.games])

    def maxassists(self):
        return max([x.assists for x in self.games ])

    def mindeath(self):
        return min([x.deaths for x in self.games])

    def tostring(self):
        res = "{}\t games num:{}\t winrate:{}\tmaxkill:{}\tmaxassists:{}\tmindeath:{}".format(
                self.name, self.getnum(),self.winrate(), self.maxkill(),self.maxassists(),
                self.mindeath()
                )

        return res



if __name__ == '__main__':
    games = []
    with open('gamesInfo.txt') as f:
        for line in f:
            game = Game(line.strip())
            games.append(game)
    #print games[0].users[1].tostring()

    plist = "jx,wyq,lv,wz,ds,jj".split(',')
    persons = []
    for one in plist:
        persons.append(Person(one))

    # 遍历game,把match的userpergame 放到个人的games里
    for game in games:
        for per in game.users:
            #print per.tostring()
            for x in [ p for p in persons if str(p.aid) == str(per.aid)]:
                x.add(per)
    
    for person in persons:
        print person.tostring()



