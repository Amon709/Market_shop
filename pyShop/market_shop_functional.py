from data import products_list
from data import categories

def page_1():
    print("\nГлавная страница:")

    top_items = [top for top in products_list if top["is_top"]]
    top_5_items = top_items[:5]
    print("\nСамые популярные товары в магазине топ 5.")
    for products in top_5_items:
        print(f"id. {products["id"]}, категория: {products["category"]},"
              f" цена: {products["price"]} количество. {products["quantity"]}.")
    print("\nПерейти на другую страницу: 'mtp'\nДобавить товары в корзину: 'atb'"
          "\nВыход: 'exit','выход'\n")


def page_2():
    print("\nКатегории товаров:")
    for num, all_categ in enumerate(categories):
        print(f"{num + 1}.{all_categ['key']}")

    print("\nВсе товары в выбранной категории:\nПо умолчанию: 'smartphones'\n")

    for categ in products_list:
        if selected_category in categ["category"]:
            print(f"id. {categ["id"]}, Категория: {categ["category"]},"
                  f" Название: {categ["name"]}, Цена: {categ["price"]} Количество. {categ["quantity"]}.")

    print("\nПерейти на другую страницу: 'mtp'\nДобавить товары в корзину: 'atb'"
          "\nИзменить категорию: 'sc'\nВыход: 'exit','выход'\n")

def page_3():
    print("\nСтраница поиска:")

    if search_query == "":
        print(f"Всего товаров {len(products_list)}.\n")

        for products in products_list:
            print(f"id: {products["id"]}. {products["name"]} - {products["price"]}$")

    else:
        print(f"Последний поиск: {search_query}")

    print("\nПерейти на другую страницу: 'mtp'\nДобавить товары в корзину: 'atb'"
          "\nСовершить поиск: 's'\nУдалить поисковую историю: 'del'\nВыход: 'exit','выход'\n")

def page_4():
    basket_summ = 0
    if len(basket) == 0:
        print("Корзина пуста!\nОформите заказ!")
    else:
        print("\nКорзина:")
        for products in basket.keys():
            print(f"id: {products}. {basket[products]["name"]}-"
                  f" {basket[products]["price"]}$: {basket[products]["quantity in basket"]} шт.")
        for products in basket.values():
            basket_summ += products["price"] * products["quantity in basket"]
        print(f"\nСумма ценности корзины: {basket_summ}$.")

    print("\nПерейти на другие страницы: 'mtp'\nОформить заказ: 'Buy'\nУдалить товар: 'itemdel'\nВыход: 'exit','выход'")

def validations_command(user_action, allowed_command):
    if user_action not in allowed_command:
        print("Не опознанная команда!\nВыберите из существующих команда!")
        return False
    return True

def action_buy(item_id_buy, baskets, product_list):
    if item_id_buy in baskets:
        quantity_in_basket = baskets[item_id_buy]["quantity in basket"]

        for product in product_list:
            if product["id"] == item_id_buy:
                product["quantity"] -= quantity_in_basket

        del baskets[item_id_buy]
        print("Заказ оформлен!\nДоставка через 3 дня!")
        return True

    print("Товара нет в корзине")
    return False

def action_mtp(input_new_page):
    print("\nСтраницы магазина.\nГлавная страница: 1.\n"
          "Страница категорий: 2.\nПоисковая страница: 3\nКорзина: 4.\n")

    if input_new_page in ["1", "2", "3", "4"]:
        return int(input_new_page)

    return None

def action_atb(input_item, baskets, product_list):

    unpacet_num = [num.strip() for num in input_item.split(",")]
    flag = False

    for num_unpuk in unpacet_num:
        if  num_unpuk == "":
            print("Ввод id пустой!")
            continue

        if not num_unpuk.isdigit():
            print(f"{num_unpuk}: это не число!")
            continue

        found = False

        for id_num in product_list:

            if id_num["id"] == num_unpuk:
                if id_num["id"] in baskets:
                    baskets[id_num["id"]]["quantity in basket"] += 1

                else:
                    baskets[id_num["id"]] = {"name": id_num["name"],
                                            "price": id_num["price"],
                                            "quantity in basket": 1
                                            }
                flag = True
                found = True
                break

        if not found:
            print(f"Товар с id: {num_unpuk} не найден!")

    return flag

