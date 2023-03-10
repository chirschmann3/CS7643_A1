""" 			  		 			     			  	   		   	  			  	
Models Base.  (c) 2021 Georgia Tech

Copyright 2021, Georgia Institute of Technology (Georgia Tech)
Atlanta, Georgia 30332
All Rights Reserved

Template code for CS 7643 Deep Learning

Georgia Tech asserts copyright ownership of this template and all derivative
works, including solutions to the projects assigned in this course. Students
and other users of this template code are advised not to share it with others
or to make it available on publicly viewable websites including repositories
such as Github, Bitbucket, and Gitlab.  This copyright statement should
not be removed or edited.

Sharing solutions with current or future students of CS 7643 Deep Learning is
prohibited and subject to being investigated as a GT honor code violation.

-----do not edit anything above this line---
"""

# Do not use packages that are not in standard distribution of python
import numpy as np
import math


class _baseNetwork:
    def __init__(self, input_size=28 * 28, num_classes=10):
        self.input_size = input_size
        self.num_classes = num_classes

        self.weights = dict()
        self.gradients = dict()

    def _weight_init(self):
        pass

    def forward(self):
        pass

    def softmax(self, scores):
        """
        Compute softmax scores given the raw output from the model

        :param scores: raw scores from the model (N, num_classes)
        :return:
            prob: softmax probabilities (N, num_classes)
        """
        prob = None
        #############################################################################
        #############################################################################
        apply_exp = lambda x: np.exp(x)
        exp_scores = apply_exp(scores)
        prob = np.array([val / np.sum(val) for val in exp_scores])
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################

        return prob

    def cross_entropy_loss(self, x_pred, y):
        """
        Compute Cross-Entropy Loss based on prediction of the network and labels
        :param x_pred: Probabilities from the model (N, num_classes)
        :param y: Labels of instances in the batch
        :return: The computed Cross-Entropy Loss
        """
        loss = None
        #############################################################################
        #############################################################################
        prob_list = [x_pred[i][y[i]] for i in range(len(y))]
        logs = [-1 * math.log(j) for j in prob_list]
        loss = sum(logs) / len(logs)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        return loss

    def compute_accuracy(self, x_pred, y):
        """
        Compute the accuracy of current batch
        :param x_pred: Probabilities from the model (N, num_classes)
        :param y: Labels of instances in the batch
        :return: The accuracy of the batch
        """
        acc = None
        #############################################################################
        #############################################################################
        pred_cat = np.array([np.argmax(row) for row in x_pred])
        correct_pred = np.count_nonzero((pred_cat - y) == 0)
        acc = correct_pred / len(y)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        return acc

    def sigmoid(self, X):
        """
        Compute the sigmoid activation for the input

        :param X: the input data coming out from one layer of the model (N, layer size)
        :return:
            out: the value after the sigmoid activation is applied to the input (N, layer size)
        """
        out = None
        #############################################################################
        #############################################################################
        sig_funct = lambda x: 1/(1 + np.exp(-x))
        out = sig_funct(X)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        return out

    def sigmoid_dev(self, x):
        """
        The analytical derivative of sigmoid function at x
        :param x: Input data
        :return: The derivative of sigmoid function at x
        """
        ds = None
        #############################################################################
        #############################################################################
        sig_deriv_func = lambda s: (1/(1 + np.exp(-s))) * (1 - 1/(1 + np.exp(-s)))
        ds = sig_deriv_func(x)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        return ds

    def ReLU(self, X):
        """
        Compute the ReLU activation for the input

        :param X: the input data coming out from one layer of the model (N, layer size)
        :return:
            out: the value after the ReLU activation is applied to the input (N, layer size)
        """
        out = None
        #############################################################################
        #############################################################################
        relu_func = lambda x: np.maximum(0, x)
        out = relu_func(X)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        return out

    def ReLU_dev(self, X):
        """
        Compute the gradient ReLU activation for the input

        :param X: the input data coming out from one layer of the model (N, layer size)
        :return:
            out: gradient of ReLU given input X
        """
        out = None
        #############################################################################
        #############################################################################
        relu_deriv_func = lambda x: (x > 0) * 1.0
        out = relu_deriv_func(X)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        return out
