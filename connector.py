import pymysql

db = pymysql.connect(host='1.13.253.88',
                     user='root',
                     password='ZkGm)n}j/yv@vI$',
                     database='NetworkTest')

cursor = db.cursor()


def insert(my_fault_id, my_fault_type, my_fault_1, my_fault_2, my_province, my_city, my_county, my_town, my_detail,
           my_fault_time):
    sql_syntax = '''
    INSERT INTO `fault_data` (`fault_id`, `fault_type`, `fault_1`, `fault_2`,
     `province`, `city`, `county`, `town`, `detail`, `fault_time`) 
     VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9})
     '''
    sql = sql_syntax.format(my_fault_id, my_fault_type, my_fault_1, my_fault_2, my_province, my_city, my_county,
                            my_town, my_detail, my_fault_time)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


db.close()
