class PersonalInfo:
    def __init__(self, name, id, phone, email) -> None:
        self.name = name
        self.id = id
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f'Name: {self.name}\nID: {self.id}\nPhone Number: {self.phone}\nEmail Address: {self.email}'
