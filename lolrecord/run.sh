python getGameListbyapp.py && python getOneGame.py && python view_game.py




if [ $? -eq 0 ]
then
    status="更新成功"
else
    status="更新失败,请更新cookie"
fi
timetxt="最近一次更新时间:$(date) ----------> ${status}" 
echo $timetxt
echo $timetxt>templates/status.txt
