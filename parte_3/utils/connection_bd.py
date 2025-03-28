import mysql.connector

def connection_bd(table):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="tables_csv"
        )

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM table")
        result = cursor.fetchall()

        if result:
            for row in result:
                print(row)
        else:
            print("Nenhum dado encontrado na tabela!")

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()