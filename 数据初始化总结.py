from tensorflow.python.keras import layers
import tensorflow as tf
from tensorflow.python import keras


class Linear(layers.Layer):
    def __init__(self,units=32):
        super(Linear,self).__init__()
        self.units = units
    # layers.Layer中__call__()方法中会调用子类的build()和call()
    def build(self,input_shape):
        self.w = self.add_weight(initializer='random_normal',shape=(input_shape[-1],self.units), trainable=True)
        self.b = self.add_weight(initializer='random_normal',shape=(self.units,),trainable=True)
    def call(self, inputs):
        return tf.matmul(inputs,self.w) + self.b
    def get_config(self):
        config = super(Linear,self).get_config()
        config.update({'units':self.units})
        return config

layer = Linear(64)
config = layer.get_config()
print(config)
print(layer.get_config())


class MLPBLOCK(layers.Layer):
    def __init__(self):
        super(MLPBLOCK,self).__init__()
        self.linear_1 = Linear(32)
        self.linear_2 = Linear(32)
        self.linear_3 = Linear(1)
    def call(self, inputs):
        x = self.linear_1(inputs)
        x = tf.nn.relu(x)
        x = self.linear_2(inputs)
        x = tf.nn.relu(x)
        print(x)
        return self.linear_3(x)
# mlp = MLPBLOCK()
# y = mlp(tf.ones(shape=(3,64)))
# print(y)
# print('weight:',mlp.weights)
# print('trainable weights', len(mlp.trainable_weights))