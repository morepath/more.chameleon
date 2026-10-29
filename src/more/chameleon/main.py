from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any

import chameleon
import morepath

if TYPE_CHECKING:
    from collections.abc import Sequence

    from webob import Response as BaseResponse

    from morepath import Request
    from morepath.settings import SettingRegistry
    from morepath.types import Render


class ChameleonApp(morepath.App):
    pass


def is_morepath_template_auto_reload() -> bool:
    """Returns True if auto reloading should be enabled."""
    auto_reload = os.environ.get("MOREPATH_TEMPLATE_AUTO_RELOAD", "")

    return auto_reload.lower() in {"1", "yes", "true", "on"}


@ChameleonApp.template_loader(extension=".pt")
def get_template_loader(
    template_directories: str | Sequence[str],
    settings: SettingRegistry,
) -> chameleon.PageTemplateLoader:
    # the settings might not exist or they may be empty
    config: dict[str, Any] = {}
    if hasattr(settings, "chameleon"):
        config = settings.chameleon.__dict__.copy()

    # the morepath reload environment variable always takes precedence
    config.update({"autoescape": is_morepath_template_auto_reload()})

    # we control the search_path entirely by what we pass here as
    # template_directories, so we never want the template itself
    # to prepend its own path
    config.update({"prepend_relative_search_path": False})

    return chameleon.PageTemplateLoader(
        template_directories, default_extension=".pt", **config
    )


@ChameleonApp.template_render(extension=".pt")
def get_chameleon_render(
    loader: chameleon.PageTemplateLoader, name: str, original_render: Render
) -> Render:
    template = loader.load(name, "xml")

    def render(content: Any, request: Request[ChameleonApp]) -> BaseResponse:
        variables: dict[str, Any] = {"request": request}
        variables.update(content)
        return original_render(template.render(**variables), request)

    return render
