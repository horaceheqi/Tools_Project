import tensorflow as tf
from keras import backend as k
from tensorflow.python.framework import graph_io
import keras
from tensorflow.python.framework.graph_util import convert_variables_to_constants


"""----------------------------------导入keras模型------------------------------"""
model = keras.models.load_model('./saved_h5/weight_detect_0304.h5')
print("input is:", model.input.name)
print("out is :", model.output.name)

"""----------------------------------保存为.pb格式------------------------------"""
sess = k.get_session()
graph = sess.graph
with graph.as_default():
    output_names = [model.output.op.name]
    input_graph_def = graph.as_graph_def()
    frozen_graph = convert_variables_to_constants(sess, input_graph_def, output_names)
graph_io.write_graph(frozen_graph, './saved_pb', 'weight_detect_0304.pb', as_text=False)