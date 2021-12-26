## notifylinux
A python package to send desktop notification in linux

**To install notifylinux run**

```pip install notifylinux```

**For instance**

```
from notifylinux.linuxnotifier import Notifier

notify = Notifier(title="Hello Aashish", descriptions="Welcome to Linux",
                  iconpath="icon/help-about.svg", timeout=5, urgency="normal")
notify.send_notification()


```
