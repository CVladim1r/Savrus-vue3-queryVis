import os

# Добавить данные бд clickhouse
class Config:
    CLICKHOUSE_HOST = os.getenv('CLICKHOUSE_HOST', 'localhost')
    CLICKHOUSE_PORT = os.getenv('CLICKHOUSE_PORT', 9000)
    CLICKHOUSE_USER = os.getenv('CLICKHOUSE_USER', 'root')
    CLICKHOUSE_PASSWORD = os.getenv('CLICKHOUSE_PASSWORD', '')
    CLICKHOUSE_DATABASE = os.getenv('CLICKHOUSE_DATABASE', 'default')
