from dataclasses import dataclass, field
from uuid import  uuid4


@dataclass
class Pc:
    title: str
    id: uuid4 = field(default_factory=uuid4)

@dataclass
class Person:
    name: str
    id: uuid4 = field(default_factory=uuid4)

@dataclass
class PersonPc:
    pc_id: uuid4 = field(default_factory=uuid4)
    person_id: uuid4 = field(default_factory=uuid4)
    id: uuid4 = field(default_factory=uuid4)
