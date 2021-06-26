import numpy as np
from keras.models import Sequential
from keras.layers import Input, Dense, Activation
from keras.optimizers import Adam

model = Sequential()
model.add(Dense(1, input_dim=2, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])


def sampler(n, x, y):
    return np.random.normal(size=[n, 2]) + [x, y]


def sample_data(n=1000, p0=(-1., -1.), p1=(1., 1.)):
    zeros, ones = np.zeros((n, 1)), np.ones((n, 1))
    labels = np.vstack([zeros, ones])
    z_sample = sampler(n, x=p0[0], y=p0[1])
    o_sample = sampler(n, x=p1[0], y=p1[1])
    return np.vstack([z_sample, o_sample]), labels


X_train, Y_train = sample_data()
X_test, Y_test = sample_data(100)

model.fit(X_train, Y_train, batch_size=16, epochs=100,
          verbose=1, validation_data=(X_test, Y_test))

model.summary()
model.trainable = True

trainable = False;

for layer in model.layers:
    trainable = True
    layer.trainable = trainable

model.compile(loss='binary_crossentropy', optimizer=Adam(lr=1e-5), metrics=['accuracy'])

X_train, Y_train = sample_data()

model.fit(X_train, Y_train, batch_size=16, epochs=15,
          verbose=1, validation_data=(X_test, Y_test))

scores = model.evaluate(X_test, Y_test)

print("Точность на тестовых данных: %.2f%%" % (scores[1]*100))
