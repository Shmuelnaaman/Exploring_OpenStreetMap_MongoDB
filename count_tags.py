#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the
'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint
import operator


def count_tags(filename):
        SITE = ['amenity', 'brand', 'capacity', 'cuisine', 'denomination',
                'designation', 'dispensing', 'fee', 'historic',
                'internet_access', 'int_name', 'information', 'landuse',
                'leisure', 'leader', 'military', 'material', 'man_made',
                'name', 'Name', 'natural', 'operator', 'opening_hours',
                'payment', 'population', 'place', 'religion', 'recycling',
                'stars', 'sport', 'smoking', 'shop', 'trees', 'tourism',
                'toilets', 'website']

        ACCESS=['bus', 'bridge', 'barrier', 'bicycle', 'border_type',
                'boundary', 'cycleway', 'cutting', 'entrance', 'enforcement',
                'emergency', 'electrified', 'from', 'frequency', 'foot',
                'footway', 'fence_type', 'foot', 'gauge', 'highway', 'horse',
                'incline', 'junction', 'lit', 'lanes', 'motorcar',
                'motor_vehicle', 'motorcycle', 'maxspeed', 'maxheight',
                'network', 'public_transport', 'phone', 'parking', 'park_ride',
                'route', 'restriction', 'railway', 'surface', 'steps', 'sign',
                'service', 'two_sided', 'tunnel', 'tram', 'trail_visibility',
                'traffic_calming', 'tracktype', 'to', 'voltage', 'vehicle',
                'width', 'wheelchair', 'waterway']

        tags = {}
        KS = {'ACCESS': 0, 'SITE': 0}
        for line, value in ET.iterparse(filename):
            for tag in value.iter("tag"):
                if tag.attrib['k'].split(':')[0] in SITE:
                    KS['SITE'] = KS['SITE'] + 1
                elif tag.attrib['k'].split(':')[0] in ACCESS:
                    KS['ACCESS'] = KS['ACCESS'] + 1
                if tag.attrib['k'] in KS.keys():
                    KS[tag.attrib['k']] = KS[tag.attrib['k']] + 1
                else:
                    KS[tag.attrib['k']] = 1
            if value.tag in tags.keys():
                    tags[value.tag] = tags[value.tag] + 1
            else:
                    tags[value.tag] = 1

        sorted_x = sorted(KS.items(), key=operator.itemgetter(1))
        return tags, sorted_x
        # print tags


def test():
    matching = ['map_1.osm',
                'map_2.osm',
                'map_3.osm',
                'map_4.osm',
                'map_5.osm',
                'map_6.osm',
                'map_7.osm',
                'map_8.osm']
    matching = ['jeru.osm']
    for file in matching:
        tags, KS = count_tags(file)
        pprint.pprint(tags)
        pprint.pprint(KS)

if __name__ == "__main__":
    test()
