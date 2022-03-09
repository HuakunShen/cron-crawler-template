from ctypes import Union
import os
import requests
from src.util import loadenv
from src.job import AbstractJob
from src.notifier.email_notifier import send_code_template, send_error

loadenv()
TO_EMAIL_ADDRESS = os.environ.get("TO_EMAIL_ADDRESS")


class Job(AbstractJob):
    name = "World Time Job"

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        res = requests.get("http://worldtimeapi.org/api/timezone/America/Toronto")
        if res.status_code != 200:
            self.fail()
        else:
            data = res.json()
            self.success(data)

    def success(self, code: str):
        send_code_template(self.name, code, TO_EMAIL_ADDRESS)

    def fail(self):
        send_error("Error from cron crawler", "Error getting world time", TO_EMAIL_ADDRESS)
