__all__ = ['chunk', 'chunk_with_index']

import pkg_resources
__version__ = pkg_resources.get_distribution("dchunk").version

from .chunking import chunk, chunk_with_index
