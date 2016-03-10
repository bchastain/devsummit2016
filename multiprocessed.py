import multiprocessing as mp
import time
import arcpy

# Function to map
def exportmap(filename):
    mxd = arcpy.mapping.MapDocument(r'C:\Users\bchastai\Documents\ArcGIS\census.mxd')
    arcpy.mapping.ExportToJPEG(mxd, filename, "",
                           1056, 816, 96, "",
                           "8-BIT_GRAYSCALE", 100)

if __name__ == '__main__':
    # Optional, default value anyways
    NUM_PROCESSES = mp.cpu_count()
    pool = mp.Pool(NUM_PROCESSES)
    out = r'C:\CGI\presentations\images\out'
    tic = time.clock()
    # Create list of filenames as our iterable
    filenames = ['%s%s.jpg' % (out, i) for i in range(100)]
    pool.map(exportmap, filenames)
    toc = time.clock()
    print (toc - tic)