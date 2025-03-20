import mysql.connector

def get_mysql_connect():
     connection = mysql.connector.connect(
         host ="localhost",
         user ="root",
         password = "password",
         database = "First_etl_prj"
     )
     return connection