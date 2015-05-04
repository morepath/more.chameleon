more.chameleon: Chameleon template integration for Morepath
===========================================================

``more.chameleon`` is an extension for Morepath_ that adds Zope Page
Template (ZPT) support for the ``.pt`` extension, using the Chameleon_
template engine.

For details on the ZPT template language see the `Chameleon language
reference`_.

Example usage::

  from more.chameleon import ChameleonApp

  class App(ChameleonApp):
      pass

  @App.path(path='persons/{name}')
  class Person(object):
       def __init__(self, name):
           self.name = name

  @App.template_directory()
  def get_template_directory():
      return 'templates'

  @App.html(model=Person, template='person.pt')
  def person_default(self, request):
      return {'name': self.name}

and then in ``person.pt`` (in the ``templates`` subdirectory)::

  <html>
  <body>
  <p>Hello ${name}!</p>
  </body>
  </html>

During development it can be helpful to have Chameleon reload templates
automatically after a change. To enable this feature use the
``MOREPATH_TEMPLATE_AUTO_RELOAD`` environment variable.

You can enable it for your process::

  MOREPATH_TEMPLATE_AUTO_RELOAD=1 python run.py

Or for your shell::

  export MOREPATH_TEMPLATE_AUTO_RELOAD=1
  python run.py

To further control Chameleon rendering you can define a ``chameleon`` setting
section in your app. For instance, here is how you turn on Chameleon's
``debug`` functionality::

  @App.setting_section(section='chameleon')
  def get_setting_section():
      return {'debug': True}

For details on Chameleon configuration options, consult the
configuration keyword arguments in the `Chameleon API reference`_.

.. _Morepath: http://morepath.readthedocs.org

.. _Chameleon: https://chameleon.readthedocs.org/

.. _`Chameleon language reference`: https://chameleon.readthedocs.org/en/latest/reference.html

.. _`Chameleon API reference`: https://chameleon.readthedocs.org/en/latest/library.html#api-reference
