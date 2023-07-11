from configs import Config, ConfigHandler
from app.filesystem_accounter.filesystem_accounter_impl import FilesystemAccounterImpl

# Masking realization,
# so we don't thing about specific class in outside code
# and can switch realization class only here
FilesystemAccounter = FilesystemAccounterImpl


__all__ = ["FilesystemAccounter"]

