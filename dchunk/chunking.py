from __future__ import print_function, division, absolute_import, unicode_literals
import itertools
import collections


def get_n_chunks(iterable_size, chunk_size):
    return (iterable_size - 1) // chunk_size + 1


class ChunkIterator(collections.Iterator):
    def __init__(self, iterable, chunk_size):
        self.iterator = iter(iterable)
        self.chunk_size = chunk_size
        if hasattr(iterable, '__len__'):
            self.n_chunks = get_n_chunks(len(iterable), chunk_size)
            self.shape = (self.n_chunks,)
        else:
            self.n_chunks = None

    def __iter__(self):
        return self

    def __next__(self):
        chunk = list(itertools.islice(self.iterator, self.chunk_size))
        if not chunk:
            raise StopIteration
        return chunk

    def next(self):
        return self.__next__()


class ChunkWithIndexIterator(ChunkIterator):
    def __init__(self, iterable, chunk_size):
        super(ChunkWithIndexIterator, self).__init__(iterable, chunk_size)
        self.chunk_start = 0
        self.chunk_end = 0

    def __next__(self):
        chunk = super(ChunkWithIndexIterator, self).__next__()
        self.chunk_start = self.chunk_end
        self.chunk_end = self.chunk_start + len(chunk)
        return chunk, self.chunk_start, self.chunk_end


chunk = ChunkIterator
chunk_with_index = ChunkWithIndexIterator
