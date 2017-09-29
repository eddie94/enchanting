class weapon():
    def __init__(self):
        self.atk = 0
        self.cri = 0
        self.name = ''

    def dmg(self):
        return self.atk * self.cri

    def set_resource(self):
        self.atk = int(input('atk??'))
        self.cri = int(input('cri??'))
        self.name = input('name??')

class bow1(weapon):

    def __init__(self):
        # self.atk = 10
        # self.cri = 10
        # self.name = 'bow1'
        self.element = 'something'

    def set_resource(self):
        self.atk = int(input('atk??'))
        self.cri = int(input('cri??'))
        self.name = input('name??')
        self.element = input('element??')

class bow2(weapon):

    def __init__(self):
        # self.atk = 20
        # self.cri = 20
        # self.name = 'bow2'
        self.element = 'anything'

    def set_resource(self):
        self.atk = int(input('atk??'))
        self.cri = int(input('cri??'))
        self.name = input('name??')
        self.element = input('element??')

a=bow1()
b=bow2()

a.set_resource()
b.set_resource()

c = b.dmg()
print(c)