import mexc
from logger_conf import setup_logger

logger = setup_logger()

logger.debug('this is test log message')

if __name__ == '__main__':
    print('PyCharm')

    logger.debug(f'MEXC FUTURES API is online : {mexc.ping()} ')

    contract_details = mexc.contract_detail()
    if not contract_details or not contract_details.data:
        logger.error(f'No data was received from MEXC')
    for symbol in contract_details.data:
        print(symbol.symbol)
