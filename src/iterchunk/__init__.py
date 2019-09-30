__all__ = ['chunk', 'chunk_with_index']

import pkg_resources
__version__ = pkg_resources.get_distribution("iterchunk").version

from .chunking import chunk, chunk_with_index
