from __future__ import annotations
from typing import Any


class Node:
    def __init__(
        self, value: Any, prev_node: None | Node = None, next_node: None | Node = None
    ) -> None:
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node


class DoubleLinkedList:
    def __init__(self) -> None:
        self.__length = 0
        self.__head: None | Node = None
        self.__tail: None | Node = None

    def __len__(self) -> int:
        return self.__length

    def __remove_node(self, node: Node) -> None:
        self.__length -= 1
        prev = node.prev_node
        _next = node.next_node
        if prev is not None:
            prev.next_node = _next
        else:
            self.__head = _next
        if _next is not None:
            _next.prev_node = prev
        else:
            self.__tail = prev
        node.prev_node = None
        node.next_node = None

    def remove(self, value: Any) -> None:
        # removes first occurance of value
        node = self.__head
        while node and node.value != value:
            node = node.next_node
        if node is not None:
            self.__remove_node(node)

    def remove_at(self, idx: int) -> None:
        node = self.__get_node(idx)
        self.__remove_node(node)

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.__length == 0:
            self.__head = new_node
        else:
            assert self.__tail is not None
            self.__tail.next_node = new_node
            new_node.prev_node = self.__tail
        self.__tail = new_node
        self.__length += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value)
        if self.__length == 0:
            self.__tail = new_node
        else:
            assert self.__head is not None
            self.__head.prev_node = new_node
            new_node.next_node = self.__head
        self.__head = new_node
        self.__length += 1

    def __get_node(self, idx: int) -> Node:
        if self.__length <= idx:
            raise IndexError(f"{idx} out of bound {self.__length}")
        # what is closer - head or tail
        jumps_left = idx
        jumps_right = self.__length - 1 - idx
        if jumps_left < jumps_right:
            node = self.__head
            for _ in range(jumps_left):
                assert node is not None
                node = node.next_node
        else:
            node = self.__tail
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
        node = self.__get_node(insert_after)
        # save ref
        node_next = node.next_node

        new_node = Node(value, prev_node=node, next_node=node_next)
        node.next_node = new_node
        if node_next is None:
            self.__tail = new_node
        else:
            node_next.prev_node = new_node
