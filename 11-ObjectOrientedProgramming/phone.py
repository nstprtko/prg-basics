class Phone():
    # creating states - constant attributes
    def __init__(self, model, year, blocking, battery):
        self.model = model
        self.year = year 
        self.blocking = blocking
        self.battery = battery

    def blocked(self):
        if self.blocking == True:
            print(f'{self.model} is blocked')

    def unblocked(self):
        if self.blocking == False:
            print(f'{self.model} is unblocked')

    def call(self, number):
        if self.blocking == True :
            print(f'{self.model} cant make calls when blocked')

        else:
            print(f'{self.model} is calling {number}')


    def message(self, number):
        if self.blocking == True :
            print(f'{self.model} cant text messages when blocked')

        else:
            print(f'{self.model} is texting {number}')
     
    def check_battery(self):
        print(f'the battery level is {self.battery}')


    
def main():
    my_phone = Phone("Iphone", 2021, True, 76)
    
    my_phone.check_battery()
    my_phone.call('000-999-111')
    my_phone.message('888-999')


if __name__ == '__main__':
    main()