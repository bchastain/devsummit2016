import time
import arcpy

mxd = arcpy.mapping.MapDocument(r'C:\CGI\presentations\testmap.mxd')
out = r'C:\CGI\presentations\images\out'
tic = time.clock()
for i in range(0,100):
	arcpy.mapping.ExportToJPEG(mxd, '%s%s.jpg' % (out, i), '',
                           	   1056, 816, 96, '', '8-BIT_GRAYSCALE', 100)
toc = time.clock()
print (toc - tic)