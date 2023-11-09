from pygame import event, QUIT

def __events__(running) -> None:
    for events in event.get():
        if events.type == QUIT:
            running = False