"""
.. module:: xformatting
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains functions for formatting text.

.. note:: The modules that are named `xsomething` like this module are prefixed with an `x` character to
          indicate they extend the functionality of a base python module and the `x` is pre-pended to
          prevent module name collisions with python modules.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

from typing import List

from io import StringIO

class CommandOutputFormat:
    DISPLAY = 0
    JSON = 1
    YAML = 2

def indent_lines(msg: str, level: int, indent: int=4) -> str:
    """
        Takes a string and splits it into multiple lines, then indents each line
        to the specified level using 'indent' spaces for each level.

        :param msg: The text content to split into lines and then indent.
        :param level: The integer level number to indent to.
        :param indent: The number of spaces to indent for each level.

        :returns: The indenting content
    """
    # Split msg into lines keeping the line endings
    msglines = msg.splitlines(True)

    pfx = " " * (level * indent)

    indented = StringIO()
    for nxtline in msglines:
        indented.write(pfx)
        indented.write(nxtline)

    return indented.getvalue()

def indent_line(lcontent: str, level: int, indent: int, pre_strip_leading: bool=True) -> str:
    """
        Takes a string and indents it to the specified level using 'indent' spaces
        for each level.

        :param lcontent: The text line to indent.
        :param level: The integer level number to indent to.
        :param indent: The number of spaces to indent for each level.
        :param pre_strip_leading: Strip any leading whitesspace before indenting the line.

        :returns: The indented line
    """
    pfx = " " * (level * indent)

    indented = None
    if pre_strip_leading:
        indented = "{}{}".format(pfx, lcontent.lstrip())
    else:
        indented = "{}{}".format(pfx, lcontent)

    return

def split_and_indent_lines(msg: str, level: int, indent: int=4, pre_strip_leading: bool=True) -> List[str]:
    """
        Takes a string and splits it into multiple lines, then indents each line
        to the specified level using 'indent' spaces for each level.

        :param msg: The text content to split into lines and then indent.
        :param level: The integer level number to indent to.
        :param indent: The number of spaces to indent for each level.
        :param pre_strip_leading: Strip any leading whitesspace before indenting the lines.

        :returns: The indenting lines
    """

    # Split msg into lines keeping the line endings
    msglines = msg.splitlines(False)

    pfx = " " * (level * indent)

    indented = None
    if pre_strip_leading:
        indented = [pfx + nxtline.lstrip() for nxtline in msglines]
    else:
        indented = [pfx + nxtline for nxtline in msglines]

    return indented
