from .filesystem_events_subscriber import FilesystemEventsSubscriber

from abc import ABC, abstractmethod

class FilesystemAccounter(FilesystemEventsSubscriber):

    @abstractmethod
    def get_file_tree(self):
        pass
