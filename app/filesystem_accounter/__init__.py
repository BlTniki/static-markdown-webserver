from configs import Config, ConfigHandler
from app.filesystem_accounter.filesystem_accounter_impl import FilesystemAccounterImpl


dirtree_accounter = FilesystemAccounterImpl(ConfigHandler.get_config())


__all__ = ["dirtree_accounter"]

