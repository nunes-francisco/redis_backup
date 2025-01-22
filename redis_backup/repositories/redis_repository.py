class RedisRepository:
    def __init__(self, config):
        self.config = config

    def get_rdb_file(self):
        return self.config.redis_rdb_path

    def get_aof_file(self):
        return self.config.redis_aof_path
