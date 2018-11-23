# Python Sop snippet to get USGS data
downloaded_csv = hou.pwd().evalParm('earthquakedata')

from eqDataVisLib import usgsData
usgsCsv = usgsData.UsgsCsv(downloaded_csv)
usgsCsv.getData()
