import os
import shutil
import subprocess
import time
import logging
import gtk
from sugar.activity.activity import Activity

logger = logging.getLogger('tuxpaint-activity')

class TuxPaintLauncher(Activity):

    def __init__(self, handle):
	print("TuxpaintActivity.__init__ ....")
	self.ready = False
	self.doc_path = os.environ.get('HOME') + './tuxpaint'
        
        # Initialize the parent
	Activity.__init__(self, handle)
        hbox = gtk.HBox()
        self.set_canvas(hbox)
        self.show_all()
	
	self.wait_to_run()
	self.close()        
   
    def wait_to_run(self):
	count = 0
	time.sleep(1)
	while count < 20:
	    print count
	    if self.ready == True:	
		self.run()
		return
	    time.sleep(0.1)
            count =+ count+1
	self.run()
 

    def run(self):
	if self.ready == True:
		print ("Starting and open file input ...")
		os.system ('tuxpaint --nolockfile --native --fullscreen 1 --noprint --savedir /home/ceibal/.tuxpaint --in-file /home/ceibal/.tuxpaint/saved/tux_pic_tmp.png &')
	else:
		print ("Starting ...")
		os.system ('tuxpaint --nolockfile --native --fullscreen 1 --noprint --savedir /home/ceibal/.tuxpaint &')
        
    def read_file(self, file_path):
	print('TuxpaintActivity.read_file: ' + file_path)
	self.file_tmp = '/home/ceibal/.tuxpaint/saved/tux_pic_tmp.png'
	os.remove(self.file_tmp)
	shutil.copy2(file_path, self.file_tmp)
	self.ready = True


    def get_documents_path(self):
        """Gets the path of the DOCUMENTS folder

        If xdg-user-dir can not find the DOCUMENTS folder it returns
        $HOME, which we omit. xdg-user-dir handles localization
        (i.e. translation) of the filenames.

        Returns: Path to $HOME/DOCUMENTS or None if an error occurs

        Code from src/jarabe/journal/model.py
        """
        try:
            pipe = subprocess.Popen(['xdg-user-dir', 'DOCUMENTS'],
                                    stdout=subprocess.PIPE)
            documents_path = os.path.normpath(pipe.communicate()[0].strip())
            if os.path.exists(documents_path) and \
                    os.environ.get('HOME') != documents_path:
                return documents_path
        except OSError, exception:
            if exception.errno != errno.ENOENT:
                logging.exception('Could not run xdg-user-dir')
        return None

