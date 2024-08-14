import sqlite3 as sql

with sql.connect("first.db") as first:
    cur = first.cursor()

    #cur.execute("DROP TABLE IF EXISTS objact")

    """Создали БД с имененм objact, в скобках указали название полей"""
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                name TEXT NOT NULL,
                sex INTEGER DEFAULT 1,
                old INTGER,
                score INTEGER
                )""")

"""
    #INSERT INTO objact (name, old, score) VALUES("Михаил",19, 999)
    name_list = ["Эдик", "Саша", "Маша", "Даша", "Ярослав", "Антон"]
    old_list = [13, 10, 22, 22, 14, 18]
    score_list = [300, 200, 1212, 895, 999999, 435]
    i = 0
    while i<len(name_list): 
        cur.execute(fINSERT INTO users
                     (name, old, score) VALUES('{name_list[i]}', {old_list[i]}, {score_list[i]})
                     )
        i +=1

"""

with sql.connect("second.db") as second:
    cur = second.cursor()
    cur.execute("""CREATE TABLE game (
                user_id INTEGER ,
                score INTEGER,
                time INTEGER
                )""")
    user_id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    score_list = [999, 1490, 1874, 879, 1234, 300, 200, 1212, 895, 999999, 435]
    time_list = [101231, 2312, 73738, 222, 3323, 34234, 32132, 23423, 21123, 33112, 32131]
    for i in user_id_list:
        cur.execute(f"""INSERT INTO game
                    (user_id, score, time) VALUES ({i},{score_list[i-1]},{time_list[i-1]})
                    """)