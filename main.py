import sys
sys.dont_write_bytecode = True

from src.checker import fetch_and_filter_journeys
import config
import time

def main():
    while True:
        fetch_and_filter_journeys()
        time.sleep(config.sleep_time)


if __name__ == "__main__":
    main()
