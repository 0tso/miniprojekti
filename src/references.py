from time import sleep
# ainostaan book toimii. haluammeko kodakoodata bookform-metodin niin kuin on tehty alhaalla,
# eli mitkä fieldit on pakollisia jne
# (vai halutaanko me hakea tämä tieto jostain tiedostosta esim mitkä fieldit
# paikollisia dokumenttilähteille, mitkä kirjoille).


class References:
    def __init__(self, io_handler, service):
        self.io_handler = io_handler
        self.service = service
        self.welcome(io_handler, service)

    def welcome(self, io_handler, service):
        io_handler.write("Welcome to MyReferences!")
        # sleep(1)
        io_handler.write("Type 0 for Add a reference")
        # sleep(1)
        io_handler.write("Type 1 for View my references")
        # sleep(1)
        io_handler.write("Type 2 to Exit")
        # sleep(1)
        command = io_handler.read("What do you want to do? ")
        if command == "0":
            self.add(io_handler, service)
            self.welcome(io_handler, service)
        elif command == "1":
            #io_handler.write("Not finished, directing you back to the start")
            for entry in self.service.get_all_books():
                io_handler.write(entry)
            sleep(2)
            self.welcome(io_handler, service)
        elif command == "2":
            io_handler.write("Exiting...")
            sleep(1)
            return
        else:
            io_handler.write("Invalid input. Please enter '0', '1' or '2'.")
            sleep(2)
            self.welcome(io_handler, service)

    def add(self, io_handler, service):
        # sleep(1)
        io_handler.write("What type of reference?")
        # sleep(1)
        io_handler.write("Type A to Add a book")
        # sleep(1)
        io_handler.write("Type B to Add an article")
        # sleep(1)
        io_handler.write("Type C to Add inproceedings")
        # sleep(1)
        io_handler.write("Type Q to Return")
        # sleep(1)
        while True:
            command = io_handler.read("Input: ")
            if command in ["A", "B", "C"]:
                self.form(service, command)
                break
            if command == "Q":
                break

            io_handler.write("Invalid input.")

    def ask_for_input(self, prompt, optional=False, input_type=str):
        while True:
            prefix = "(Optional) " if optional else ""
            user_input = self.io_handler.read(prefix + prompt + ": ")
            if not user_input and not optional:
                self.io_handler.write(
                    "Field cannot be empty. Please provide a valid input.")
            elif user_input and input_type:
                try:
                    return {prompt: input_type(user_input)}
                except ValueError:
                    self.io_handler.write("Please enter a valid interger.")
            else:

                return {prompt: user_input}




    def ask_for_multiple_inputs(self, prompt):
        items = []
        first_item = self.ask_for_input(prompt)[prompt]
        items.append(first_item)

        while True:
            more_items = self.io_handler.read(
                f"Next {prompt}? Press enter to skip ")
            if more_items:
                items.append(more_items)
            else:
                break

        return {prompt: items}

    @staticmethod
    def get_form_data(ref_type):
        if ref_type == "A":
            form = {
                "mandatory": [("key", str, False), ("title", str, False),
                              ("author", str, True), ("publisher", str, False),
                              ("year", int, False)],
                "optional": [("volume", int, False), ("number", int, False),
                             ("pages", str, False), ("month", int, False),
                             ("notes", str, False)]
            }

        elif ref_type == "B":
            form = {
                "mandatory": [("key", str, False), ("title", str, False),
                              ("author", str, True), ("journal", str, False),
                              ("year", int, False)],
                "optional": [("volume", int, False), ("number", int, False),
                             ("pages", str, False), ("month", int, False),
                             ("notes", str, False)]
            }

        elif ref_type == "C":
            form = {
                "mandatory": [("key", str, False), ("title", str, False),
                              ("booktitle", str, False),
                              ("author", str, True),
                              ("year", int, False)],
                "optional": [("volume", int, False), ("number", int, False),
                             ("series", str, False), ("pages",
                                                      str, False), ("address", str, False),
                             ("month", int, False),
                             ("organization", str, False), ("publisher", str, False),
                             ("notes", str, False)]
            }
        else:
            raise NotImplementedError

        return form

    def form(self, service, ref_type):

        form = self.get_form_data(ref_type)

        ref_items = {}
        for item in form["mandatory"]:
            if item[2]:
                user_input = self.ask_for_multiple_inputs(item[0])
            else:
                user_input = self.ask_for_input(item[0], False, item[1])
            ref_items.update(user_input)

        for item in form["optional"]:
            if item[2]:
                user_input = self.ask_for_multiple_inputs(item[0])
            else:
                user_input = self.ask_for_input(item[0], True, item[1])
            ref_items.update(user_input)

        if ref_type == "A":
            service.config_book_reference(**ref_items)
        elif ref_type == "B":
            service.config_article_reference(**ref_items)
        elif ref_type == "C":
            service.config_inpro_reference(**ref_items)
        else:
            raise NotImplementedError

        self.io_handler.write("New reference added!")

        sleep(2)
