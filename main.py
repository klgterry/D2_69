# 샘플 Python 스크립트입니다.

# ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.

import pymysql
from openpyxl import load_workbook
import pandas as pd
from tabulate import tabulate
from flask import Flask, render_template, request
import timer

sensor_db = pymysql.connect(
    user='root',
    passwd='12341234',
    host='127.0.0.1',
    db='D2_69',
    charset='utf8'
)

#cursor = sensor_db.cursor(pymysql.cursors.DictCursor)
cursor = sensor_db.cursor()

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':

    load_wb = load_workbook("input/69내전기록표_0920_v27.xlsm", read_only=True, data_only=True)
    print(load_wb.sheetnames)

    load_ws = load_wb['현재시즌']

    load_wb_s2 = load_workbook("input/시즌2.xlsx", read_only=True, data_only=True)
    print(load_wb_s2.sheetnames)

    load_ws_s2 = load_wb_s2['결과']

#####################################################
    index_s2 = []

    get_cells = load_ws_s2['A2': 'F2']
    for row in get_cells:
        for cell in row:
            index_s2.append(cell.value)
    print(index_s2)

    rank_s2 = []
    get_cells = load_ws_s2['A3': 'A19']
    for row in get_cells:
        for cell in row:
            rank_s2.append(cell.value)
    print(rank_s2)

    tier_s2 = []
    get_cells = load_ws_s2['B3': 'B19']
    for row in get_cells:
        for cell in row:
            tier_s2.append(cell.value)
    print(tier_s2)

    id_s2 = []
    get_cells = load_ws_s2['C3': 'C19']
    for row in get_cells:
        for cell in row:
            id_s2.append(cell.value)
    print(id_s2)

    tier_score_s2 = []
    get_cells = load_ws_s2['D3': 'D19']
    for row in get_cells:
        for cell in row:
            tier_score_s2.append(round(cell.value, 2))
    print(tier_score_s2)

    mmr_rank_s2 = []
    get_cells = load_ws_s2['E3': 'E19']
    for row in get_cells:
        for cell in row:
            mmr_rank_s2.append(cell.value)
    print(mmr_rank_s2)

    total_game_s2 = []
    get_cells = load_ws_s2['F3': 'F19']
    for row in get_cells:
        for cell in row:
            total_game_s2.append(cell.value)
    print(total_game_s2)

#####################################################

    index = []

    get_cells = load_ws['B83': 'G83']
    for row in get_cells:
        for cell in row:
            index.append(cell.value)
    print(index)

    rank = []
    get_cells = load_ws['B84': 'B103']
    for row in get_cells:
        for cell in row:
            rank.append(cell.value)
    print(rank)

    tier = []
    get_cells = load_ws['C84': 'C103']
    for row in get_cells:
        for cell in row:
            tier.append(cell.value)
    print(tier)

    id = []
    get_cells = load_ws['D84': 'D103']
    for row in get_cells:
        for cell in row:
            id.append(cell.value)
    print(id)

    tier_score = []
    get_cells = load_ws['E84': 'E103']
    for row in get_cells:
        for cell in row:
            tier_score.append(round(cell.value, 2))
    print(tier_score)

    mmr_rank = []
    get_cells = load_ws['F84': 'F103']
    for row in get_cells:
        for cell in row:
            mmr_rank.append(cell.value)
    print(mmr_rank)

    total_game = []
    get_cells = load_ws['G84': 'G103']
    for row in get_cells:
        for cell in row:
            total_game.append(cell.value)
    print(total_game)

    #result = pd.DataFrame({'전체 순위':rank, '티어':tier, '아이디':id, '티어점수':tier_score, 'MMR순위':mmr_rank, '총 게임수':total_game})
    #print(tabulate(result, headers='keys', tablefmt='grid', showindex=True, stralign='center'))

    i = 0
    index = 1
    index_s2 = 1
    for i in range(len(rank)):
        sql = "INSERT INTO D2_69.table_s3 VALUES(" + '"' + str(index) + '","' + rank[i] + '","' + tier[i] + '","' + id[i] + '","' + str(tier_score[i]) + '","' + str(mmr_rank[i]) + '","' + str(total_game[i]) + '")'
        cursor.execute(sql)
        index = index + 1

    for i in range(len(rank_s2)):
        sql_s2 = "INSERT INTO D2_69.table_s2 VALUES(" + '"' + str(index_s2) + '","' + rank_s2[i] + '","' + tier_s2[i] + '","' + id_s2[i] + '","' + str(tier_score_s2[i]) + '","' + str(mmr_rank_s2[i]) + '","' + str(total_game_s2[i]) + '")'
        cursor.execute(sql_s2)
        index_s2 = index_s2 + 1

    sensor_db.commit()

    #sql = "SELECT * from D2_69.table_s3"
    #cursor.execute(sql)
    #data_list = cursor.fetchall()

    #for data in data_list:
    #    print(data)


load_wb.close()
load_wb_s2.close()
cursor.close()