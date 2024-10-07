from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, value: Any, next_node: None | Node = None) -> None:
        self.value = value
        self.next_node = next_node
