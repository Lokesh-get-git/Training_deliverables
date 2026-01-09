from logger import Logger
from config import Config
# from retry import Retry
from rate_limiter import RateLimiter
# logs=Logger("INFO","core_utils/logs.txt")
# logs.error("debug")

# configs=Config("core_utils/config.json")
# print(configs.get("HOME"))

rl=RateLimiter(2,5)
rl.allow()
rl.allow()
rl.allow()
rl.allow()