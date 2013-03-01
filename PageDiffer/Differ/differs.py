#!/usr/bin/env python
import requests
from md5 import md5
import json
from argparse import ArgumentParser
from django.conf import settings

def diff_site(url, name):

    filename = "%s/%s" % (settings.DEFAULT_DIFF_STORAGE, name)

    try:
        hash_file = open(filename, "r")
        lines = json.load(hash_file)
        hash_file.close()
    except IOError:
        lines = []

    page_request = requests.get(url)
    content_hash = md5(page_request.content).hexdigest()
    
    return_value = False
    
    for line in lines:
        if content_hash != line:
            return_value = True
        
    hash_file = open(filename, "wb")
    lines.append(content_hash)
    json.dump(lines, hash_file)

    hash_file.close()

    return return_value

def command_line_controller():

    parser = ArgumentParser(description="Poll a site to see if there is a difference since your first poll.") 
    parser.add_argument('url', metavar="S", type=str, help="Site you want to poll.")
    parser.add_argument('name', metavar="N", type=str, help="Name you want to give this site.")
    args = parser.parse_args()
    diff_site(args.url, args.name)

if __name__ == '__main__':
    command_line_controller()
