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
        if x == batch - 1:
            batches.append(data[i:])
        else:
            batches.append(data[i:(i+batch_size)])
        i += batch_size
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

        x = tf.get_collection('x', scope=None)[0]
        y = tf.get_collection('y', scope=None)[0]

        loss = tf.get_collection('loss', scope=None)[0]
        accuracy = tf.get_collection('accuracy', scope=None)[0]
        train_op = tf.get_collection('train_op', scope=None)[0]

        batch = X_train.shape[0]/batch_size
        if batch % int(batch) != 0:
            batch = int(batch) + 1

        for epoche in range(epochs+1):
            X_shuffled_train, Y_shuffled_train = shuffle_data(X_train, Y_train)
            train_acc, train_loss = sess.run((accuracy, loss),
                                             {x: X_train, y: Y_train})
            valid_acc, valid_loss = sess.run((accuracy, loss),
                                             {x: X_valid, y: Y_valid})

            print("After {} epochs:".format(epoche))
            print("\tTraining Cost: {}".format(train_loss))
            print("\tTraining Accuracy: {}".format(train_acc))
            print("\tValidation Cost: {}".format(valid_loss))
            print("\tValidation Accuracy: {}".format(
                valid_acc))

            if epoche < epochs:
                mini_batch_X_t = split_data_batch(X_shuffled_train,
                                                  batch, batch_size)
                mini_batch_Y_t = split_data_batch(Y_shuffled_train,
                                                  batch, batch_size)

                batchline = len(mini_batch_X_t) + 1
                for step in range(1, batchline):

                    sess.run(train_op, {
                        x: mini_batch_X_t[step - 1],
                        y: mini_batch_Y_t[step - 1]
                    })

                    train_loss, train_acc = sess.run((loss, accuracy), {
                        x: mini_batch_X_t[step - 1],
                        y: mini_batch_Y_t[step - 1]
                    })
                    if(step % 100 == 0 and step > 0):
                        print("\tStep {}:".format(step))
                        print("\t\tCost: {}".format(train_loss))
                        print("\t\tAccuracy: {}".format(train_acc))
        return saver.save(sess, save_path)
