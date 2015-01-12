import morepath
import chameleon


class ChameleonApp(morepath.App):
    pass


@ChameleonApp.setting_section(section='chameleon')
def get_setting_section():
    return {'auto_reload': False}


@ChameleonApp.template_loader(extension='.pt')
def get_template_loader(template_directories, settings):
    settings = settings.chameleon.__dict__.copy()
    # we control the search_path entirely by what we pass here as
    # template_directories, so we never want the template itself
    # to prepend its own path
    settings['prepend_relative_search_path'] = False
    return chameleon.PageTemplateLoader(
        template_directories,
        default_extension='.pt',
        **settings)


@ChameleonApp.template_render(extension='.pt')
def get_chameleon_render(loader, name, original_render):
    template = loader.load(name, 'xml')

    def render(content, request):
        variables = {'request': request}
        variables.update(content)
        return original_render(template.render(**variables), request)
    return render
