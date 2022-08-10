import logging as log


log.basicConfig(
    
    level=log.INFO,
    format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        log.FileHandler("upload.log", encoding="utf-8"),
        log.StreamHandler()
    ])
