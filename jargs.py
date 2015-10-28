# -*- coding: utf-8 -*-
__author__ = 'panasko_ev'
#-------------------------------------------------------------------------------
# Name:        Модуль розбору переданих із командної строки параметрів
# Purpose: Параметри, що передаються повинні відповідати формату:
#  renFilesCon -mask [p[C], ![C], !obl, ...] -maskCountBeg [0, 1, ...] -path <шлях до папки де файли знаходяться> <перелік файлів для перейменування>
#
# Result: Формуються властивисті:
#  mask (str) - маска для перейменування файлів, - може містити [C] лічильник якщо файлів декілька,
#  mask_count_beg (int) - № з якого починати лічильник,
#  path (str) - шлях до папки де знаходяться файли, що потрібно перейменувати,
#  debug - включення режиму журналізації для відладки, без параметрів - наявність параметру включає режим формування лог-файла
#  lFiles (list) - список файлів для що потрібно перейменувати
#
# Author:      panasko_ev
#
# Created:     27.08.2015
# Copyright:   (c) panasko_ev 2015
# Licence:     Free
#-------------------------------------------------------------------------------
import argparse

class args(object):
	def __init__(self):
		parser=argparse.ArgumentParser(description="Перейменування групи файлів за вказаними правилами")
		parser.add_argument("-path", nargs="?", required=True, help="Шлях до файлів які треба перейменувати")
		parser.add_argument("-mask", nargs="?", required=True, help="Маска(шаблон), який застосовується для перейменування")
		parser.add_argument("-maskCountBeg", nargs="?", default="1", type=int, help="Початковий № для застосування в нумерації по масці(шаблону)")
		parser.add_argument("-debug", dest="log_mode", action="store_const", const="DEBUG", default="INFO", help="Включення режиму відладки")
		parser.add_argument("files", metavar="file_name", nargs="*", help="Перелік файлів, що потрібно перейменувати")

		arg=parser.parse_args()

		self.path=arg.path
		self.mask=arg.mask
		self.maskCountBeg=arg.maskCountBeg
		self.logMode=arg.log_mode
		self.files=arg.files