def action_sc(user_input, sel_category, categoria):

    if user_input == "":
        print("Пустой ввод!")
        return None

    if user_input not in ["1", "2", "3"]:
        print("Некорректный Ввод!\nПовторите ввод по новой!")
        return None

    new_category = categoria[int(user_input) - 1]["key"]

    if new_category == sel_category:
        print("Сменяемая категория равна текущей!")
        return None

    return new_category

def action_search(user_input, product_list):
    if user_input == "":
        return print("Пустой ввод поиска!")

    else:
        for search_product in product_list:
            if search_query in search_product["name"].lower():
                return print(f"id: {search_product["id"]}. {search_product["name"]} - {search_product["price"]}$")

    return None

def action_itemdel(id_delite, baskets):

        if id_delite not in baskets:
            print("Такого товара для удаления нету!")
            return False

        baskets[id_delite]["quantity in basket"] -= 1


        if baskets[id_delite]["quantity in basket"] == 0:
            del baskets[id_delite]
            print("Товар удален с корзины!")
        return True

basket = {}
current_page = 1
selected_category = "smartphones"
search_query = ""


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
        page_1()

        action = input("Выберите действие: ").lower().strip()

        if not validations_command(action, ["mtp", "atb", "exit", "выход"]):
            continue

    if current_page == 2:
        page_2()

        action = input("\nВыберите действие: ").lower().strip()

        if not validations_command(action, ["mtp", "atb", "exit", "выход", "sc"]):
            continue

    if current_page == 3:
        page_3()

        action = input("\nВыберите действие: ").lower().strip()
        if not validations_command(action, ["mtp", "atb", "exit", "выход", "s", "del"]):
            continue

    if current_page == 4:
        page_4()

        action = input("Выберите действие: ").lower().strip()

        if not validations_command(action, ["mtp", "buy", "exit", "выход", "itemdel"]):
            continue

    if action == "buy":
        user_buy = input("Введите id товара для оформления из корзины: ").lower().strip()

        buy_status = action_buy(user_buy, basket, products_list)

    if action == "itemdel":
        itemdel_id = input("Введите id для удаления товара: ")

        action_itemdel(itemdel_id, basket)

    if action == "del":
        if search_query == "":
            print("Нет истории поиска для удаления!\nРекомендуем что нибудь поискать!")

        else:
            search_query = ""
            print("История поиска очищена!")

    if action == "mtp":

        user_pade_input = input("Введите номер страницы из перечисленных: ").lower().strip()

        new_page = action_mtp(user_pade_input)
        if new_page is not None:
            current_page = new_page

        continue

    if action == "atb":
        if current_page in [1, 2, 3]:

            user_input_items_basket = input("Введите id товаров через запятую для добавления: ").lower().strip()

            result = (
                action_atb(user_input_items_basket, basket, products_list))

            if result:
                print("Успешное добавление!")
            else:
                print("Ошибка добавления товара! товар не найден.")

        else:
            print("Текущая страница не поддерживает добавление в корзину.")

    if action == "sc":
        if current_page == 2:
            user_input_category = input("Smartphones: 1, Laptop: 2, Computers 3."
                                        "\nВыберите категорию по номерам: ").strip().lower()

            result_sc = action_sc(user_input_category, selected_category, categories)

            if result_sc:
                selected_category = result_sc
                print("Успешная смена категории!")

        else:
            print("Текущая страница не поддерживает выбор категории товаров.")

    if action == "s":
        if current_page == 3:
            search_query = input("\nВведите поисковой запрос: ").lower().strip()
            action_search(search_query, products_list)

        else:
            print("Текущая страница не поддерживает поиск товаров.")

    if action in ["exit", "выход"]:
        print("Выход из программы.")
        break
