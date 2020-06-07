import socket
from settings import *
import argparse


def main():
    argparser = argparse.ArgumentParser(description='A simple app to check if your ports are closed')
    argparser.add_argument("port", help="A port.")
    args = argparser.parse_args()

    try:
        a = int(args.port)
        if a < 0 or a > 65535:
            raise ValueError()
    except ValueError:
        print("Provided port was not valid, please set a number between 0 and 65535")
        exit(0)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex((LOCALHOST, int(args.port)))
        if result == 0:
            print('The selected port is OPENED')
        else:
            print('The selected port is CLOSED')


if __name__ == "__main__":
    main()
