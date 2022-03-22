#  creating a customised logging output

import logging

extData = {
    "user": "imran@example.com"
}
def anotherFunction():
    logging.debug("This is a debug-level message", extra=extData)

def main():
    # set the output file and debug level
    # use custom formatting specification
    fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output_custom_log",
                        level=logging.DEBUG,
                        filemode="a",
                        format=fmtstr,
                        datefmt=datestr,
                        )

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level messsage", extra=extData)

if __name__ == '__main__':
    main()