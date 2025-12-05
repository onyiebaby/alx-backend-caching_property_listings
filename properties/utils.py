def get_all_properties(): "", Property.objects.all(), cache.get, all_properties, 3600, get_all_properties
def get_redis_cache_metrics(): "", keyspace_hits, keyspace_misses
if total_requests > 0 else 0
return logger.error