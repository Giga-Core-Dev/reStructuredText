#! /usr/bin/env python

"""
:Author: David Goodger
:Contact: goodger@users.sourceforge.net
:Revision: $Revision: 1.1 $
:Date: $Date: 2002/03/12 03:33:03 $
:Copyright: This module has been placed in the public domain.

Tests for unknown directives.
"""

import RSTTestSupport

def suite():
    s = RSTTestSupport.ParserTestSuite()
    s.generateTests(totest)
    return s

totest = {}

totest['unknown'] = [
["""\
.. reStructuredText-unknown-directive::

.. reStructuredText-unknown-directive:: argument

.. reStructuredText-unknown-directive::
   block
""",
"""\
<document>
    <system_message level="3" type="ERROR">
        <paragraph>
            Unknown directive type "reStructuredText-unknown-directive" at line 1.
        <literal_block>
            .. reStructuredText-unknown-directive::
    <system_message level="3" type="ERROR">
        <paragraph>
            Unknown directive type "reStructuredText-unknown-directive" at line 3.
        <literal_block>
            .. reStructuredText-unknown-directive:: argument
    <system_message level="3" type="ERROR">
        <paragraph>
            Unknown directive type "reStructuredText-unknown-directive" at line 5.
        <literal_block>
            .. reStructuredText-unknown-directive::
               block
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
