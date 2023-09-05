import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

# Set up the training data set
(training_images, training_labels), (testing_images, testing_labels) = keras.datasets.cifar10.load_data()

# Now normalize the data, scale it down to between 0 and 1. Pixel brightness of picture ranges from 0-255
training_images, testing_images = training_images / 255, testing_images / 255

#These align with the images in the dataset https://www.cs.toronto.edu/~kriz/cifar.html
class_names = ["Plane", "Car", "Bird", "Cat", "Deer", "Dog", "Frog", "Horse", "Ship", "Truck"]

# create a visual of some of the test pictures
for image in range(16):
    plt.subplot(4,4,image+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(training_images[image])
    plt.xlabel(class_names[training_labels[image][0]])

plt.show()

# reduce amount of images sent in (saves time and resources)
# in this case training of 20000 and testing of 4000
# training_images = training_images[:20000]
# training_labels = training_labels[:20000]
# testing_images = testing_images[:4000]
# testing_labels = testing_labels[:4000]

model = keras.models.Sequential()
# convolutional layer (looks for specific features in an image)
model.add(keras.layers.Conv2D(32, (3,3), activation="relu", input_shape=(32,32,3)))
# Max pooling layer that simplifies to essential information
model.add(keras.layers.MaxPooling2D((2,2)))
# convolutional layer
model.add(keras.layers.Conv2D(64, (3,3), activation="relu"))
# Another max pooling layer
model.add(keras.layers.MaxPooling2D((2,2)))
# convolutional layer
model.add(keras.layers.Conv2D(64, (3,3), activation="relu"))
# flatten the matrix into a single layer
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation="relu"))
# will give the final layer with the probability it is each of the 10 classes
model.add(keras.layers.Dense(10, activation="softmax"))
# define our lass function and what we are focused on (which will be accuracy)
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# epochs is how often model sees same data over again
model.fit(training_images, training_labels, epochs=10, validation_data=(testing_images, testing_labels))

loss, accuracy = model.evaluate(testing_images, testing_labels)
print(f"Loss: {loss}")
print(f"Accuracy: {accuracy}")

# Saves the model when the training is done
model.save('image_classifier.model')


#Once the model is trained and saved, you can directly assign it to our model value
# model = model.load_model('image_classifier.model')

#Now load in the image
# img = cv.imread("File Name")
# # trained model on rgb so need the correct colour format
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# plt.imshow(img)

# prediction = model.predict(np.array([img]) / 255)
# # index of highest prediction
# index = np.argmax(prediction)
# print(f"Predisction is {class_names[index]}")