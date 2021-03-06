#!/usr/bin/env python
# encoding: utf8

import socket
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit("Usage: %s <socket-filename> <command>" % sys.argv[0])
    filename = sys.argv[1]
    command = sys.argv[2]
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(filename)
    fd = s.makefile()
    fd.write(' '.join(sys.argv[2:])+'\n')
    fd.flush()
    resp=fd.read().split('\n')
    if len(resp) == 0:
        exit(1)
    else:
        sys.stdout.write('\n'.join(resp[1:]))
        exit(int(resp[0]))
