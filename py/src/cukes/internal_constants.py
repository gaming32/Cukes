from .constants import *


class Commands:
    initiate_handshake = b'\x00'
    handshake_complete = b'\x01'
    get_nodes = b'\x10'


for command in dir(Commands):
    command_value = getattr(Commands, command)
    if command[0] == '_' or not isinstance(command_value, bytes):
        continue
    setattr(Commands, command, command_value.rjust(2, '\0'))
del command, command_value
