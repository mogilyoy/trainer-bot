score = """
Привет, мужик!\n
Для записи результата в базу данных вводи название упражнения и число количества повторений. \nНапример: "пресс 150"\n
Я запишу твой результат и он отобразится в разделе "Мой прогресс".\n
В базе данных строго определены упражнения для записи. Ты можешь записать свой результат по таким базовым упражнениям как: \n
1. ходьба\n
2. отжимания на брусьях\n
3. скакалка\n
4. подтягивания\n 
5. приседания\n
6. планка\n
7. отжимания\n
8. бег\n
9. пресс\n
10. турник\n
А также все упражнения, доступные в разделе "Упражнения"\n
При этом мне не важно, как именно вы напишете "отжимания" или "анжумания", я вас понимаю. Я сам люблю такие упражнения как "бегит", "прес качат" и другие.\n
Надеюсь эта информация тебе поможет! Если что не так, пиши админу в разделе "Профиль"
"""

def profile(name, user_name, language):
    a = f"""Имя: {name}\nНикнейм: {user_name}\nЯзык: {'русский' if language == 'ru' else 'не определен'}"""
    return a