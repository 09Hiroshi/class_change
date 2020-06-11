import py_setting
import students_info
import random
from copy import deepcopy
import my_function

#目的関数値が何世代変化していないか
unchanging_count = 0

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

#初期世代の生成
def generate():
    put_students()


#個体の評価
def evaluation():
    global unchanging_count
    
    evaluation_value = 0 #目的関数の値

    for i in range(py_setting.classes): #クラス数だけ繰り返す
        total_per_class = 0 #クラスごとの合計点

        for j in range(len(py_setting.list_classes[i])): #各クラスの生徒数だけ繰り返す
            total_per_class += py_setting.list_classes[i][j]['deviation_value']

        evaluation_value += abs(total_per_class / len(py_setting.list_classes[i]) - my_function.average_deviation_value())

    if py_setting.best_score > evaluation_value:
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

        if constraint_gender(py_setting.list_classes[random_class[0]][random_student_1], py_setting.list_classes[random_class[1]][random_student_2]):

            py_setting.list_classes[random_class[0]][random_student_1], py_setting.list_classes[random_class[1]][random_student_2] = py_setting.list_classes[random_class[1]][random_student_2], py_setting.list_classes[random_class[0]][random_student_1]
            break
        else:
            pass


#突然変異