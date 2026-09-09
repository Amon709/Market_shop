import json
from data import products_list, categories

# def print_action():
#     return print("Введите действия: ")

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
        return self.page_commands.get(self.current_page, [])# не понял функцию понял то что он берет
        # команды из класса и находит текущую страницу и печатает текущие команды под нужный page ?

    def print_commands(self):
        return print("\nEnter the command:", ", ".join(self.get_commands()))# вводят команду из нужных по текущей
        # странице и печатает обяденив нужыне команды из get_command ?

    def is_valid(self, action):# проверка команды валидная ли она или нет и выдавание результата
        return action in self.get_commands()

     # --------------------- this is end validations commands --------------------------


    # ------------------ this is json saving programs data -----------------------------
    # 2. СОХРАНЕНИЕ В JSON
    def save_data(self):
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
        print("Главная страница.")
        top_items_products = [top_5 for top_5 in self.products if top_5["is_top"]]
        top_five_items = top_items_products[:5]
        for product in top_five_items:
            print(f"id. {product['id']}, categories: {product['category']}, price: {product['price']} - {product['quantity']} pcs.")
        # ... твой код page_1, только products_list → self.products

    def page_2(self):
        pass

    def page_3(self):
        pass

    def page_4(self):
        pass
    #--------------------------------- this is end page blog ----------------------------

    # 5. ДЕЙСТВИЯ (переносишь свои action_*)
    # ------------------------- this is start user actions commands -----------------------
    def action_atb(self, user_input):
        #
        # ... твой код action_atb, basket → self.basket, products_list → self.products
        pass

    def action_mtp(self, user_input):
        pass

    def action_sc(self, user_input):
        pass

    def action_s(self, user_input):
        pass

    def action_buy(self, user_input):
        pass

    def action_del(self, user_input):
        pass

    def action_itemdel(self, user_input):
        pass

    # 6. ГЛАВНЫЙ ЦИКЛ
    def run(self):
        while True:
            if self.current_page == 1:
                self.page_1()
                self.print_commands()

            action = input("\nEnter the command: ").strip().lower()

            if not self.is_valid(action):
                print("unknow commands!\n")
                continue

            if action == "atb":
                ids = input("Enter the id: ")

                self.action_atb(ids)

            if action == "mtp":
                input_number_page = input("Enter the page number to modify:  ")

                self.action_mtp(input_number_page)
                pass

            if action == "sc":
                pass
            if action == "s":
                pass

            if action == "buy":
                pass

            if action == "del":
                pass

            if action == "itemdel":
                pass

            if action == "exit":

                print("Program termination!")
                break

        # После выхода из цикла — сохраняем
        self.save_data()
        print("Данные сохранены.")

# 7. ЗАПУСК
if __name__ == "__main__":
    shop = Marketplace()
    shop.run()