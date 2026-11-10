from abc import ABC, abstractmethod



class SmartDevice(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):

    def turn_on(self):
        print(f"{self.name}: The light is now ON.")


class SmartFan(SmartDevice):

    def turn_on(self):
        print(f"{self.name}: The fan is now spinning.")



class SmartSpeaker(SmartDevice):

    def turn_on(self):
        print(f"{self.name}: The speaker is now playing music.")


def main():
    print("Smart Device Command Center")
    print("---------------------------")

    devices = [
        SmartLight("Living Room Light"),
        SmartFan("Bedroom Fan"),
        SmartSpeaker("Kitchen Speaker")
    ]

    
    for device in devices:
        device.turn_on()


if __name__ == "__main__":
    main()