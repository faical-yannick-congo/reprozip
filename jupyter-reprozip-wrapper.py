#!/usr/bin/env python

from datetime import datetime
import logging
import os
import shutil
import subprocess
import sys
import tempfile


logger = logging.getLogger('jupyter-reprozip')


def main():
    logging.basicConfig(level=logging.DEBUG,
                        filename='/tmp/jupyter-reprozip.log')

    kernel_id = datetime.now().strftime("%Y-%m-%d_%H-%M_%S")
    kernel_dir = os.path.join(tempfile.gettempdir(), kernel_id)
    kernel_pack = os.path.join(tempfile.gettempdir(), '%s.rpz' % kernel_id)

    connection_file = os.path.join(tempfile.gettempdir(),
                                   '%s.conn' % kernel_id)
    shutil.copyfile(sys.argv[1], connection_file)

    logger.info("Starting kernel trace")
    args = [connection_file if a == 'RPZ_CONNECTION_FILE' else a
            for a in sys.argv[2:]]
    proc = subprocess.Popen([
        '/home/vagrant/venv27/bin/reprozip', '-v',
        'trace', '-d', kernel_dir] + args,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.communicate()[0]
    logger.debug(out)

    logger.info("Kernel finished, running pack")
    proc = subprocess.Popen([
        'reprozip', '-v',
        'pack', '-d', kernel_dir, kernel_pack],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.communicate()[0]
    logger.debug(out)

    # TODO: Remove py/pyc files from inputs, add the connection file under a
    # fixed name

    logging.info("Packing done")


if __name__ == '__main__':
    main()
