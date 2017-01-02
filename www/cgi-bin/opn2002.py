#!/usr/bin/env python

from cs1504 import CS1504
import sys, time, serial

########################################################################
# Symbols for Serial Data
STX = '\x02'
ETX = '\x03'
########################################################################



class OPN2002(CS1504):
  """ Extend the existing USB class for OPN devices that use ASCII """

   def __init__(self, port='/dev/cu.usbserial'):
      self.os_vers = None

   def interrogate(self, cmd):
   """ Gets data from OPN_2002 type timer """
      self.send(cmd)
      time.sleep(0.6) 
      data = self.recv(20000)
      return data

   def send(self, cmd):
   """Send a command to the OPN_2002 timer"""
      self.ser.write(STX+cmd+ETX)

   def is_ascii(self, s):
   """ Verifies is value is within ASCII character set """
      return all(30 < ord(c) < 128 for c in s)

   def recv(self, length=MAX_RESP):
   """Receive a response. For fixed-size responses, specifying it will take
      less time as we won't need to wait for the timeout to return data
   """
      rawdata = self.ser.read(length)

      data=[]

      for num in range(length):
        
        if (rawdata[num] == STX):
             continue

        if (rawdata[num] != ETX):
            if (self.is_ascii(rawdata[num])):
                data.append(rawdata[num])

        else:
            break

     return data
