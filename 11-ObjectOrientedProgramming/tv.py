class Tv:
    def __init__(self, channel_no = 1, volume = 0):
        self.is_on = False
        self.channel_no = channel_no
        self.channels = []
        self.volume = volume
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print('The TV is off')

    def turn_onn(self):
        if not self.is_on:
            self.is_on = True
            print(f'The TV is on, channel {self.channel_no}')
            

    def set_channels(self, channels_list):
        self.channels = channels_list
        print('channels have been set')
        
    def show_channels(self):
        if not self.channels:
            print('nothing to show')
        else:
            print('List:')
            for i, channel in enumerate(self.channels, start=1):
                print(f'{i}. {channel}')

    def change_channel(self, channel_no):
        if 1<= channel_no <= len(self.channels):
            self.channel_no = channel_no
            print(f'channel is {self.channel_no}')
        else:
            print('unavailable')

    def show_status(self):
        if not self.is_on:
            status = 'ON'
            if 1<= self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no - 1]

                print(f'{status}. channel {self.channel_no}. {channel_name}')
                print(f'volume is now {self.volume}')
        else:
            status = 'OFF'
        print(f'TV is {status}')

    def volume_increase(self):
        if 0<= self.volume <= 10:
            self.volume +=1
            print(f'volume is now {self.volume}')
        else:
            print('max volume is reached')

    def volume_decrease(self):
        if 0<= self.volume <= 10:
            self.volume -=1
            print(f'volime is now {self.volume}')
        else:
            print('min volume is reached ')


    