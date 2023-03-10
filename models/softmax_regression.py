""" 			  		 			     			  	   		   	  			  	
Softmax Regression Model.  (c) 2021 Georgia Tech

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

from ._base_network import _baseNetwork


class SoftmaxRegression(_baseNetwork):
    def __init__(self, input_size=28 * 28, num_classes=10):
        """
        A single layer softmax regression. The network is composed by:
        a linear layer without bias => (activation) => Softmax
        :param input_size: the input dimension
        :param num_classes: the number of classes in total
        """
        super().__init__(input_size, num_classes)
        self._weight_init()

    def _weight_init(self):
        '''
        initialize weights of the single layer regression network. No bias term included.
        :return: None; self.weights is filled based on method
        - W1: The weight matrix of the linear layer of shape (num_features, hidden_size)
        '''
        np.random.seed(1024)
        self.weights['W1'] = 0.001 * np.random.randn(self.input_size, self.num_classes)
        self.gradients['W1'] = np.zeros((self.input_size, self.num_classes))

    def forward(self, X, y, mode='train'):
        """
        Compute loss and gradients using softmax with vectorization.

        :param X: a batch of image (N, 28x28)
        :param y: labels of images in the batch (N,)
        :return:
            loss: the loss associated with the batch
            accuracy: the accuracy of the batch
        """
        loss = None
        gradient = None
        accuracy = None
        #############################################################################
        # Hint:                                                                     #
        #   Store your intermediate outputs before ReLU for backwards               #
        #############################################################################

        Z = np.matmul(X, self.weights['W1'])    # Nx784 * 784xC= NxC
        A = _baseNetwork.ReLU(self, Z)                         # NxC
        p = _baseNetwork.softmax(self, A)                      # NxC
        loss = _baseNetwork.cross_entropy_loss(self, p, y)     # scalar
        accuracy = _baseNetwork.compute_accuracy(self, p, y)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        if mode != 'train':
            return loss, accuracy

        #############################################################################

        #############################################################################
        p[range(y.shape[0]), y] -= 1    # source https://deepnotes.io/softmax-crossentropy
        dloss_da = 1 / y.shape[0] * p                                            # NxC
        dloss_dz = np.multiply(dloss_da, _baseNetwork.ReLU_dev(self, Z))         # NxC elemwise NxC = NxC
        dloss_dw = np.matmul(dloss_dz.transpose(), X)                            # CxN * Nx784 = Cx784
        # TODO: Make so weights aren't static
        self.gradients['W1'] = dloss_dw.transpose()                              # Needs to be 784xC
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        return loss, accuracy
