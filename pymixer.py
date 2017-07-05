#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pymixer.py - wrapper for amixer command line tool

.. Created on 2017-07-05
.. Licence MIT
.. codeauthor:: Jan Lipovský <janlipovsky@gmail.com>, janlipovsky.cz
"""

import subprocess
import logging


class PyMixer(object):
    """
    Wrapping class for linux command line ``amixer`` to get/set volume

    **Example:**

    .. code-block:: python

        from pymixer import PyMixer

        mixer = PyMixer()

        # to set volume you can do just
        mixer.set_volume(50)

        # if you want to know current volume call
        volume = mixer.get_volume()
    """

    amixer = 'amixer'  #: linux command
    logger = None

    def __init__(self):
        self.logger = logging.getLogger("PyMixer")

    def set_volume(self, value):
        """
        Set volume to value (percent 0 - 100)

        :param int value: volume to set (percent 0 - 100)
        """

        if value < 0:
            self.logger.debug("Norm value to: 0")
            value = 0

        if value > 100:
            self.logger.debug("Norm value to: 100")
            value = 100

        volume = int((65536/100) * int(value))
        subprocess.call([self.amixer, "set", "Master", "{}".format(volume)])
        self.logger.info("Volume set to: {}%".format(value))

    def get_volume(self):
        """
        Get current level of volume

        :return: percent of current volume
        :rtype: int
        """
        temp = subprocess.check_output([self.amixer, "get", "Master"], universal_newlines=True)

        pos = str(temp).find('[')
        volume = temp[pos+1:pos+4]

        if volume[2] == '%':
            volume = volume[:2]

        return int(volume)
