#! /usr/bin/env python

"""
:Author: David Goodger
:Contact: goodger@users.sourceforge.net
:Revision: $Revision: 1.10 $
:Date: $Date: 2002/04/18 02:40:50 $
:Copyright: This module has been placed in the public domain.

Tests for states.py.
"""

import RSTTestSupport

def suite():
    s = RSTTestSupport.ParserTestSuite()
    s.generateTests(totest)
    return s

totest = {}

totest['option_lists'] = [
["""\
Short options:

-a       option -a

-b file  option -b

-c name  option -c
""",
"""\
<document>
    <paragraph>
        Short options:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -a
            <description>
                <paragraph>
                    option -a
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -b
                    <option_argument delimiter=" ">
                        file
            <description>
                <paragraph>
                    option -b
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -c
                    <option_argument delimiter=" ">
                        name
            <description>
                <paragraph>
                    option -c
"""],
["""\
Long options:

--aaaa       option --aaaa
--bbbb=file  option --bbbb
--cccc name  option --cccc
--d-e-f-g    option --d-e-f-g
--h_i_j_k    option --h_i_j_k
""",
"""\
<document>
    <paragraph>
        Long options:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --aaaa
            <description>
                <paragraph>
                    option --aaaa
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --bbbb
                    <option_argument delimiter="=">
                        file
            <description>
                <paragraph>
                    option --bbbb
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --cccc
                    <option_argument delimiter=" ">
                        name
            <description>
                <paragraph>
                    option --cccc
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --d-e-f-g
            <description>
                <paragraph>
                    option --d-e-f-g
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --h_i_j_k
            <description>
                <paragraph>
                    option --h_i_j_k
"""],
["""\
Old GNU-style options:

+a       option +a

+b file  option +b

+c name  option +c
""",
"""\
<document>
    <paragraph>
        Old GNU-style options:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        +a
            <description>
                <paragraph>
                    option +a
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        +b
                    <option_argument delimiter=" ">
                        file
            <description>
                <paragraph>
                    option +b
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        +c
                    <option_argument delimiter=" ">
                        name
            <description>
                <paragraph>
                    option +c
"""],
["""\
VMS/DOS-style options:

/A        option /A
/B file   option /B
/CCC      option /CCC
/DDD string  option /DDD
/EEE=int  option /EEE
""",
"""\
<document>
    <paragraph>
        VMS/DOS-style options:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        /A
            <description>
                <paragraph>
                    option /A
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        /B
                    <option_argument delimiter=" ">
                        file
            <description>
                <paragraph>
                    option /B
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        /CCC
            <description>
                <paragraph>
                    option /CCC
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        /DDD
                    <option_argument delimiter=" ">
                        string
            <description>
                <paragraph>
                    option /DDD
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        /EEE
                    <option_argument delimiter="=">
                        int
            <description>
                <paragraph>
                    option /EEE
"""],
["""\
Mixed short, long, and VMS/DOS options:

-a           option -a
--bbbb=file  option -bbbb
/C           option /C
--dddd name  option --dddd
-e string    option -e
/F file      option /F
""",
"""\
<document>
    <paragraph>
        Mixed short, long, and VMS/DOS options:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -a
            <description>
                <paragraph>
                    option -a
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --bbbb
                    <option_argument delimiter="=">
                        file
            <description>
                <paragraph>
                    option -bbbb
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        /C
            <description>
                <paragraph>
                    option /C
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --dddd
                    <option_argument delimiter=" ">
                        name
            <description>
                <paragraph>
                    option --dddd
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -e
                    <option_argument delimiter=" ">
                        string
            <description>
                <paragraph>
                    option -e
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        /F
                    <option_argument delimiter=" ">
                        file
            <description>
                <paragraph>
                    option /F
"""],
["""\
Aliased options:

-a, --aaaa, /A                 option -a, --aaaa, /A
-b file, --bbbb=file, /B file  option -b, --bbbb, /B
""",
"""\
<document>
    <paragraph>
        Aliased options:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -a
                <option>
                    <option_string>
                        --aaaa
                <option>
                    <option_string>
                        /A
            <description>
                <paragraph>
                    option -a, --aaaa, /A
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -b
                    <option_argument delimiter=" ">
                        file
                <option>
                    <option_string>
                        --bbbb
                    <option_argument delimiter="=">
                        file
                <option>
                    <option_string>
                        /B
                    <option_argument delimiter=" ">
                        file
            <description>
                <paragraph>
                    option -b, --bbbb, /B
"""],
["""\
Multiple lines in descriptions, aligned:

-a       option -a, line 1
         line 2
-b file  option -b, line 1
         line 2
""",
"""\
<document>
    <paragraph>
        Multiple lines in descriptions, aligned:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -a
            <description>
                <paragraph>
                    option -a, line 1
                    line 2
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -b
                    <option_argument delimiter=" ">
                        file
            <description>
                <paragraph>
                    option -b, line 1
                    line 2
"""],
["""\
Multiple lines in descriptions, not aligned:

-a  option -a, line 1
    line 2
-b file  option -b, line 1
    line 2
""",
"""\
<document>
    <paragraph>
        Multiple lines in descriptions, not aligned:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -a
            <description>
                <paragraph>
                    option -a, line 1
                    line 2
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -b
                    <option_argument delimiter=" ">
                        file
            <description>
                <paragraph>
                    option -b, line 1
                    line 2
"""],
["""\
Descriptions begin on next line:

-a
    option -a, line 1
    line 2
-b file
    option -b, line 1
    line 2
""",
"""\
<document>
    <paragraph>
        Descriptions begin on next line:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -a
            <description>
                <paragraph>
                    option -a, line 1
                    line 2
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -b
                    <option_argument delimiter=" ">
                        file
            <description>
                <paragraph>
                    option -b, line 1
                    line 2
"""],
["""\
Multiple body elements in descriptions:

-a  option -a, para 1

    para 2
-b file
    option -b, para 1

    para 2
""",
"""\
<document>
    <paragraph>
        Multiple body elements in descriptions:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -a
            <description>
                <paragraph>
                    option -a, para 1
                <paragraph>
                    para 2
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        -b
                    <option_argument delimiter=" ">
                        file
            <description>
                <paragraph>
                    option -b, para 1
                <paragraph>
                    para 2
"""],
["""\
--option
empty item above, no blank line
""",
"""\
<document>
    <paragraph>
        --option
        empty item above, no blank line
"""],
["""\
An option list using equals:

--long1=arg1  Description 1
--long2=arg2  Description 2

An option list using spaces:

--long1 arg1  Description 1
--long2 arg2  Description 2

An option list using mixed delimiters:

--long1=arg1  Description 1
--long2 arg2  Description 2

An option list using mixed delimiters in one line:

--long1=arg1, --long2 arg2  Description
""",
"""\
<document>
    <paragraph>
        An option list using equals:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --long1
                    <option_argument delimiter="=">
                        arg1
            <description>
                <paragraph>
                    Description 1
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --long2
                    <option_argument delimiter="=">
                        arg2
            <description>
                <paragraph>
                    Description 2
    <paragraph>
        An option list using spaces:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --long1
                    <option_argument delimiter=" ">
                        arg1
            <description>
                <paragraph>
                    Description 1
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --long2
                    <option_argument delimiter=" ">
                        arg2
            <description>
                <paragraph>
                    Description 2
    <paragraph>
        An option list using mixed delimiters:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --long1
                    <option_argument delimiter="=">
                        arg1
            <description>
                <paragraph>
                    Description 1
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --long2
                    <option_argument delimiter=" ">
                        arg2
            <description>
                <paragraph>
                    Description 2
    <paragraph>
        An option list using mixed delimiters in one line:
    <option_list>
        <option_list_item>
            <option_group>
                <option>
                    <option_string>
                        --long1
                    <option_argument delimiter="=">
                        arg1
                <option>
                    <option_string>
                        --long2
                    <option_argument delimiter=" ">
                        arg2
            <description>
                <paragraph>
                    Description
"""],
["""\
Some edge cases:

--option=arg arg  too many arguments

--option=arg,arg  not supported (yet?)

--option=arg=arg  too many arguments

--option arg arg  too many arguments

-a letter arg2    too many arguments

/A letter arg2    too many arguments

--option=         argument missing

--=argument       option missing

--                everything missing

-                 this should be a bullet list item

These next ones should be simple paragraphs:

-1

--option

--1

-1 and this one too.
""",
"""\
<document>
    <paragraph>
        Some edge cases:
    <paragraph>
        --option=arg arg  too many arguments
    <paragraph>
        --option=arg,arg  not supported (yet?)
    <paragraph>
        --option=arg=arg  too many arguments
    <paragraph>
        --option arg arg  too many arguments
    <paragraph>
        -a letter arg2    too many arguments
    <paragraph>
        /A letter arg2    too many arguments
    <paragraph>
        --option=         argument missing
    <paragraph>
        --=argument       option missing
    <paragraph>
        --                everything missing
    <bullet_list bullet="-">
        <list_item>
            <paragraph>
                this should be a bullet list item
    <paragraph>
        These next ones should be simple paragraphs:
    <paragraph>
        -1
    <paragraph>
        --option
    <paragraph>
        --1
    <paragraph>
        -1 and this one too.
"""],
]

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
