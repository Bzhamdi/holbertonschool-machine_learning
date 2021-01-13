#!/usr/bin/env python3
"""
trains a loaded neural network model using mini-batch gradient descent:
"""

import tensorflow as tf
shuffle_data = __import__('2-shuffle_data').shuffle_data


def split_data_batch(data, batch, batch_size=32):
    """
    split_data_batch
    data = batch * batch_size

    """

    batches = []
    i = 0

    for x in range(batch):
        if i == batch - 1:
            batches.append(data[i * batch_size:])
        else:
            batches.append(data[i * batch_size:((i + 1) * batch_size)])
        i = i + 1
    return batches


def train_mini_batch(X_train, Y_train, X_valid, Y_valid,
                     batch_size=32, epochs=5,
                     load_path="/tmp/model.ckpt",
                     save_path="/tmp/model.ckpt"):
    """ train with mini batch """

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        saver = tf.train.import_meta_graph('{}.meta'.format(load_path))
        saver.restore(sess, '{}'.format(load_path))

        x = tf.get_collection('x', scope=None)
        y = tf.get_collection('y', scope=None)

        loss = tf.get_collection('loss', scope=None)
        accuracy = tf.get_collection('accuracy', scope=None)
        train_op = tf.get_collection('train_op', scope=None)
        x = x[0]
        y = y[0]

        batch = X_train.shape[0]/batch_size
        if batch % 1 != 0:
            batch = int(batch) + 1

        for epoche in range(epochs+1):
            X_shuffled_train, Y_shuffled_train = shuffle_data(X_train, Y_train)

            train_loss = sess.run(loss, {
                x: X_train,
                y: Y_train
            })
            train_acc = sess.run(accuracy, {
                x: X_train,
                y: Y_train
            })
            valid_acc = sess.run(accuracy, {
                x: X_valid,
                y: Y_valid
            })

            valid_loss = sess.run(loss, {
                x: X_valid,
                y: Y_valid
            })

            print("After {} epochs:".format(epoche))
            print("\tTraining Cost: {}".format(train_loss))
            print("\tTraining Accuracy: {}".format(train_acc))
            print("\tValidation Cost: {}".format(valid_loss))
            print("\tValidation Accuracy: {}".format(
                valid_acc))

            mini_batch_X_t = split_data_batch(X_shuffled_train,
                                              batch, batch_size)
            mini_batch_Y_t = split_data_batch(Y_shuffled_train,
                                              batch, batch_size)

            if epoche < epochs:
                batchline = len(mini_batch_X_t)
                for step in range(0, batchline):

                    sess.run(train_op, {
                        x: mini_batch_X_t[step],
                        y: mini_batch_Y_t[step]
                    })

                    train_loss = sess.run(loss, {
                        x: mini_batch_X_t[step],
                        y: mini_batch_Y_t[step]
                    })
                    train_acc = sess.run(accuracy, {
                        x: mini_batch_X_t[step],
                        y: mini_batch_Y_t[step]
                    })
                    z = step + 1
                    if(z % 100 == 0 and z > 0):
                        print("\tStep {}:".format(z))
                        print("\tTraining Cost: {}".format(train_loss))
                        print("\tTraining Accuracy: {}".format(train_acc))
        return saver.save(sess, save_path)
