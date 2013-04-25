#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This file is part of account_treasury module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

import sys
import os
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

import datetime
from decimal import Decimal
import unittest
import trytond.tests.test_tryton
from trytond.transaction import Transaction
from trytond.tests.test_tryton import test_view, test_depends
from trytond.tests.test_tryton import POOL, DB_NAME, USER, CONTEXT


class AccountTreasuryTestCase(unittest.TestCase):
    '''
    Test AccountTreasury module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('account_treasury')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('account_treasury')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountTreasuryTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
