from fritzconnection import FritzConnection


def run(address: str, user: str, password: str, command: str, ain: str) -> None:
    fc = FritzConnection(address=address, user=user, password=password)
    fc.call_http(command, ain)
