import os
import morepath
import chameleon


class ChameleonApp(morepath.App):
    pass


@ChameleonApp.setting_section(section='chameleon')
def get_setting_section():
    return {'auto_reload': False}


def get_loader(registry, search_path):
    result = getattr(registry, 'chameleon_loader', None)
    if result is not None:
        return result
    result = registry.chameleon_loader = chameleon.PageTemplateLoader(
        search_path, **registry.settings.chameleon.__dict__)
    return result


@ChameleonApp.template_engine(extension='.pt')
def get_chameleon_render(name, original_render, registry, search_path):
    config = registry.settings.chameleon.__dict__
    loader = get_loader(registry, search_path)
    fullpath = os.path.join(search_path, name)
    def render(content, request):
        path = morepath.template_path(name, request, lookup=request.lookup)
        if path is None:
            path = fullpath
        template = loader.load(path, 'xml')
        variables = {'request': request}
        variables.update(content)
        return original_render(template.render(**variables), request)
    return render
