import py_setting
import students_info
import random
from copy import deepcopy
import my_function

#性別カウンター
def gender_counter(list_studens):
    count_mens = 0
    count_womens = 0
    
    for i in range(len(list_studens)):
        if list_studens[i]['gender'] == 1:
            count_mens += 1
        elif list_studens[i]['gender'] == 0:
            count_womens += 1
        else:
            print('ERROR')

    return count_mens, count_womens

#男女数を均等に各クラスへ振り分ける
#for文を後で別の関数にまとめる
def put_students():
    count_mens, count_womens = gender_counter(students_info.list_students)

    #各クラスの男子数
    mensOneSet = int(count_mens / py_setting.classes)
    #残りの男子
    remaining_mens = count_mens - (mensOneSet * py_setting.classes)

    #生徒のリストから男子だけを抽出
    count_students = 0
    #(int(男子数/クラス数)+1)人のクラスに男子を代入
    for i in range(remaining_mens):
        for _ in range(mensOneSet+1):
            if students_info.list_students[count_students]['gender'] == 1:
                py_setting.list_classes[i].append(students_info.list_students[count_students])
                count_students += 1
            else:
                while True :
                    count_students += 1
                    if students_info.list_students[count_students]['gender'] == 1:
                        py_setting.list_classes[i].append(students_info.list_students[count_students])
                        count_students += 1
                        break
    
    #(int(男子数/クラス数))人のクラスに男子を代入
    for i in range(remaining_mens, py_setting.classes):
        for _ in range(mensOneSet):
            if students_info.list_students[count_students]['gender'] == 1:
                py_setting.list_classes[i].append(students_info.list_students[count_students])
                count_students += 1
            else:
                while True :
                    count_students += 1
                    if students_info.list_students[count_students]['gender'] == 1:
                        py_setting.list_classes[i].append(students_info.list_students[count_students])
                        count_students += 1
                        break

    #各クラスの女子数
    womensOneSet = int(count_womens / py_setting.classes)
    #残りの女子
    remaining_womens = count_womens - (womensOneSet * py_setting.classes)

    #生徒のリストから女子だけを抽出
    count_students = 0
    #(int(女子数/クラス数)+1)人のクラスに女子を代入
    for i in range(remaining_womens):
        for _ in range(womensOneSet+1):
            if students_info.list_students[count_students]['gender'] == 0:
                py_setting.list_classes[i].append(students_info.list_students[count_students])
                count_students += 1
            else:
                while True :
                    count_students += 1
                    if students_info.list_students[count_students]['gender'] == 0:
                        py_setting.list_classes[i].append(students_info.list_students[count_students])
                        count_students += 1
                        break

    #(int(女子数/クラス数))人のクラスに女子を代入
    for i in range(remaining_womens, py_setting.classes):
        for _ in range(womensOneSet):
            if students_info.list_students[count_students]['gender'] == 0:
                py_setting.list_classes[i].append(students_info.list_students[count_students])
                count_students += 1
            else:
                while True :
                    count_students += 1
                    if students_info.list_students[count_students]['gender'] == 0:
                        py_setting.list_classes[i].append(students_info.list_students[count_students])
                        count_students += 1
                        break

#ピアノが多いクラスと少ないクラスの生徒を交換
def exchange_piano(piano_under_list, piano_over_list):
    gender_of_over = None

    for i in range(len(piano_over_list)):
        if piano_over_list[i]['piano'] == 1:
            gender_of_over = piano_over_list[i]['gender']
            tmp = piano_over_list.pop(i)
            piano_under_list.append(tmp)
            break

    for i in range(len(piano_under_list)):
        if piano_under_list[i]['piano'] == 0 and piano_under_list[i]['gender'] == gender_of_over:
            tmp = piano_under_list.pop(i)
            piano_over_list.append(tmp)
            break

#ピアノをフラットに
def flatten_piano():
    while True:
        piano_under_list = []
        piano_over_list = []

        for i in py_setting.list_classes:
            piano_count = 0
            for j in i:
                if j['piano'] == 1:
                    piano_count += 1
            if piano_count < py_setting.piano_min:
                piano_under_list = i
                break

        for i in py_setting.list_classes:
            piano_count = 0
            for j in i:
                if j['piano'] == 1:
                    piano_count += 1
            if piano_count > py_setting.piano_max:
                piano_over_list = i
                break

        if piano_under_list == [] and piano_over_list == []:
            break

        elif piano_under_list != [] and piano_over_list != []:

            exchange_piano(piano_under_list, piano_over_list)

        elif piano_under_list == [] and piano_over_list != []:
            for i in py_setting.list_classes:
                piano_count = 0
                for j in i:
                    if j['piano'] == 1:
                        piano_count += 1
                if piano_count == py_setting.piano_min:
                    piano_under_list = i
                    break

            exchange_piano(piano_under_list, piano_over_list)
        
        elif piano_under_list != [] and piano_over_list == []:
            for i in py_setting.list_classes:
                piano_count = 0
                for j in i:
                    if j['piano'] == 1:
                        piano_count += 1
                if piano_count == py_setting.piano_max:
                    piano_over_list = i
                    break

            exchange_piano(piano_under_list, piano_over_list)

