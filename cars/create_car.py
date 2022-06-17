class Car:
    def __init__(self, title, model, color):
        self.title = title
        self.model = model
        self.color = color

    def start_engine(self):
        print(f"{self.title} {self.model} engine started!")

    def stop_engine(self):
        print(f"\n{self.title} {self.model} engine stop!")



#     def car_info(self):
#         pass
#
#
# car1 = Car("Bugatti", "Chiron Super Sport")
# car1.start_engine()
# car1.stop_engine()
