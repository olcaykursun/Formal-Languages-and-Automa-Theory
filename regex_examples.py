# -*- coding: utf-8 -*-
"""regex examples.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15B7YiKneRQ2oV0pCW9BOeVmfbKE4ziEj
"""

import re

members = '''abbcbcaaa
abaaaa
cccbbbaaa
cbcaaaaaa
aaa
ccbaaa
cccaaa'''

nonmembers = '''abc
ac
aaaa
a

cccbbbbbba
aaaab'''

pattern = re.compile(r'^([abc]{3})*aaa$', re.MULTILINE)   
#alphabet of {a,b,c} and it ends with aaa and the length is a multiple of 3

#let us check if only the member strings are matched with the expression
matches = set([x.group(0) for x in pattern.finditer(members+'\n'+nonmembers)])
print(matches == set(members.split('\n')))
print(matches)

import re

members = '''abbcbcabb
abaaba
cccbbbaaaccc
cbcaaaaaacbc
aaa
ccbccb
cccccc'''

nonmembers = '''abcc
ac
aaaa
a

cccbbbbbba
aaaab'''

pattern = re.compile(r'^([abc]{3})(([abc]{3})*\1)?$', re.MULTILINE)   
#alphabet of {ab,c} and it ends with the same 3-symbols it starts with and the length is a multiple of 3

#let us check if only the member strings are matched with the expression
matches = set([x.group(0) for x in pattern.finditer(members+'\n'+nonmembers)])
print(matches == set(members.split('\n')))
print(matches)

import re

members = '''abbcbcabb
abaaba
cccbbbaaaccc
cbcaaaaaacbc
aaa
zzz
123aba123
___
ccbccb
cccccc'''

nonmembers = '''abcc
ac
aaaa
a

cccbbbbbba
aaaab'''

pattern = re.compile(r'^(\w{3})((\w{3})*\1)?$', re.MULTILINE)   
#alphabet is alphanumeric characters and it ends with the same 3-symbols it starts with and the length is a multiple of 3

#let us check if only the member strings are matched with the expression
matches = set([x.group(0) for x in pattern.finditer(members+'\n'+nonmembers)])
print(matches == set(members.split('\n')))
print(matches)