#リーダーが多いクラスと少ないクラスの生徒を交換
def exchange_leader(leader_under_list, leader_over_list):
    gender_of_over = None

    for i in range(len(leader_over_list)):
        if leader_over_list[i]['leader'] == 1 and leader_over_list[i]['piano'] == 0:
            gender_of_over = leader_over_list[i]['gender']
            tmp = leader_over_list.pop(i)
            leader_under_list.append(tmp)
            break

    for i in range(len(leader_under_list)):
        if leader_under_list[i]['piano'] == 0 and leader_under_list[i]['gender'] == gender_of_over and leader_under_list[i]['piano'] == 0:
            tmp = leader_under_list.pop(i)
            leader_over_list.append(tmp)
            break

#リーダーをフラットに
def flatten_leader():
    while True:
        leader_under_list = []
        leader_over_list = []

        for i in py_setting.list_classes:
            leader_count = 0
            for j in i:
                if j['leader'] == 1:
                    leader_count += 1
            if leader_count < py_setting.leader_min:
                leader_under_list = i
                break

        for i in py_setting.list_classes:
            leader_count = 0
            for j in i:
                if j['leader'] == 1:
                    leader_count += 1
            if leader_count > py_setting.leader_max:
                leader_over_list = i
                break

        if leader_under_list == [] and leader_over_list == []:
            break

        elif leader_under_list != [] and leader_over_list != []:

            exchange_leader(leader_under_list, leader_over_list)

        elif leader_under_list == [] and leader_over_list != []:
            for i in py_setting.list_classes:
                leader_count = 0
                for j in i:
                    if j['leader'] == 1:
                        leader_count += 1
                if leader_count == py_setting.leader_min:
                    leader_under_list = i
                    break

            exchange_leader(leader_under_list, leader_over_list)
        
        elif leader_under_list != [] and leader_over_list == []:
            for i in py_setting.list_classes:
                leader_count = 0
                for j in i:
                    if j['leader'] == 1:
                        leader_count += 1
                if leader_count == py_setting.leader_max:
                    leader_over_list = i
                    break

            exchange_leader(leader_under_list, leader_over_list)

#初期世代の生成
def generate():
    put_students()
    flatten_piano()
    flatten_leader()


#目的関数値が何世代変化していないか
unchanging_count = 0
#個体の評価
def evaluation():
    global unchanging_count
    
    evaluation_value = 0 #目的関数の値

    #クラス数だけ繰り返す
    for i in range(py_setting.classes): 
        #各クラスの偏差値の合計
        deviation_value_per_class = 0

        #各クラスの生徒数だけ繰り返す
        for j in range(len(py_setting.list_classes[i])):
            deviation_value_per_class += py_setting.list_classes[i][j]['deviation_value']

        evaluation_value += abs(deviation_value_per_class / len(py_setting.list_classes[i]) - my_function.average_deviation_value())

    if evaluation_value < py_setting.best_score:
        py_setting.best_score = evaluation_value
        py_setting.best_individuals = py_setting.list_classes 

        unchanging_count = 0

    else:
         unchanging_count += 1

    return py_setting.best_score

#目的関数値がN世代変化していなかった場合に処理終了
def escape_loop(n):
    global unchanging_count
    if unchanging_count == n:
        return True


#自然淘汰


def constraint_gender(compare_student_1, compare_student_2):
    return compare_student_1['gender'] == compare_student_2['gender']

def constraint_piano(compare_student_1, compare_student_2):
    return compare_student_1['piano'] == compare_student_2['piano']

def constraint_leader(compare_student_1, compare_student_2):
    return compare_student_1['leader'] == compare_student_2['leader']

#交叉
def crossover():
    random_class = my_function.random_classes() #0~(クラス数-1) 0~5

    py_setting.list_classes = deepcopy(py_setting.best_individuals)

    subscript_1 = len(py_setting.list_classes[random_class[0]])
    subscript_2 = len(py_setting.list_classes[random_class[1]])

    #whileの中身を後でリファクタ
    while True:
        random_student_1 = random.randint(0, subscript_1 - 1)
        random_student_2 = random.randint(0, subscript_2 - 1)

        bool_gender = constraint_gender(py_setting.list_classes[random_class[0]][random_student_1], py_setting.list_classes[random_class[1]][random_student_2])
        bool_piano = constraint_piano(py_setting.list_classes[random_class[0]][random_student_1], py_setting.list_classes[random_class[1]][random_student_2])
        bool_leader = constraint_leader(py_setting.list_classes[random_class[0]][random_student_1], py_setting.list_classes[random_class[1]][random_student_2])

        if bool_gender and bool_piano and bool_leader:
            py_setting.list_classes[random_class[0]][random_student_1], py_setting.list_classes[random_class[1]][random_student_2] = py_setting.list_classes[random_class[1]][random_student_2], py_setting.list_classes[random_class[0]][random_student_1]
            break
        else:
            pass


#突然変異
