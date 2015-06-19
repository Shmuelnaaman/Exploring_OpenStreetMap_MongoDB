#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""


def get_user(element):
    return


def process_map(filename):
    users = set()
    users_m = []
    add_m = []
    for _, element in ET.iterparse(filename):
            if "uid"in element.keys():
                users_m.append(element.attrib['uid'])
                add_m.append(element.attrib['uid'])
    users = set(users_m)
    return users


def test():

    users = process_map('jeru.osm')
    # pprint.pprint(users)
    print len(set(users))


if __name__ == "__main__":
    test()
    