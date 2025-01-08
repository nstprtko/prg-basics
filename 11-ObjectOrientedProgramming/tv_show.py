from tv import Tv

def main():
    my_tv = Tv(3)
    my_tv.show_status()
    my_tv.turn_onn()
    my_tv.show_status()
    my_tv.turn_off()
    my_tv.show_status()
    my_tv.show_channels()

    channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
    my_tv.set_channels(channels)
    my_tv.show_channels()
    my_tv.change_channel(4)
    my_tv.show_status()
    my_tv.change_channel(5)
    my_tv.show_status()
    my_tv.change_channel(9)
    my_tv.show_status()
    my_tv.volume_increase()
    my_tv.volume_increase()
    my_tv.volume_decrease()
    my_tv.show_status
    my_tv.turn_off()


if __name__ =='__main__':
    main()