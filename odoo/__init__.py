from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any


@dataclass
class _Field:
    args: tuple[Any, ...]
    kwargs: dict[str, Any]


class _Fields(SimpleNamespace):
    def __init__(self) -> None:
        super().__init__(
            Boolean=_Field,
            Char=_Field,
            Datetime=_Field,
            Many2one=_Field,
            One2many=_Field,
        )


class _Models(SimpleNamespace):
    class Model:
        ...


api = SimpleNamespace()
fields = _Fields()
models = _Models()

