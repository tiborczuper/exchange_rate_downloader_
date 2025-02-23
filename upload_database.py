import mysql.connector
from get_exchange_rates import get_exchange_rate_cl, get_exchange_rate_oexr, crypto_to_usd, timestamp_convert
import mysql.connector
from mysql.connector import Error


def upload_database(timestamp, data: dict):
    try:
        # Megpróbálunk csatlakozni
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",  # Felhasználó
            password="password",  # Jelszó
            database="exchange_rates"
        )

        # Ha sikerült csatlakozni
        if connection.is_connected():
            cursor = connection.cursor()
            data = crypto_to_usd(data)

            for k, v in data.items():
                cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {k} (
                        timestamp TIMESTAMP,
                        value DECIMAL(30, 6)
                    )
                ''')
                cursor.execute(f'''
                    INSERT INTO {k} (timestamp, value) VALUES (%s, %s)
                ''', (timestamp_convert(timestamp), v))

            connection.commit()
            return True  # Sikerült a csatlakozás és az adatok feltöltése

        # Ha nem sikerült csatlakozni
        return False

    except Exception:
        # Ha bármi hiba történik, ne dobjon ki hibát, csak False-t adjon vissza
        return False

    finally:
        # Ha van nyitott kapcsolat, zárjuk le
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    ts_cl, data_cl = get_exchange_rate_cl()
    ts_oexr, data_oexr = get_exchange_rate_oexr()
    ASD = upload_database(ts_cl, data_cl)
    ASD1 = upload_database(ts_oexr,data_oexr)

    print(ASD)
    print(ASD1)
