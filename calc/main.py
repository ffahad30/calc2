"""Observer for CSV files"""
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# creating event handler
if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

# handling events
def on_created(event):
    my_event_handler.on_created = on_created
    print(f"{event.src_path} has been created!")


def on_deleted(event):
    my_event_handler.on_deleted = on_deleted
    print(f"{event.src_path} has been deleted!")


def on_modified(event):
    my_event_handler.on_modified = on_modified
    print(f"{event.src_path} has been modified!")


def on_moved(event):
    my_event_handler.on_moved = on_moved
    print(f" {event.src_path} has been moved to {event.dest_path}!")


# create observer
path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)


# start observer
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()