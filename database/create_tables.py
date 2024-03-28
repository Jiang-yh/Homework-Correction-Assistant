import pymysql.cursors


HOST = 'localhost'

# 1. 连接数据库，
conn = pymysql.connect(
    host=HOST,
    user='root',
    password='10290293',
    db='homework_view',
    charset='utf8',
    # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
)


# create_users_table = 'create table Users (User_id INT primary key,' \
#                                                     'Identity INT ,' \
#                                                      'Account VARCHAR(1000) ,'  \
#                                                     'Password VARCHAR(50)' \
#                                                     ');'
# create_teachers_table = 'create table Teachers (User_id INT primary key,' \
#                                                     'Name VARCHAR(20) ,' \
#                                                     'Class_id INT ' \
#                                                    ');'
# create_students_table = 'create table Students (User_id INT primary key,' \
#                                                 'Name VARCHAR(20) ,' \
#                                                 'Class_id INT ' \
#                                                 ');'
# create_oqb_table = 'create table Obj_Ques_Bank (O_qid INT primary key,' \
#                                                'question VARCHAR(300) ,' \
#                                                'answer VARCHAR(50) ' \
#                                                ');'
# create_sqb_table = 'create table Subj_Ques_Bank (S_qid INT primary key,' \
#                                                'question VARCHAR(300) ,' \
#                                                'answer VARCHAR(1000) ' \
#                                                ');'


# # 作业id， 本次作业题号， 问题， 分值
# create_homework_table = 'create table Homework_Table (Homework_id INT,' \
#                                                'Qid INT ,' \
#                                                 'Question VARCHAR(300) ,' \
#                                                 'Points INT ' \
#                                                ');'
# # 学生得分表
# # 作业id， 学生id， 本次作业题号， 得分
# create_score_table = 'create table Score_Table (Homework_id INT,' \
#                           'Student_id INT ,' \
#                           'Qid INT ,' \
#                           'Score INT ' \
#                             ');'
#
# create_storage_table = 'create table Storage_Path_Table (Homework_id INT,' \
#                           'Path VARCHAR(100) ,' \
#                           'Upload_time DATETIME ' \
#                             ');'

create_users_table = 'create table Users (User_id INT primary key,' \
                                                    'Identity VARCHAR(10) ,' \
                                                     'Account VARCHAR(1000) ,'  \
                                                    'Password VARCHAR(50),' \
                                                     'Name VARCHAR(50) ,' \
                                                     'Class_id VARCHAR(30)' \
                                                    ');'


create_questions_table = 'create table questions_table (user_id INT,' \
                                               'question_id INT,' \
                                               'question VARCHAR(300) ,' \
                                                'answer VARCHAR(300) ,' \
                                                'question_type INT ,' \
                                                'primary key(user_id,question_id));'

create_homework_table = 'create table homework_table (Homework_id INT,' \
                                'user_id int,'\
                                 'Homework_name varchar(30) ,' \
                                 'start_date DATETIME ,' \
                                 'ddl DATETIME ,' \
                                'class_id varchar(20) ' \
                                ');'


# # 作业id， 本次作业题号， 问题， 分值
create_question_homework_table = 'create table question_homework_table (Homework_id INT,' \
                                               'question_id INT ,' \
                                                'Points INT ,' \
                                                'question_type INT ,' \
                                                 'class_id varchar(20) ' \
                                                 ');'

# # 学生得分表
# # 作业id， 学生id， 本次作业题号， 得分
create_score_table = 'create table Score_Table (Homework_id INT,' \
                          'User_id INT ,' \
                          'question_id INT ,' \
                          'Score INT ,' \
                            'student_answer varchar(1000),'\
                        'primary key(Homework_id,User_id,question_id));'



cur = conn.cursor()

try:
    # cur.execute(create_questions_table)
    # cur.execute('drop table homework_table')
    # cur.execute(create_homework_table)
    # cur.execute(create_question_homework_table)
    # cur.execute('alter table questions_table modify column answer varchar(1000)')
    # cur.execute('alter table score_table add column student_answer varchar(1000);')
    cur.execute('alter table score_table change column qid question_id int;')
    # cur.execute(create_score_table)
except Exception as e:
    print("创建数据表失败:", e)
else:
    print("创建数据表成功")