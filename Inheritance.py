from ClassExamp import Employees


class Manager(Employees):

    def __init__(self, tecrube):
        # üst sınıfın init fonksiyounun kullanmak istersek, super func çağırabiliriz.
        super().__init__()
        self.tecrube = tecrube

    def calis(self):
        super().calis()


new_manager = Manager(10)
new_manager.calis()
