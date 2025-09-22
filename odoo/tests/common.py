from __future__ import annotations

import unittest
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any, Dict, Mapping, MutableMapping


@dataclass
class ReferenceRecord:
    value: Any


class FakeEnv:
    def __init__(self, references: Mapping[str, Any] | None = None) -> None:
        self._references: Dict[str, Any] = dict(references or {})

    def ref(self, identifier: str) -> ReferenceRecord:
        try:
            reference = self._references[identifier]
        except KeyError as exc:
            raise KeyError(f"Unknown reference: {identifier}") from exc

        if isinstance(reference, ReferenceRecord):
            return reference
        if isinstance(reference, MutableMapping):
            return ReferenceRecord(**reference)
        if isinstance(reference, SimpleNamespace):
            return ReferenceRecord(**reference.__dict__)
        return ReferenceRecord(value=reference)

    def add_reference(self, identifier: str, value: Any) -> None:
        self._references[identifier] = value


class SingleTransactionCase(unittest.TestCase):
    reference_values: Mapping[str, Any] = {"access_token_expires_in": 31536000}

    def setUp(self) -> None:
        super().setUp()
        self.env = FakeEnv(self.reference_values)

    def add_reference(self, identifier: str, value: Any) -> None:
        self.env.add_reference(identifier, value)

