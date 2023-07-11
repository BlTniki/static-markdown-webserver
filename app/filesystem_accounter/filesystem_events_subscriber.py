from abc import ABC, abstractmethod
from watchdog.events import FileSystemEvent


class FilesystemEventsSubscriber(ABC):

    @abstractmethod
    def update(self, event: FileSystemEvent):
        pass


