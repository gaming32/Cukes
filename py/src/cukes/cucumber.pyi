from typing import Union, List
from socket import AddressFamily


class CucumberClient:
    def __init__(self,
                 address_family: AddressFamily = ...): ...

    def connect(self,
                host: Union[str, bytes] = ...,
                port: int = ...,
                address: Union[tuple, str, bytes] = ...) -> None: ...

    def get_nodes(self) -> List: ...
