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
	logger.info("TuxpaintActivity.__init__ ....")
        self.prepare_all()
        # Initialize the parent
	Activity.__init__(self, handle)
        hbox = gtk.HBox()
        self.set_canvas(hbox)
        self.show_all()
	
	self.wait_to_run()
	self.close()        

    def prepare_all(self):
	self.ready = False
	self.savedir = os.path.join(os.environ.get('HOME'),'.tuxpaint')
	self.file_tmp = os.path.join(self.savedir, 'saved/tux_pic_tmp.png')
	self.convert_script = './tuxpaint-import.sh'	
	
	if not os.path.exists(self.savedir):
	    os.mkdir(self.savedir)
	
	if not os.path.exists(os.path.join(self.savedir,'saved')):
	    os.mkdir(os.path.join(self.savedir,'saved'))		
   
    def wait_to_run(self):
	count = 0
	time.sleep(1)
	while count < 15:
	    if self.ready == True:	
		self.run()
		return
	    time.sleep(0.1)
            count =+ count+1
	self.run()
 

    def run(self):
	if self.ready == True:
		logger.info ("Starting and open file input ...")
		os.system ('tuxpaint --nolockfile --native --fullscreen 1 --noprint --savedir /home/ceibal/.tuxpaint --in-file /home/ceibal/.tuxpaint/saved/tux_pic_tmp.png &')
	else:
		logger.info ("Starting ...")
		os.system ('tuxpaint --nolockfile --native --fullscreen 1 --noprint --savedir /home/ceibal/.tuxpaint &')
        
    def read_file(self, file_path):
	logger.info('TuxpaintActivity.read_file: ' + file_path)
	
	if os.path.isfile(self.file_tmp):
		os.remove(self.file_tmp)
	
	if '.png' in file_path:
		shutil.copy(file_path, self.file_tmp)
	else:
		os.system(self.convert_script +' '+ file_path)
	self.ready = True



