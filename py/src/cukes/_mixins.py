class _CucumberMixin:

    def _send_chunks(self, data, chunk=8192):
        """expects:
hasattr(self, 'sock: socket.socket')'"""
        while data:
            data_to_send, data = data[:chunk], data[chunk:]
            self.sock.send(data_to_send)

    def _recv_exact(self, bufsize, chunk=8192, flags=0):
        """expects:
hasattr(self, 'sock: socket.socket')'"""
        left = min(bufsize, chunk)
        data = b''
        while left:
            newbc = min(chunk, left)
            try:
                newdata = self.sock.recv(newbc)
            except ConnectionError:
                break
            data += newdata
            left -= newbc
        return data
