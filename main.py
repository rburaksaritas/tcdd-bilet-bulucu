import sys
sys.dont_write_bytecode = True

from src.functions import fetch_and_filter_journeys
import config
import time

def main():
    while True:
        print(f"### Started checking.")
        fetch_and_filter_journeys()
        print(f"### Completed checking. \n### Will restart in {config.sleep_time} seconds.")
        time.sleep(config.sleep_time)


if __name__ == "__main__":
    main()
