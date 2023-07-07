import psycopg2
from src.config.logger import Logger


class Database:
    connection = None

    @classmethod
    def get_instance(cls):
        if cls.connection is None:
            cls.__create_instance(cls)
        return cls.connection

    def __create_instance(self):
        try:
            logger = Logger.get_instance()

            # TODO: get credentials from .env
            port = 5432
            database = 'postgres'
            username = 'postgres'
            password = 'postgres'

            conn = 'port={} dbname={} user={} password={}'.format(
                port, database, username, password)

            logger.debug('Connecting to PostgreSQL Database')
            self.connection = psycopg2.connect(conn)
            logger.debug('Connected to PostgreSQL Database successfully')
        except Exception as error:
            logger.error('Could not connect to PostgreSQL Database', error)
            raise error
