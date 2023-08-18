#!/usr/bin/python3
''' Log parsing
'''


import sys


def print_stats(file_size, status_codes):
    '''Prints the stats
    '''
    print('File size: {:d}'.format(file_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print('{:s}: {:d}'.format(key, value))


if __name__ == '__main__':
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    file_size = 0
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            file_size += int(data[-1])
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
            if count % 10 == 0:
                print_stats(file_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_stats(file_size, status_codes)
    print_stats(file_size, status_codes)
    
