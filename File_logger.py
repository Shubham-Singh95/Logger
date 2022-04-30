import sys
import time
import logging
from logging.handlers import RotatingFileHandler
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class CustomLoggingEventHandler(LoggingEventHandler):
    """Logs all the events captured."""

    def __init__(self, logger):
        self.logger = logger

    def on_moved(self, event):
        super().on_moved(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Moved %s: from %s to %s", what, event.src_path,
                     event.dest_path)

    def on_created(self, event):
        super().on_created(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        super().on_deleted(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Deleted %s: %s", what, event.src_path)

    def on_modified(self, event):
        super().on_modified(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Modified %s: %s", what, event.src_path)


def dlp_logger():
    logging.basicConfig(filename='test.csv',
                        level=logging.DEBUG,
                        format='%(asctime)s, %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger('test')
    handler = RotatingFileHandler("test.csv", maxBytes=2000, backupCount=2)
    logger.addHandler(handler)

    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path='C:/Users/Asus/Desktop/restAPI', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":

    dlp_logger()





