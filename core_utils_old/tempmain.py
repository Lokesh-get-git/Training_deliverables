from logger import Logger
from config import Config
from retry import Retry #type:ignore
from rate_limiter import RateLimiter

# logs=Logger("INFO","logs.txt")
# logs.info("info")
# logs.debug("debug")
# logs.level=10
# logs.debug("debug")

configs=Config("config.json")
print(configs.get("HOME"))

# rl=RateLimiter(2,5)
# rl.allow()
# rl.allow()
# rl.allow()
# rl.allow()

# attempts=0

# def retryfunc():
#     global attempts
#     attempts+=1
#     print(f"attempt number:{attempts}")

#     if attempts<3:
#         raise ValueError("error")
#     return "success"
# result= Retry(
#     retryfunc
# )
# print(result)