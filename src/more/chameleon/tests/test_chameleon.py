import os

from webtest import TestApp as Client

from more.chameleon.main import is_morepath_template_auto_reload

from .fixtures import (
    override_template,
    override_template_loader,
    template,
    template_macro,
    template_settings,
)


def test_is_morepath_template_auto_reload() -> None:
    os.environ["MOREPATH_TEMPLATE_AUTO_RELOAD"] = ""
    assert not is_morepath_template_auto_reload()

    os.environ["MOREPATH_TEMPLATE_AUTO_RELOAD"] = "False"
    assert not is_morepath_template_auto_reload()

    os.environ["MOREPATH_TEMPLATE_AUTO_RELOAD"] = "FALSE"
    assert not is_morepath_template_auto_reload()

    os.environ["MOREPATH_TEMPLATE_AUTO_RELOAD"] = "0"
    assert not is_morepath_template_auto_reload()

    os.environ["MOREPATH_TEMPLATE_AUTO_RELOAD"] = "1"
    assert is_morepath_template_auto_reload()

    os.environ["MOREPATH_TEMPLATE_AUTO_RELOAD"] = "on"
    assert is_morepath_template_auto_reload()

    os.environ["MOREPATH_TEMPLATE_AUTO_RELOAD"] = "yes"
    assert is_morepath_template_auto_reload()

    os.environ["MOREPATH_TEMPLATE_AUTO_RELOAD"] = "True"
    assert is_morepath_template_auto_reload()


def test_template() -> None:

    c = Client(template.App())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<body>
<p>Hello world!</p>
</body>
</html>"""
    )


def test_template_macro() -> None:

    c = Client(template_macro.App())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<head>
</head>
<body>
<div id="content">
<p>Hello world!</p>
</div>
</body>
</html>
"""
    )


def test_template_settings() -> None:
    # without a ``chameleon`` settings section Chameleon uses its defaults
    c = Client(template_settings.App())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<body>
<p active="True">Hello world!</p>
</body>
</html>"""
    )

    # settings from the ``chameleon`` section are passed on to Chameleon
    c = Client(template_settings.SettingsApp())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<body>
<p active="active">Hello world!</p>
</body>
</html>"""
    )


def test_override_template() -> None:
    c = Client(override_template.App())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<body>
<p>Hello world!</p>
</body>
</html>"""
    )

    c = Client(override_template.SubApp())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<body>
<div>Hi world!</div>
</body>
</html>"""
    )


def test_override_template_loader() -> None:
    c = Client(override_template_loader.App())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<head>
</head>
<body>
<div id="content">
<p>Hello world!</p>
</div>
</body>
</html>
"""
    )

    c = Client(override_template_loader.SubApp())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<head>
</head>
<body>
<div id="content2">
<p>Hello world!</p>
</div>
</body>
</html>
"""
    )
