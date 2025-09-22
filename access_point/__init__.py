from __future__ import annotations

import importlib
import logging

_LOGGER = logging.getLogger(__name__)


def _odoo_runtime_available() -> bool:
    required_modules = ("odoo", "odoo.http")
    for module in required_modules:
        try:
            importlib.import_module(module)
        except ModuleNotFoundError:
            _LOGGER.debug(
                "Skipping optional import of access_point submodules; missing dependency: %s",
                module,
            )
            return False
    return True


if _odoo_runtime_available():
    from . import controllers
    from . import models

