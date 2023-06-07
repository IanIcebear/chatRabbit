import os

# 是否开启debug模式  
DEBUG = True

# #读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'root')
password = os.environ.get("MYSQL_PASSWORD", '+1sYZH466105')
db_address = os.environ.get("MYSQL_ADDRESS", '10.16.111.167:3306')

# username = os.environ.get("MYSQL_USERNAME", 'root')
# password = os.environ.get("MYSQL_PASSWORD", '+1sYZH466105')
# db_address = os.environ.get("MYSQL_ADDRESS", 'sh-cynosdbmysql-grp-i747p6v2.sql.tencentcdb.com:20742')
