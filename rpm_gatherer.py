import rpm
import os
import sys
import shutil


def copy_file(base, path):
    dest_folder = base + path[:-len(os.path.basename(path)) - 1]
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    try:
        shutil.copy(path, base + path)
    except IOError:
        print(('File \'%s\' not found.' % path))


def print_header(header):
    for files in header.fiFromHeader():
        copy_file(base, files[0])


def read_rpm_header(ts, rpm_name):
    rpm_file = os.open(rpm_name, os.O_RDONLY)
    header = ts.hdrFromFdno(rpm_file)
    os.close(rpm_file)
    return header


def open_rpm(rpm_name):
    ts = rpm.TransactionSet()
    header = read_rpm_header(ts, rpm_name)
    print_header(header)


if len(sys.argv) != 3:
    sys.exit('Usage: %s target_file.rpm destination_path' % sys.argv[0])

try:
    base = sys.argv[2]
    open_rpm(sys.argv[1])
    print('Done!')
except:
    sys.exit('RPM file error!')