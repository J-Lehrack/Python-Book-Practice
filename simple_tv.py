# A simple simulated tv, where you can surf channels
# look up a specific channel, change the volume, or turn off the tv

class Television(object):
    def __init__(self, name, channel=1, volume=1):
        self.name = name
        self.channel = channel
        self.volume = volume

    def channel_up(self):
        self.channel += 1
        if self.channel > 500:
            self.channel = 1

    def channel_down(self):
        self.channel -= 1
        if self.channel < 1:
            self.channel = 500

    def channel_search(self, channel):
        self.channel = channel
        if 1 <= self.channel <= 500:
            self.channel = channel
        elif self.channel < 1:
            self.channel = 500
        elif self.channel > 500:
            self.channel = 1
        else:
            print("That is not a valid input")

    def volume_up(self):
        self.volume += 1
        if self.volume > 100:
            self.volume = 100

    def volume_down(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0


def main():
    tv_name = input("What is your name?: ")
    print("Hello", tv_name)
    tv = Television(tv_name)

    choice = None
    while choice != "0":
        print(
            """
            Your TV (Current Subscription: 500 Channels)
            
            0 - Shut Off
            1 - Channel Up
            2 - Channel Down
            3 - Channel Search
            4 - Volume Up
            5 - Volume Down
            """)

        choice = input("Choice: ")
        print()

        # Exit program
        if choice == "0":
            print("Shutting Off")

        elif choice == "1":
            tv.channel_up()
            print("Ch", tv.channel)

        elif choice == "2":
            tv.channel_down()
            print("Ch", tv.channel)

        elif choice == "3":
            channel = int(input("What channel would you like?: "))
            tv.channel_search(channel)
            print("Ch", tv.channel)

        elif choice == "4":
            tv.volume_up()
            print("Vol", tv.volume)

        elif choice == "5":
            tv.volume_down()
            print("Vol", tv.volume)

        else:
            print("\n Sorry, but", choice, "is not a valid choice.")


main()
input("\nPress any key to exit the program")
