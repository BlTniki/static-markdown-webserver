from abc import ABC, abstractmethod
from watchdog.events import FileSystemEvent


class FilesystemEventsSubscriber(ABC):

    @abstractmethod
    def update(self, event: FileSystemEvent):
        pass


# class fafa(FilesystemEventsSubscriber):
#     def update(self, event: FileSystemEvent):
#         pass
#
#
# if __name__ == "__main__":
#     fi = FilesystemEventsSubscriber
#     fa = fafa()
#     print(isinstance(fa, FilesystemEventsSubscriber))
#     print(isinstance(fa, fafa))
