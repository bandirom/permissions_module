import argparse
from .models.urls import url_patterns

DEFAULT_PORT = 9000


def parse_arguments():
    """python main.py -db DB_NAME --host 192.168.0.25 etc.."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", required=False, help="DB name", action="store_true")
    parser.add_argument("-h", "--host", required=False, help="DB host", action="store_true")
    arguments = parser.parse_args()
    return arguments


def connect_to_db(arguments):
    """Here is the connection process"""
    return "connection"


def port_binding(port=None):
    """Binding port"""
    f"bind({port or DEFAULT_PORT})"
    return "success or error"


def entrypoint():
    arguments = parse_arguments()
    connect_to_db(arguments)
    port_binding(arguments.port)
    connect_endpoints()


def connect_endpoints():
    for url in url_patterns:
        """connect ur"""


if __name__ == '__main__':
    entrypoint()
