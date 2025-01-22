import mysql.connector
from mysql.connector import Error
from get_exchange_rates import get_exchange_rate_cl, get_exchange_rate_oexr, crypto_to_usd, timestamp_convert

def upload_database(timestamp,data: dict):
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Borkauszkar24",
            database="exchange_rates"
        )

        if conn.is_connected():
            print("Sikeres kapcsolódás!")

            cursor = conn.cursor()
            data = crypto_to_usd(data)
            for k, v in data.items():
                cursor.execute(f'''
                        CREATE TABLE IF NOT EXISTS {k} (
                            timestamp TIMESTAMP,
                            value DECIMAL(30 ,6)
                        )
                        ''')
                cursor.execute(f'''
                        INSERT INTO {k} (timestamp, value) VALUE (%s, %s)
                        ''', (timestamp_convert(timestamp), v))


            conn.commit()

            print("Adatok sikeresen hozzáadva!")

    except Error as e:
        print("Hiba történt:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Kapcsolat lezárva.")

if __name__ == '__main__':
    ts_cl, data_cl = get_exchange_rate_cl()
    ts_oexr, data_oexr = get_exchange_rate_oexr()
    upload_database(ts_cl, data_cl)
    upload_database(ts_oexr,data_oexr)
