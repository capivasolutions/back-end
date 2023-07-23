import psycopg2

from .logger import Logger
from .environment import Environment


class Database:
    """
        Database handles connections with the PostgreSQL Database.
    """

    instance = None

    @classmethod
    def get_instance(cls):
        if Database.instance is None:
            cls.instance = cls.__create_instance(cls)
        return cls.instance

    def __create_instance(cls):
        logger = Logger.get_instance()
        try:
            conn = 'host={} port={} dbname={} user={} password={}'.format(
                Environment.DATABASE_HOST,
                Environment.DATABASE_PORT,
                Environment.DATABASE_NAME,
                Environment.DATABASE_USER,
                Environment.DATABASE_PASSWORD
            )

            logger.debug('Connecting to PostgreSQL Database')
            connection = psycopg2.connect(conn)
            logger.debug('Connected to PostgreSQL Database successfully')
            return connection
        except Exception as error:
            logger.error('Could not connect to PostgreSQL Database', error)
            raise error
