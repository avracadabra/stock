"""Blok declaration example
"""
from anyblok.blok import Blok


class Awb_http(Blok):
    """Awb_http's Blok class definition
    """

    version = "0.1.0"
    author = "Pierre Verkest"
    required = ["anyblok-core", "wms-core", "wms-inventory"]

    @classmethod
    def import_declaration_module(cls):
        """Python module to import in the given order at start-up
        """
        # from . import model  # noqa

    @classmethod
    def reload_declaration_module(cls, reload):
        """Python module to import while reloading server (ie when
        adding Blok at runtime
        """
        # from . import model  # noqa

        # reload(model)

    @classmethod
    def pyramid_load_config(cls, config):
        config.add_route("container_list", "/api/wms/containers")
        config.add_route("container_type", "/api/wms/container/type/{id}")
        config.scan(cls.__module__ + ".views")

    def update(self, latest):
        """Update blok"""
        # if we install this blok in the database we add a new record
        # if not latest:
        #     self.registry.Example.insert(name="An example")
