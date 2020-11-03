import random, numpy

number_of_students = 246
list_students = []

#性別の設定
gender_list = [0, 1] #0:女子, 1:男子
gender_probability_list = [0.50, 0.50]

#ピアノの設定
piano_list = [0, 1] #0:できない, 1:できる
piano_probability_list = [0.95, 0.05]

#リーダーの設定
leader_list = [0, 1] #0:素質なし, 1:素質あり
leader_probability_list = [0.95, 0.05]

#体力テストの設定
physical_point_list = [8, 11, 21, 31, 41, 51, 61, 71]
physical_point_probability_list = [0.01, 0.04, 0.15, 0.20, 0.33, 0.20, 0.05, 0.02]

#文理タイプの設定
subjects_type_list = ['理系', '文系', '普通']
subjects_type_probability_list = [0.20, 0.40, 0.40]
#基礎点の設定
basic_point_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
basic_point_probability_list = [0.01, 0.02, 0.03, 0.05, 0.15, 0.30, 0.25, 0.10, 0.04, 0.03, 0.02]
#点数範囲(Min-基礎点/基礎点-Max)の設定
range_of_point_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
range_of_point_probability_list = [0.05, 0.30, 0.35, 0.10, 0.05, 0.05, 0.04, 0.03, 0.02, 0.01]

for i in range(number_of_students):
    student_ability = {'students_number': 0, 'gender': 0, 'japanese': 0,'society': 0,'mathematics': 0, 'science': 0,'english': 0, 'deviation_value': None, 'physical_point': 0, 'piano': 0, 'leader': 0}

    #生徒番号の付与
    student_ability['students_number'] = i + 1

    #性別の付与
    student_ability['gender'] = numpy.random.choice(a=gender_list, p=gender_probability_list)

    #ピアノの付与
    student_ability['piano'] = numpy.random.choice(a=piano_list, p=piano_probability_list)

    #リーダーの付与
    student_ability['leader'] = numpy.random.choice(a=leader_list, p=leader_probability_list)

    #体力テストの付与
    physical_axis_value = numpy.random.choice(a=physical_point_list, p=physical_point_probability_list)
    if physical_axis_value == 8:
        student_ability['physical_point'] = random.randint(8, 10)
    else:
        student_ability['physical_point'] = random.randint(physical_axis_value, physical_axis_value+9)

    #文理タイプの付与
    subjects_type = numpy.random.choice(a=subjects_type_list, p=subjects_type_probability_list)
    #基礎点の付与
    basic_point = numpy.random.choice(a=basic_point_list, p=basic_point_probability_list)
    #点数範囲の付与
    range_of_point = numpy.random.choice(a=range_of_point_list, p=range_of_point_probability_list)

    

    #各教科(国社数理英)の点数付与
    if subjects_type == '理系':
        student_ability['japanese'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point)
        student_ability['society'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point)
        student_ability['mathematics'] = random.randint(basic_point, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
        student_ability['science'] = random.randint(basic_point, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
        student_ability['english'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
    elif subjects_type == '文系':
        student_ability['japanese'] = random.randint(basic_point, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
        student_ability['society'] = random.randint(basic_point, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
        student_ability['mathematics'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point)
        student_ability['science'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point)
        student_ability['english'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
    elif subjects_type == '普通':
        student_ability['japanese'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
        student_ability['society'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
        student_ability['mathematics'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
        student_ability['science'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
        student_ability['english'] = random.randint(basic_point-range_of_point if basic_point-range_of_point > 0 else 0, basic_point+range_of_point if basic_point+range_of_point < 100 else 100)
    else:
        print('Error')

    list_students.append(student_ability)
    print(student_ability)

def check_element():
    men_count = 0
    women_count = 0
    piano_count = 0
    leader_count = 0
    piano_and_leader_count = 0

    for i in list_students:
        if i['gender'] == 1:
            men_count += 1
        elif i['gender'] == 0:
            women_count += 1
        else:
            print('ERROR')
        
        if i['piano'] == 1:
            piano_count += 1

        if i['leader'] == 1:
            leader_count += 1
        
        if i['piano'] == 1 and i['leader'] == 1:
            piano_and_leader_count += 1


    print('**********************')

    print('生徒数　：' + str(len(list_students)) + '人')
    print('男子数　：' + str(men_count) + '人, ' + '女子数：' + str(women_count) + '人')
    print('ピアノ　：' + str(piano_count) + '人')
    print('リーダー：' + str(leader_count) + '人')
    print('ピアノ＆リーダー：' + str(piano_and_leader_count) + '人')

    print('**********************')

check_element()