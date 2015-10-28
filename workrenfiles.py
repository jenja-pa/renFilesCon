# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 16:12:05 2015

@author: panasko_ev
"""

import os.path
import logging
from os import rename, remove

def processRenameFiles(pars):
  """
  Проведення роботи по перейменуванню файлів
  """

  # Перевіряємо чи існує папка в якій буде проводитись робота
  logger = logging.getLogger(__name__)
  print "processRenameFiles"
  workPath=pars.path.replace('"','')
  if not os.path.exists (workPath):
    logger.debug(u"шлях для проведення роботи:%s НЕ існує",  workPath)
    return

  #Визначаємо кількість файлів, що потрібно перейменувати
  listFilesTemp=pars.files
  listFiles=[]
  #оскільки із-за невідомої ревлізації імена файлів які містять пробіли, б'ються
  #на частина навіть якщо вони взяті в кавички, то додатково обробимо отриманий
  #список файлів
  lst=[] # список для накоплення частин імені файла
  for el in listFilesTemp:
    if el.find(".")>0 and el.find('"')==-1: #.-є, і "-немає - назва файла без пробілів
      listFiles.append(el)
    else:
      lst.append(el)
      if el.find('"')>0 and len(lst)!=0: # останній фрагмент імені ф-ла
        listFiles.append(" ".join(lst).replace('"',''))
        lst=[]
  logger.debug(u"файли для обробки:%s",  listFiles)

  countFiles=len(listFiles)
  logger.debug(u"кількість файлів для обробки:%d",  countFiles)
  #Визначимо потрібну кількість розрядів лічильника по кількості файлів для обробки
  lenDiginCounter=len("{0:d}".format(countFiles))
  if lenDiginCounter==1:
      lenDiginCounter+=1
  logger.debug(u"кількість розрядів для лічильника:%d",  lenDiginCounter)

  # Визначаємо чи потрібно застосовувати лічильник для генерації, та
  #  підправляємо його формат
  mask=pars.mask
  presentCounter = False
  if pars.mask.find("[C]"):
    logger.debug(u"лічильник для генерації номерів існує, має вигляд:%s",  mask)
    mask = mask.replace("[C]", "{0:0%dd}" %(lenDiginCounter))
    presentCounter = True
    logger.debug(u"лічильник для генерації номерів змінений на форматну строку:%s",  mask)

  beginCounter = pars.maskCountBeg
  logger.debug(u"розпочинати генерацію з числа :%d",  beginCounter)

  if presentCounter:  # Якщо у шаблоні імені є лічильник
    logger.debug(u"counter present")
    fname_ch = [] #файли зі зміненими іменами, що потрібно буде перенести
    for f in listFiles:
      ext=f.split(".")[1].lower()
      logger.debug(u"rename: %s to %s", os.path.join(workPath, f), os.path.join(workPath, mask.format(beginCounter)+"."+ext))
      if os.path.isfile(os.path.join(workPath, f)):  #якщо файл існує
        rename(os.path.join(workPath, f), "".join([mask.format(beginCounter),".",ext]))
        fname_ch.append("".join([mask.format(beginCounter),".",ext]))
        logger.debug(u"змінюємо файл %s на %s",  f, mask.format(beginCounter))
        beginCounter+=1
    #Безпечне перенесення файлів в папку призначення
    for f in fname_ch:
        logger.debug(u"Переносимо файл %s в %s",  f, os.path.join(workPath, f))
        safety_remove_file(f, os.path.join(workPath, f))
    

  else:  # Якщо у шаблоні імені відсутній лічильник перейменувати ільки 1 файл
    if os.path.isfile(os.path.join(workPath, listFiles[0])):  #якщо файл існує
      ext=listFiles[0].split(".")[1].lower()
      rename(os.path.join(workPath, listFiles[0]), os.path.join([mask,".",ext]))
      logger.debug(u"змінюємо файл %s на %s",  listFiles[0], mask)
      logger.debug(u"Переносимо файл %s в %s", os.path.join(mask,".",ext), os.path.join(workPath, "".join([mask,".",ext])))
      safety_remove_file(os.path.join(mask,".",ext), os.path.join(workPath, "".join([mask,".",ext])))

def safety_remove_file(src, dst):
    one_save_del="!fordel" #префікс для одноразового збереження
    #Перевірка існування файла dst
    if os.path.isfile(dst):
        #файл присутній треба його перейменувати для одноразового збереження - перед іменем добавимо !fordel_
        pn, fn=os.path.split(dst)
        #якщо таке збереження існує, видаляємо його безповоротно        
        if os.path.isfile(os.path.join(pn, one_save_del+fn)):
            remove(os.path.join(pn, one_save_del+fn))
        #Проводимо перейменування існуючого файла dst в !fordel_dst
        rename(dst, os.path.join(pn, one_save_del+fn))
    #Переносимо потрібний файл
    rename(src, dst)