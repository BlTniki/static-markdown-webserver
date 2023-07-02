from config import Config
from .filesystem_accounter_impl import FilesystemAccounterImpl

dirtree_accounter = FilesystemAccounterImpl(Config())

__all__ = ["dirtree_accounter"]
