import logging
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.INFO: Fore.BLUE,  # INFO -> Green
        logging.WARNING: Fore.YELLOW,  # WARNING -> Yellow
        logging.ERROR: Fore.GREEN,  # ERROR -> Red
        logging.CRITICAL: Fore.RED + Style.BRIGHT  # CRITICAL -> Bright Red
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelno, Fore.WHITE)  # Default is white
        log_message = super().format(record)
        return f"{log_color}{log_message}{Style.RESET_ALL}"

# Create logger
logger = logging.getLogger("ColoredLogger")
logger.setLevel(logging.DEBUG)

# Create console handler and set format
console_handler = logging.StreamHandler()
formatter = ColoredFormatter("%(levelname)s: %(message)s")
console_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(console_handler)

