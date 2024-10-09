from __future__ import annotations
from typing import Any


class Node:
    def __init__(
        self, value: Any, prev_node: Node | None = None, next_node: Node | None = None
    ) -> None:
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node


class DoubleLinkedList:
    def __init__(self) -> None:
        self.__length = 0
        self.__head = Node(
            None,
        )
        self.__tail = Node(None, prev_node=self.__head)
        self.__head.next_node = self.__tail

    def __len__(self) -> int:
        return self.__length

    def __remove_node(self, node: Node) -> None:
        self.__length -= 1
        prev = node.prev_node
        assert prev is not None
        _next = node.next_node
        assert _next is not None
        node.prev_node = None
        node.next_node = None
        prev.next_node = _next
        _next.prev_node = prev

    def remove(self, value: Any) -> None:
        # removes first occurance of value
        node = self.__head.next_node
        assert node is not None
        while node != self.__tail and node.value != value:
            node = node.next_node
            assert node is not None
        if node != self.__tail:
            self.__remove_node(node)

    def remove_at(self, idx: int) -> None:
        node = self.__get_node(idx)
        self.__remove_node(node)

    def append(self, value: Any) -> None:
        self.__tail.prev_node = Node(
            value, prev_node=self.__tail.prev_node, next_node=self.__tail
        )
        self.__length += 1

    def prepend(self, value: Any) -> None:
        self.__head.next_node = Node(
            value, prev_node=self.__head, next_node=self.__head.next_node
        )
        self.__length += 1

    def __get_node(self, idx: int) -> Node:
        if self.__length <= idx:
            raise IndexError(f"{idx} out of bound {self.__length}")
        # what is closer - head or tail
        jumps_left = idx
        jumps_right = self.__length - 1 - idx
        if jumps_left < jumps_right:
            node = self.__head.next_node
            for _ in range(jumps_left):
                assert node is not None
                node = node.next_node
        else:
            node = self.__tail.prev_node
            for _ in range(jumps_right):
                assert node is not None
                node = node.prev_node
        assert node is not None
        return node

    def __getitem__(self, idx: int) -> Any:
        return self.__get_node(idx).value

    get = __getitem__

    def insert_at(self, value: Any, idx: int) -> None:
        # insert before first
        idx = min(self.__length, idx)
        if idx == 0:
            self.prepend(value)
            return

        insert_after = idx - 1
        parent_node = self.__get_node(insert_after)
        cur_next = parent_node.next_node
        assert cur_next is not None
        new_node = Node(value, prev_node=parent_node, next_node=cur_next)
        parent_node.next_node = new_node
        cur_next.prev_node = new_node
