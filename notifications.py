from plyer import notification

def notify(title, message, duration=5):
    notification.notify(
        title=title,
        message=message,
        app_name="Pomo🍅",
        timeout=duration
    )