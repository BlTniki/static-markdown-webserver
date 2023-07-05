from .filesystem_events_publisher import FilesystemEventsPublisher
from .filesystem_events_subscriber import FilesystemEventsSubscriber

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent


class WatchdogEventHandlerPublisher(FileSystemEventHandler, FilesystemEventsPublisher):

    def subscribe(self, subscriber: FilesystemEventsSubscriber):
        self.subscribers.append(subscriber)

    def notifyAll(self, event: FileSystemEvent):
        for sub in self.subscribers:
            sub.update(event)

    def on_any_event(self, event: FileSystemEvent):
        # Handle the event
        self.notifyAll(event)


class MdStaticWatchdog:

    def __init__(self, directory_to_watch):
        # Create an observer and event handler
        self.publisher = WatchdogEventHandlerPublisher()
        self.observer = Observer()

        # Set up the observer to watch the directory
        self.observer.schedule(self.publisher, directory_to_watch, recursive=True)

        # Start the observer
        self.observer.start()
        print(f"I'm listening to the directory:\n{directory_to_watch}")


if __name__ == "__main__":
    wd = MdStaticWatchdog(r'D:\!Important\Progrog\Python\static-markdown-webserver\app\md_static')
    try:
        while True:
            wd.observer.join(1)
    except KeyboardInterrupt:
        wd.observer.stop()
    finally:
        wd.observer.stop()
        wd.observer.join()
