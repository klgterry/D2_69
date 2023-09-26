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
sql = "SELECT * FROM D2_69.table_s3"

cursor.execute(sql)

data_list = cursor.fetchall()
#print(data_list)

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')  # 접속하는 url
def main():

    sql = "SELECT * from D2_69.table_s3"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    print(data_list)

    now = datetime.now()

    return render_template('index.html', data_list=data_list, now=now.date())


@app.route('/next')
def next():
    name = request.args.get('name')

    sql = "SELECT * from D2_69.table_s3 where id = " + "'" + name + "'"


    cursor.execute(sql)
    data_list = cursor.fetchall()
    print(data_list)

    now = datetime.now()

    return render_template("next.html", data_list=data_list, name=name, now=now.date())

@app.route('/next_cur_season_total')
def next_cur_season_total():
    name = request.args.get('name')
    print(name)

    sql = "SELECT * from D2_69.table_s3"

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

    sql = "SELECT * from D2_69.table_s2 where id = " + "'" + name + "'"

    cursor.execute(sql)
    data_list = cursor.fetchall()

    now = datetime.now()

    return render_template("next_season2.html", data_list=data_list, name=name, now=now.date())


if __name__ == '__main__':
    #app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    app.run(host="0.0.0.0", port="6969", debug=True)