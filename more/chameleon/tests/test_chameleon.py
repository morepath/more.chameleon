import morepath
import more.chameleon
from webtest import TestApp as Client
from .fixtures import (
    template, template_macro, override_template, override_template_loader)


def setup_module(module):
    morepath.disable_implicit()


def test_template():
    config = morepath.setup()
    config.scan(more.chameleon, ignore=['.tests'])
    config.scan(template)
    config.commit()
    c = Client(template.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>'''


def test_template_macro():
    config = morepath.setup()
    config.scan(more.chameleon, ignore=['.tests'])
    config.scan(template_macro)
    config.commit()
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
    config = morepath.setup()
    config.scan(more.chameleon, ignore=['.tests'])
    config.scan(override_template)
    config.commit()
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
    config = morepath.setup()
    config.scan(more.chameleon, ignore=['.tests'])
    config.scan(override_template_loader)
    config.commit()
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
