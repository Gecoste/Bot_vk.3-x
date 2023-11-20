import pymysql

class BaseDate:
    def __init__(self, port, host, user, pswd):
        self.connect = pymysql.connect(host=host, user=user, passwd=pswd, port=port)
        self.cursor = self.connect.cursor()