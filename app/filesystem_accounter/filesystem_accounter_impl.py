from .filesystem_accounter_abs import FilesystemAccounterABS
from .md_static_watchdog import MdStaticWatchdog
from configs import Config

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

def filter_directory_tree(tree: list[dict], url_iter: iter):

    cur_dir = next(url_iter, None)
    if not cur_dir:
        return tree

    for node in tree:
        if node["text"] == cur_dir:
            return filter_directory_tree(node["children"], url_iter)

    # if we got here --> throw error
    raise ValueError("Given dir non exist!")


class FilesystemAccounterImpl(FilesystemAccounterABS):

    def __init__(self, config: Config):
        self.PATH_TO_VAULT = config.PATH_TO_VAULT
        self._valid_events = (FileCreatedEvent, FileMovedEvent, FileDeletedEvent,
                              DirCreatedEvent, DirMovedEvent, DirDeletedEvent)

        self._file_tree = build_directory_dict(self.PATH_TO_VAULT)

        self._wd = MdStaticWatchdog(self.PATH_TO_VAULT)
        self._wd.publisher.subscribe(self)

    def get_file_tree(self):
        return self._file_tree

    def get_file_tree_for_dir(self, dir_url: str):
        # without filter split will output like "/some/url/" -> ["", "some", "url", ""]
        url_iter = iter(filter(lambda s: len(s) > 0, dir_url.split("/")))
        return filter_directory_tree(self._file_tree, url_iter)

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
