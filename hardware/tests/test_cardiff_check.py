#
# Copyright (C) 2014 eNovance SAS <licensing@enovance.com>
#
# Author: Erwan Velu <erwan.velu@enovance.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import unittest

from hardware.cardiff import check
from hardware.cardiff import utils


_BASEDIR = os.path.dirname(os.path.abspath(__file__))


def load_samples(bench_values):
    for health in utils.find_file(os.path.join(_BASEDIR, 'cardiff_samples'),
                                  '*.hw_'):
        bench_values.append(eval(open(health).read()))


class TestDetect(unittest.TestCase):

    def test_cpu(self):
        hw = []
        load_samples(hw)
        result = check.cpu(utils.find_sub_element(hw, 'serial', 'cpu'),
                           'serial')

        self.maxDiff = None
        for element in result:
            group = result[element]
        p = ['CZ3404YWP4', 'CZ3404YWNW', 'CZ3404YWP6', 'CZ3404YWPP',
             'CZ3404YWP2', 'CZ3404YWPS', 'CZ3404YWP8', 'CZ3404YWPC',
             'CZ3404YWPX', 'CZ3404YWPV', 'CZ3404YWNT', 'CZ3404YWNR',
             'CZ3404YWPE', 'CZ3404YWPA', 'CZ3404YWPM', 'CZ3404YWNN',
             'CZ3404YWR0', 'CZ3404YWPH', 'CZ3404YWPK']
        self.assertEqual(sorted(p), sorted(group))
        res = set([('cpu', 'physical_0', 'cores', '8'),
                   ('cpu', 'physical_1', 'clock', '100000000'),
                   ('cpu', 'physical_0', 'physid', '400'),
                   ('cpu', 'physical_0', 'threads', '16'),
                   ('cpu', 'physical_1', 'frequency', '2000000000'),
                   ('cpu', 'physical_0', 'clock', '100000000'),
                   ('cpu', 'physical_0', 'enabled_cores', '8'),
                   ('cpu', 'physical_0', 'product',
                    'Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz'),
                   ('cpu', 'physical_1', 'vendor', 'Intel Corp.'),
                   ('cpu', 'physical', 'number', '2'),
                   ('cpu', 'physical_1', 'physid', '401'),
                   ('cpu', 'physical_1', 'product',
                    'Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz'),
                   ('cpu', 'physical_0', 'vendor', 'Intel Corp.'),
                   ('cpu', 'physical_1', 'threads', '16'),
                   ('cpu', 'physical_0', 'frequency', '2000000000'),
                   ('cpu', 'physical_1', 'enabled_cores', '8'),
                   ('cpu', 'physical_1', 'cores', '8'),
                   ('cpu', 'logical', 'number', '32')])
        self.assertEqual(sorted(res), sorted(eval(element)))

    def test_network_interfaces(self):
        hw = []
        load_samples(hw)
        result = check.network_interfaces(
            utils.find_sub_element(hw, 'serial', 'network'), 'serial')
        self.maxDiff = None
        for element in result:
            group = result[element]
        p = ['CZ3404YWP4', 'CZ3404YWNW', 'CZ3404YWP6', 'CZ3404YWNR',
             'CZ3404YWP2', 'CZ3404YWPS', 'CZ3404YWP8', 'CZ3404YWPX',
             'CZ3404YWNT', 'CZ3404YWR0', 'CZ3404YWPE', 'CZ3404YWPA',
             'CZ3404YWPP', 'CZ3404YWPC', 'CZ3404YWNN', 'CZ3404YWPM',
             'CZ3404YWPV', 'CZ3404YWPH', 'CZ3404YWPK']
        self.assertEqual(sorted(p), sorted(group))
        res = set([('network', 'eth0', 'duplex', 'full'),
                   ('network', 'eth0', 'latency', '0'),
                   ('network', 'eth1', 'autonegotiation', 'on'),
                   ('network', 'eth1', 'duplex', 'full'),
                   ('network', 'eth1', 'link', 'yes'),
                   ('network', 'eth1', 'driver', 'be2net'),
                   ('network', 'eth1', 'businfo', 'pci@0000:04:00.1'),
                   ('network', 'eth0', 'autonegotiation', 'on'),
                   ('network', 'eth0', 'businfo', 'pci@0000:04:00.0'),
                   ('network', 'eth1', 'latency', '0'),
                   ('network', 'eth0', 'driver', 'be2net'),
                   ('network', 'eth0', 'link', 'yes')])
        self.assertEqual(sorted(res), sorted(eval(element)))

    def test_memory_timing(self):
        hw = []
        load_samples(hw)
        result = check.memory_timing(utils.find_sub_element(hw, 'serial',
                                                            'memory'),
                                     'serial')
        self.maxDiff = None
        for element in result:
            group = result[element]
        p = ['CZ3404YWP4', 'CZ3404YWNW', 'CZ3404YWP6', 'CZ3404YWNR',
             'CZ3404YWP2', 'CZ3404YWPS', 'CZ3404YWP8', 'CZ3404YWPX',
             'CZ3404YWNT', 'CZ3404YWR0', 'CZ3404YWPE', 'CZ3404YWPA',
             'CZ3404YWPP', 'CZ3404YWPC', 'CZ3404YWNN', 'CZ3404YWPM',
             'CZ3404YWPV', 'CZ3404YWPH', 'CZ3404YWPK']
        self.assertEqual(sorted(p), sorted(group))
        res = set([('memory', 'DDR_1', 'tWTPr', '31'),
                   ('memory', 'DDR_2', 'tFAW', '63'),
                   ('memory', 'DDR_2', 'tCL', '11'),
                   ('memory', 'DDR_2', 'tRFC', '511'),
                   ('memory', 'DDR_2', 'tRRD', '7'),
                   ('memory', 'DDR_2', 'B2B', '31'),
                   ('memory', 'DDR_0', 'tCL', '11'),
                   ('memory', 'DDR_2', 'tRCD', '15'),
                   ('memory', 'DDR_1', 'tRAS', '31'),
                   ('memory', 'DDR_1', 'tRCD', '15'),
                   ('memory', 'DDR', 'type', '3'),
                   ('memory', 'DDR_1', 'tRFC', '511'),
                   ('memory', 'DDR_2', 'tRTPr', '15'),
                   ('memory', 'DDR_0', 'tRAS', '31'),
                   ('memory', 'DDR_2', 'tWTPr', '31'),
                   ('memory', 'DDR_1', 'tWR', '11'),
                   ('memory', 'DDR_0', 'tRTPr', '15'),
                   ('memory', 'DDR_1', 'tRRD', '7'),
                   ('memory', 'DDR_0', 'tFAW', '63'),
                   ('memory', 'DDR_0', 'tRCD', '15'),
                   ('memory', 'DDR_1', 'tRP', '15'),
                   ('memory', 'DDR_1', 'B2B', '31'),
                   ('memory', 'DDR_2', 'tRP', '15'),
                   ('memory', 'DDR_0', 'tRFC', '511'),
                   ('memory', 'DDR_1', 'tFAW', '63'),
                   ('memory', 'DDR_1', 'tRTPr', '15'),
                   ('memory', 'DDR_0', 'tRRD', '7'),
                   ('memory', 'DDR_0', 'tWR', '11'),
                   ('memory', 'DDR_0', 'tWTPr', '31'),
                   ('memory', 'DDR_0', 'tRP', '15'),
                   ('memory', 'DDR_2', 'tWR', '11'),
                   ('memory', 'DDR_1', 'tCL', '11'),
                   ('memory', 'DDR_0', 'B2B', '31'),
                   ('memory', 'DDR_2', 'tRAS', '31')])
        self.assertEqual(sorted(res), sorted(eval(element)))

    def test_firmware(self):
        hw = []
        load_samples(hw)
        result = check.firmware(
            utils.find_sub_element(hw, 'serial', 'firmware'), 'serial')
        self.maxDiff = None
        for element in result:
            group = result[element]
        p = ['CZ3404YWP4', 'CZ3404YWNW', 'CZ3404YWP6', 'CZ3404YWNR',
             'CZ3404YWP2', 'CZ3404YWPS', 'CZ3404YWP8', 'CZ3404YWPX',
             'CZ3404YWNT', 'CZ3404YWR0', 'CZ3404YWPE', 'CZ3404YWPA',
             'CZ3404YWPP', 'CZ3404YWPC', 'CZ3404YWNN', 'CZ3404YWPM',
             'CZ3404YWPV', 'CZ3404YWPH', 'CZ3404YWPK']
        self.assertEqual(sorted(p), sorted(group))
        res = set([('firmware', 'bios', 'date', '09/18/2013'),
                   ('firmware', 'bios', 'version', 'I31'),
                   ('firmware', 'bios', 'vendor', 'HP')])
        self.assertEqual(sorted(res), sorted(eval(element)))

    def test_systems(self):
        hw = []
        load_samples(hw)
        result = check.systems(
            utils.find_sub_element(hw, 'serial', 'system'), 'serial')
        self.maxDiff = None
        for element in result:
            group = result[element]
        p = ['CZ3404YWP4', 'CZ3404YWNW', 'CZ3404YWP6', 'CZ3404YWNR',
             'CZ3404YWP2', 'CZ3404YWPS', 'CZ3404YWP8', 'CZ3404YWPX',
             'CZ3404YWNT', 'CZ3404YWR0', 'CZ3404YWPE', 'CZ3404YWPA',
             'CZ3404YWPP', 'CZ3404YWPC', 'CZ3404YWNN', 'CZ3404YWPM',
             'CZ3404YWPV', 'CZ3404YWPH', 'CZ3404YWPK']
        self.assertEqual(sorted(p), sorted(group))
        res = set([('system', 'ipmi', 'channel', '2'),
                   ('system', 'product', 'name',
                    'ProLiant BL460c Gen8 (641016-B21)'),
                   ('system', 'product', 'vendor', 'HP')])
        self.assertEqual(sorted(res), sorted(eval(element)))

    def test_logical_disks(self):
        hw = []
        load_samples(hw)
        result = check.logical_disks(
            utils.find_sub_element(hw, 'serial', 'disk'), 'serial')
        self.maxDiff = None
        for element in result:
            group = result[element]
        p = ['CZ3404YWP4', 'CZ3404YWNW', 'CZ3404YWP6', 'CZ3404YWNR',
             'CZ3404YWP2', 'CZ3404YWPS', 'CZ3404YWP8', 'CZ3404YWPX',
             'CZ3404YWNT', 'CZ3404YWR0', 'CZ3404YWPE', 'CZ3404YWPA',
             'CZ3404YWPP', 'CZ3404YWPC', 'CZ3404YWNN', 'CZ3404YWPM',
             'CZ3404YWPV', 'CZ3404YWPH', 'CZ3404YWPK']
        self.assertEqual(sorted(p), sorted(group))
        res = set([('disk', 'sdb', 'Write Cache Enable', '0'),
                   ('disk', 'sdb', 'model', 'LOGICAL VOLUME'),
                   ('disk', 'sdb', 'rev', '4.68'),
                   ('disk', 'sdb', 'size', '299'),
                   ('disk', 'sda', 'Write Cache Enable', '0'),
                   ('disk', 'sdb', 'vendor', 'HP'),
                   ('disk', 'sda', 'rev', '4.68'),
                   ('disk', 'sda', 'Read Cache Disable', '0'),
                   ('disk', 'sdb', 'Read Cache Disable', '0'),
                   ('disk', 'sda', 'vendor', 'HP'),
                   ('disk', 'sda', 'model', 'LOGICAL VOLUME'),
                   ('disk', 'sda', 'size', '299')])
        self.assertEqual(sorted(res), sorted(eval(element)))

    def test_hp_physical_disks(self):
        hw = []
        load_samples(hw)
        result = check.physical_hpa_disks(utils.find_sub_element(hw, 'serial',
                                                                 'disk'),
                                          'serial')
        self.maxDiff = None
        item = 0
        for element in result:
            group = result[element]
            if item == 0:
                p = ['CZ3404YWNW']
                res = set([('disk', '1I:1:3', 'size', '1000'),
                           ('disk', '1I:1:7', 'slot', '3'),
                           ('disk', '1I:1:2', 'type', 'SATA'),
                           ('disk', '1I:1:8', 'type', 'SATA'),
                           ('disk', '1I:1:4', 'size', '1000'),
                           ('disk', '1I:1:3', 'slot', '3'),
                           ('disk', '1I:1:2', 'size', '300'),
                           ('disk', '1I:1:1', 'type', 'SATA'),
                           ('disk', '1I:1:4', 'type', 'SATA'),
                           ('disk', '1I:1:6', 'slot', '3'),
                           ('disk', '1I:1:5', 'slot', '3'),
                           ('disk', '1I:1:5', 'size', '1000'),
                           ('disk', '1I:1:5', 'type', 'SATA'),
                           ('disk', '1I:1:3', 'type', 'SATA'),
                           ('disk', '1I:1:2', 'type', 'SAS'),
                           ('disk', '1I:1:6', 'type', 'SATA'),
                           ('disk', '1I:1:1', 'size', '1000'),
                           ('disk', '1I:1:1', 'size', '300'),
                           ('disk', '1I:1:6', 'size', '1000'),
                           ('disk', '1I:1:4', 'slot', '3'),
                           ('disk', '1I:1:8', 'size', '1000'),
                           ('disk', '1I:1:1', 'slot', '0'),
                           ('disk', '1I:1:2', 'slot', '3'),
                           ('disk', '1I:1:1', 'slot', '3'),
                           ('disk', '1I:1:2', 'size', '1000'),
                           ('disk', '1I:1:2', 'slot', '0'),
                           ('disk', '1I:1:7', 'size', '1000'),
                           ('disk', '1I:1:7', 'type', 'SATA'),
                           ('disk', '1I:1:8', 'slot', '3'),
                           ('disk', '1I:1:1', 'type', 'SAS')])
            else:
                p = ['CZ3404YWP4', 'CZ3404YWP6', 'CZ3404YWNR', 'CZ3404YWP2',
                     'CZ3404YWPS', 'CZ3404YWP8', 'CZ3404YWPX', 'CZ3404YWNT',
                     'CZ3404YWR0', 'CZ3404YWPE', 'CZ3404YWPA', 'CZ3404YWPP',
                     'CZ3404YWPC', 'CZ3404YWNN', 'CZ3404YWPM', 'CZ3404YWPV',
                     'CZ3404YWPH', 'CZ3404YWPK']
                res = set([('disk', '1I:1:2', 'type', 'SAS'),
                           ('disk', '1I:1:1', 'slot', '0'),
                           ('disk', '1I:1:2', 'size', '300'),
                           ('disk', '1I:1:2', 'slot', '0'),
                           ('disk', '1I:1:1', 'size', '300'),
                           ('disk', '1I:1:1', 'type', 'SAS')])
                item = item + 1
                self.assertEqual(sorted(p), sorted(group))
                self.assertEqual(sorted(res), sorted(eval(element)))
