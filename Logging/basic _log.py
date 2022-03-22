# demonstrating the logging api in python

import logging

def main():

    # using basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG,
                        filename="output.log",
                        filemode="w")

    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

    # Output formatted strings to the log
    logging.info("Here's a {0} variable and an int: {1}".format("string", 10))

if __name__ == '__main__':
    main()