import numpy as np
import cv2
import tensorflow as tf

# mnist=tf.keras.datasets.mnist
# (x_train,y_train),(x_test,y_test)=mnist.load_data()
# x_train=tf.keras.utils.normalize(x_train,axis=1)
# x_test=tf.keras.utils.normalize(x_test,axis=1)
# model=tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128,activation='relu'))
# model.add(tf.keras.layers.Dense(128,activation='relu'))
# model.add(tf.keras.layers.Dense(10,activation='softmax'))
# model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# model.fit(x_train,y_train,epochs=3)
# model.save('handwritten.keras')
model=tf.keras.models.load_model('handwritten.keras')
img=cv2.imread('digit3.png')[:,:,0]
img1=img[:,0:28]
img2=img[:,28:56]
#print(img.shape,'\n',img1.shape,'\n',img2.shape)
img1=np.invert(np.array([img1]))
img2=np.invert(np.array([img2]))
prediction1=model.predict(img1)
prediction2=model.predict(img2)
tenth=np.argmax(prediction1)
units=np.argmax(prediction2)
print('This number is probably',tenth*10+units)

