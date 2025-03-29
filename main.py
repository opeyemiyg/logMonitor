import sys
import logging


def main():
    # using sys.argv to determine the log file path.
    # uses the argument provided, otherwise defaults to logs.log

    if len(sys.argv) > 1:
        logFile = sys.argv[1]
    else:
        logFile =  "logs[14].log"


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    main()