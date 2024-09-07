import logging

logging.basicConfig(
    filename='logs/app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
