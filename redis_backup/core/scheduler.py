import time

import schedule


class Scheduler:
    @staticmethod
    def start():
        while True:
            schedule.run_pending()
            time.sleep(1)
