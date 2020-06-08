import py_setting
import students_info
import random
from copy import deepcopy
import my_function

#目的関数値が何世代変化していないか
unchanging_count = 0


#初期世代の生成
def generate():
    count_students = 0
    studentsOneSet = int(py_setting.students / py_setting.classes) #各クラスの生徒数
    remaining_students = py_setting.students - (studentsOneSet * py_setting.classes) #残りの生徒

    for i in range(py_setting.classes): #クラス数だけ繰り返す
        for _ in range(studentsOneSet): #各クラスの生徒数だけ繰り返す
            py_setting.list_classes[i].append(students_info.list_students[count_students])
            count_students += 1

    for i in range(remaining_students): #残りの生徒数だけ繰り返す
            py_setting.list_classes[i].append(students_info.list_students[count_students])
            count_students += 1


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


#交叉
def crossover():
    random_class = my_function.random_classes() #0~(クラス数-1) 0~5

    py_setting.list_classes = deepcopy(py_setting.best_individuals)

    subscript_1 = len(py_setting.list_classes[random_class[0]])
    subscript_2 = len(py_setting.list_classes[random_class[1]])

    random_student_1 = random.randint(0, subscript_1 - 1)
    random_student_2 = random.randint(0, subscript_2 - 1)

    py_setting.list_classes[random_class[0]][random_student_1], py_setting.list_classes[random_class[1]][random_student_2] = py_setting.list_classes[random_class[1]][random_student_2], py_setting.list_classes[random_class[0]][random_student_1] # ランダムで生徒を変更(a,b=b,a)


#突然変異