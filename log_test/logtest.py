#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import argparse

from logconf import LOGGING
import logging
import logging.config
import os
import sys


# load config from file
# print logconf
logging.config.dictConfig(LOGGING)
# logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

logger = logging.getLogger(__name__)


def main():
    print "main"
    logger.debug("yo debug")
    logger.info("yo info")
    logger.warn("yo warn")
    logger.error("yo error")
    logger.critical("yo critical")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=("script example "))
    parser.add_argument('conf', help='configuration file', type=str)
    parser.add_argument('--destination', '-d', help='a path', type=str)
    parser.add_argument('--verbose', '-v', help='verbose mode', action='store_true')
    args = parser.parse_args()
    shouldquit = False

    if not os.path.exists(args.conf):
        shouldquit = True
        print "configuration file  does not exist:" + args.conf.encode('utf-8')

    if shouldquit:
        sys.exit(1)

    conf = {}

    execfile(args.conf, conf)
    main()
