import logging
from typing import Optional, Any
import json

logger = logging.getLogger(__name__)

# Redis Client placeholder
_redis_client = None

try:
    import redis
    # Initialize connection pool
    # Port 6379, DB 0, socket_timeout=2
    _pool = redis.ConnectionPool(host="localhost", port=6379, db=0, socket_timeout=2)
    _redis_client = redis.Redis(connection_pool=_pool)
except Exception as e:
    logger.warning(f"Could not initialize Redis client (Redis packages might be missing): {e}")


class RedisCache:
    """Redis cache manager with connection-error tolerance."""
    
    @staticmethod
    def get(key: str) -> Optional[Any]:
        """Get value from Redis cache. Returns None on cache miss or connection failure."""
        if _redis_client is None:
            return None
        try:
            val = _redis_client.get(key)
            if val:
                return json.loads(val)
        except Exception as e:
            logger.debug(f"Redis cache read error for key {key}: {e}")
        return None
        
    @staticmethod
    def set(key: str, value: Any, expire: int = 3600) -> bool:
        """Set value in Redis cache. Returns False on failure."""
        if _redis_client is None:
            return False
        try:
            _redis_client.set(key, json.dumps(value), ex=expire)
            return True
        except Exception as e:
            logger.debug(f"Redis cache write error for key {key}: {e}")
        return False

    @staticmethod
    def delete(key: str) -> bool:
        """Delete key from Redis cache. Returns False on failure."""
        if _redis_client is None:
            return False
        try:
            _redis_client.delete(key)
            return True
        except Exception as e:
            logger.debug(f"Redis cache delete error for key {key}: {e}")
        return False
        
    @staticmethod
    def clear_pattern(pattern: str) -> bool:
        """Clear keys matching a pattern. Returns False on failure."""
        if _redis_client is None:
            return False
        try:
            keys = _redis_client.keys(pattern)
            if keys:
                _redis_client.delete(*keys)
            return True
        except Exception as e:
            logger.debug(f"Redis cache pattern clear error for pattern {pattern}: {e}")
        return False
