""" 			  		 			     			  	   		   	  			  	
MLP Model.  (c) 2021 Georgia Tech

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

np.random.seed(1024)
from ._base_network import _baseNetwork


class TwoLayerNet(_baseNetwork):
    def __init__(self, input_size=28 * 28, num_classes=10, hidden_size=128):
        super().__init__(input_size, num_classes)

        self.hidden_size = hidden_size
        self._weight_init()

    def _weight_init(self):
        """
        initialize weights of the network
        :return: None; self.weights is filled based on method
        - W1: The weight matrix of the first layer of shape (num_features, hidden_size)
        - b1: The bias term of the first layer of shape (hidden_size,)
        - W2: The weight matrix of the second layer of shape (hidden_size, num_classes)
        - b2: The bias term of the second layer of shape (num_classes,)
        """

        # initialize weights
        self.weights['b1'] = np.zeros(self.hidden_size)
        self.weights['b2'] = np.zeros(self.num_classes)
        np.random.seed(1024)
        self.weights['W1'] = 0.001 * np.random.randn(self.input_size, self.hidden_size)
        np.random.seed(1024)
        self.weights['W2'] = 0.001 * np.random.randn(self.hidden_size, self.num_classes)

        # initialize gradients to zeros
        self.gradients['W1'] = np.zeros((self.input_size, self.hidden_size))
        self.gradients['b1'] = np.zeros(self.hidden_size)
        self.gradients['W2'] = np.zeros((self.hidden_size, self.num_classes))
        self.gradients['b2'] = np.zeros(self.num_classes)

    def forward(self, X, y, mode='train'):
        """
        The forward pass of the two-layer net. The activation function used in between the two layers is sigmoid, which
        is to be implemented in self.,sigmoid.
        The method forward should compute the loss of input batch X and gradients of each weights.
        Further, it should also compute the accuracy of given batch. The loss and
        accuracy are returned by the method and gradients are stored in self.gradients

        :param X: a batch of images (N, input_size)
        :param y: labels of images in the batch (N,)
        :param mode: if mode is training, compute and update gradients;else, just return the loss and accuracy
        :return:
            loss: the loss associated with the batch
            accuracy: the accuracy of the batch
            self.gradients: gradients are not explicitly returned but rather updated in the class member self.gradients
        """
        loss = None
        accuracy = None
        #############################################################################

        #############################################################################

        Z1 = np.matmul(X, self.weights['W1']) + self.weights['b1']   # Nx784 * 784xH= NxH
        A = _baseNetwork.sigmoid(self, Z1)                           # NxH
        Z2 = np.matmul(A, self.weights['W2'] + self.weights['b2'])   # NxH * HxC= NxC
        p = _baseNetwork.softmax(self, Z2)                           # NxC
        loss = _baseNetwork.cross_entropy_loss(self, p, y)           # scalar
        accuracy = _baseNetwork.compute_accuracy(self, p, y)

        if mode != 'train':
            return loss, accuracy
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################

        #############################################################################

        #############################################################################
        p[range(y.shape[0]), y] -= 1  # source https://deepnotes.io/softmax-crossentropy
        dloss_dz2 = 1 / y.shape[0] * p                                     # NxC

        dloss_dw2 = np.matmul(dloss_dz2.transpose(), A)                    # CxN * NxH = CxH
        self.gradients['W2'] = dloss_dw2.transpose()                       # should be HxC
        self.gradients['b2'] = np.sum(dloss_dz2, axis=0)                   # should be Cx1

        dloss_da = np.matmul(dloss_dz2, self.weights['W2'].transpose())          # NxC*HxC = NxH
        dloss_dz1 = np.multiply(dloss_da, _baseNetwork.sigmoid_dev(self, Z1) )   # NxH elemwise NxH = NxH
        dloss_dw1 = np.matmul(dloss_dz1.transpose(), X)                          # HxN * Nx784 = Hx784
        self.gradients['W1'] = dloss_dw1.transpose()                             # should be Hx784
        self.gradients['b1'] = np.sum(dloss_dz1, axis=0)                         # should be Hx1
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################

        return loss, accuracy
