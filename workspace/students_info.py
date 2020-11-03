#ユーザに入力させるデータ
#仮データ
list_students = [
    {'students_number':  1, 'gender': 0, 'japanese': 84,'society': 78,'mathematics': 68, 'science': 95,'english': 86, 'deviation_value': None, 'physical_point': 75, 'piano': 1, 'leader': 0},
    {'students_number':  2, 'gender': 0, 'japanese': 50,'society': 55,'mathematics': 43, 'science': 32,'english': 36, 'deviation_value': None, 'physical_point': 56, 'piano': 0, 'leader': 0},
    {'students_number':  3, 'gender': 1, 'japanese': 72,'society': 46,'mathematics': 89, 'science': 86,'english': 56, 'deviation_value': None, 'physical_point': 37, 'piano': 0, 'leader': 1},
    {'students_number':  4, 'gender': 0, 'japanese': 60,'society': 90,'mathematics':100, 'science': 88,'english': 80, 'deviation_value': None, 'physical_point': 64, 'piano': 0, 'leader': 0},
    {'students_number':  5, 'gender': 1, 'japanese': 36,'society': 38,'mathematics': 20, 'science': 39,'english': 15, 'deviation_value': None, 'physical_point': 59, 'piano': 0, 'leader': 0},
    {'students_number':  6, 'gender': 1, 'japanese': 76,'society': 85,'mathematics': 82, 'science': 89,'english': 75, 'deviation_value': None, 'physical_point': 48, 'piano': 0, 'leader': 0},
    {'students_number':  7, 'gender': 0, 'japanese': 92,'society': 70,'mathematics': 86, 'science': 62,'english': 99, 'deviation_value': None, 'physical_point': 45, 'piano': 0, 'leader': 0},
    {'students_number':  8, 'gender': 1, 'japanese': 39,'society': 77,'mathematics': 81, 'science': 82,'english': 67, 'deviation_value': None, 'physical_point': 60, 'piano': 0, 'leader': 0},
    {'students_number':  9, 'gender': 0, 'japanese': 57,'society': 23,'mathematics': 67, 'science': 82,'english': 10, 'deviation_value': None, 'physical_point': 64, 'piano': 0, 'leader': 1},
    {'students_number': 10, 'gender': 0, 'japanese': 57,'society': 50,'mathematics': 69, 'science': 45,'english': 76, 'deviation_value': None, 'physical_point': 51, 'piano': 0, 'leader': 0},
    {'students_number': 11, 'gender': 1, 'japanese': 63,'society': 31,'mathematics': 92, 'science': 67,'english': 59, 'deviation_value': None, 'physical_point': 40, 'piano': 0, 'leader': 0},
    {'students_number': 12, 'gender': 1, 'japanese': 35,'society': 26,'mathematics': 12, 'science':  8,'english': 23, 'deviation_value': None, 'physical_point': 34, 'piano': 1, 'leader': 0},
    {'students_number': 13, 'gender': 1, 'japanese': 49,'society': 49,'mathematics': 96, 'science': 73,'english': 24, 'deviation_value': None, 'physical_point': 22, 'piano': 0, 'leader': 0},
    {'students_number': 14, 'gender': 0, 'japanese': 22,'society': 52,'mathematics': 73, 'science': 40,'english': 53, 'deviation_value': None, 'physical_point': 28, 'piano': 0, 'leader': 0},
    {'students_number': 15, 'gender': 0, 'japanese': 82,'society':100,'mathematics': 72, 'science': 86,'english': 80, 'deviation_value': None, 'physical_point': 30, 'piano': 0, 'leader': 0},
    {'students_number': 16, 'gender': 0, 'japanese': 28,'society': 22,'mathematics':  8, 'science': 36,'english': 21, 'deviation_value': None, 'physical_point': 53, 'piano': 0, 'leader': 0},
    {'students_number': 17, 'gender': 1, 'japanese': 82,'society': 76,'mathematics': 53, 'science': 60,'english': 55, 'deviation_value': None, 'physical_point': 59, 'piano': 0, 'leader': 0},
    {'students_number': 18, 'gender': 0, 'japanese': 91,'society': 58,'mathematics': 64, 'science': 82,'english': 71, 'deviation_value': None, 'physical_point': 58, 'piano': 0, 'leader': 0},
    {'students_number': 19, 'gender': 0, 'japanese': 15,'society': 20,'mathematics':  0, 'science': 15,'english': 18, 'deviation_value': None, 'physical_point': 58, 'piano': 0, 'leader': 0},
    {'students_number': 20, 'gender': 0, 'japanese': 73,'society': 45,'mathematics': 98, 'science': 84,'english': 79, 'deviation_value': None, 'physical_point': 52, 'piano': 0, 'leader': 0},
    {'students_number': 21, 'gender': 0, 'japanese': 37,'society': 59,'mathematics': 52, 'science': 34,'english': 62, 'deviation_value': None, 'physical_point': 63, 'piano': 0, 'leader': 0},
    {'students_number': 22, 'gender': 1, 'japanese': 93,'society': 80,'mathematics': 95, 'science': 97,'english': 95, 'deviation_value': None, 'physical_point': 42, 'piano': 0, 'leader': 0},
    {'students_number': 23, 'gender': 1, 'japanese': 10,'society':  4,'mathematics': 11, 'science': 25,'english':  8, 'deviation_value': None, 'physical_point': 49, 'piano': 0, 'leader': 0},
    {'students_number': 24, 'gender': 0, 'japanese': 59,'society': 56,'mathematics': 70, 'science': 80,'english': 21, 'deviation_value': None, 'physical_point': 46, 'piano': 0, 'leader': 0},
    {'students_number': 25, 'gender': 1, 'japanese': 82,'society': 76,'mathematics': 82, 'science': 63,'english': 90, 'deviation_value': None, 'physical_point': 57, 'piano': 1, 'leader': 0},
    {'students_number': 26, 'gender': 0, 'japanese': 16,'society': 24,'mathematics': 11, 'science': 34,'english': 35, 'deviation_value': None, 'physical_point': 55, 'piano': 0, 'leader': 0},
    {'students_number': 27, 'gender': 1, 'japanese': 34,'society': 27,'mathematics': 25, 'science': 35,'english': 11, 'deviation_value': None, 'physical_point': 47, 'piano': 0, 'leader': 0},
    {'students_number': 28, 'gender': 0, 'japanese': 20,'society': 58,'mathematics': 64, 'science': 85,'english': 15, 'deviation_value': None, 'physical_point': 68, 'piano': 0, 'leader': 0},
    {'students_number': 29, 'gender': 0, 'japanese': 65,'society': 65,'mathematics': 63, 'science': 88,'english': 73, 'deviation_value': None, 'physical_point': 66, 'piano': 0, 'leader': 1},
    {'students_number': 30, 'gender': 0, 'japanese': 74,'society': 84,'mathematics': 52, 'science': 11,'english': 53, 'deviation_value': None, 'physical_point': 37, 'piano': 0, 'leader': 0},
    {'students_number': 31, 'gender': 0, 'japanese': 33,'society': 83,'mathematics': 77, 'science': 37,'english': 57, 'deviation_value': None, 'physical_point': 57, 'piano': 1, 'leader': 0},
    {'students_number': 32, 'gender': 0, 'japanese': 79,'society': 34,'mathematics': 37, 'science': 83,'english': 94, 'deviation_value': None, 'physical_point': 75, 'piano': 0, 'leader': 0},
    {'students_number': 33, 'gender': 0, 'japanese': 18,'society': 53,'mathematics': 47, 'science': 34,'english': 22, 'deviation_value': None, 'physical_point': 54, 'piano': 0, 'leader': 1},
    {'students_number': 34, 'gender': 1, 'japanese': 47,'society': 77,'mathematics': 88, 'science': 63,'english': 84, 'deviation_value': None, 'physical_point': 46, 'piano': 0, 'leader': 0},
    {'students_number': 35, 'gender': 0, 'japanese': 52,'society': 65,'mathematics': 99, 'science': 66,'english': 84, 'deviation_value': None, 'physical_point': 66, 'piano': 0, 'leader': 0},
    {'students_number': 36, 'gender': 0, 'japanese': 93,'society': 78,'mathematics': 95, 'science': 73,'english': 96, 'deviation_value': None, 'physical_point': 57, 'piano': 0, 'leader': 0},
    {'students_number': 37, 'gender': 0, 'japanese': 50,'society': 77,'mathematics': 74, 'science': 74,'english': 64, 'deviation_value': None, 'physical_point': 48, 'piano': 0, 'leader': 1},
    {'students_number': 38, 'gender': 1, 'japanese':  5,'society':  4,'mathematics':  8, 'science': 11,'english': 25, 'deviation_value': None, 'physical_point': 58, 'piano': 0, 'leader': 0},
    {'students_number': 39, 'gender': 1, 'japanese': 63,'society': 54,'mathematics': 57, 'science': 47,'english': 65, 'deviation_value': None, 'physical_point': 52, 'piano': 0, 'leader': 0},
    {'students_number': 40, 'gender': 1, 'japanese': 52,'society': 52,'mathematics': 37, 'science': 47,'english': 45, 'deviation_value': None, 'physical_point': 70, 'piano': 0, 'leader': 0},
    {'students_number': 41, 'gender': 0, 'japanese': 74,'society': 66,'mathematics': 73, 'science': 77,'english': 67, 'deviation_value': None, 'physical_point': 35, 'piano': 1, 'leader': 0},
    {'students_number': 42, 'gender': 1, 'japanese': 63,'society': 85,'mathematics': 84, 'science': 73,'english': 78, 'deviation_value': None, 'physical_point': 48, 'piano': 0, 'leader': 0},
    {'students_number': 43, 'gender': 1, 'japanese': 24,'society': 27,'mathematics': 84, 'science': 74,'english': 27, 'deviation_value': None, 'physical_point': 34, 'piano': 0, 'leader': 0},
    {'students_number': 44, 'gender': 0, 'japanese': 21,'society': 36,'mathematics': 32, 'science': 13,'english': 47, 'deviation_value': None, 'physical_point': 57, 'piano': 0, 'leader': 1},
    {'students_number': 45, 'gender': 1, 'japanese': 47,'society': 24,'mathematics': 58, 'science': 50,'english': 44, 'deviation_value': None, 'physical_point': 56, 'piano': 0, 'leader': 0},
    {'students_number': 46, 'gender': 0, 'japanese': 77,'society': 26,'mathematics': 88, 'science': 26,'english': 48, 'deviation_value': None, 'physical_point': 62, 'piano': 0, 'leader': 0},
    {'students_number': 47, 'gender': 0, 'japanese': 39,'society': 78,'mathematics': 44, 'science': 22,'english': 28, 'deviation_value': None, 'physical_point': 65, 'piano': 0, 'leader': 0},
    {'students_number': 48, 'gender': 0, 'japanese': 36,'society': 83,'mathematics': 57, 'science': 58,'english': 18, 'deviation_value': None, 'physical_point': 53, 'piano': 0, 'leader': 0},
    {'students_number': 49, 'gender': 1, 'japanese': 88,'society': 37,'mathematics': 83, 'science': 27,'english': 10, 'deviation_value': None, 'physical_point': 48, 'piano': 0, 'leader': 0},
    {'students_number': 50, 'gender': 0, 'japanese': 55,'society': 73,'mathematics': 18, 'science': 27,'english':  4, 'deviation_value': None, 'physical_point': 47, 'piano': 0, 'leader': 0},
    {'students_number': 51, 'gender': 0, 'japanese': 63,'society': 73,'mathematics': 81, 'science': 84,'english': 63, 'deviation_value': None, 'physical_point': 44, 'piano': 0, 'leader': 0},
    {'students_number': 52, 'gender': 1, 'japanese': 14,'society': 22,'mathematics':  0, 'science': 12,'english':  3, 'deviation_value': None, 'physical_point': 58, 'piano': 1, 'leader': 1},
    {'students_number': 53, 'gender': 0, 'japanese': 83,'society': 41,'mathematics': 40, 'science': 10,'english': 58, 'deviation_value': None, 'physical_point': 30, 'piano': 0, 'leader': 0},
    {'students_number': 54, 'gender': 1, 'japanese': 73,'society': 63,'mathematics': 95, 'science': 74,'english': 10, 'deviation_value': None, 'physical_point': 59, 'piano': 0, 'leader': 0},
    {'students_number': 55, 'gender': 0, 'japanese': 13,'society': 67,'mathematics': 54, 'science': 52,'english': 82, 'deviation_value': None, 'physical_point': 73, 'piano': 0, 'leader': 0},
    {'students_number': 56, 'gender': 0, 'japanese': 73,'society': 83,'mathematics': 61, 'science': 76,'english': 78, 'deviation_value': None, 'physical_point': 51, 'piano': 0, 'leader': 0},
    {'students_number': 57, 'gender': 1, 'japanese': 74,'society': 74,'mathematics': 47, 'science': 78,'english': 74, 'deviation_value': None, 'physical_point': 78, 'piano': 0, 'leader': 0},
    {'students_number': 58, 'gender': 1, 'japanese': 48,'society': 12,'mathematics': 33, 'science': 39,'english': 38, 'deviation_value': None, 'physical_point': 49, 'piano': 0, 'leader': 1},
    {'students_number': 59, 'gender': 1, 'japanese': 13,'society': 72,'mathematics': 62, 'science': 51,'english':  1, 'deviation_value': None, 'physical_point': 58, 'piano': 0, 'leader': 1},
    {'students_number': 60, 'gender': 0, 'japanese': 57,'society': 38,'mathematics': 76, 'science': 44,'english':  3, 'deviation_value': None, 'physical_point': 58, 'piano': 0, 'leader': 0},
    {'students_number': 61, 'gender': 0, 'japanese': 27,'society': 59,'mathematics': 24, 'science': 76,'english': 76, 'deviation_value': None, 'physical_point': 46, 'piano': 0, 'leader': 0},
    {'students_number': 62, 'gender': 0, 'japanese': 32,'society': 20,'mathematics': 52, 'science': 15,'english': 26, 'deviation_value': None, 'physical_point': 41, 'piano': 0, 'leader': 1},
    {'students_number': 63, 'gender': 0, 'japanese':  7,'society': 63,'mathematics': 39, 'science': 67,'english': 47, 'deviation_value': None, 'physical_point': 67, 'piano': 0, 'leader': 0},
    {'students_number': 64, 'gender': 1, 'japanese': 14,'society': 11,'mathematics': 39, 'science': 20,'english': 33, 'deviation_value': None, 'physical_point': 62, 'piano': 0, 'leader': 0},
    {'students_number': 65, 'gender': 1, 'japanese': 21,'society': 70,'mathematics': 61, 'science': 38,'english': 72, 'deviation_value': None, 'physical_point': 45, 'piano': 0, 'leader': 0},
    {'students_number': 66, 'gender': 0, 'japanese': 65,'society': 56,'mathematics': 93, 'science': 45,'english': 59, 'deviation_value': None, 'physical_point': 50, 'piano': 0, 'leader': 1},
    {'students_number': 67, 'gender': 0, 'japanese': 51,'society': 20,'mathematics': 72, 'science': 83,'english': 95, 'deviation_value': None, 'physical_point': 54, 'piano': 0, 'leader': 0},
    {'students_number': 68, 'gender': 1, 'japanese': 65,'society': 83,'mathematics':  4, 'science': 29,'english': 20, 'deviation_value': None, 'physical_point': 65, 'piano': 0, 'leader': 1},
    {'students_number': 69, 'gender': 1, 'japanese': 10,'society': 65,'mathematics': 66, 'science': 82,'english': 39, 'deviation_value': None, 'physical_point': 46, 'piano': 0, 'leader': 0},
    {'students_number': 70, 'gender': 0, 'japanese': 65,'society': 78,'mathematics':  5, 'science': 67,'english': 75, 'deviation_value': None, 'physical_point': 53, 'piano': 0, 'leader': 0},
    {'students_number': 71, 'gender': 1, 'japanese': 14,'society': 63,'mathematics': 90, 'science': 51,'english': 87, 'deviation_value': None, 'physical_point': 47, 'piano': 1, 'leader': 1},
    {'students_number': 72, 'gender': 0, 'japanese': 60,'society': 12,'mathematics': 38, 'science':  8,'english': 51, 'deviation_value': None, 'physical_point': 71, 'piano': 0, 'leader': 0},
    {'students_number': 73, 'gender': 1, 'japanese': 85,'society': 99,'mathematics': 74, 'science': 85,'english': 74, 'deviation_value': None, 'physical_point': 52, 'piano': 0, 'leader': 0},
    {'students_number': 74, 'gender': 1, 'japanese': 52,'society': 40,'mathematics': 58, 'science': 43,'english': 99, 'deviation_value': None, 'physical_point': 66, 'piano': 0, 'leader': 0},
    {'students_number': 75, 'gender': 0, 'japanese': 61,'society': 62,'mathematics': 37, 'science':  9,'english': 51, 'deviation_value': None, 'physical_point': 25, 'piano': 0, 'leader': 1},
    {'students_number': 76, 'gender': 0, 'japanese': 62,'society': 54,'mathematics': 49, 'science': 59,'english': 62, 'deviation_value': None, 'physical_point': 30, 'piano': 0, 'leader': 0},
    {'students_number': 77, 'gender': 1, 'japanese': 45,'society': 51,'mathematics': 51, 'science': 60,'english': 65, 'deviation_value': None, 'physical_point': 37, 'piano': 0, 'leader': 1},
    {'students_number': 78, 'gender': 1, 'japanese': 10,'society': 29,'mathematics': 19, 'science': 17,'english': 29, 'deviation_value': None, 'physical_point': 64, 'piano': 0, 'leader': 0},
    {'students_number': 79, 'gender': 0, 'japanese': 44,'society': 58,'mathematics': 78, 'science': 93,'english': 53, 'deviation_value': None, 'physical_point': 53, 'piano': 0, 'leader': 1},
    {'students_number': 80, 'gender': 1, 'japanese': 55,'society': 93,'mathematics': 55, 'science': 95,'english': 40, 'deviation_value': None, 'physical_point': 59, 'piano': 1, 'leader': 0},
    {'students_number': 81, 'gender': 0, 'japanese': 25,'society': 44,'mathematics': 69, 'science': 48,'english': 28, 'deviation_value': None, 'physical_point': 67, 'piano': 0, 'leader': 0},
    {'students_number': 82, 'gender': 0, 'japanese': 74,'society': 89,'mathematics': 53, 'science': 66,'english': 56, 'deviation_value': None, 'physical_point': 62, 'piano': 0, 'leader': 0},
    {'students_number': 83, 'gender': 1, 'japanese':  4,'society': 23,'mathematics': 32, 'science': 21,'english': 37, 'deviation_value': None, 'physical_point': 49, 'piano': 0, 'leader': 0},
    {'students_number': 84, 'gender': 1, 'japanese': 89,'society': 61,'mathematics': 46, 'science': 59,'english': 52, 'deviation_value': None, 'physical_point': 61, 'piano': 0, 'leader': 0},
    {'students_number': 85, 'gender': 0, 'japanese': 93,'society': 96,'mathematics': 66, 'science': 66,'english': 28, 'deviation_value': None, 'physical_point': 35, 'piano': 0, 'leader': 0},
    {'students_number': 86, 'gender': 0, 'japanese': 52,'society': 27,'mathematics': 20, 'science': 60,'english': 84, 'deviation_value': None, 'physical_point': 46, 'piano': 0, 'leader': 0},
    {'students_number': 87, 'gender': 1, 'japanese': 31,'society': 44,'mathematics': 97, 'science': 55,'english': 41, 'deviation_value': None, 'physical_point': 49, 'piano': 0, 'leader': 0},
    {'students_number': 88, 'gender': 0, 'japanese': 97,'society': 47,'mathematics': 33, 'science': 67,'english': 37, 'deviation_value': None, 'physical_point': 63, 'piano': 0, 'leader': 0},
    {'students_number': 89, 'gender': 0, 'japanese': 10,'society': 39,'mathematics': 77, 'science': 83,'english': 86, 'deviation_value': None, 'physical_point': 50, 'piano': 0, 'leader': 0},
    {'students_number': 90, 'gender': 0, 'japanese': 68,'society': 62,'mathematics': 49, 'science': 42,'english': 85, 'deviation_value': None, 'physical_point': 58, 'piano': 0, 'leader': 0},
    {'students_number': 91, 'gender': 0, 'japanese': 22,'society': 20,'mathematics': 21, 'science': 64,'english': 50, 'deviation_value': None, 'physical_point': 59, 'piano': 0, 'leader': 0},
    {'students_number': 92, 'gender': 1, 'japanese': 57,'society': 69,'mathematics': 49, 'science': 16,'english': 46, 'deviation_value': None, 'physical_point': 53, 'piano': 0, 'leader': 0},
    {'students_number': 93, 'gender': 1, 'japanese': 92,'society': 58,'mathematics': 44, 'science': 72,'english': 59, 'deviation_value': None, 'physical_point': 34, 'piano': 0, 'leader': 0},
    {'students_number': 94, 'gender': 0, 'japanese': 33,'society': 80,'mathematics': 72, 'science': 66,'english': 73, 'deviation_value': None, 'physical_point': 74, 'piano': 0, 'leader': 0},
    {'students_number': 95, 'gender': 1, 'japanese': 23,'society': 34,'mathematics':  6, 'science': 31,'english': 18, 'deviation_value': None, 'physical_point': 61, 'piano': 0, 'leader': 0},
    {'students_number': 96, 'gender': 0, 'japanese': 10,'society': 72,'mathematics': 15, 'science': 56,'english': 73, 'deviation_value': None, 'physical_point': 49, 'piano': 0, 'leader': 0},
    {'students_number': 97, 'gender': 0, 'japanese': 74,'society': 49,'mathematics': 17, 'science': 48,'english': 68, 'deviation_value': None, 'physical_point': 55, 'piano': 0, 'leader': 0},
    {'students_number': 98, 'gender': 1, 'japanese': 66,'society': 28,'mathematics': 52, 'science': 26,'english': 44, 'deviation_value': None, 'physical_point': 52, 'piano': 0, 'leader': 0},
    {'students_number': 99, 'gender': 0, 'japanese': 47,'society': 84,'mathematics': 38, 'science': 42,'english': 97, 'deviation_value': None, 'physical_point': 58, 'piano': 0, 'leader': 0},
    {'students_number':100, 'gender': 1, 'japanese': 83,'society': 96,'mathematics': 60, 'science': 70,'english': 64, 'deviation_value': None, 'physical_point': 60, 'piano': 0, 'leader': 1}
]

