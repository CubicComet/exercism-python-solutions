import collections


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, length):
        self.buffer = collections.deque([], length)

    def clear(self):
        self.buffer.clear()

    def read(self):
        try:
            return self.buffer.popleft()
        except IndexError:
            raise BufferEmptyException

    def write(self, val):
        if len(self.buffer) < self.buffer.maxlen:
            self.buffer.append(val)
        else:
            raise BufferFullException

    def overwrite(self, val):
        self.buffer.append(val)
