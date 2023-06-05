from Animals import Fish, Mammal, Bird

class Fabric:
    def _build(self, type):
        types = {"Fish": Fish, "Mammal": Mammal, "Bird": Bird}
        return types[type]

    def make_animal(self, type, *args, **kwargs):
        new_animal = self._build(type)
        return new_animal(*args, **kwargs)

if __name__ == '__main__':
    fabric = Fabric()
    fish_from_fabric = fabric.make_animal("Fish", "Dory", 5, 'blue')
    print(f'Name:{fish_from_fabric.get_name()},', f'Age:{fish_from_fabric.get_age()},', f'Specific:{fish_from_fabric.get_specific()}')