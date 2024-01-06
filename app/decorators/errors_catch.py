import logging
import time

# logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")


def catch_error(err):
    def wrapped():
        try:
            return err()
        except Exception as e:
            logging.info(f"TIME:[{time.strftime('%H:%M:%S')}]   ERROR {e}")
            print("Error:", e)

    return wrapped