# -*- coding: utf-8 -*-

import abc
from collections import OrderedDict

import torch.nn as nn

from DLtorch.base import BaseComponent


class BaseAdvGenerator(BaseComponent):
    def __init__(
        self, 
        criterion = nn.CrossEntropyLoss(), 
        eval_mode: bool = True
        ):
        super(BaseAdvGenerator, self).__init__()
        self.logger.info("Adversary Constructed.")

        self.criterion = criterion
        self.eval_mode = eval_mode

    @abc.abstractmethod
    def generate_adv(self, net, inputs, targets, outputs):
        """
        Generate adversarial types of the inputs.
        """
