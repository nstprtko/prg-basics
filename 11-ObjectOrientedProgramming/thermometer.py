
class Thermometer:
    def __init__(self):
        self.is_on = False
    
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print('The thermometer is on')

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print('The thermometer is off')

    def measure(self, temperature):
        self.temperature = temperature
        if 37 <= self.temperature <= 41:
            print(f'Your temperature is {self.temperature}.(fever)')
        elif 41<= self.temperature <= 42:
            print(f'Your temeperature is {self.temperature}.(critical temperature)')
        else:
            print('Invalid')

    
    