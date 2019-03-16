import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn
    


def select_task_by_priority(conn, priority):
    a=input("Enter the required company :")
    cur = conn.cursor()
    cur.execute("SELECT Name FROM COMPANY WHERE Symbol=?", (a))

    rows = cur.fetchall()

    for row in rows:
        print(Name)


def main():
    database = "com.db"
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn,1)


if __name__ == '__main__':
    main()
