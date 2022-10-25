import sqlite3


def create_db(base_name: str, spisok: list):
    # Создание таблицы базы данных, на основании полученного списка из парсинга эксель файла.
    # На входе имя базы данных и список загрузки
    connect = sqlite3.connect(base_name)
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS dis (contract, counterparty, city, point, street, house, tp)')
    sqlite_insert_query = """INSERT INTO dis
                                 (contract, counterparty, city, point, street, house, tp)
                                 VALUES (?, ?, ?, ?, ?, ?, ?);"""
    cursor.executemany(sqlite_insert_query, spisok)
    connect.commit()
    connect.close()


def search_by_contract(base_name: str, contract: str):
    # Функция поиска по лицевому счету
    connect = sqlite3.connect(base_name)
    cursor = connect.cursor()
    results = cursor.execute(f"SELECT * FROM dis WHERE contract LIKE '%{contract}%'").fetchall()
    connect.commit()
    connect.close()
    return results


def search_by_counterparty(base_name: str, counterparty: str):
    # функция поиска по ФИО, наименованию
    connect = sqlite3.connect(base_name)
    cursor = connect.cursor()
    results = cursor.execute(f"SELECT * FROM dis WHERE counterparty LIKE '%{counterparty}%'").fetchall()
    connect.commit()
    connect.close()
    return results


def search_by_address(base_name: str, address: list):
    # Функция поиска по адресу, как полному так и неполному.
    # В случае неполного адреса выдаются выборка подпадающие под условия
    connect = sqlite3.connect(base_name)
    cursor = connect.cursor()
    for i in range(len(address)):   # Цикл проверяет, что в адресе есть символы и заменяет их пустой строкой
        if not address[i].isalnum():
            address[i] = ''
    results = cursor.execute(f"SELECT * FROM dis WHERE (city like '%{address[0]}%' or point like '%{address[0]}%') "
                             f"and street like '%{address[1]}%' and house like '%{address[2]}%'").fetchall()
    connect.commit()
    connect.close()
    return results


def search_by_tp(base_name: str, tp: str):
    # Функция поиска по ТП
    connect = sqlite3.connect(base_name)
    cursor = connect.cursor()
    results = cursor.execute(f"SELECT * FROM dis WHERE tp LIKE '%{tp}%'").fetchall()
    connect.commit()
    connect.close()
    return results


def add_to_bd(base_name: str, newdis: list):
    for i in range(len(newdis)):
        newdis[i] = newdis[i].lower()
    connect = sqlite3.connect(base_name)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO dis VALUES (?, ?, ?, ?, ?, ?, ?);",
                   (newdis[0], newdis[1], newdis[2], newdis[2], newdis[3], newdis[4], newdis[5]))
    connect.commit()
    connect.close()


def delete_from_bd(base_name: str, cont: str):
    connect = sqlite3.connect(base_name)
    cursor = connect.cursor()
    cursor.execute(f"DELETE from dis where contract LIKE '%{cont}%'")
    connect.commit()
    connect.close()
