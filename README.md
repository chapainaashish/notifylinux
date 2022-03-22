## notifylinux
A Python package to send desktop notification in linux

**Project link**

```
https://pypi.org/project/notifylinux
```

**Install notifylinux**

```
pip install notifylinux
```

**For instance**

```
from notifylinux.linuxnotifier import Notifier

notify = Notifier(title="Hello World", descriptions="Welcome to Linux",
                  iconpath="icon/hello.svg", timeout=5, urgency="normal")
notify.send_notification()


```
