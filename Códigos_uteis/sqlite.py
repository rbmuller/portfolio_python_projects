#Importing SQL extension
import sqlite3 as sl

#Instantiate an object with our database
con = sl.connect('my-test.db')

#create table and columns 
with con:
    con.execute("""
    CREATE TABLE USER(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    );
    """)

#Input data in our database
sql = 'INSERT INTO USER (id,name,age) values(?,?,?)'
data = [
    (1,'Alice',22),
    (2,'Bob',22),
    (3,'Chris',23)
]

with con:
    con.executemany(sql,data)


#Create a query in the database
with con:
    data = con.execute('SELECT * FROM USER WHERE age <= 22')    
    for row in data:
        print(row)


#Connect to Pandas
import pandas as pd

df_skill = pd.DataFrame({
    'user_id':[1,1,2,2,3,3,3],
    'skill':['Network Security','Algorithm Development','Network Security',
             'Java','Python','Data Science','Machine Learning']
})

#Save the Pandas dataframe to the Database with to_sql
df_skill.to_sql('SKILL',con)

#Join the just created Pandas df to the other table previously created 
#using a SQL Query command 

df = pd.read_sql('''
    SELECT s.user_id,u.name,u.age,s.skill
    FROM USER u LEFT JOIN SKILL s on u.id = s.user_id
    ''',con)

df    

df.to_sql('USER_SKILL',con)

