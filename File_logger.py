import sys
import time
import logging
from logging.handlers import RotatingFileHandler
from watchdog.observers import Observer

# To log all the events captured
from watchdog.events import LoggingEventHandler


def dlp_logger():

    "Logs in the events into a CSV file that are sent by LoggingEventHandler"

    # Initializes the format of the logs

    logging.basicConfig(filename='event_logger.csv',
                        level=logging.NOTSET,
                        format='%(asctime)s, %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
   
    # Creates a logger named Event_Logger

    logger = logging.getLogger('event_logger')

    # Switches from one file to the next when the current file reaches a 2000 bytes
    
    handler = RotatingFileHandler("event_logger.csv", maxBytes=2000, backupCount=2)

    # Parses the handler to the test logger

    logger.addHandler(handler)

    # Creating the instance of Class LoggingEventHandler

    event_handler = LoggingEventHandler()

    # Observer polls the changes made the in the directory

    observer = Observer()
    observer.schedule(event_handler, path='/', recursive=True)
    observer.start()
    try:
        while True:
            # Re-triggers the logging every sec , thus sleep(1)

            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":

    dlp_logger()





