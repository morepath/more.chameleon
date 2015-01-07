from more.chameleon import ChameleonApp


class App(ChameleonApp):
    pass


@App.path(path='persons/{name}')
class Person(object):
    def __init__(self, name):
        self.name = name


@App.html(model=Person, template='templates/person2.pt')
def person_default(self, request):
    return {'name': self.name}
