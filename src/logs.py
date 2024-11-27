import time
import logging



def logger(name, log_file, level=logging.DEBUG):
    """Function to setup a logger with a specified time format for log messages."""
    
    # Create a formatter that includes the time format
    formatter = logging.Formatter(' %(levelname)-4s - %(message)s')
    
    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    # Create a logger with the specified name and level
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    
    return logger



# Example usage:
if __name__ == '__main__':
    while True:
        log= logger('example_logger', 'example.log')
        log.info('This is an info message')
        time.sleep(5)