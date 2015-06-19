

def parse_file():
    matching = ['map_1.osm',
                'map_2.osm',
                'map_3.osm',
                'map_4.osm',
                'map_5.osm',
                'map_6.osm',
                'map_7.osm',
                'map_8.osm']
    file_out = "{}.osm".format('jeru')
    n = -1
    for file in matching:
        with open(file, 'rb') as f1:
            for line in f1:
                if '<?xml version="1.0" encoding="UTF-8"?>' in line:
                    n += 1
                    if n == 0:
                        with open(file_out, 'w') as f2:
                            f2.write(line)
                    else:
                        next(f1)
                else:
                    if '<osm ' in line and n == 0:
                        with open(file_out, 'a') as f2:
                            f2.write(line)
                    elif '<osm ' in line and n != 0:
                        pass
                    elif '</osm>' in line and n == (len(matching)-1):
                        with open(file_out, 'a') as f2:
                            f2.write(line)
                    elif '</osm>' in line and n != (len(matching)-1):
                        pass
                    elif '<osm ' not in line and '</osm>' not in line:
                        with open(file_out, 'a') as f2:
                            f2.write(line)
    f2.close()
