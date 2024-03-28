import pymysql.cursors


account = Mydatabase()
score = Mydatabase()

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
            insertTo_users = "insert into users values(%d, '%s', '%s','%s' ,'%s', '%d');" % (max(user_ids)+1,'学生',account,password,name,class_id)
            self.cur.execute(insertTo_users)
        if identity == "教师":
            insertTo_users = "insert into users values(%d, '%s', '%s','%s' ,'%s', '%d');" % (max(user_ids)+1,'教师',account,password,name,class_id)
            self.cur.execute(insertTo_users)
        self.conn.commit()
        return "注册成功！"


    def login(self,account,password):
        inquire_sql = 'select * from users where account=%s;' % account
        self.cur.execute(inquire_sql)
        res = self.cur.fetchone()
        if res:
            if password == res[3]:
                return res[0],res[1],res[4],res[5]
            else:
                return "密码错误"
        else:
            return '用户不存在，请先注册'

    def inquire_score(self):
        return

    # def inquire(self):
    #     inquire_sql = 'select * from users'
    #     self.cur.execute(inquire_sql)
    #     for i in self.cur.fetchall():
    #         print(i)

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