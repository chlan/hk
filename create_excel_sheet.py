#!/usr/bin/env python

import openpyxl as xl

wb= xl.load_workbook('template_bewertung_20191004.xlsx')

pl = [['Sasse', 'Jonas'],
      ['Sayman', 'Savas'],
      ['Schliemann', 'Tobias'],
      ['Schliewack', 'Leon'],
      ['Schlüter', 'Simon'],
      ['Schmidt', 'Leon Marc'],
     ]

print(pl)

for r in range(0, len(pl)):
    print(pl[r])
    n0= pl[r][0] + ', ' + pl[r][1]
    n1= pl[r][0] + '_' + pl[r][1]
    fn1= 'bewertung_' + n1 + '_CHL' + '.xlsx'
    fn2= 'bewertung_' + n1 + '.xlsx'
    print(r,n0, n1, fn1, fn2)
    wb= xl.load_workbook('template_bewertung_20191004.xlsx')
    sheet= wb['Dokumentation']
    cell= sheet.cell(7,2)
    cell.value= n0
    wb.save(fn1)
    wb.save(fn2)

