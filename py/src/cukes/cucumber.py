import socket
import _thread
from ._mixins import _CucumberMixin
from .error import InvalidDataError
from .internal_constants import Commands


class CucumberClient(_CucumberMixin):
    def __init__(self, address_family=socket.AF_INET):
        self.sock = socket.socket(address_family)

    def _handshake(self):
        self._send_chunks(Commands.initiate_handshake)
        done_check = self._recv_exact(2)
        if done_check != Commands.handshake_complete:
            raise InvalidDataError('invalid handshake end: %r' % done_check)

    def connect(self, host='localhost', port=28537, address=None):
        if address is None:
            address = (host, port)
        self.sock.connect(address)
        self._handshake()

    def get_nodes(self):
        pass


__all__ = ['CucumberClient']
