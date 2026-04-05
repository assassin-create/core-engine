import logging
import os
import random
import string
import time

from core_engine.core.logger import get_logger

class Util:
    @staticmethod
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    @staticmethod
    def get_current_time():
        return time.time()

    @staticmethod
    def get_current_date():
        return time.strftime("%Y-%m-%d")

    @staticmethod
    def get_current_datetime():
        return time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_logger(name):
        return get_logger(name)

    @staticmethod
    def get_project_root():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def get_file_size(file_path):
        return os.path.getsize(file_path)

    @staticmethod
    def is_file_exists(file_path):
        return os.path.exists(file_path)