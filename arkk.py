#!/usr/bin/python3

import datetime
import PyPDF2
import os
import pickle
import sys
import yfinance as yf

def ReadPdf():
   '''Used once to extract raw text, not called in regular analysis'''

   # creating a pdf file object
   pdfFileObj = open('ARK_INNOVATION_ETF_ARKK_HOLDINGS_2020-04-14.pdf', 'rb')

   # creating a pdf reader object
   pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

   # printing number of pages in pdf file
   print(pdfReader.numPages)

   # creating a page object
   pageObj = pdfReader.getPage(0)

   # extracting text from page
   print(pageObj.extractText())

   pdfFileObj.close()

def LoadSyms(dateStr):
   symFile = f'{dateStr}.txt'
   syms = {}
   f = open(symFile, 'rt')
   while True:
      line = f.readline()
      if not line:
         break
      data = line.split()
      syms[data[0]] = { 'ratio': float(data[1]) / 100 }

   return syms

def NextDay(dateStr):
   date = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
   date += datetime.timedelta(days=1)
   return date.strftime('%Y-%m-%d')

def LoadPrice(syms, dateRange):
   fromDate = dateRange[0]
   toDate = dateRange[1]
   fromDate2 = NextDay(fromDate)
   toDate2 = NextDay(toDate)
   for sym in syms.keys():
      info = syms[sym]
      startPrice = yf.download(sym, start=fromDate, end=fromDate2)
      stopPrice = yf.download(sym, start=toDate, end=toDate2)
      startPriceAdjClose = startPrice['Adj Close'][0]
      stopPriceAdjClose = stopPrice['Adj Close'][0]
      print(f'{sym} ({fromDate} {startPriceAdjClose}) ({toDate} {stopPriceAdjClose})')
      info['startPrice'] = startPriceAdjClose
      info['stopPrice'] = stopPriceAdjClose

def CalcProfit(syms):
   startValue = 0
   endValue = 0
   for sym in syms.keys():
      info = syms[sym]
      startValue += info['startPrice'] * info['ratio']
      endValue += info['stopPrice'] * info['ratio']
   ratio = endValue / startValue
   print(f'EndValue / StartValue = {ratio:.2f}')

def main():
   # ReadPdf(); sys.exit(0) # convert PDF to text

   #dateRange = ['2019-10-28', '2020-04-14']
   dateRange = ['2020-04-14', '2020-08-06']

   syms = {'ARKK': {'ratio': 1}}
   LoadPrice(syms, dateRange)
   CalcProfit(syms)

   syms = LoadSyms(dateRange[0])
   LoadPrice(syms, dateRange)
   CalcProfit(syms)

if __name__ == '__main__':
   main()
