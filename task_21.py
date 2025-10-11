#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Содержимое файла config_default.txt
# Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?
#
# # Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?
#
# # Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?
#
# # Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?
#
#
# # Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True

# Настройки базы данных
# db_host     =  5432
# .....

f = open('config_default.txt', 'rt', encoding='utf-8')
lines = f.readlines()
f.close()
keys = list(config_values.keys())
new_lines = []
keys_cnt = 0
lines_cnt = 0
while keys_cnt < len(keys) - 3 and lines_cnt < len(lines):
    if keys[keys_cnt] in lines[lines_cnt]:
        if config_values[keys[keys_cnt]] == 'NextGen':
            new_lines.append(keys[keys_cnt].ljust(12) + '= ' + f'"{config_values[keys[keys_cnt]]}"' + '\n')
        elif isinstance(config_values[keys[keys_cnt]], int):
            new_lines.append(keys[keys_cnt].ljust(12) + '= ' + f'{config_values[keys[keys_cnt]]}' + '\n')
        else:
            new_lines.append(keys[keys_cnt].ljust(12) + '= ' + f"'{config_values[keys[keys_cnt]]}'" + '\n')
        lines_cnt += 1
        keys_cnt += 1
    elif lines[lines_cnt].isspace():
        new_lines.append('\n')
        lines_cnt += 1
f = open('config.txt', 'wt', encoding='utf-8')
f.writelines(new_lines)
f.close()
