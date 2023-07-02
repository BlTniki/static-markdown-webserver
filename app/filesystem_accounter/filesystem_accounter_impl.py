from .filesystem_accounter_abs import FilesystemAccounter
from .md_static_watchdog import MdStaticWatchdog
from config import Config

from watchdog.events import FileSystemEvent
from watchdog.events import FileCreatedEvent, FileMovedEvent, FileDeletedEvent
from watchdog.events import DirCreatedEvent, DirMovedEvent, DirDeletedEvent
import os
import urllib.parse


def build_directory_dict(rootdir, pwd="/md_static"):
    dirs = []
    for elem in os.listdir(rootdir):
        path = rootdir + os.sep + elem

        if os.path.isdir(path):
            # if it's a dir create dict with dir name
            # and build children recursively
            elem_dict = {
                "text": elem,
                "children": build_directory_dict(path, pwd + "/" + elem)
            }
        else:
            # else build file dict with name and url to file
            elem_dict = {
                "text": elem,
                "a_attr": {"href": urllib.parse.quote(pwd + "/" + elem)}  # make str url safe
            }

        dirs.append(elem_dict)

    return dirs


class FilesystemAccounterImpl(FilesystemAccounter):

    def __init__(self, config: Config):
        self.PATH_TO_VAULT = config.PATH_TO_VAULT
        self._valid_events = (FileCreatedEvent, FileMovedEvent, FileDeletedEvent,
                              DirCreatedEvent, DirMovedEvent, DirDeletedEvent)

        self._file_tree = build_directory_dict(self.PATH_TO_VAULT)

        self._wd = MdStaticWatchdog(self.PATH_TO_VAULT)
        self._wd.publisher.subscribe(self)

    def get_file_tree(self):
        return self._file_tree

    def update(self, event: FileSystemEvent):
        # filter non important events
        if isinstance(event, self._valid_events):
            # rebuild tree
            self._file_tree = build_directory_dict(self.PATH_TO_VAULT)


if __name__ == "__main__":
    a = FilesystemAccounterImpl(Config())
    try:
        while True:
            a._wd.observer.join(1)
    except KeyboardInterrupt:
        a._wd.observer.stop()
    finally:
        a._wd.observer.stop()
        a._wd.observer.join()
