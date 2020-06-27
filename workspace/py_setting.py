import students_info
import numpy

#クラス数
classes = 6
#クラス数のリストを作成
list_classes = []
for _ in range(classes):
    list_classes.append([])

#目的関数が最低値の時のリスト
best_individuals = []

#目的関数の値
best_score = 10 ** 7 #0に近づくほど良い値



count_womens = 0
count_mens = 0
#性別チェッカー
def gender_check(check):
    global count_womens, count_mens

    if check == 0:
        count_womens += 1
    else:
        count_mens += 1

#「ピアノ&リーダー」カウンター
def piano_and_leader_counter():
    piano_and_leader_count = 0
    for i in students_info.list_students:
        if i['piano'] == 1 and i['leader'] == 1:
            piano_and_leader_count += 1
    return piano_and_leader_count

#リーダーの各クラスにおける最小値,最大値
piano_and_leader_min = None
piano_and_leader_max = None

if piano_and_leader_counter() % classes == 0:
    piano_and_leader_min = piano_and_leader_counter() / classes
    piano_and_leader_max = piano_and_leader_counter() / classes
else:
    piano_and_leader_min = int(piano_and_leader_counter() / classes)
    piano_and_leader_max = int(piano_and_leader_counter() / classes) + 1

#ピアノカウンター
def piano_counter():
    piano_count = 0
    for i in students_info.list_students:
        if i['piano'] == 1:
            piano_count += 1
    return piano_count

#ピアノの各クラスにおける最小値,最大値
piano_min = None
piano_max = None

if piano_counter() % classes == 0:
    piano_min = piano_counter() / classes
    piano_max = piano_counter() / classes
else:
    piano_min = int(piano_counter() / classes)
    piano_max = int(piano_counter() / classes) + 1

#リーダーカウンター
def leader_counter():
    leader_count = 0
    for i in students_info.list_students:
        if i['leader'] == 1:
            leader_count += 1
    return leader_count

#リーダーの各クラスにおける最小値,最大値
leader_min = None
leader_max = None

if leader_counter() % classes == 0:
    leader_min = leader_counter() / classes
    leader_max = leader_counter() / classes
else:
    leader_min = int(leader_counter() / classes)
    leader_max = int(leader_counter() / classes) + 1

#各教科の合計
japanese_scores = []
society_scores = []
mathematics_scores = []
science_scores = []
english_scores = []

for i in range(len(students_info.list_students)):
    gender_check(students_info.list_students[i]['gender']) #男女数のカウント

    japanese_scores.append(students_info.list_students[i]['japanese'])
    society_scores.append(students_info.list_students[i]['society'])
    mathematics_scores.append(students_info.list_students[i]['mathematics'])
    science_scores.append(students_info.list_students[i]['science'])
    english_scores.append(students_info.list_students[i]['english'])

np_japanese_scores = numpy.array(japanese_scores)
np_society_scores = numpy.array(society_scores)
np_mathematics_scores = numpy.array(mathematics_scores)
np_science_scores = numpy.array(science_scores)
np_english_scores = numpy.array(english_scores)

#各教科の平均
mean_japanese = numpy.mean(np_japanese_scores)
mean_society = numpy.mean(np_society_scores)
mean_mathematics = numpy.mean(np_mathematics_scores)
mean_science = numpy.mean(np_science_scores)
mean_english = numpy.mean(np_english_scores)

#各教科の標準偏差
std_japanese = numpy.std(np_japanese_scores)
std_society = numpy.std(np_society_scores)
std_mathematics = numpy.std(np_mathematics_scores)
std_science = numpy.std(np_science_scores)
std_english = numpy.std(np_english_scores)

#各教科の偏差値と全教科の平均偏差値
for i in range(len(students_info.list_students)):
    deviation_japanese = (students_info.list_students[i]['japanese'] - mean_japanese) / std_japanese
    deviation_society = (students_info.list_students[i]['society'] - mean_society) / std_society
    deviation_mathematics = (students_info.list_students[i]['mathematics'] - mean_mathematics) / std_mathematics
    deviation_science = (students_info.list_students[i]['science'] - mean_science) / std_science
    deviation_english = (students_info.list_students[i]['english'] - mean_english) / std_english
    deviation_value_japanese = 50 + deviation_japanese * 10
    deviation_value_society = 50 + deviation_society * 10
    deviation_value_mathematics = 50 + deviation_mathematics * 10
    deviation_value_science = 50 + deviation_science * 10
    deviation_value_english = 50 + deviation_english * 10

    deviation_value_average = (deviation_value_japanese + deviation_value_society + deviation_value_mathematics + deviation_value_science + deviation_value_english) / 5
    students_info.list_students[i]['deviation_value'] = deviation_value_average