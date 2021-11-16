import json
import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def meow(self):
        print("Meow!")


# j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

c = Cat("Charles", "Tabby")
# json
j = json.dumps(c.__dict__)
print(j)

# jsonpickle
frozen = jsonpickle.encode(c)
print(frozen)

# save jsonpickle to file
with open("cat.json", "w") as file:
    frozen = jsonpickle.encode(c)
    file.write(frozen)

# read jsonpickle from file
with open("cat.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    # we can use class Cat methods
    unfrozen.meow()
