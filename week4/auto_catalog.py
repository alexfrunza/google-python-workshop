class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.color = None

    def paint(self, color: str):
        self.color = color

    def show_color(self) -> str:
        return self.color

    def __str__(self):
        if self.color is not None:
            return f'{self.brand} {self.model} - {self.color}'

        return f'{self.brand} {self.model}'


class WarmCar(Car):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
        self.seat_warmer = None

    def tune(self, seat_warmer: bool):
        self.seat_warmer = seat_warmer

    def __str__(self):
        output = f"Brand: {self.brand}\nModel: {self.model}"

        if self.color is not None:
            output += f"\nColor: {self.color}"

        if self.seat_warmer is not None:
            output += f"\nSeat warmer: {self.seat_warmer}"

        return output


class BrightCar(Car):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
        self.led_optic_blocks = None

    def tune(self, led_optic_blocks: bool):
        self.led_optic_blocks = led_optic_blocks

    def __str__(self):
        output = f"Brand: {self.brand}\nModel: {self.model}"

        if self.color is not None:
            output += f"\nColor: {self.color}"

        if self.led_optic_blocks is not None:
            output += f"\nLed optic blocks: {self.led_optic_blocks}"

        return output


# Tests

# Instantiate the objects
car1 = WarmCar("Aro", "M461")
car1.tune(False)
car1.paint("Red")

car2 = BrightCar("Dacia", "1310")
car2.tune(False)
car2.paint("Black")

# Show the data
print(car1)
print()
print(car2)
