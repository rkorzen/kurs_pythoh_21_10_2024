import logging

FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(level=logging.WARNING,format=FORMAT, filename="logi.log")

logging.debug("Najniższy poziom")
logging.info("Info")
logging.warning("Warning")
logging.error("Warning")
logging.critical("Warning")