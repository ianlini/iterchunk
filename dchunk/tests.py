import unittest
from itertools import islice

from dchunk import chunk, chunk_with_index


class TestChunking(unittest.TestCase):
    def test_chunk_with_full_last_chunk(self):
        chunks = list(chunk(range(6), 2))
        self.assertEqual(len(chunks), 3)
        self.assertListEqual(chunks[0], [0, 1])
        self.assertListEqual(chunks[1], [2, 3])
        self.assertListEqual(chunks[2], [4, 5])

    def test_chunk_with_nonfull_last_chunk(self):
        chunks = list(chunk(range(5), 2))
        self.assertEqual(len(chunks), 3)
        self.assertListEqual(chunks[0], [0, 1])
        self.assertListEqual(chunks[1], [2, 3])
        self.assertListEqual(chunks[2], [4])

    def test_chunk_with_one_full_chunk(self):
        chunks = list(chunk(range(2), 2))
        self.assertEqual(len(chunks), 1)
        self.assertListEqual(chunks[0], [0, 1])

    def test_chunk_with_one_nonfull_chunk(self):
        chunks = list(chunk(range(1), 2))
        self.assertEqual(len(chunks), 1)
        self.assertListEqual(chunks[0], [0])

    def test_chunk_with_no_chunk(self):
        chunks = list(chunk([], 2))
        self.assertEqual(len(chunks), 0)

    def test_chunk_shape(self):
        self.assertFalse(hasattr(chunk(islice([0], 1), 2), 'shape'))
        self.assertEqual(chunk([], 2).shape, (0,))
        self.assertEqual(chunk(range(1), 2).shape, (1,))
        self.assertEqual(chunk(range(2), 2).shape, (1,))
        self.assertEqual(chunk(range(3), 2).shape, (2,))
        self.assertEqual(chunk(range(4), 2).shape, (2,))
        self.assertEqual(chunk(range(5), 2).shape, (3,))
        self.assertEqual(chunk(range(6), 2).shape, (3,))

    def test_chunk_with_index_with_full_last_chunk(self):
        chunks = list(chunk_with_index(range(6), 2))
        self.assertEqual(len(chunks), 3)
        self.assertTupleEqual(chunks[0], ([0, 1], 0, 2))
        self.assertTupleEqual(chunks[1], ([2, 3], 2, 4))
        self.assertTupleEqual(chunks[2], ([4, 5], 4, 6))

    def test_chunk_with_index_with_nonfull_last_chunk(self):
        chunks = list(chunk_with_index(range(5), 2))
        self.assertEqual(len(chunks), 3)
        self.assertTupleEqual(chunks[0], ([0, 1], 0, 2))
        self.assertTupleEqual(chunks[1], ([2, 3], 2, 4))
        self.assertTupleEqual(chunks[2], ([4], 4, 5))

    def test_chunk_with_index_with_one_full_chunk(self):
        chunks = list(chunk_with_index(range(2), 2))
        self.assertEqual(len(chunks), 1)
        self.assertTupleEqual(chunks[0], ([0, 1], 0, 2))

    def test_chunk_with_index_with_one_nonfull_chunk(self):
        chunks = list(chunk_with_index(range(1), 2))
        self.assertEqual(len(chunks), 1)
        self.assertTupleEqual(chunks[0], ([0], 0, 1))

    def test_chunk_with_index_with_no_chunk(self):
        chunks = list(chunk_with_index([], 2))
        self.assertEqual(len(chunks), 0)

    def test_chunk_with_index_shape(self):
        self.assertFalse(hasattr(chunk_with_index(islice([0], 1), 2), 'shape'))
        self.assertEqual(chunk_with_index([], 2).shape, (0,))
        self.assertEqual(chunk_with_index(range(1), 2).shape, (1,))
        self.assertEqual(chunk_with_index(range(2), 2).shape, (1,))
        self.assertEqual(chunk_with_index(range(3), 2).shape, (2,))
        self.assertEqual(chunk_with_index(range(4), 2).shape, (2,))
        self.assertEqual(chunk_with_index(range(5), 2).shape, (3,))
        self.assertEqual(chunk_with_index(range(6), 2).shape, (3,))
