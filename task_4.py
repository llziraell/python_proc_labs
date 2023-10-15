users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

visit_info = {
"Общее количество": 0,
"Уникальные посещения": 0
}

visit_info["Общее количество"] = len(users)
visit_info["Уникальные посещения"] = len(set(users))

print(visit_info)
