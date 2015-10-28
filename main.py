# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name: renFileCon Головний модуль утиліти по перейменуванню файлів
# Purpose:
#
# Author:      panasko_ev
#
# Created:     21.08.2015
# Copyright:   (c) panasko_ev 2015
# Licence:     free
#-------------------------------------------------------------------------------
import jargs
import logging
import sys

from workrenfiles import processRenameFiles

def main(arg):
  """
  Основна робота програми по перейменуванню файлів
  """
  processRenameFiles(arg)

if __name__ == '__main__':
	#Розбір параметрів, що були передані за допомогою командної строки
	arg=jargs.args()
##	print "path=", arg.path
##	print "mask=", arg.mask
##	print "maskContBeg=", arg.maskContBeg
##	print "files=", arg.files
##	print "logMode=", arg.logMode

	#Ініціалізація підсистеми журнацізації
	# Словник перелік режимів журналізації
	logDict={
       u"DEBUG":logging.DEBUG, u"CRITICAL":logging.CRITICAL,
       u"ERROR":logging.ERROR, u"FATAL":logging.FATAL,
       u"WARN":logging.WARN, u"WARNING":logging.WARNING
      }
	#Настройка журналізації
	if unicode(arg.logMode) in logDict.keys():
		levLogging=logDict[unicode(arg.logMode)]
	else:
		levLogging = logging.INFO
	logging.basicConfig(
        format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
        filemode='w', filename=u'renFileCon.log', level=levLogging
      )
	logger = logging.getLogger(__name__)
	logger.info(u"Початок роботи та журналізації %s",  u"Програми по перейменуванню файлів")
	logger.info(u"Передаються параметри %s",  sys.argv)
	logger.debug(u"параметр path=%s",  arg.path)
	logger.debug(u"параметр mask=%s",  arg.mask)
	logger.debug(u"параметр maskContBeg=%s",  arg.maskCountBeg)
	logger.debug(u"параметр files=%s",  arg.files)

	main(arg)

	logger.info(u"Кінець роботи та журналізації %s",  u"Програми по перейменуванню файлів")
	print "end execute"
