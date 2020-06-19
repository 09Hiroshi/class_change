import genetic_algorithm, my_function, py_setting, students_info
import time

def GA():
    startTime = time.time() #処理前の時刻

    genetic_algorithm.generate()
    genetic_algorithm.evaluation(physical_weight=0.2)

    print('')
    print('第1世代')
    my_function.view_class()

    print('【目的関数】' + str(py_setting.best_score))
    print('-------------------------------------------------------------------------\n')
    
    for i in range(2, 1001):
        genetic_algorithm.crossover()
        genetic_algorithm.evaluation(physical_weight=0.2)

        generation = i
        print('第' + str(generation) + '世代')
        my_function.view_class()

        print('【目的関数】' + str(py_setting.best_score))
        print('-------------------------------------------------------------------------\n')

        if genetic_algorithm.escape_loop(50):
            break

    endTime = time.time() #処理後の時刻
    elapsed_time = endTime - startTime

    print('【最終世代】' + '第' + str(generation) + '世代')
    print('【最終目的関数値】' + str(py_setting.best_score))
    print('【経過時間】' + str(elapsed_time) + '(s)')

if __name__ == '__main__':
    GA()