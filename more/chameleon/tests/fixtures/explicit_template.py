from more.chameleon import ChameleonApp


class App(ChameleonApp):
    pass


@App.path(path='persons/{name}')
class Person(object):
    def __init__(self, name):
        self.name = name


@App.template_path('templates/person.pt')
def get_template_path(request):
    if request.GET.get('two') is not None:
        return 'templates/person2.pt'
    return 'templates/person.pt'


@App.html(model=Person, template='templates/person.pt')
def person_default(self, request):
    return {'name': self.name}
