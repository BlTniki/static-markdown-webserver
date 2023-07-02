from .filesystem_events_subscriber import FilesystemEventsSubscriber

from abc import ABC, abstractmethod
from watchdog.events import FileSystemEvent


class FilesystemEventsPublisher(ABC):
    subscribers = list()

    @abstractmethod
    def subscribe(self, subscriber: FilesystemEventsSubscriber):
        pass

    @abstractmethod
    def notifyAll(self, event: FileSystemEvent):
        pass
