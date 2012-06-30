# coding: utf-8

PROP_DESCRIPTORS = ['String']

import sys
name = 'semistructured.django_sdb'
__import__(name)
prop = sys.modules[name]

_tmp = __import__('django_sdb', globals(), locals(), ['Persistent'], -1)
Persistent = _tmp.Persistent

