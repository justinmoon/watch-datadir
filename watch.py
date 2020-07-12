import time

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def on_created(event):
    print(f"created: {event.src_path}")

def on_deleted(event):
    print(f"deleted: {event.src_path}")

def on_modified(event):
    print(f"modified {event.src_path}")

def on_moved(event):
    print(f"moved {event.src_path} to {event.dest_path}")


if __name__ == "__main__":
    # Create event handler
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    # Register callbacks for specific events
    handler.on_created = on_created
    handler.on_deleted = on_deleted
    handler.on_modified = on_modified
    handler.on_moved = on_moved

    # Create filesystem watcher
    path = "/home/justin/.bitcoin"
    recursive = True
    observer = Observer()
    observer.schedule(handler, path, recursive=recursive)

    # Run the watcher in another thread, watch for ctrl-c
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
