# timer.py

import datetime
from unicodedata import name

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None
        self._stop_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        #self._start_time = time.perf_counter()
        self._start_time = datetime.datetime.today()
        return self._start_time

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        #elapsed_time = time.perf_counter() - self._start_time
        self._stop_time = datetime.datetime.today()
        print(f"{self._stop_time} minus {self._start_time}")
        elapsed_time =   self._stop_time - self._start_time
        #print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return elapsed_time
    
    def reset(self):
        self._start_time = None
        self._stop_time = None
           
    @property
    def StartTime(self):
        return self._start_time

    @StartTime.setter
    def StartTime(self, value):
        self._start_time = value
    
    @property
    def StopTime(self):
        return self._stop_time
