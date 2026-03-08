import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def process_payment(amount: float, user_id: str) -> bool:
    logger.info(f"Processing payment {amount} for user {user_id}")
    if amount <= 0:
        logger.error(f"Invalid amount : {amount}")
        return False
    if amount > 10000:
        logger.warning(f"Large transaction detected: {amount}")
    logger.debug("Payment approved")
    return True


process_payment(500.0, "user_123")
process_payment(-10.0, "user_456")
process_payment(15000.0, "user_789")
