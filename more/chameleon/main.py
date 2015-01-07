import os
import morepath
import chameleon


class ChameleonApp(morepath.App):
    pass


@ChameleonApp.setting_section(section='chameleon')
def get_setting_section():
    return {'auto_reload': False}


@ChameleonApp.template_engine(extension='.pt')
def get_chameleon_render(name, original_render, registry, search_path):
    config = registry.settings.chameleon.__dict__
    template = chameleon.PageTemplateFile(os.path.join(search_path, name),
                                          **config)
    def render(content, request):
        variables = {'request': request}
        variables.update(content)
        return original_render(template.render(**variables), request)
    return render
