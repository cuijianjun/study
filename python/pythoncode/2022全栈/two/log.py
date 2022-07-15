import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
    filename='back.log',
    filemode='w'
)

logging.info('这是一个记录日志的地方')