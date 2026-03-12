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

basket = {}
current_page = 1
selected_category = "smartphones"
search_query = ""

categories = [
    {"key": "smartphones", "name": "Смартфоны"},
    {"key": "laptops", "name": "Ноутбуки"},
    {"key": "computers", "name": "Компьютеры"},
]

while True:
    action = ""
    print("\n" + "-" * 50 + "\n")

    if current_page == 1:
        print(
            "1. Главная страница\n"
            "2. Страница категорий\n"
            "3. Страница поиска\n"
            "4. Страница корзины\n"
            "5. Выход\n"
        )

    if current_page == 1:
        print("\nГлавная страница:")
        top_items = [top for top in products_list if top["is_top"]]
        top_5_items = top_items[:5]
        print("\nСамые популярные товары в магазине топ 5.")
        for product in top_5_items:
            print(f"id. {product["id"]}, категория: {product["category"]},"
                  f" цена: {product["price"]} количество. {product["quantity"]}.")
        print("\nПерейти на другую страницу: 'mtp'\nДобавить товары в корзину: 'atb'"
              "\nВыход: 'exit','выход'\n")
            
        action = input("Выберите действие: ").lower().strip()
            
        if action not in ["mtp", "atb", "exit", "выход"]:
            print("Не опознанная команда!\nВыберите из существующих команд!")

    if current_page == 2:
        print("\nКатегории товаров:")
        for num, all_categ in enumerate(categories):
            print(f"{num + 1}.{all_categ["key"]}")

        print("\nВсе товары в выбранной категории:\nПо умолчанию: 'smartphones'\n")

        for categ in products_list:
            if selected_category in categ["category"]:
                print(f"id. {categ["id"]}, Категория: {categ["category"]},"
                      f" Название: {categ["name"]}, Цена: {categ["price"]} Количество. {categ["quantity"]}.")

        print("\nПерейти на другую страницу: 'mtp'\nДобавить товары в корзину: 'atb'"
              "\nИзменить категорию: 'sc'\nВыход: 'exit','выход'\n")

        action = input("\nВыберите действие: ").lower().strip()

        if action not in ["mtp", "atb", "exit", "выход", "sc"]:
            print("Не опознанная команда!\nВыберите из существующих команд!")

    if current_page == 3:
        print("\nСтраница поиска:")

        if search_query == "":
            print(f"Всего товаров {len(products_list)}.\n")

            for product in products_list:
                print(f"id: {product["id"]}. {product["name"]} - {product["price"]}$")

        else:
            print(f"Последний поиск: {search_query}")

        print("\nПерейти на другую страницу: 'mtp'\nДобавить товары в корзину: 'atb'"
              "\nСовершить поиск: 's'\nУдалить поисковую историю: 'del'\nВыход: 'exit','выход'\n")

        action = input("\nВыберите действие: ").lower().strip()

        if action not in ["mtp", "atb", "exit", "выход", "s", "del"]:
            print("Не опознанная команда!\nВыберите из существующих команд!")

        if action == "del":
            search_query = ""

    if current_page == 4:
        basket_summ = 0
        if len(basket) == 0:
            print("Корзина пуста!\nОформите заказ!")
        else:
            print("\nКорзина:")
            for product in basket.keys():
                print(f"id: {product}. {basket[product]["name"]}-"
                      f" {basket[product]["price"]}$: {basket[product]["quantity in basket"]} шт.")
            for product in basket.values():
                basket_summ += product["price"] * product["quantity in basket"]
            print(f"\nСумма ценности корзины: {basket_summ}$.")

        print("\nПерейти на другие страницы: 'mtp'\nОформить заказ: 'Buy'\nУдалить товар: 'itemdel'\nВыход: 'exit','выход'")
        action = input("Выберите действие: ").lower().strip()

        if action not in ["mtp", "buy", "exit", "выход", "itemdel"]:
            print("Не опознанная команда!\nВыберите из существующих команд!")

        if action == "itemdel":
            itemdel_id = input("Введите id для удаления товара ")
            if itemdel_id not in basket.keys():
                print("Такого товара для удаления нету!")
            else:
                for id_nums in basket:
                    if id_nums == itemdel_id:
                        basket[id_nums]["quantity in basket"] -= 1
                    if basket[id_nums]["quantity in basket"] == 0:
                        print("Товар удален с корзины!")
                del basket[itemdel_id]

    if action == "buy":
        user_buy = input("Введите id товара для оформления из корзины: ").lower().strip()

        if user_buy in basket:
            quantity_in_basket = basket[user_buy]["quantity in basket"]

            for product in products_list:
                if product["id"] == user_buy:
                    product["quantity"] -= quantity_in_basket

            del basket[user_buy]

            print("Заказ оформлен!\nДоставка через 3 дня!")
        else:
            print("Товара нет в корзине")

    if action == "mtp":
        print("\nСтраницы магазина.\nГлавная страница: 1.\n"
              "Страница категорий: 2.\nПоисковая страница: 3\nКорзина: 4.\n")

        user_pade_input = input("Введите номер страницы из перечисленных: ").lower().strip()

        if user_pade_input in ["1", "2", "3", "4"]:
            current_page = int(user_pade_input)
            continue

    if action == "atb":
        if current_page in [1, 2, 3]:

            user_input_items_basket = input("Введите id товаров через запятую для добавления: ").lower().strip()
            user_split = user_input_items_basket.split(",")
            unpacet_num = [num.strip() for num in user_split]
            flag = False

            for id_num in products_list:

                for num_unpuk in unpacet_num:

                    if id_num["id"] == num_unpuk:
                        if id_num["id"] in basket:
                             basket[id_num["id"]]["quantity in basket"] += 1

                        else:
                            basket[id_num["id"]] = {"name": id_num["name"],
                                                    "price": id_num["price"],
                                                    "quantity in basket": 1
                                                    }
                        flag = True

            if flag:
                print("Успешное добавление!")
            else:
                print("Ошибка добавления товара! товар не найден.")

        else:
            print("Текущая страница не поддерживает добавление в корзину.")

    if action == "sc":
        if current_page == 2:
            user_input_category = input("Smartphones: 1, Laptop: 2, computers 3."
                                        "\nВыберите категорию по номерам: ").strip().lower()

            if user_input_category == "":
                print("Пустой ввод!")
            elif user_input_category not in ["1", "2", "3"]:
                print("Некорректный Ввод!\nПовторите ввод по новой!")

            else:
                if user_input_category == "1":
                    selected_category = "smartphones"
                elif user_input_category == "2":
                    selected_category = "laptops"
                elif user_input_category == "3":
                    selected_category = "computers"

                print("Успешная смена категории!")

        else:
            print("Текущая страница не поддерживает выбор категории товаров.")

    if action == "s":
        if current_page == 3:
            search_query = input("\nВведите поисковой запрос: ").lower().strip()
            if search_query == "":
                print("Пустой ввод поиска!")

            else:
                for search_product in products_list:
                    if search_query in search_product["name"].lower():
                        print(f"id: {search_product["id"]}. {search_product["name"]} - {search_product["price"]}$")
                        print(search_query)
        else:
            print("Текущая страница не поддерживает поиск товаров.")

    if action in ["exit", "выход"]:
        print("Выход из программы.")
        break
