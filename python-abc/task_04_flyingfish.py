class fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(bird, fish):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives in both water and sky!")


flying_fish = FlyingFish()
flying_fish.fly()
flying_fish.swim()
flying_fish.habitat()
print(Flying_Fish.mro())
