import os
import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()


class Database:
    @staticmethod
    def get_connection():
        host = os.getenv('DB_HOST', '127.0.0.1')
        user = os.getenv('DB_USER', 'ecotech_user')
        password = os.getenv('DB_PASSWORD', 'ecotech_pass')
        db = os.getenv('DB_NAME', 'ecotech_management')
        port = int(os.getenv('DB_PORT', '3306'))
        conn = pymysql.connect(
            host=host, 
            user=user, 
            password=password, 
            database=db, 
            port=port, 
            cursorclass=DictCursor, 
            autocommit=False
        )
        return conn
