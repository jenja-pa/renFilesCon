# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        setup - Створення win exe файла із даного проекта
# Purpose:
#
# Author:      panasko_ev
#
# Created:     02.10.2015
# Copyright:   (c) panasko_ev 2015
# Licence:     free
#
# Run to generate exe python setup.py py2exe
#-------------------------------------------------------------------------------
def main():
	from distutils.core import setup
	import py2exe
	setup(console=['main.py'])

if __name__ == '__main__':
    main()
