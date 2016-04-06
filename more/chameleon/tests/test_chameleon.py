import morepath
import more.chameleon
import os
from more.chameleon.main import is_morepath_template_auto_reload
from webtest import TestApp as Client
from .fixtures import (
    template, template_macro, override_template, override_template_loader)


def setup_module(module):
    morepath.disable_implicit()


def test_is_morepath_template_auto_reload():
    os.environ['MOREPATH_TEMPLATE_AUTO_RELOAD'] = ''
    assert not is_morepath_template_auto_reload()

    os.environ['MOREPATH_TEMPLATE_AUTO_RELOAD'] = 'False'
    assert not is_morepath_template_auto_reload()

    os.environ['MOREPATH_TEMPLATE_AUTO_RELOAD'] = 'FALSE'
    assert not is_morepath_template_auto_reload()

    os.environ['MOREPATH_TEMPLATE_AUTO_RELOAD'] = '0'
    assert not is_morepath_template_auto_reload()

    os.environ['MOREPATH_TEMPLATE_AUTO_RELOAD'] = '1'
    assert is_morepath_template_auto_reload()

    os.environ['MOREPATH_TEMPLATE_AUTO_RELOAD'] = 'on'
    assert is_morepath_template_auto_reload()

    os.environ['MOREPATH_TEMPLATE_AUTO_RELOAD'] = 'yes'
    assert is_morepath_template_auto_reload()

    os.environ['MOREPATH_TEMPLATE_AUTO_RELOAD'] = 'True'
    assert is_morepath_template_auto_reload()


def test_template():

    morepath.scan(more.chameleon, ignore=['.tests'])
    morepath.scan(template)
    morepath.commit(template.App)
    c = Client(template.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>'''


def test_template_macro():

    morepath.scan(more.chameleon, ignore=['.tests'])
    morepath.scan(template_macro)
    morepath.commit(template_macro.App)
    c = Client(template_macro.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<head>
</head>
<body>
<div id="content">
<p>Hello world!</p>
</div>
</body>
</html>
'''


def test_override_template():
    morepath.scan(more.chameleon, ignore=['.tests'])
    morepath.scan(override_template)
    morepath.commit(override_template.App, override_template.SubApp)
    c = Client(override_template.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>'''

    c = Client(override_template.SubApp())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<div>Hi world!</div>
</body>
</html>'''


def test_override_template_loader():
    morepath.scan(more.chameleon, ignore=['.tests'])
    morepath.scan(override_template_loader)
    morepath.commit(
        override_template_loader.App,
        override_template_loader.SubApp
    )
    c = Client(override_template_loader.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<head>
</head>
<body>
<div id="content">
<p>Hello world!</p>
</div>
</body>
</html>
'''

    c = Client(override_template_loader.SubApp())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<head>
</head>
<body>
<div id="content2">
<p>Hello world!</p>
</div>
</body>
</html>
'''
