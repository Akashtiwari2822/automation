import mysql.connector as connector
import configparser

class DBHelper:
    def __init__(self):
            # config = configparser.ConfigParser()
            # config.read('config.ini')
            # try:
            #     config.add_section("SUPPORT")
            # except configparser.DuplicateSectionError:
            #         pass
            # path_items = config.items("paths")
            # db = config.get('LOGIN', 'db')
            # host = config.get('LOGIN', 'hostname')
            # password = config.get('LOGIN', 'password')
            # user = config.get('LOGIN', 'user')
            
            db = 'test'
            host = 'localhost'
            password = ''
            user = 'root'
            print(db,password,user)
            self.con = connector.connect(host=host,
                                         port="3306",
                                        user=user,
                                        password=password,
                                        database=db)
            # query = 'create table if not exists user(userId int primary key,userName varchar(200), phone varchar(12))'
           

    def select(self):
        query1 = "select count(id) from team "
        # print(query1)
        cur = self.con.cursor()
        cur.execute(query1)
        
  
    #Fech All
# DBHelper.select('')