#coding: utf-8

from redis import StrictRedis


class RedisQUEUE(StrictRedis):
    def set_item(self, queue, item, unique=True):
        """
        set queue item
        :param queue:
        :param item:
        :param unique:
        :return:
        """
        if unique and self.exists_item(queue, item):
            return False
        self.rpush(queue, item)
        return True

    def pop_item(self, queue):
        """
        remove, get and return queue item
        :param queue:
        :return:
        """
        return self.lpop(queue)

    def get_queue(self, queue):
        """
        all items that contains in queue
        :param queue:
        :return:
        """
        return self.lrange(queue, 0, -1)

    def exists_item(self, queue, item):
        """
        Check exists item in queue
        :param queue:
        :param item:
        :return:
        """
        if item in self.get_queue(queue):
            return True
        return False
