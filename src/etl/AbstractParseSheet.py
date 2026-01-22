from abc import ABC, abstractmethod


# Abstract class defining the common methods of child classes tasked with parsing a particular Excel sheet
class AbstractParseSheet(ABC):
    @abstractmethod
    def get_headers(self): pass

    @abstractmethod
    def validate_headers(self, sheet): pass

    @abstractmethod
    def get_value(self, row, column): pass
