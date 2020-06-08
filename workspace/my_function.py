import genetic_algorithm
import py_setting
import students_info
import random


#平均値
def average_deviation_value():
    sum_list_math = 0

    for i in range(len(students_info.list_students)): #生徒数だけ繰り返す
        sum_list_math += students_info.list_students[i]['deviation_value']

    ave_list = sum_list_math / py_setting.students

    return ave_list


#クラスをランダムで二つ決定
def random_classes():
    class_1 = 0
    class_2 = 0

    while class_1 == class_2:
        class_1 = random.randint(0, py_setting.classes - 1)
        class_2 = random.randint(0, py_setting.classes - 1)

    return class_1, class_2

#性別チェック
def gender_check(student_gender):
    if student_gender == 0:
        return '女子'
    elif student_gender == 1:
        return '男子'
    else:
        return 'ERROR'

#現在の最高個体を表示
def view_class():
    for i in range(py_setting.classes):
        class_number = i + 1
        print('-' + str(class_number) + '組-')

        count = 0
        men_count = 0
        wemen_count = 0

        for j in range(len(py_setting.best_individuals[i])):
            count += py_setting.best_individuals[i][j]['deviation_value']
            
            if j != len(py_setting.best_individuals[i]) - 1:
                if py_setting.best_individuals[i][j]['gender'] == 0:
                    wemen_count += 1
                elif py_setting.best_individuals[i][j]['gender'] == 1:
                    men_count += 1
                else:
                    print('ERROR')
                
                print('学籍番号：' + str(py_setting.best_individuals[i][j]['students_number']), end=' ')
                print('性別：' + gender_check(py_setting.best_individuals[i][j]['gender']), end=' ')
                print('国語：' + str(py_setting.best_individuals[i][j]['japanese']), end=' ')
                print('社会：' + str(py_setting.best_individuals[i][j]['society']), end=' ')
                print('数学：' + str(py_setting.best_individuals[i][j]['mathematics']), end=' ')
                print('理科：' + str(py_setting.best_individuals[i][j]['science']), end=' ')
                print('英語：' + str(py_setting.best_individuals[i][j]['english']), end=' ')
                print('偏差値：' + str(py_setting.best_individuals[i][j]['deviation_value']))

            else:
                if py_setting.best_individuals[i][j]['gender'] == 0:
                    wemen_count += 1
                elif py_setting.best_individuals[i][j]['gender'] == 1:
                    men_count += 1
                else:
                    print('ERROR')

                print('学籍番号：' + str(py_setting.best_individuals[i][j]['students_number']), end=' ')
                print('性別：' + gender_check(py_setting.best_individuals[i][j]['gender']), end=' ')
                print('国語：' + str(py_setting.best_individuals[i][j]['japanese']), end=' ')
                print('社会：' + str(py_setting.best_individuals[i][j]['society']), end=' ')
                print('数学：' + str(py_setting.best_individuals[i][j]['mathematics']), end=' ')
                print('理科：' + str(py_setting.best_individuals[i][j]['science']), end=' ')
                print('英語：' + str(py_setting.best_individuals[i][j]['english']), end=' ')
                print('偏差値：' + str(py_setting.best_individuals[i][j]['deviation_value']), end='      ')
                print('【人数】' + str(len(py_setting.best_individuals[i])) + '人(男子：' + str(men_count) + ', 女子：' + str(wemen_count) + ') ', end='')
                print('【偏差値の平均】', count/len(py_setting.best_individuals[i]))
        print('')