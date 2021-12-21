import shutil
import subprocess


class Notifier():
    """linuxnotifier: Display Notification in linux"""

    def __init__(self, title, descriptions="", timeout=5, urgency="normal", iconpath="", appname=""):
        """
        Args:
            title ([type]): [description]
            descriptions (str, optional): [description]. Defaults to "".
            timeout (int, optional): [description]. Defaults to 5.
            urgency (str, optional): [description]. Defaults to "normal".
            [low, normal, critical]
            iconpath (str, optional): [description]. Defaults to "".
            appname (str, optional): [description]. Defaults to "".

        """
        self.__title = title
        self.__descriptions = descriptions
        self.__timeout = timeout
        self.__urgency = urgency
        self.__iconpath = iconpath
        self.__appname = appname

        if title is None or title == "":
            raise ValueError("Title can't be empty")

        if urgency not in ["normal", "low", "critical", None]:
            raise ValueError("Inappropriate urgency given")

    def send_notification(self):
        """Display notification"""
        # raising error if 'notify-send' command can't be found
        if shutil.which("notify-send") is None:
            raise SystemError(
                "Install libnotify-bin\n run 'sudo apt-get install libnotify-bin'")

        else:
            # Creating notify-send command into list
            notification = ["notify-send", self.__title,
                            self.__descriptions, "-t", f"{self.__timeout * 1000}", ]

            # if urgency level is given
            if self.__urgency != "":
                notification += ["-u", self.__urgency]

            # if iconpath is given
            if self.__iconpath != "":
                notification += ["-i", self.__iconpath]
            # if appname is given
            if self.__appname != "":
                notification += ["-a", self.__appname]

            # Executing Process
            subprocess.Popen(notification, shell=False)

