class Thing:

    def __init__(self, name: str):
        self.name = name

    def return_hello_name(self) -> str:
        return "Hello " + self.name + "!"
