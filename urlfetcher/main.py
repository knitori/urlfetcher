#!/usr/bin/env python3

import os
import sys
import urlfetcher
import logging

FORMAT = '[%(asctime)-15s] %(message)s'
logging.basicConfig(
    format=FORMAT,
    level=logging.INFO,
    filemode='a',
    filename=os.path.expanduser('~/.logs/urlfetcher.log'))


def main():
    url = sys.argv[1]
    logging.info('Retrieving url {}'.format(url))
    try:
        result = urlfetcher.fetcher.fetch(url)
    except Exception as e:
        logging.exception(e)
        print('{}: {!s} (maybe corrupt or to big)'.format(type(e).__name__, e))
    else:
        print(' '.join(result.split()))
