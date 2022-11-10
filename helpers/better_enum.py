from enum import Enum
from typing import TypeVar, Type, Any

EnumFromValue = TypeVar('EnumFromValue', bound=Enum)


class BetterEnum(Enum):
    @classmethod
    def from_value(cls: Type[EnumFromValue], value: Any) -> EnumFromValue:
        for item in cls:
            if item.value == value:
                return item
        raise ValueError(f'Value "{value}" not found in Enum "{cls.__name__}"')

    @classmethod
    def from_name(cls: Type[EnumFromValue], name: str) -> EnumFromValue:
        for item in cls:
            if item.name == name:
                return item
        raise ValueError(f'Name "{name}" not found in Enum "{cls.__name__}"')

    @classmethod
    def from_human_name(cls: Type[EnumFromValue], name: str) -> EnumFromValue:
        machine_name = human_name_to_machine_name(name)
        for item in cls:
            if item.name == machine_name:
                return item
        raise ValueError(f'Name "{machine_name}" not found in Enum "{cls.__name__}"')


def human_name_to_machine_name(value: str) -> str:
    return value.replace(' ', '_').replace('-', '_').lower()
