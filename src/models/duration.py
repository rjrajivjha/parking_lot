import math
from datetime import datetime, timedelta


class Duration:
    def __init__(self, start_time, end_time):
        self.timedelta = end_time - start_time

    def hours(self):
        return math.ceil(self.timedelta.total_seconds() / 3600)
