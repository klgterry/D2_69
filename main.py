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

    load_wb_s3 = load_workbook("input/시즌3.xlsx", read_only=True, data_only=True)
    print(load_wb_s3.sheetnames)

    load_ws_s3 = load_wb_s3['결과']

#####################################################
    index_s2 = []

    get_cells = load_ws_s2['A2': 'U2']
    for row in get_cells:
        for cell in row:
            index_s2.append(cell.value)
    print(index_s2)

    rank_s2 = []
    get_cells = load_ws_s2['A3': 'A22']
    for row in get_cells:
        for cell in row:
            rank_s2.append(cell.value)
    print(rank_s2)

    tier_s2 = []
    get_cells = load_ws_s2['B3': 'B22']
    for row in get_cells:
        for cell in row:
            tier_s2.append(cell.value)
    print(tier_s2)

    id_s2 = []
    get_cells = load_ws_s2['C3': 'C22']
    for row in get_cells:
        for cell in row:
            id_s2.append(cell.value)
    print(id_s2)

    tier_score_s2 = []
    get_cells = load_ws_s2['D3': 'D22']
    for row in get_cells:
        for cell in row:
            tier_score_s2.append(round(cell.value, 2))
    print(tier_score_s2)

    mmr_rank_s2 = []
    get_cells = load_ws_s2['E3': 'E22']
    for row in get_cells:
        for cell in row:
            mmr_rank_s2.append(cell.value)
    print(mmr_rank_s2)

    total_game_s2 = []
    get_cells = load_ws_s2['F3': 'F22']
    for row in get_cells:
        for cell in row:
            total_game_s2.append(cell.value)
    print(total_game_s2)

    total_win_s2 = []
    get_cells = load_ws_s2['G3': 'G22']
    for row in get_cells:
        for cell in row:
            total_win_s2.append(cell.value)
    print(total_win_s2)

    total_lose_s2 = []
    get_cells = load_ws_s2['H3': 'H22']
    for row in get_cells:
        for cell in row:
            total_lose_s2.append(cell.value)
    print(total_lose_s2)

    total_rate_s2 = []
    get_cells = load_ws_s2['I3': 'I22']
    for row in get_cells:
        for cell in row:
            total_rate_s2.append(round(cell.value*100, 1))
    print(total_rate_s2)

    druid_win_s2 = []
    get_cells = load_ws_s2['J3': 'J22']
    for row in get_cells:
        for cell in row:
            druid_win_s2.append(cell.value)
    print(druid_win_s2)

    druid_lose_s2 = []
    get_cells = load_ws_s2['K3': 'K22']
    for row in get_cells:
        for cell in row:
            druid_lose_s2.append(cell.value)
    print(druid_lose_s2)

    druid_rate_s2 = []
    get_cells = load_ws_s2['L3': 'L22']
    for row in get_cells:
        for cell in row:
            druid_rate_s2.append(round(cell.value*100, 1))
    print(druid_rate_s2)

    ass_win_s2 = []
    get_cells = load_ws_s2['M3': 'M22']
    for row in get_cells:
        for cell in row:
            ass_win_s2.append(cell.value)
    print(ass_win_s2)

    ass_lose_s2 = []
    get_cells = load_ws_s2['N3': 'N22']
    for row in get_cells:
        for cell in row:
            ass_lose_s2.append(cell.value)
    print(ass_lose_s2)

    ass_rate_s2 = []
    get_cells = load_ws_s2['O3': 'O22']
    for row in get_cells:
        for cell in row:
            ass_rate_s2.append(round(cell.value*100, 1))
    print(ass_rate_s2)

    nec_win_s2 = []
    get_cells = load_ws_s2['P3': 'P22']
    for row in get_cells:
        for cell in row:
            nec_win_s2.append(cell.value)
    print(nec_win_s2)

    nec_lose_s2 = []
    get_cells = load_ws_s2['Q3': 'Q22']
    for row in get_cells:
        for cell in row:
            nec_lose_s2.append(cell.value)
    print(nec_lose_s2)

    nec_rate_s2 = []
    get_cells = load_ws_s2['R3': 'R22']
    for row in get_cells:
        for cell in row:
            nec_rate_s2.append(round(cell.value*100, 1))
    print(nec_rate_s2)

    pala_win_s2 = []
    get_cells = load_ws_s2['S3': 'S22']
    for row in get_cells:
        for cell in row:
            pala_win_s2.append(cell.value)
    print(pala_win_s2)

    pala_lose_s2 = []
    get_cells = load_ws_s2['T3': 'T22']
    for row in get_cells:
        for cell in row:
            pala_lose_s2.append(cell.value)
    print(pala_lose_s2)

    pala_rate_s2 = []
    get_cells = load_ws_s2['U3': 'U22']
    for row in get_cells:
        for cell in row:
            pala_rate_s2.append(round(cell.value*100, 1))
    print(pala_rate_s2)

