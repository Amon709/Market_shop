# Маленький проект онлайн маркетплейс
# Видение проекта:

# Интернет-магазин должен иметь меню:

# 1. Главная страница:
#    1. Будет составлять топ 5 товаров по продаваемости на сайте
#    2. Функционал добавления топ 5 товаров из главной страницы
#    3. Функционал перехода на другие страницы их 3 всего
#
# 2. Страница категорий:
#    1. Показ категорий перечисление из ассортимента для выбора:
#         1. smartphones
#         2. laptops
#         3. computers
# 2. Показ категории для выбора по умолчанию: smartphones
#    1. показ самих элементов smartphones для показа
#    2. Функционал добавления самих вещей в корзину
#    3. Функционал для принятия вывода других категорий по выбору пользователя
#    4. Функционал для перехода на другую страницу

# 3. Страница поиска
# 4. Страница корзины

# Каждый товар имеет следующие характеристики:
# - уникальный ключ;
# - категория;
# - является ли товар топом продаж;
# - название;
# - цену;
# - количество.


# ---------------------- Version 0.1 ----------------------------


products_list = [
    {"id": "1", "category": "smartphones", "is_top": True, "name": "iPhone 13", "price": 900, "quantity": 10},
    {"id": "2", "category": "laptops", "is_top": True, "name": "MacBook Air", "price": 1100, "quantity": 5},
    {"id": "3", "category": "smartphones", "is_top": False, "name": "Samsung Galaxy", "price": 700, "quantity": 15},
    {"id": "4", "category": "laptops", "is_top": False, "name": "HP Pavilion", "price": 800, "quantity": 7},
    {"id": "5", "category": "computers", "is_top": False, "name": "Dell Desktop", "price": 750, "quantity": 8},
    {"id": "6", "category": "computers", "is_top": True, "name": "Apple iMac", "price": 1500, "quantity": 4},
    {"id": "7", "category": "smartphones", "is_top": True, "name": "Google Pixel", "price": 800, "quantity": 3},
    {"id": "8", "category": "laptops", "is_top": False, "name": "Asus ZenBook", "price": 1050, "quantity": 6},
    {"id": "9", "category": "smartphones", "is_top": False, "name": "Xiaomi Mi 11", "price": 650, "quantity": 12},
    {"id": "10", "category": "laptops", "is_top": True, "name": "Lenovo ThinkPad", "price": 950, "quantity": 9},
    {"id": "11", "category": "computers", "is_top": False, "name": "HP Envy Desktop", "price": 900, "quantity": 11},
    {"id": "12", "category": "smartphones", "is_top": True, "name": "OnePlus 9", "price": 850, "quantity": 6},
    {"id": "13", "category": "laptops", "is_top": False, "name": "Dell XPS 13", "price": 1200, "quantity": 3},
    {"id": "14", "category": "computers", "is_top": True, "name": "Acer Aspire", "price": 1100, "quantity": 7},
    {"id": "15", "category": "smartphones", "is_top": False, "name": "Sony Xperia", "price": 750, "quantity": 5},
    {"id": "16", "category": "laptops", "is_top": False, "name": "Microsoft Surface Laptop", "price": 1300,
     "quantity": 2},
                ]
                    # продуктовый лист сами товары !

basket = {} #  корзина
current_page = 1 # текущая страница
selected_category = "smartphones" # выбранная категория
search_query = "" # поисковый запрос

categories = [
    {"key": "smartphones", "name": "Смартфоны"},
    {"key": "laptops", "name": "Ноутбуки"},
    {"key": "computers", "name": "Компьютеры"},
             ]
                # это сами категории товаров/ не изменять !

while True:

    action = ""
    print("\n" + "-" * 50 + "\n")
    print(
        "1. Главная страница\n"
        "2. Страница категорий\n"
        "3. Страница поиска\n"
        "4. Страница корзины\n"
        "5. Выход"
         )

    if current_page == 1:
        print("\nГлавная страница.")

        # Код для отображения главной страницы
        top_items = [top for top in products_list if top["is_top"]]
        top_5_items = top_items[:5]

        print("\nСамые популярные товары в магазине.\n")
        for products in top_5_items:

            print(f"id.{products["id"]} категория: {products["category"]} цена: {products["price"]}")

    action = input("\nПерейти на следующую страницу: mtp \nДобавить товары в корзину: atb\nВыберите действие: ").strip().lower()

    if current_page == 2:
        print("\nКатегории товаров:")
        
        # Код для отображения страницы категорий



    if action == "atb":
        if current_page in [1, 2, 3]:
            # Код для добавления в корзину
            user_take_id_basket = input("Введите товар по номеру для добавления в корзину: ").strip().lower()

            for id_num in products_list:
                if user_take_id_basket in id_num.values():

                    basket[user_take_id_basket] = {"category": id_num["category"],
                                                   "name": id_num["name"],
                                                   "price": id_num["price"],
                                                   "quantity": id_num["quantity"]
                                                   }

        print(basket)

    if action == "exit":
        print("Выход из программы.")
        break
