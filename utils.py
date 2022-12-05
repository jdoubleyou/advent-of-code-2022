import functools
from functools import reduce
from textwrap import indent
from typing import Iterable
from typing import TypeVar

T = TypeVar("T")
ListOrStr = TypeVar("ListOrStr", str, list)


class BetterList(list):
    Self = TypeVar("Self", bound="BetterList")

    def map(self: Self, func) -> Self:
        return BetterList(func(a) for a in self)

    def filter_to(self: Self, func) -> Self:
        return BetterList(a for a in self if bool(func(a)))

    def filter_out_value(self: Self, value) -> Self:
        return BetterList(a for a in self if a != value)

    def filter_out(self: Self, func) -> Self:
        return BetterList(a for a in self if not bool(func(a)))

    def divide(self: Self, func) -> tuple[Self, Self]:
        return (self.filter_to(func), self.filter_out(func))

    def reduce(self: Self, func, initial=functools._initial_missing):
        r = reduce(func, self, initial)
        return BetterList(r) if isinstance(r, Iterable) else r

    def foreach(self: Self, func) -> Self:
        for _ in self:
            func()
        return self

    def foreach_val(self: Self, func) -> Self:
        for i in self:
            func(i)
        return self

    def inspect(self: Self) -> Self:
        return self.foreach(print)

    def concat(self: Self, iterable: Iterable) -> Self:
        self.extend(iterable)
        return self

    def join(self: Self, delimiter) -> "BetterStr":
        return BetterStr(delimiter.join(self))

    def enumerate(self: Self) -> Self:
        return BetterList(enumerate(self))

    def split_each_on(self: Self, delimiter) -> Self:
        split = lambda delimiter: lambda s: BetterList(s.split(delimiter))
        return self.map(split(delimiter))


class BetterStr(str):
    Self = TypeVar("Self", bound="BetterStr")

    def split(self: Self, *a, **k):
        return BetterList(super().split(*a, **k))

    def splitlines(self: Self, *a, **k):
        return BetterList(super().splitlines(*a, **k))

    def indent(self: Self, indent_str: str) -> Self:
        return BetterStr(indent(self, indent_str))


class IntWrapper:
    Self = TypeVar("Self", bound="IntWrapper")

    def __init__(self: Self, value: int) -> None:
        self._value = value

    def increment(self: Self) -> None:
        self._value += 1

    def decrement(self: Self) -> None:
        self._value += 1

    def get(self):
        return self._value

    def __sub__(self, other):
        return self._value.__sub__(other)

    def __str__(self) -> str:
        return BetterStr(self._value)


def join_lists(l: list[list[T]]) -> BetterList[T]:
    return reduce(
        lambda accum, next: accum + next
        if isinstance(next, (tuple, list, BetterList))
        else accum + BetterList(next),
        l,
        BetterList(),
    )


def multi_split(delimiters: str, string: str, join=False) -> BetterList[ListOrStr]:
    if not delimiters:
        return string
    func = join_lists if join else lambda a: a
    return func(
        BetterList(multi_split(delimiters[1:], i) for i in string.split(delimiters[0]))
    )


def split_and_do(delimiter, string: str, mapper: callable) -> BetterList[str]:
    return BetterList(mapper(s) for s in string.split(delimiter))
