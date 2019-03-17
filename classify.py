import tensorflow as tf
import sys
import glob, os
import tkinter as tk
from tkinter import filedialog

# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

# image_path = sys.argv[1]


root = tk.Tk()
root.withdraw()

base = '' # isi dengan direktori base
test_base = '' # isi dengan pathfile untuk test_file
os.chdir(test_base)
# image_paths = [base+"Lainnya-01-001.jpg", base+"Lainnya-01-002.jpg"]
# image_path = filedialog.askopenfilename()

for image_path in glob.glob("*.*"):
# for image_path in image_paths:
    if image_path:
        print("========================")
        print(image_path)
        
        # Read the image_data
        os.chdir(test_base)
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()

        os.chdir(base)

        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line 
                           in tf.gfile.GFile("tf_files/retrained_labels.txt")]

        # Unpersists graph from file
        with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            
            predictions = sess.run(softmax_tensor, \
                     {'DecodeJpeg/contents:0': image_data})
            
            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            
            max_score = 0;
            max_node = 0;
            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                if score > max_score:
                    max_score = score
                    max_node = node_id
                print('%s (score = %.5f)' % (human_string, score))

        true = 0;
        false = 0;
        print('%s dideteksi merupakan batik jenis %s' % (image_path, label_lines[max_node]))
        if image_path.split('-')[0].lower() == "nitik" and label_lines[max_node] == "nitik":
            true = true + 1;
            print("BENAR DETEKSI")
        elif image_path.split('-')[0].lower() != "nitik" and label_lines[max_node] == "bukannitik":
            true = true + 1;
            print("BENAR DETEKSI")
        else:
            false = false + 1;
            print("SALAH DETEKSI")
        print("Performa akurasi")
        print(true / (true + false))


        print("=================================")