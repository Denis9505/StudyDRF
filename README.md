# StudyDRF
 # Тестовое задание "Менеджер учёта расходов"   
Вам необходимо реализовать API для учета расходов пользователя.   

Минимальные требования:   
- Регистрация пользователя   
- Авторизация пользователя (по токену)   
- Транзакции пользователя - CRUD
С помощью транзакций происходит списание, начисление баланса пользователя.
Транзакция должна содержать в себе: сумму\*, время\*, категорию\*, организацию\*, описание.
Пользователь должен иметь возможность сортировать, фильтровать транзакции по времени, сумме, дате.
   
- Категории пользователя - CRUD
При регистрации пользователь получает набор стандартных категорий:
"Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина", "Образование", "Отдых и развлечения", "Платежи, комиссии", "Покупки: одежда, техника", "Продукты", "Проезд".
Пользователь может изменять/удалять стандартные категории как пожелает, а также создавать свои.   
- Просмотр профиля пользователя (информация о текущем балансе)   
- Статистика пользователя.
Реализовать отправку статистики на почту пользователя утром каждый день.
Объём получаемой статистики можете выбрать сами.   
   
   
Если у Вас есть желание продемонстрировать знание какой-то технологии или подхода, то можно реализовать произвольную дополнительную функциональность на Ваше усмотрение.   
   
Нефункциональные требования:   
- Язык программирования: Python 3.10+   
- DRF 3+   
- Соответствие исходного кода PEP 8   
   
   
Будет плюсом:   
- Docker / Docker Compose   
- Деплой проекта   
