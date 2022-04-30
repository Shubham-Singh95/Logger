import sys
import time
import logging
from logging.handlers import RotatingFileHandler
from watchdog.observers import Observer

# To log all the events captured
from watchdog.events import LoggingEventHandler


def dlp_logger():

    "Logs in the events into a CSV file that are sent by LoggingEventHandler"

    logging.basicConfig(filename='event_logger.csv',
                        level=logging.NOTSET,
                        format='%(asctime)s, %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')  # Initializes the format of the logs

    logger = logging.getLogger('event_logger') # Creates a logger named Event_Logger
    handler = RotatingFileHandler("event_logger.csv", maxBytes=2000, backupCount=2) # Switches from one file to the next when the current file reaches a 2000 byte
    logger.addHandler(handler)  # Parses the handler to the test logger

    event_handler = LoggingEventHandler() # Creating the instance of Class LoggingEventHandler
    
    observer = Observer()  # Observer polls the changes made the in the directory
    observer.schedule(event_handler, path='/', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)  # Re-triggers the logging every sec , thus sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":

    dlp_logger()





