import morepath
import chameleon
import os


class ChameleonApp(morepath.App):
    pass


def is_morepath_template_auto_reload():
    """ Returns True if auto reloading should be enabled. """
    auto_reload = os.environ.get('MOREPATH_TEMPLATE_AUTO_RELOAD', '')

    return auto_reload.lower() in {'1', 'yes', 'true', 'on'}


@ChameleonApp.template_loader(extension='.pt')
def get_template_loader(template_directories, settings):

    # the settings might not exist or they may be empty
    if hasattr(settings, 'chameleon'):
        settings = settings.chameleon.__dict__.copy()
    else:
        settings = {}

    # the morepath reload environment variable always takes precedence
    settings['auto_reload'] = is_morepath_template_auto_reload()

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
