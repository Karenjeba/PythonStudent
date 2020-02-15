import sqlite3

def sql_connection(): 
    try: 
        con = sqlite3.connect('mydatabase.db') 
        return con 
    except Error: 
        print(Error)

def sql_table(con): 
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Student(sid integer,sname text, scourse text)")
    con.commit() 
con = sql_connection() 
#sql_table(con)

def sql_insert(con,sid,name,course):
    cursorObj = con.cursor()
    cursorObj.execute("insert into student(sid,sname,scourse) values (?,?,?)", (sid,name,course))
    con.commit()
#sql_insert(con,2,'Mary','C')
def sql_selectAll(con):
    cursorObj = con.cursor()
    cursorObj.execute('select * from student')
    for row in cursorObj:
        print(row)
    con.commit()
#sql_selectAll(con)

def sql_update(con,sid,course):
    cursorObj = con.cursor()
    sql = 'UPDATE STUDENT SET scourse=? where sid = ?'
    args = (course,sid)
    cursorObj.execute(sql,args)
    con.commit()
#sql_update(con,1,'C')
#sql_selectAll(con)
    
def sql_delete(con,sid):
    cursorObj = con.cursor()
    sql = 'Delete from STUDENT where sid = ?'
    cursorObj.execute(sql,(sid,))
    con.commit()
#sql_delete(con,2)
#sql_selectAll(con)


#Get input from user

print('1. Add Student')
print('2. Update Student')
print('3. Delete Student')
print('4. View All Students')
print('5. Exit')

option = int(input('Enter your choice'))

if option == 1:
    sid = int(input("Enter id:"))
    sname = input("Enter name:")
    scourse = input("Enter Course")
    sql_table(con)
    sql_insert(con,sid,sname,scourse)
elif option == 2:
    sid = int(input("Enter id to update :"))
    scourse = input("Enter Course")
    sql_update(con,sid,scourse)
    sql_selectAll(con)
elif option==3:
    sid = int(input("Enter id to delete :"))
    sql_delete(sid)
elif option==4:
    sql_selectAll(con)
elif option==5:
    exit(0)
    

 
