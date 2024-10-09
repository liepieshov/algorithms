from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, value: Any, next_node: None | Node = None) -> None:
        self.value = value
        self.next_node = next_node


class SingleLinkedList:
    def __init__(self) -> None:
        self.__length = 0
        self.__head = Node(None)

    def __len__(self) -> int:
        return self.__length

    def __remove_next_node(self, parent_node: Node) -> None:
        self.__length -= 1
        assert parent_node.next_node is not None
        removed_node = parent_node.next_node
        parent_node.next_node = removed_node.next_node
        removed_node.next_node = None

    def remove(self, value: Any) -> None:
        # removes first occurance of value
        node = self.__head
        while node.next_node and node.next_node.value != value:
            node = node.next_node
        if node.next_node is not None:
            self.__remove_next_node(node)

    def remove_at(self, idx: int) -> None:
        parent_node = self.__get_parent_node(idx)
        self.__remove_next_node(parent_node)

    def prepend(self, value: Any) -> None:
        cur_next = self.__head.next_node
        new_node = Node(value, next_node=cur_next)
        self.__head.next_node = new_node
        self.__length += 1

    def __get_parent_node(self, idx: int) -> Node:
        if self.__length <= idx:
            raise IndexError(f"{idx} out of bound {self.__length}")
        node = self.__head
        for _ in range(idx):
            assert node is not None
            node = node.next_node
        assert node is not None
        return node

    def __getitem__(self, idx: int) -> Any:
        parent_node = self.__get_parent_node(idx)
        node = parent_node.next_node
        assert node is not None
        return node.value

    get = __getitem__

    def insert_at(self, value: Any, idx: int) -> None:
        # insert before first
        idx = min(self.__length, idx)
        if idx == 0:
            self.prepend(value)
            return
        insert_after = idx - 1
        parent_node = self.__get_parent_node(insert_after).next_node
        assert parent_node is not None
        parent_node.next_node = Node(value, next_node=parent_node.next_node)
        self.__length += 1
