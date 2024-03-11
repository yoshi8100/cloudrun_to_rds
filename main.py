from flask import Flask
import pymysql
import logging
from pymysql.err import OperationalError

app = Flask(__name__)

# AWS RDS 接続情報 こちらは各自必要な情報に置き換えてください。
DB_USER = 'user_name'
DB_PASSWORD = 'password'
DB_NAME = 'db_name'
DB_HOST = 'xxxxxxx.xxxxxx.ap-northeast-1.rds.amazonaws.com'

# Flask の標準ログ設定
logging.basicConfig(level=logging.INFO)

def get_db_connection():
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
        return conn
    except OperationalError as e:
        app.logger.error('Failed to connect to the database:', e)
        return None

@app.route('/')
def test_db():
    conn = get_db_connection()
    if conn:
        app.logger.info('Successfully connected to the database.')
        conn.close()
        return 'Successfully connected to the database.'
    else:
        return 'Failed to connect to the database.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)