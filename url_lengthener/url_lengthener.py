import requests
import sys
import argparse
from requests.exceptions import ConnectionError

def get_url_info(short_url):
    '''Gets user info about the url'''
    try:
        response = requests.get(short_url)

        url_info = {}
        url_info['status'] = response.status_code
        url_info['url'] = response.url
        url_info['encoding'] = response.apparent_encoding

        return url_info
    except ConnectionError as e:
        return None

def usage():
    '''Prints usage'''
    print('python url_lengthener.py <short_url>')

if __name__=='__main__':
    if len(sys.argv) != 2:
        usage()
        exit(0)
    else:
        url_info = get_url_info(sys.argv[1])
        if url_info:
            for k,v in url_info.iteritems():
                print('{0}: {1}'.format(k, v))
        else:
            print('Invald url: {0}'.format(sys.argv[1]))