list_students_tmp = [
    {'students_number':  1, 'gender': 0, 'japanese': 84,'society': 78,'mathematics': 68, 'science': 95,'english': 86, 'deviation_value': None, 'physical_point': 75, 'piano': 0, 'leader': 1},
    {'students_number':  2, 'gender': 0, 'japanese': 50,'society': 55,'mathematics': 43, 'science': 32,'english': 36, 'deviation_value': None, 'physical_point': 56, 'piano': 0, 'leader': 0},
    {'students_number':  3, 'gender': 1, 'japanese': 72,'society': 46,'mathematics': 89, 'science': 86,'english': 56, 'deviation_value': None, 'physical_point': 37, 'piano': 0, 'leader': 1},
    {'students_number':  4, 'gender': 0, 'japanese': 60,'society': 90,'mathematics':100, 'science': 88,'english': 80, 'deviation_value': None, 'physical_point': 64, 'piano': 0, 'leader': 0},
    {'students_number':  5, 'gender': 1, 'japanese': 36,'society': 38,'mathematics': 20, 'science': 39,'english': 15, 'deviation_value': None, 'physical_point': 59, 'piano': 0, 'leader': 1},
    {'students_number':  6, 'gender': 1, 'japanese': 76,'society': 85,'mathematics': 82, 'science': 89,'english': 75, 'deviation_value': None, 'physical_point': 48, 'piano': 1, 'leader': 0},
    {'students_number':  7, 'gender': 1, 'japanese': 92,'society': 70,'mathematics': 86, 'science': 62,'english': 99, 'deviation_value': None, 'physical_point': 45, 'piano': 0, 'leader': 0},
    {'students_number':  8, 'gender': 1, 'japanese': 80,'society': 77,'mathematics': 81, 'science': 82,'english': 67, 'deviation_value': None, 'physical_point': 60, 'piano': 0, 'leader': 0},
    {'students_number':  9, 'gender': 0, 'japanese': 57,'society': 23,'mathematics': 67, 'science': 82,'english': 10, 'deviation_value': None, 'physical_point': 64, 'piano': 0, 'leader': 0},
    {'students_number': 10, 'gender': 0, 'japanese': 57,'society': 50,'mathematics': 69, 'science': 45,'english': 76, 'deviation_value': None, 'physical_point': 51, 'piano': 1, 'leader': 0},
    {'students_number': 11, 'gender': 1, 'japanese': 63,'society': 31,'mathematics': 92, 'science': 67,'english': 59, 'deviation_value': None, 'physical_point': 40, 'piano': 0, 'leader': 0},
    {'students_number': 12, 'gender': 1, 'japanese': 35,'society': 26,'mathematics': 12, 'science':  8,'english': 23, 'deviation_value': None, 'physical_point': 34, 'piano': 1, 'leader': 0},
    {'students_number': 13, 'gender': 1, 'japanese': 49,'society': 49,'mathematics': 96, 'science': 73,'english': 24, 'deviation_value': None, 'physical_point': 22, 'piano': 0, 'leader': 0},
    {'students_number': 14, 'gender': 0, 'japanese': 22,'society': 52,'mathematics': 73, 'science': 40,'english': 53, 'deviation_value': None, 'physical_point': 28, 'piano': 0, 'leader': 0},
    {'students_number': 15, 'gender': 0, 'japanese': 82,'society':100,'mathematics': 72, 'science': 86,'english': 80, 'deviation_value': None, 'physical_point': 30, 'piano': 0, 'leader': 0},
    {'students_number': 16, 'gender': 0, 'japanese': 28,'society': 22,'mathematics':  8, 'science': 36,'english': 21, 'deviation_value': None, 'physical_point': 53, 'piano': 0, 'leader': 0},
    {'students_number': 17, 'gender': 1, 'japanese': 82,'society': 76,'mathematics': 53, 'science': 60,'english': 55, 'deviation_value': None, 'physical_point': 59, 'piano': 0, 'leader': 1},
    {'students_number': 18, 'gender': 0, 'japanese': 91,'society': 58,'mathematics': 64, 'science': 82,'english': 71, 'deviation_value': None, 'physical_point': 58, 'piano': 0, 'leader': 0},
    {'students_number': 19, 'gender': 0, 'japanese': 15,'society': 20,'mathematics':  0, 'science': 15,'english': 18, 'deviation_value': None, 'physical_point': 58, 'piano': 0, 'leader': 0},
    {'students_number': 20, 'gender': 0, 'japanese': 73,'society': 45,'mathematics': 98, 'science': 84,'english': 79, 'deviation_value': None, 'physical_point': 52, 'piano': 0, 'leader': 0},
]


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