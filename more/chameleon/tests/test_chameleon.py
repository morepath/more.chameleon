import morepath
import more.chameleon
from webtest import TestApp as Client
import pytest
from .fixtures import template, template_macro, explicit_template


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


def test_explicit_template():
    config = morepath.setup()
    config.scan(more.chameleon, ignore=['.tests'])
    config.scan(explicit_template)
    config.commit()
    c = Client(explicit_template.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>'''

    response = c.get('/persons/world?two=other')
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


