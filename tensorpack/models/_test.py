# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# File: _test.py


import logging
import unittest
import tensorflow as tf


class TestModel(unittest.TestCase):

    def run_variable(self, var):
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        if isinstance(var, list):
            return sess.run(var)
        else:
            return sess.run([var])[0]

    def make_variable(self, *args):
        if len(args) > 1:
            return [tf.Variable(k) for k in args]
        else:
            return tf.Variable(args[0])


def run_test_case(case):
    suite = unittest.TestLoader().loadTestsFromTestCase(case)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    import tensorpack
    from tensorpack.utils import logger
    from . import *  # noqa
    logger.setLevel(logging.CRITICAL)
    subs = tensorpack.models._test.TestModel.__subclasses__()
    for cls in subs:
        run_test_case(cls)
