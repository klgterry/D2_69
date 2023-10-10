from flask import Flask, render_template, request, g
import pymysql
from datetime import datetime

sensor_db = pymysql.connect(
    user='root',
    passwd='12341234',
    host='127.0.0.1',
    db='D2_69',
    charset='utf8'
)

#cursor = sensor_db.cursor(pymysql.cursors.DictCursor)
cursor = sensor_db.cursor()

#sql = "DELETE FROM sensor WHERE _id = 2;"
sql = "SELECT * FROM D2_69.table_s3_result"

cursor.execute(sql)

data_list = cursor.fetchall()
#print(data_list)

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')  # 접속하는 url
def main():

    sql = "SELECT * from D2_69.table_s3_result"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    print(data_list)

    now = datetime.now()

    return render_template('index.html', data_list=data_list, now=now.date())


@app.route('/next')
def next():
    name = request.args.get('name')

    sql = "SELECT * from D2_69.table_s3_result where id = " + "'" + name + "'"

    cursor.execute(sql)
    data_list = cursor.fetchall()
    print(data_list)

    if not data_list :
        name1 = "언랭크"
    else:
        name1 = name

    print(name)

    now = datetime.now()

    return render_template("next.html", data_list=data_list, name=name, name1=name1, now=now.date())

@app.route('/next_cur_season_total')
def next_cur_season_total():
    name = request.args.get('name')
    print(name)

    sql = "SELECT * from D2_69.table_cur_s_result"

    cursor.execute(sql)
    data_list = cursor.fetchall()
    print(data_list)

    now = datetime.now()

    return render_template("next_cur_season_total.html", data_list=data_list, name=name, now=now.date())

@app.route('/next_season2')
def next_season2():
    season = request.args.get('season')
    name = request.args.get('name')
    print(season)
    print(name)
    player_name = ""

    if name == "린스":
        player_name = "lince"
    elif name == "태식":
        player_name = "taesik"
    elif name == "반짝":
        player_name = "banzzak"
    elif name == "민형":
        player_name = "mh"
    elif name == "하리보":
        player_name = "haribo"
    elif name == "야로":
        player_name = "yaro"
    elif name == "훈":
        player_name = "hoon"
    elif name == "넘버":
        player_name = "number"
    elif name == "용이":
        player_name = "yongi"
    elif name == "용갈":
        player_name = "yongal"
    elif name == "울프":
        player_name = "wolf"
    elif name == "조네":
        player_name = "jone"
    elif name == "사카시":
        player_name = "sakasy"
    elif name == "블핑":
        player_name = "blackpink"
    elif name == "도건":
        player_name = "dogeon"
    elif name == "살수":
        player_name = "salsu"
    elif name == "참치":
        player_name = "chamchi"
    elif name == "르기":
        player_name = "rgi"
    elif name == "플토":
        player_name = "pluto"
    elif name == "필찌":
        player_name = "pilzzi"
    elif name == "솔":
        player_name = "sol"
    elif name == "라위":
        player_name = "lawe"
    else:
        player_name = ""

    print(player_name)

    if season == "season2":
        sql = "SELECT * from D2_69.table_s2_result where id = " + "'" + name + "'"
    else:
        sql = "SELECT * from D2_69.table_s3_result where id = " + "'" + name + "'"

    cursor.execute(sql)
    data_list = cursor.fetchall()

    if season == "season2":
        sql = "SELECT * from D2_69.table_s2_char where id = " + "'" + name + "'"
    else:
        sql = "SELECT * from D2_69.table_s3_char where id = " + "'" + name + "'"

    cursor.execute(sql)
    data_list_char = cursor.fetchall()
    print(data_list_char)

    if not player_name == "":

        if season == "season2":
            sql = "SELECT * FROM d2_69.table_s2_duo_win_rate_" + player_name
        else:
            sql = "SELECT * FROM d2_69.table_s3_duo_win_rate_" + player_name

        print(sql)
        cursor.execute(sql)
        data_list_duo_win_rate = cursor.fetchall()
        print(data_list_duo_win_rate)

        if season == "season2":
            sql = "SELECT * FROM d2_69.table_s2_relative_record_" + player_name
        else:
            sql = "SELECT * FROM d2_69.table_s3_relative_record_" + player_name

        cursor.execute(sql)
        data_list_relative_record = cursor.fetchall()
        print(data_list_relative_record)

        if season == "season2":
            sql = "SELECT * FROM d2_69.table_s2_win_lose_straight_" + player_name
        else:
            sql = "SELECT * FROM d2_69.table_s3_win_lose_straight_" + player_name

        cursor.execute(sql)
        data_list_win_lose_straight = cursor.fetchall()
        print(data_list_win_lose_straight)
    else:
        data_list_duo_win_rate = []
        data_list_relative_record = []
        data_list_win_lose_straight = []

        name1 = "언랭크"

    now = datetime.now()

    return render_template("next_season2.html", data_list=data_list,
                           name=name,
                           name1=name1,
                           season=season,
                           data_list_char=data_list_char,
                           data_list_duo_win_rate=data_list_duo_win_rate,
                           data_list_relative_record=data_list_relative_record,
                           data_list_win_lose_straight=data_list_win_lose_straight,
                           now=now.date())


if __name__ == '__main__':
    #app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    app.run(host="0.0.0.0", port="6969", debug=True)