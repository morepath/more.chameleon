from __future__ import annotations

from typing import TYPE_CHECKING, Any

from more.chameleon import ChameleonApp

if TYPE_CHECKING:
    from morepath import Request


class App(ChameleonApp):
    pass


@App.path(path="persons/{name}")
class Person:
    def __init__(self, name: str) -> None:
        self.name = name


@App.template_directory()
def get_template_dir() -> str:
    return "templates"


@App.html(model=Person, template="person_settings.pt")
def person_default(self: Person, request: Request[App]) -> dict[str, Any]:
    return {"name": self.name, "active": True}


class SettingsApp(App):
    pass


@SettingsApp.setting_section(section="chameleon")
def get_setting_section() -> dict[str, Any]:
    return {"boolean_attributes": {"active"}}
