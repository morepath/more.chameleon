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


@App.html(model=Person, template="person.pt")
def person_default(self: Person, request: Request) -> dict[str, Any]:
    return {"name": self.name}
