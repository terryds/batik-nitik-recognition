import tensorflow as tf
import sys
import os
import tkinter as tk

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Disable tensorflow compilation warnings
# os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# import tensorflow as tf

# image_path = sys.argv[1]


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Batik Recognizer")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Exit",command=self.client_exit)
        quitButton.place(x=430, y=550, anchor=NW)
        imageButton = Button(self, text="load image", command=self.showImg)
        imageButton.place(x=40,y=550, anchor=NW)
        clearButton = Button(self, text="clear image", command=self.clearImg)
        clearButton.place(x=180,y=550, anchor=NW)
    def client_exit(self):
        exit()
    def showImg(self):

        image_path = filedialog.askopenfilename()
        load = Image.open(image_path)
        load = load.resize((int(100*load.width/load.height), int(250*load.height/load.width)), Image.ANTIALIAS)
        load.load()
        # render = ImageTk.PhotoImage(load)
    def clearImg(self):
        self.canvas.delete()
    

root = Tk()
# root.withdraw()
root.geometry("500x600")
root.resizable(width=False,height=False)

app = Window(root)
    

root.mainloop()

# if image_path:
    
#     # Read the image_data
#     image_data = tf.gfile.FastGFile(image_path, 'rb').read()

#     # Loads label file, strips off carriage return
#     label_lines = [line.rstrip() for line 
#                        in tf.gfile.GFile("tf_files/retrained_labels.txt")]

#     # Unpersists graph from file
#     with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
#         graph_def = tf.GraphDef()
#         graph_def.ParseFromString(f.read())
#         _ = tf.import_graph_def(graph_def, name='')

#     with tf.Session() as sess:
#         # Feed the image_data as input to the graph and get first prediction
#         softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
#         predictions = sess.run(softmax_tensor, \
#                  {'DecodeJpeg/contents:0': image_data})
        
#         # Sort to show labels of first prediction in order of confidence
#         top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        
#         for node_id in top_k:
#             human_string = label_lines[node_id]
#             score = predictions[0][node_id]
#             print('%s (score = %.5f)' % (human_string, score))