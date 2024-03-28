import pymysql.cursors
import datetime


class Mydatabase():
    def __init__(self, host, user, password, database):

        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=database,
            charset='utf8',
            # autocommit=True,
        )
        self.cur = self.conn.cursor()


    def register(self,account,class_id,identity,name,password,ensure_passwd):
        # 检测两次密码输入是否一致
        if password != ensure_passwd:
            return "两次密码输入不一致"

        # 查找所有用户id和账号
        inquire_sql = 'select User_id,Account from users;'
        self.cur.execute(inquire_sql)

        res = self.cur.fetchall()
        user_ids = [i[0] for i in res]
        accounts = [i[1] for i in res]
        if account in accounts:
            return "账号已存在"

        if identity == "学生":
            try:
                insertTo_users = "insert into users values(%d, '%s', '%s','%s' ,'%s', '%s');" % (
                max(user_ids) + 1, '学生', account, password, name, class_id)
                self.cur.execute(insertTo_users)
            except ValueError:
                insertTo_users = "insert into users values(%d, '%s', '%s','%s' ,'%s', '%s');" % (
                1, '学生', account, password, name, class_id)
                self.cur.execute(insertTo_users)

        elif identity == "教师":
            try:
                insertTo_users = "insert into users values(%d, '%s', '%s','%s' ,'%s', '%s');" % (
                max(user_ids) + 1, '教师', account, password, name, class_id)
                self.cur.execute(insertTo_users)
            except ValueError:
                insertTo_users = "insert into users values(%d, '%s', '%s','%s' ,'%s', '%s');" % (
                    1, '教师', account, password, name, class_id)
                self.cur.execute(insertTo_users)

        elif identity == "管理员":
            try:
                insertTo_users = "insert into users values(%d, '%s', '%s','%s' ,'%s', '%s');" % (
                    max(user_ids) + 1, '管理员', account, password, name, class_id)
                self.cur.execute(insertTo_users)
            except ValueError:
                insertTo_users = "insert into users values(%d, '%s', '%s','%s' ,'%s', '%s');" % (
                    1, '管理员', account, password, name, class_id)
                self.cur.execute(insertTo_users)
        self.conn.commit()
        return 0


    def login(self,account,password):
        inquire_sql = 'select * from users where account="%s";' % account
        self.cur.execute(inquire_sql)
        res = self.cur.fetchone()
        if res:
            if password == res[3]:
                return res[0],res[1],res[4],res[5]
            else:
                return "密码错误"
        else:
            return '用户不存在，请先注册'

    def student_inquire_homework(self, user_id):
        select_sql = "select DISTINCT homework_id from score_table where user_id='%d' " % (user_id)
        self.cur.execute(select_sql)
        ids = self.cur.fetchall()
        select_sql = "select (homework_id, homework_name, start_time, ddl) from homework_table where  homework_id in ids"
        select_sql = "select (homework_id, homework_name, start_time, ddl) from homework_table where  homework_id not in ids"


        select_sql = "select * from homework_table"
        self.cur.execute(select_sql)
        homeworks = self.cur.fetchall()

        res = []
        for homework in homeworks:
            scores = self.cur.fetchall()
            homework = list(homework)
            if len(scores):
                homework.append(True)
            else:
                homework.append(False)
            res.append(homework)
        return res

    # 管理员主页显示
    def admin_inquire_users(self,user_id):
        select_sql = "select * from users"
        self.cur.execute(select_sql)
        users = self.cur.fetchall()
        return users

    # 管理员题库显示
    def admin_inquire_questions(self):
        select_sql = "select * from questions_table"
        self.cur.execute(select_sql)
        res = self.cur.fetchall()
        res = sorted(res,key=lambda x:(x[4],x[1]))
        return res

    def modify_question(self,user_id,question_id,question,answer,question_type):
        del_sql = "delete from questions_table where user_id=%d and question_id=%d"%(user_id, question_id)
        self.cur.execute(del_sql)
        self.save_question(user_id,question_id,question,answer,question_type)

    def save_question(self,user_id,question_id,question,answer,question_type):
        if question_id is not None:
            insert_sql = "insert into questions_table values(%d,%d,'%s','%s',%d)" % (user_id,question_id,question,answer,question_type)
        else:
            select_sql = "select max(question_id) from questions_table"
            self.cur.execute(select_sql)
            question_id = self.cur.fetchone()[0] + 1
            insert_sql = "insert into questions_table values(%d,%d,'%s','%s',%d)" % (user_id,question_id,question,answer,question_type)
        self.cur.execute(insert_sql)
        self.conn.commit()
        return user_id, question_id


    def del_question(self,user_id,question_id):
        del_sql = "delete from questions_table where user_id=%d and question_id=%d" % (user_id,question_id)
        self.cur.execute(del_sql)
        self.conn.commit()

    def admin_inquire_accounts(self):
        select_sql = "select * from Users"
        self.cur.execute(select_sql)
        res = self.cur.fetchall()
        # res = sorted(res, key=lambda x: (x[4], x[1]))
        return res

    def admin_modify_user(self,user_id,Identity,account,password,name,class_id):
        del_sql = "delete from users where user_id=%d" % (user_id)
        self.cur.execute(del_sql)
        self.save_user(user_id,Identity,account,password,name,class_id)

    def save_user(self,user_id,Identity,account,password,name,class_id):
        insert_sql = "insert into users values(%d,'%s','%s','%s','%s','%s')" % (user_id,Identity,account,password,name,class_id)
        self.cur.execute(insert_sql)
        self.conn.commit()

    def admin_del_users(self,user_id):
        del_sql = "delete from users where user_id=%s" % user_id
        self.cur.execute(del_sql)
        self.conn.commit()

    def admin_homepage(self):
        select_users_sql = "select identity from users"
        select_questions_sql = "select question_type from questions_table"

        self.cur.execute(select_users_sql)
        identities = [i[0] for i in self.cur.fetchall()]
        total_user_num = len(identities)
        idtt_dic = {i:0 for i in identities}
        for i in identities:
            idtt_dic[i] += 1

        self.cur.execute(select_questions_sql)
        question_types = [i[0] for i in self.cur.fetchall()]
        total_ques_num = len(question_types)
        ques_type_dic = {"主观题":0,"客观题":0}
        for i in question_types:
            if i==0:
                ques_type_dic["主观题"] += 1
            else:
                ques_type_dic["客观题"] += 1

        return total_user_num,idtt_dic,total_ques_num,ques_type_dic

    # 教师题库显示
    def teacher_inquire_questions(self,user_id):
        user_id = self.account2userid(user_id)
        select_sql = "select * from questions_table where user_id=%s" % user_id
        self.cur.execute(select_sql)
        questions = self.cur.fetchall()
        return questions

    def account2userid(self,account):
        select_sql = "select user_id from users where account='%s'" % account
        self.cur.execute(select_sql)
        return self.cur.fetchall()[0][0]

    def userid2account(self,user_id):
        select_sql = "select account from users where user_id='%s'" % user_id
        self.cur.execute(select_sql)
        return self.cur.fetchall()[0][0]

    # 最后一个参数为（question_id-分值-题型）三元组的列表，ddl用datetime.datetime格式存
    def teacher_release_homework(self,user_id, homework_name,ddl,class_id,questions_points_and_questiontypes):
        select_sql = "select homework_id from homework_table"
        self.cur.execute(select_sql)
        res = self.cur.fetchall()
        if res:
            homework_id = max([i[0] for i in res]) + 1
        else:
            homework_id = 1
        start_date = datetime.datetime.now()
        insert_sql = "insert into homework_table values(%d,%d,'%s','%s','%s','%s')" % (homework_id,user_id,homework_name,start_date,ddl,class_id)
        self.cur.execute(insert_sql)
        for question_id,points,question_type in questions_points_and_questiontypes:
            self.save_homework_questions(homework_id,class_id,question_id,points,question_type)
        self.conn.commit()

    def save_homework_questions(self,homework_id,class_id,question_id,points,question_type):
        insert_sql = "insert into question_homework_table values(%d,%d,%d,%d,'%s')" % (homework_id,question_id,points,question_type,class_id)
        self.cur.execute(insert_sql)

    # 返回（homework_id,homework_name,start_date,ddl）

    def student_inquire_homework(self,class_id,user_id):
        select_sql = "select homework_id,homework_name,start_date,ddl from homework_table where class_id='%s'" % class_id
        self.cur.execute(select_sql)
        select_res = self.cur.fetchall()

        res = []
        for i in select_res:
            coh = self.content_of_homework(i[0],user_id)
            i = list(i)
            i.append(coh)
            res.append(i)
        return res

    # 返回[ homework_id, homework_name, start_date, ddl, 作业内容 ]
    # 其中作业内容是一个列表,元素是本次作业的题目
    def teacher_class_id2user_id(self,class_id):
        select_sql = "select user_id from users where class_id='%s' and identity='教师'" % class_id
        self.cur.execute(select_sql)
        return self.cur.fetchone()[0]

    # 返回[ homework_id, homework_name, start_date, ddl, 作业内容 ,True/False]
    # 其中作业内容是一个列表,元素是本次作业的题目
    def student_homepage(self,user_id,class_id):
        select_sql = "select homework_id,homework_name,start_date,ddl from homework_table where class_id='%s'" % class_id
        self.cur.execute(select_sql)
        select_res = self.cur.fetchall()

        uploaded = self.student_is_upload(user_id)
        res = []
        for i in select_res:
            coh = self.content_of_homework(i[0],class_id)
            res.append(list(i))
            res[-1].append([c[0] for c in coh])
            res[-1].append(i[0] in uploaded)
        return res

    def content_of_homework(self,homework_id,class_id):
        user_id = self.teacher_class_id2user_id(class_id)
        select_sql = "select question_id from questions_table where user_id=%d and question_id in " \
                     "(select question_id from question_homework_table where homework_id=%d and " \
                     "class_id='%s');" % (user_id,homework_id,class_id)
        self.cur.execute(select_sql)
        questions = self.cur.fetchall()
        return questions

    def student_is_upload(self,user_id):
        select_sql = "select homework_id from score_table where user_id=%d" % user_id
        self.cur.execute(select_sql)
        return self.cur.fetchall()

    def check_student_is_upload(self,user_id, homework_id):
        select_sql = "select * from score_table where user_id=%d and homework_id=%d" % (user_id, homework_id)
        self.cur.execute(select_sql)
        return self.cur.fetchall()

    # question,answer,question_type,point,student_answer
    def inquire_homework(self, user_id, homework_id, question_id):
        select_question_answer = "select question,answer from questions_table where question_id=%d" % question_id
        select_type_point = "select question_type,points from question_homework_table where question_id=%d and homework_id=%d" % (
        question_id, homework_id)
        select_st_answer = "select student_answer from score_table where question_id=%d and homework_id=%d and user_id=%d" % (
        question_id, homework_id, user_id)

        self.cur.execute(select_question_answer)
        question_answer = self.cur.fetchone()
        question = question_answer[0]
        answer = question_answer[1]

        self.cur.execute(select_type_point)
        type_point = self.cur.fetchone()
        question_type = type_point[0]
        point = type_point[1]

        self.cur.execute(select_st_answer)
        st_answer = self.cur.fetchone()

        if st_answer:
            student_answer = st_answer[0]
        else:
            student_answer = None

        return question, answer, question_type, point, student_answer

    def inquire_score(self, user_id, homework_id, question_id):
        select_st_answer = "select score from score_table where question_id=%d and homework_id=%d and user_id=%d" % (
        question_id, homework_id, user_id)
        self.cur.execute(select_st_answer)
        score = self.cur.fetchone()
        if score:
            return score[0]
        else:
            return None

    def inquire_student_answer(self,homework_id,question_id):
        select_sql = "select user_id,student_answer from score_table where homework_id=%d and question_id=%d" % (homework_id,question_id)
        self.cur.execute(select_sql)
        return self.cur.fetchall()

    def save_score(self,homework_id,user_id,question_id,score,question_type,student_answer):
        select_sql = "select * from score_table where homework_id=%d and user_id=%d and question_id=%d;" % (homework_id,user_id,question_id)
        self.cur.execute(select_sql)
        if self.cur.fetchall():
            del_sql = "delete from score_table where homework_id=%d and user_id=%d and question_id=%d;" % (homework_id,user_id,question_id)
            self.cur.execute(del_sql)
            self.conn.commit()
        insert_sql = "insert into score_table values(%d,%d,%d,%d,'%s');" % (homework_id,user_id,question_id,score,student_answer)
        self.cur.execute(insert_sql)
        self.conn.commit()

    def student_report(self, homework_id, class_id, user_id):
        select_sql = "select user_id from users where class_id='%s' and Identity='学生'" % class_id
        self.cur.execute(select_sql)
        st_num = len(self.cur.fetchall())

        select_sql = "select user_id,score from score_table where homework_id=%d" % homework_id
        self.cur.execute(select_sql)
        res = self.cur.fetchall()
        students = {i[0]: 0 for i in res}

        for i in res:
            if i[1] == -1:
                students[i[0]] = -100
            else:
                students[i[0]] += i[1]

        rank_lst = [i[0] for i in sorted(students.items(), key=lambda x: x[1], reverse=False)]
        rank = rank_lst.index(user_id) + 1

        return st_num, rank

    def inquery_teacher_homework(self, uid):
        select_sql = "select Homework_id, Homework_name, start_date, ddl from homework_table where user_id=%d;" % (uid)
        self.cur.execute(select_sql)
        return self.cur.fetchall()

    def teacher_report(self, homework_id):

        select_sql = "select user_id,score from score_table where homework_id=%d" % homework_id
        self.cur.execute(select_sql)
        res = self.cur.fetchall()
        students = {i[0]: 0 for i in res}

        for i in res:
            if i[1] == -1:
                students[i[0]] = -100
            else:
                students[i[0]] += i[1]

        kv_pair = []
        for i in students.items():
            select_sql = "select name from users where user_id=%d" % i[0]
            self.cur.execute(select_sql)
            name = self.cur.fetchone()[0]
            kv_pair.append([name, i[1]])
        rank_lst = sorted(kv_pair, key=lambda x: x[1], reverse=True)

        return len(rank_lst), rank_lst

    def inquire_total_point(self, homework_id):
        select_sql = "select points from question_homework_table where homework_id=%d" % homework_id
        self.cur.execute(select_sql)
        return sum(self.cur.fetchall()[0])

    # def inquery_homework_total_score(self, homework_id):
    #     select_sql = "select sum(score) from score_table where homework_id=%d;" % (homework_id)
    #     self.cur.execute(select_sql)
    #     return self.cur.fetchall()[0]

if __name__ == '__main__':
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='10290293',
        db='homework_view',
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )

    mydb = Mydatabase('localhost','root','MIMA','mk_asst')

    print(mydb.register(account="12312123", class_id=22, identity="学生", name="徐邵洋", password="123456",
                        ensure_passwd="123456"))
    print(mydb.login(account="12312123",  password="123456"))
    # mydb.inquire()