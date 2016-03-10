from Queue import Queue
from threading import Thread
import time

import arcpy


class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            filename = self.queue.get()
            mxd = arcpy.mapping.MapDocument(r'C:\CGI\presentations\testmap.mxd')
            arcpy.mapping.ExportToJPEG(mxd, filename, '',
                                       1056, 816, 96, '', '8-BIT_GRAYSCALE', 100)
            self.queue.task_done()

if __name__ == '__main__':    
    tic = time.clock()
    out = r'C:\CGI\presentations\images\out'
    filenames = []
    for i in range(0,100):
        filenames.append('%s%s.jpg' % (out, i))
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    for x in range(8):
        worker = DownloadWorker(queue)
        # Setting daemon to True will let the main thread exit even
        # though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    for file in filenames:
        print 'Queueing {}'.format(file)
        queue.put(file)
    # Causes the main thread to wait for the queue to finish processing
    # all the tasks
    queue.join()
    print 'Took {}'.format(time.clock() - tic)