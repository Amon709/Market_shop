import json
from data import products_list, categories

class Marketplace:
    # 1. КОНСТРУКТОР — создаёт объект и загружает данные
    def __init__(self):
        self.products = products_list
        self.categories = categories
        self.basket = {}
        self.current_page = 1
        self.selected_category = "smartphones"
        self.search_history = {}
        self.page_commands = {
            1: ["mtp", "atb", "exit"],
            2: ["mtp", "atb", "sc", "exit"],
            3: ["mtp", "atb", "s", "del", "exit"],
            4: ["mtp", "buy", "itemdel", "exit"],
        }

        # ПРИ ЗАПУСКЕ — автоматом загружаем сохранённую корзину
        self.load_data()

    # --------------- this is validation input commands -----------------

    def get_commands(self):

        """
        """
        return self.page_commands.get(self.current_page, [])# не понял функцию понял то что он берет
        # команды из класса и находит текущую страницу и печатает текущие команды под нужный page ?

    def print_commands(self):
        """

        """
        return print("\nEnter the command:", ", ".join(self.get_commands()))# вводят команду из нужных по текущей
        # странице и печатает обяденив нужыне команды из get_command ?

    def is_valid(self, action):# проверка команды валидная ли она или нет и выдавание результата
        return action in self.get_commands()

     # --------------------- this is end validations commands --------------------------

    # ------------------ this is json saving programs data -----------------------------
    # 2. СОХРАНЕНИЕ В JSON
    def save_data(self):
        """
        """
        data_to_save = {
            "basket": self.basket,
            "current_page": self.current_page,
            "selected_category": self.selected_category,
            "search_history": self.search_history
        }
        with open("shop_data.json", "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    # ------------------- this is download from json save files -----------------------
    # 3. ЗАГРУЗКА ИЗ JSON
    def load_data(self):
        try:
            with open("shop_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.basket = data.get("basket", {})
                self.current_page = data.get("current_page", 1)
                self.selected_category = data.get("selected_category", "smartphones")
                self.search_history = data.get("search_history", {})
        except FileNotFoundError:
            # Если файла нет — просто работаем с пустыми данными
            pass

    # 4. МЕТОДЫ СТРАНИЦ (переносишь свои page_1, page_2...)

    #--------------------- this is start page blog --------------------------
    def page_1(self):
        """ Показывает главную страницу и топ 5 товаров:

        Пример печати топ 5 товаров:
            id. 1, categories: smartphones, price: 900 - 10 pcs.
            id. 2, categories: laptops, price: 1100 - 5 pcs.
        """
        # Пример команд для главной страницы перечисление:
        # Enter the command: mtp, atb, exit
        #
        # mtp команда для перехода по страницам
        #
        # atb команда для добавления товаров в корзину
        #
        # exit команда для выхода из программы и магазина после до выхода
        # при наборе команды exit происходит сохранение данных в json

        print("Главная страница.")
        top_items_products = [top_5 for top_5 in self.products if top_5["is_top"]]
        top_five_items = top_items_products[:5]
        for product in top_five_items:
            print(f"id. {product['id']}, categories: {product['category']}, price: {product['price']} - {product['quantity']} pcs.")
        # ... твой код page_1, только products_list → self.products

    def page_2(self):
        print("\nКатегории товаров:")
        for num, all_categ in enumerate(self.categories):
            print(f"{num + 1}.{all_categ['key']}")

        print("\nВсе товары в выбранной категории:\nПо умолчанию: 'smartphones'\n")

        for categ in self.products:
            if self.selected_category in categ["category"]:
                print(f"id. {categ["id"]}, Категория: {categ["category"]},"
                      f" Название: {categ["name"]}, Цена: {categ["price"]} Количество. {categ["quantity"]}.")

        print("\nПерейти на другую страницу: 'mtp'\nДобавить товары в корзину: 'atb'"
              "\nИзменить категорию: 'sc'\nВыход: 'exit','выход'\n")

    def page_3(self):
        print("\nСтраница поиска:")

        if len(self.search_history) == 0:
            print(f"Всего товаров {len(self.products)}.\n")

            for products in self.products:
                print(f"id: {products["id"]}. {products["name"]} - {products["price"]}$")

        else:
            for num, name in enumerate(self.search_history):
                print(f"Последний поиск: {num + 1}. {name} - {self.search_history[name]}.")

        print("\nПерейти на другую страницу: 'mtp'\nДобавить товары в корзину: 'atb'"
              "\nСовершить поиск: 's'\nУдалить поисковую историю: 'del'\nВыход: 'exit','выход'\n")

    def page_4(self):
        basket_summ = 0
        if len(self.basket) == 0:
            print("Корзина пуста!\nОформите заказ!")
        else:
            print("\nКорзина:")
            for products in self.basket.keys():
                print(f"id: {products}. {self.basket[products]["name"]}-"
                      f" {self.basket[products]["price"]}$: {self.basket[products]["quantity in basket"]} шт.")

            for products in self.basket.values():
                basket_summ += products["price"] * products["quantity in basket"]
            print(f"\nСумма ценности корзины: {basket_summ}$.")

        print(
            "\nПерейти на другие страницы: 'mtp'\nОформить заказ: 'Buy'\nУдалить товар: 'itemdel'\nВыход: 'exit','выход'")
    #--------------------------------- this is end page blog ----------------------------

    # 5. ДЕЙСТВИЯ (переносишь свои action_*)
    # ------------------------- this is start user actions commands -----------------------
    def action_atb(self, user_input):
        # ... твой код action_atb, basket → self.basket, products_list → self.products

        unpacet_num = [num.strip() for num in user_input.split(",")]

        flag = False

        for num_unpuk in unpacet_num:
            if  num_unpuk == "":
                print("Ввод id пустой!")
                continue

            if not num_unpuk.isdigit():
                print(f"{num_unpuk}: это не число!")
                continue

            found = False

            for id_num in self.products:

                if id_num["id"] == num_unpuk:
                    if id_num["id"] in self.basket:
                        self.basket[id_num["id"]]["quantity in basket"] += 1

                    else:
                        self.basket[id_num["id"]] = {"name": id_num["name"],
                                                "price": id_num["price"],
                                                "quantity in basket": 1
                                                }
                    flag = True
                    found = True
                    break

            if not found:
                print(f"Товар с id: {num_unpuk} не найден!")

        return flag

    def action_mtp(self, input_new_page):

        if input_new_page == "":
            print("Пустой ввод!")

        elif input_new_page in ["1", "2", "3", "4"]:
            return int(input_new_page)

        elif not input_new_page.isdigit():
            print(f"{input_new_page}: это не число!")

        return None

    def action_sc(self, user_input_category):

        if user_input_category == "":
            print("Пустой ввод!")
            return None

        if user_input_category not in ["1", "2", "3"]:
            print("Некорректный Ввод!\nПовторите ввод по новой!")
            return None

        new_category = self.categories[int(user_input_category) - 1]["key"]

        if new_category == self.selected_category:
            print("Сменяемая категория равна текущей!")
            return None

        return new_category

    def action_s(self, user_input_search):
        if user_input_search == "":
            print("Пустой ввод!")
            return None

        user_search_found = []
        flag = False

        for product in self.products:
            if user_input_search.lower() in product["name"].lower():
                user_search_found.append(product)
                flag = True

        if flag:
            self.search_history[user_input_search] = user_search_found
            for product in user_search_found:
                print(f"id: {product["id"]}. {product["name"]} - {product["price"]}$")

        else:
            self.search_history[user_input_search] = "Нет результатов!"
            print(f"Результат поиска: {user_input_search} - ничего не найдено!")

        return None

    def action_buy(self, buy_ids_input):
        if not buy_ids_input:
            print("Пустой ввод!")
            return False

        if buy_ids_input in self.basket:

            quantity_in_basket = self.basket[buy_ids_input]["quantity in basket"]

            for product in self.products:
                if product["id"] == buy_ids_input:
                    product["quantity"] -= quantity_in_basket

            del self.basket[buy_ids_input]
            print("Заказ оформлен!\nДоставка через 3 дня!")
            return True

        print("Товара нет в корзине")
        return False

    def action_itemdel(self, input_id_delite):

        if not input_id_delite:
            print("Пустой ввод!")
            return False

        if input_id_delite not in self.basket:
            print("Такого товара для удаления нету!")
            return False

        self.basket[input_id_delite]["quantity in basket"] -= 1

        if self.basket[input_id_delite]["quantity in basket"] == 0:
            del self.basket[input_id_delite]
            print("Товар удален с корзины!")

        return True

    # 6. ГЛАВНЫЙ ЦИКЛ
    def run(self):
        while True:
            if self.current_page == 1:
                self.page_1()

            elif self.current_page == 2:
                self.page_2()

            elif self.current_page == 3:
                self.page_3()

            elif self.current_page == 4:
                self.page_4()

            self.print_commands()

            action = input("\nEnter the command: ").strip().lower()

            if not self.is_valid(action):
                print("unknow commands!\n")
                continue

            if action == "atb":
                ids = input("Enter the id: ")

                if self.action_atb(ids):
                    print("Успешное добавление!")
                    self.save_data()

                else:
                    print("Ничего не добавлено!")

            elif action == "mtp":
                input_number_page = input("Enter the page number to modify:  ")

                new_page = self.action_mtp(input_number_page)

                if new_page is not None:
                    self.current_page = new_page
                    self.save_data()
                continue

            elif action == "sc":

                user_input_category = input("Smartphones: 1, Laptop: 2, Computers 3."
                                            "\nВыберите категорию по номерам: ").strip().lower()

                result_sc = self.action_sc(user_input_category)

                if result_sc:
                    self.selected_category = result_sc
                    print("Успешная смена категории!")
                    self.save_data()


            elif action == "s":

                search_query = input("\nВведите поисковой запрос: ").lower().strip()
                self.action_s(search_query)
                self.save_data()


            elif action == "buy":

                user_buy = input("Введите id товара для оформления из корзины: ").lower().strip()

                if not user_buy.isdigit():
                    print("id должен быть числом!")

                    continue

                if self.action_buy(user_buy):
                    self.save_data()

            elif action == "del":
                if len(self.search_history) == 0:
                    print("Нет истории поиска для удаления!\nРекомендуем что нибудь поискать!")

                else:
                    self.search_history.clear()
                    print("История поиска очищена!")
                    self.save_data()

            elif action == "itemdel":

                itemdel_id = input("Введите id для удаления товара: ").lower().strip()

                if not itemdel_id.isdigit():
                    print("id должен быть числом!")
                    continue

                if self.action_itemdel(itemdel_id):
                    self.save_data()

            elif action == "exit":

                print("Program termination!")
                break

        # После выхода из цикла — сохраняем
        self.save_data()
        print("Данные сохранены.")

# 7. ЗАПУСК
if __name__ == "__main__":
    shop = Marketplace()
    shop.run()
