def God():
    return [Man('Adam'), Woman('Eva')]


class Human:
    def __init__(self, human):
        self.human = human


class Man(Human):
    pass


class Woman(Human):
    pass


paradise = God()
print([person.human for person in paradise])