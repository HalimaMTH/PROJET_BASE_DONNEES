import sqlite3

def run_sql_script():
    conn = sqlite3.connect("hotel.db")
    with open("script_hotel.sql", "r", encoding="utf-8") as file:
        sql = file.read()
        conn.executescript(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_sql_script()
