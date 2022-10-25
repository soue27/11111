import my_db
import my_xls
import os

if not os.path.isfile('disabled.sqlite3'):
    spisok = my_xls.migration_xls_sqllite('Ограниченные ЧуЭС.xls')
    my_db.create_db('disabled.sqlite3', spisok)
else:
    print('файл уже есть')

#
# qw = input('введите лицевой счет')
# for result in my_db.search_by_contract('disabled.sqlite3', qw):
#     print(result)
# #
# # qw = input('введите фамилию').lower()
# # for result in my_db.search_by_counterparty('disabled.sqlite3', qw):
# #     print(result)
# #
# # qw = input('введите номер ТП')
# # for result in my_db.search_by_tp('disabled.sqlite3', qw):
# #     print(result)
# #
# # new = input().split(",")
# # my_db.add_to_bd('disabled.sqlite3', new)
# # #
# my_db.delete_from_bd('disabled.sqlite3', input('Введите номер лицевого счета'))
