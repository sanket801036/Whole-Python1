class mobile:
    def __init__(self, company, model, ram, storages):
        self.company = company
        self.model = model
        self.ram = ram
        self.storages = storages

    def details_mobile(self):
        print("""
        
                Company_name: {self.company}
                mode_no: {self.model}
                ram_no: {self.ram}
                storages_mo: {self.storages}

                """)

e = mobile("apple", "s11", 8, 128)
e.details_mobile()