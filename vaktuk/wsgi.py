from pyramid.config import Configurator

from .extensibility import include_me
from .resources import Resource

def main(global_config, **settings):
    """ Application entry point.

    The application entry point. Provides a WSGI application that represents
    our a basic pyramid application which uses Vaktuk. Usually, you will want to
    create your own application and do something akin to what this function does
    in order to use the CMS - but also extend it with your own functionality.

    """

    config = Configurator(settings=settings, root_factory=Resource.factory)

    include_me(config)

    return config.make_wsgi_app()
