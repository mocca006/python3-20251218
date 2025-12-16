# 修改自：Using autograd in TensorFlow to Solve a Regression Problem
# https://machinelearningmastery.com/using-autograd-in-tensorflow-to-solve-a-regression-problem/
# 更多範例：http://www.math-exercises.com/equations-and-inequalities/systems-of-linear-equations-and-inequalities
import tensorflow as tf
import random

X = tf.Variable(random.random())
Y = tf.Variable(random.random())

# Gradient descent loop
EPOCHS = 1000
optimizer = tf.keras.optimizers.Nadam(learning_rate=0.1)
for _ in range(EPOCHS):
    with tf.GradientTape() as tape:
        # simple eq.
        y1 = 2*X + 3*Y - 9
        y2 = X - Y - 2
        
        # 1b
        # y1 = 2*X + 2 - (X-Y)
        # y2 = 3*X + 2*Y
        sqerr = y1*y1 + y2*y2
    gradX, gradY = tape.gradient(sqerr, [X, Y])
    optimizer.apply_gradients([(gradX, X), (gradY, Y)])

print(f'X={X.numpy()}')
print(f'Y={Y.numpy()}')