#####################################################

    index_s3 = []

    get_cells = load_ws_s3['A2': 'F2']
    for row in get_cells:
        for cell in row:
            index_s3.append(cell.value)
    print(index_s3)

    rank_s3 = []
    get_cells = load_ws_s3['A3': 'A22']
    for row in get_cells:
        for cell in row:
            rank_s3.append(cell.value)
    print(rank_s3)

    tier_s3 = []
    get_cells = load_ws_s3['B3': 'B22']
    for row in get_cells:
        for cell in row:
            tier_s3.append(cell.value)
    print(tier_s3)

    id_s3 = []
    get_cells = load_ws_s3['C3': 'C22']
    for row in get_cells:
        for cell in row:
            id_s3.append(cell.value)
    print(id_s3)

    tier_score_s3 = []
    get_cells = load_ws_s3['D3': 'D22']
    for row in get_cells:
        for cell in row:
            tier_score_s3.append(round(cell.value, 2))
    print(tier_score_s3)

    mmr_rank_s3 = []
    get_cells = load_ws_s3['E3': 'E22']
    for row in get_cells:
        for cell in row:
            mmr_rank_s3.append(cell.value)
    print(mmr_rank_s3)

    total_game_s3 = []
    get_cells = load_ws_s3['F3': 'F22']
    for row in get_cells:
        for cell in row:
            total_game_s3.append(cell.value)
    print(total_game_s3)

    total_win_s3 = []
    get_cells = load_ws_s3['G3': 'G22']
    for row in get_cells:
        for cell in row:
            total_win_s3.append(cell.value)
    print(total_win_s3)

    total_lose_s3 = []
    get_cells = load_ws_s3['H3': 'H22']
    for row in get_cells:
        for cell in row:
            total_lose_s3.append(cell.value)
    print(total_lose_s3)

    total_rate_s3 = []
    get_cells = load_ws_s3['I3': 'I22']
    for row in get_cells:
        for cell in row:
            total_rate_s3.append(round(cell.value * 100, 1))
    print(total_rate_s3)

    druid_win_s3 = []
    get_cells = load_ws_s3['J3': 'J22']
    for row in get_cells:
        for cell in row:
            druid_win_s3.append(cell.value)
    print(druid_win_s3)

    druid_lose_s3 = []
    get_cells = load_ws_s3['K3': 'K22']
    for row in get_cells:
        for cell in row:
            druid_lose_s3.append(cell.value)
    print(druid_lose_s3)

    druid_rate_s3 = []
    get_cells = load_ws_s3['L3': 'L22']
    for row in get_cells:
        for cell in row:
            druid_rate_s3.append(round(cell.value * 100, 1))
    print(druid_rate_s3)

    ass_win_s3 = []
    get_cells = load_ws_s3['M3': 'M22']
    for row in get_cells:
        for cell in row:
            ass_win_s3.append(cell.value)
    print(ass_win_s3)

    ass_lose_s3 = []
    get_cells = load_ws_s3['N3': 'N22']
    for row in get_cells:
        for cell in row:
            ass_lose_s3.append(cell.value)
    print(ass_lose_s3)

    ass_rate_s3 = []
    get_cells = load_ws_s3['O3': 'O22']
    for row in get_cells:
        for cell in row:
            ass_rate_s3.append(round(cell.value * 100, 1))
    print(ass_rate_s3)

    nec_win_s3 = []
    get_cells = load_ws_s3['P3': 'P22']
    for row in get_cells:
        for cell in row:
            nec_win_s3.append(cell.value)
    print(nec_win_s3)

    nec_lose_s3 = []
    get_cells = load_ws_s3['Q3': 'Q22']
    for row in get_cells:
        for cell in row:
            nec_lose_s3.append(cell.value)
    print(nec_lose_s3)

    nec_rate_s3 = []
    get_cells = load_ws_s3['R3': 'R22']
    for row in get_cells:
        for cell in row:
            nec_rate_s3.append(round(cell.value * 100, 1))
    print(nec_rate_s3)

    pala_win_s3 = []
    get_cells = load_ws_s3['S3': 'S22']
    for row in get_cells:
        for cell in row:
            pala_win_s3.append(cell.value)
    print(pala_win_s3)

    pala_lose_s3 = []
    get_cells = load_ws_s3['T3': 'T22']
    for row in get_cells:
        for cell in row:
            pala_lose_s3.append(cell.value)
    print(pala_lose_s3)

    pala_rate_s3 = []
    get_cells = load_ws_s3['U3': 'U22']
    for row in get_cells:
        for cell in row:
            pala_rate_s3.append(round(cell.value * 100, 1))
    print(pala_rate_s3)

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
    index_s3 = 1

    sql = "DELETE FROM D2_69.table_cur_s_result"
    cursor.execute(sql)
    sql = "DELETE FROM D2_69.table_s2_result"
    cursor.execute(sql)
    sql = "DELETE FROM D2_69.table_s3_result"
    cursor.execute(sql)

    for i in range(len(rank)):
        sql = "INSERT INTO D2_69.table_cur_s_result VALUES(" + '"' + str(index) + '","' + rank[i] + '","' + tier[i] + '","' + id[i] + '","' + str(tier_score[i]) + '","' + str(mmr_rank[i]) + '","' + str(total_game[i]) + '")'
        cursor.execute(sql)
        index = index + 1

    for i in range(len(rank_s2)):
        sql_s2 = ("INSERT INTO D2_69.table_s2_result VALUES(" + '"' + str(index_s2) + '","' +
                  rank_s2[i] + '","' +
                  tier_s2[i] + '","' +
                  id_s2[i] + '","' +
                  str(tier_score_s2[i]) + '","' +
                  str(mmr_rank_s2[i]) + '","' +
                  str(total_game_s2[i]) + '","' +
                  str(total_win_s2[i]) + '","' +
                  str(total_lose_s2[i]) + '","' +
                  str(total_rate_s2[i]) + "%" + '","' +
                  str(druid_win_s2[i]) + '","' +
                  str(druid_lose_s2[i]) + '","' +
                  str(druid_rate_s2[i]) + "%" + '","' +
                  str(ass_win_s2[i]) + '","' +
                  str(ass_lose_s2[i]) + '","' +
                  str(ass_rate_s2[i]) + "%" + '","' +
                  str(nec_win_s2[i]) + '","' +
                  str(nec_lose_s2[i]) + '","' +
                  str(nec_rate_s2[i]) + "%" + '","' +
                  str(pala_win_s2[i]) + '","' +
                  str(pala_lose_s2[i]) + '","' +
                  str(pala_rate_s2[i]) + "%" + '")')
        cursor.execute(sql_s2)
        index_s2 = index_s2 + 1

    for i in range(len(rank_s3)):
        sql_s3 = ("INSERT INTO D2_69.table_s3_result VALUES(" + '"' + str(index_s3) + '","' +
                  rank_s3[i] + '","' +
                  tier_s3[i] + '","' +
                  id_s3[i] + '","' +
                  str(tier_score_s3[i]) + '","' +
                  str(mmr_rank_s3[i]) + '","' +
                  str(total_game_s3[i]) + '","' +
                  str(total_win_s3[i]) + '","' +
                  str(total_lose_s3[i]) + '","' +
                  str(total_rate_s3[i]) + "%" + '","' +
                  str(druid_win_s3[i]) + '","' +
                  str(druid_lose_s3[i]) + '","' +
                  str(druid_rate_s3[i]) + "%" + '","' +
                  str(ass_win_s3[i]) + '","' +
                  str(ass_lose_s3[i]) + '","' +
                  str(ass_rate_s3[i]) + "%" + '","' +
                  str(nec_win_s3[i]) + '","' +
                  str(nec_lose_s3[i]) + '","' +
                  str(nec_rate_s3[i]) + "%" + '","' +
                  str(pala_win_s3[i]) + '","' +
                  str(pala_lose_s3[i]) + '","' +
                  str(pala_rate_s3[i]) + "%" + '")')
        cursor.execute(sql_s3)
        index_s3 = index_s3 + 1

    sensor_db.commit()

    #####################################################
    load_ws_s2 = load_wb_s2['주캐릭']

    id_s2 = []

    get_cells = load_ws_s2['A3': 'A39']
    for row in get_cells:
        for cell in row:
            id_s2.append(cell.value)
    print(id_s2)

    dru_s2 = []

    get_cells = load_ws_s2['B3': 'B39']
    for row in get_cells:
        for cell in row:
            dru_s2.append(cell.value)
    print(dru_s2)

    ass_s2 = []

    get_cells = load_ws_s2['C3': 'C39']
    for row in get_cells:
        for cell in row:
            ass_s2.append(cell.value)
    print(ass_s2)

    nec_s2 = []

    get_cells = load_ws_s2['D3': 'D39']
    for row in get_cells:
        for cell in row:
            nec_s2.append(cell.value)
    print(nec_s2)

    sm_s2 = []

    get_cells = load_ws_s2['E3': 'E39']
    for row in get_cells:
        for cell in row:
            sm_s2.append(cell.value)
    print(sm_s2)

    #####################################################
    load_ws_s3 = load_wb_s3['주캐릭']

    id_s3 = []

    get_cells = load_ws_s3['A3': 'A39']
    for row in get_cells:
        for cell in row:
            id_s3.append(cell.value)
    print(id_s3)

    dru_s3 = []

    get_cells = load_ws_s3['B3': 'B39']
    for row in get_cells:
        for cell in row:
            dru_s3.append(cell.value)
    print(dru_s3)

    ass_s3 = []

    get_cells = load_ws_s3['C3': 'C39']
    for row in get_cells:
        for cell in row:
            ass_s3.append(cell.value)
    print(ass_s3)

    nec_s3 = []

    get_cells = load_ws_s3['D3': 'D39']
    for row in get_cells:
        for cell in row:
            nec_s3.append(cell.value)
    print(nec_s3)

    sm_s3 = []

    get_cells = load_ws_s3['E3': 'E39']
    for row in get_cells:
        for cell in row:
            sm_s3.append(cell.value)
    print(sm_s3)

    sql = "DELETE FROM D2_69.table_s2_char"
    cursor.execute(sql)
    sql = "DELETE FROM D2_69.table_s3_char"
    cursor.execute(sql)
    for i in range(len(id_s2)):
        sql_s2 = "INSERT INTO D2_69.table_s2_char VALUES(" + '"' + id_s2[i] + '","' + dru_s2[i] + '","' + ass_s2[i] + '","' + nec_s2[i] + '","' + sm_s2[i] + '")'
        cursor.execute(sql_s2)

    for i in range(len(id_s3)):
        sql_s3 = "INSERT INTO D2_69.table_s3_char VALUES(" + '"' + id_s3[i] + '","' + dru_s3[i] + '","' + ass_s3[i] + '","' + nec_s3[i] + '","' + sm_s3[i] + '")'
        cursor.execute(sql_s3)



    sensor_db.commit()

    #sql = "SELECT * from D2_69.table_s3"
    #cursor.execute(sql)
    #data_list = cursor.fetchall()

    #for data in data_list:
    #    print(data)


load_wb.close()
load_wb_s2.close()
load_wb_s3.close()
cursor.close()