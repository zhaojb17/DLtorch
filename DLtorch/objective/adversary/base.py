# DLtorch Framework
# Author: Junbo Zhao <zhaojb17@mails.tsinghua.edu.cn>.

import abc
from collections import OrderedDict


class BaseAdvGenerator(object):
    def __init__(self, criterion, eval_mode: bool = True):
        self.criterion = criterion
        self.eval_mode = eval_mode

    @abc.abstractmethod
    def generate_adv(self, net, inputs, targets, outputs):
        """
        Generate adversarial types of the inputs.
        """