class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_recipt(self):
        print(f'rate per km : {self.rate_per_km}')
        print(f'distance is {self.distance}')
        print(f'fare is {self.fare}')

def main():
    # your program
    ride1 = TaxiRide(rate_per_km=2)
    ride1.calculate_fare(distance=10)
    ride1.print_recipt()

    ride2 = TaxiRide(rate_per_km= 3)
    ride2.calculate_fare(distance=20)
    ride2.print_recipt()

if __name__ == "__main__":
    main()
