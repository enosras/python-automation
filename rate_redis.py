import time

import redis


class RedisTokenBucketLimiter:
    def __init__(self, redis_client: redis.Redis, capacity: int, refill_rate: float):
        """
        capacity: Maximum tokens the bucket can hold.
        refill_rate: Tokens added per second.
        """
        self.redis = redis_client
        self.capacity = capacity
        self.refill_rate = refill_rate

        # Lua script executes entirely inside Redis to ensure atomic operations across servers
        self.lua_script = self.redis.register_script("""
            local key = KEYS[1]
            local capacity = tonumber(ARGV[1])
            local refill_rate = tonumber(ARGV[2])
            local now = tonumber(ARGV[3])
            
            -- Retrieve the last saved state
            local data = redis.call('HMGET', key, 'tokens', 'last_updated')
            local tokens = tonumber(data[1])
            local last_updated = tonumber(data[2])
            
            -- If new user/key, initialize full bucket
            if not tokens then
                tokens = capacity
                last_updated = now
            else
                -- Calculate how many tokens accumulated since last request
                local elapsed = now - last_updated
                tokens = math.min(capacity, tokens + (elapsed * refill_rate))
            end
            
            -- Check if we have enough tokens
            if tokens >= 1 then
                tokens = tokens - 1
                -- Save state and set a 1-hour expiration to keep Redis clean
                redis.call('HSET', key, 'tokens', tokens, 'last_updated', now)
                redis.call('EXPIRE', key, 3600)
                return 1 -- Request Allowed
            else
                return 0 -- Request Denied
            end
        """)

    def is_allowed(self, client_id: str) -> bool:
        redis_key = f"rate_limit:{client_id}"
        current_time = time.time()

        # Run the Lua script in Redis
        result = self.lua_script(
            keys=[redis_key], args=[self.capacity, self.refill_rate, current_time]
        )
        return result == 1


# --- Simulation across "Multiple Servers" ---
# Connect to your shared Redis instance
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# Define rule: Max 5 tokens, refills at 1 token per second
limiter = RedisTokenBucketLimiter(redis_client=r, capacity=5, refill_rate=1.0)

# Simulate different application servers checking the same client
client = "user_12345"

print("--- Rapid burst of requests ---")
for i in range(7):
    allowed = limiter.is_allowed(client)
    print(f"Request {i + 1}: {'ALLOWED' if allowed else 'DENIED (Rate Limited)'}")

print("\n--- Waiting 2 seconds for refill ---")
time.sleep(2)

for i in range(3):
    allowed = limiter.is_allowed(client)
    print(f"Delayed Request {i + 1}: {'ALLOWED' if allowed else 'DENIED'}")
