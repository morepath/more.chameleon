more.chameleon: Chameleon template integration for Morepath
===========================================================

``more.chameleon`` is an extension for Morepath_ that adds
Zope Page Template (ZPT) support for the ``.pt`` extension, using
the Chameleon_ template engine.

Example usage::

  from more.chameleon import ChameleonApp

  class App(ChameleonApp):
      pass

  @App.path(path='persons/{name}')
  class Person(object):
       def __init__(self, name):
           self.name = name

  @App.html(model=Person, template='person.pt')
  def person_default(self, request):
      return {'name': self.name}

and then in ``person.pt`` (in the same directory as the module)::

  <html>
  <body>
  <p>Hello ${name}!</p>
  </body>
  </html>

.. _Morepath: http://morepath.readthedocs.org

.. _Chameleon: https://chameleon.readthedocs.org/
