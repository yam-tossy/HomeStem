import logging

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)
    logger.info("Start Home Stem System...")


if __name__ == "__main__":
    # execute only if run as a script
    main()
