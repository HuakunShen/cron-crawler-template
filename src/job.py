from abc import ABC, abstractmethod
from typing import Any


class AbstractJob(ABC):
    name = "Abstract Job"

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def success(self, payload: Any):
        raise NotImplementedError

    @abstractmethod
    def fail(self, payload: Any):
        raise NotImplementedError
