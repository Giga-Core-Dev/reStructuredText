#! /usr/bin/env python

"""
:Author: David Goodger
:Contact: goodger@users.sourceforge.net
:Revision: $Revision: 1.8 $
:Date: $Date: 2002/03/07 03:25:20 $
:Copyright: This module has been placed in the public domain.

English-language mappings for language-dependent features of
reStructuredText.
"""

__docformat__ = 'reStructuredText'

__all__ = ['directives']


from dps import nodes


directives = {
      'attention': 'attention',
      'caution': 'caution',
      'danger': 'danger',
      'error': 'error',
      'hint': 'hint',
      'important': 'important',
      'note': 'note',
      'tip': 'tip',
      'warning': 'warning',
      'image': 'image',
      'figure': 'figure',
      'contents': 'contents',
      'footnotes': 'footnotes',
      'citations': 'citations',
      'topic': 'topic',
      'meta': 'meta',
      'imagemap': 'imagemap',
      'raw': 'raw',
      'restructuredtext-test-directive': 'restructuredtext-test-directive'}
"""English name to registered (in directives/__init__.py) directive name
mapping."""
