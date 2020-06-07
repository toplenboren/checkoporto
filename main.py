import socket
from settings import *
import argparse


def main():
    argparser = argparse.ArgumentParser(description='A simple app to check if your ports are closed')
    argparser.add_argument("port", help="A port.")
    args = argparser.parse_args()

    try:
        int(args.port)
    except TypeError:
        print("Provided port was not integer, please set a number")
        exit(0)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex((LOCALHOST, int(args.port)))
        if result == 0:
            print('The selected port is OPENED')
        else:
            print('The selected port is CLOSED')


if __name__ == "__main__":
    main()
