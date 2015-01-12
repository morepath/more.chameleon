from more.chameleon import ChameleonApp


class App(ChameleonApp):
    pass


@App.path(path='persons/{name}')
class Person(object):
    def __init__(self, name):
        self.name = name


@App.template_directory()
def get_template_dir():
    return 'templates'


@App.html(model=Person, template='person_macro.pt')
def person_default(self, request):
    return {'name': self.name}
