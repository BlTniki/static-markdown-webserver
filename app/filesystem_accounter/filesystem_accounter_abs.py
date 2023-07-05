from .filesystem_events_subscriber import FilesystemEventsSubscriber

from abc import ABC, abstractmethod

class FilesystemAccounterABS(FilesystemEventsSubscriber):

    @abstractmethod
    def get_file_tree(self):
        pass

    @abstractmethod
    def get_file_tree_for_dir(self, dir_url: str):
        pass
