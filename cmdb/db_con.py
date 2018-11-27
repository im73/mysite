from django.db import connection as con

class  mysql_con(object):

    def __init__(self):

        self.conn=con
        cursor=self.conn.cursor()




    def close_conn(self):

        try:
            if self.conn:
                self.conn.close()
        except con.Error as e:
            print('Error: %s'%e)




    def show_allusers(self):

        try:
            sql_order = 'select * from transcript;'
            cursor = self.conn.cursor()
            cursor.execute(sql_order)
            data = cursor.fetchall()
            if data:
                rest = [dict(zip([k[0] for k in cursor.description], row))
                                for row in data]
            else:
                rest = None
            print("查询成功")
        except:
            cursor.close()
            rest=None
            print("查询失败")
        cursor.close()
        return rest





    def modify(self,stid,new_grade):

        try:
            sql_order="update transcript set grade=%s where stid =%s;"
            cursor = self.conn.cursor()
            cursor.execute(sql_order % (new_grade,stid))
            self.conn.commit()
            print("修改成功")
        except:
            self.conn.rollback()
            print("修改失败")
        cursor.close()


    def searchbyid(self,stid):

        try:
            sql_order = 'select * from transcript where stid =%s;'
            cursor = self.conn.cursor()

            cursor.execute(sql_order % stid)
            data=cursor.fetchone()

            if data:
                rest = dict(zip([k[0] for k in cursor.description], data))
            else:
                rest = None
            print("查询成功")
        except:
            print("查询失败")
        cursor.close()
        return rest



    def delete(self,stid):

        try:

            sql_order = 'delete from transcript where stid =%s;'
            cursor = self.conn.cursor()

            cursor.execute(sql_order % stid)
            self.conn.commit()
            print("删除成功")

        except:

            self.conn.rollback()
            print("删除失败")

        cursor.close()


    def insert(self,name,stid,csnm,grade):

        try:
            sql_order = "insert transcript(name,stid,csnm,grade)  \
                                values(%s,%s,%s,%s);"
            cursor = self.conn.cursor()
            cursor.execute(sql_order, (name,stid ,csnm , grade))
            self.conn.commit()
            print("插入成功")
        except:
            self.conn.rollback()
            print("插入失败")
        cursor.close()

# def main():
#     obj=mysqlsearch()
#     #insert 测试
#     #
#     # obj.insert('tom1', '16090876', '数据库原理', 87)
#     # obj.insert('tom2', '16090877', '数据库原理', 86)
#     # obj.insert('tom3', '16090878', '数据库原理', 97)
#     # obj.insert('tom4', '16090879', '数据库原理', 80)
#     # obj.insert('tom5', '16090880', '数据库原理', 88)
#     obj.modify(16090881,100)
#
#     dics=obj.show_allusers()
#
#     print("%-10s %-10s %-10s %-10s %-10s" %('序号','名字','学号','课程名','分数'))
#
#     for dic in dics:
#         for value in dic.values():
#             print("%-10s"%value,end='  ')
#         print('')
#     obj.conn.close()
#
#
# if __name__=='__main__':
#     main()

