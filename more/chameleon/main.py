import morepath
import chameleon


class ChameleonApp(morepath.App):
    pass


@ChameleonApp.setting_section(section='chameleon')
def get_setting_section():
    return {
        'auto_reload': False
    }


@ChameleonApp.template_engine(extension='.pt')
def get_chameleon_render(path, original_render, settings):
    config = {'auto_reload': settings.chameleon.auto_reload}
    template = chameleon.PageTemplateFile(path, **config)
    def render(content, request):
        variables = {'request': request}
        variables.update(content)
        return original_render(template.render(**variables), request)
    return render
