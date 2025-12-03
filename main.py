import mexc
from logger_conf import setup_logger

logger = setup_logger()

logger.debug('this is test log message')

if __name__ == '__main__':
    print('PyCharm')

    logger.debug(f'MEXC FUTURES API is online : {mexc.ping()} ')

    mexc.contract_info()
