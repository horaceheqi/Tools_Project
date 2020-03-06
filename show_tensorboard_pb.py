import tensorflow as tf


model = r'D:\UMPAY\Project\Coding\test_keras_online\saved_pb\weight_detect.pb' #请将这里的pb文件路径改为自己的
graph = tf.get_default_graph()
graph_def = graph.as_graph_def()
graph_def.ParseFromString(tf.gfile.FastGFile(model, 'rb').read())
tf.import_graph_def(graph_def, name='graph')
summaryWriter = tf.summary.FileWriter('./log/', graph)