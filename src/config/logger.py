import logging


class Logger:
    logger = None

    @classmethod
    def get_instance(cls):
        if cls.logger is None:
            cls.__create_instance(cls)
        return cls.logger

    def __create_instance(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%d/%m/%YT%H:%M:%S',
        )
        self.logger = logging.getLogger()
