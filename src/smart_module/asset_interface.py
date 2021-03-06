#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
HAPI Generic Asset Interface
Authors: Tyler Reed
Release: April 2017, Alpha Milestone
Copyright 2016 Maya Culpa, LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import importlib
import asset_wt

class AssetInterface(object):
    # def __init__(self, asset_type):
    #     # determine the correct asset library and import it
    #     self.asset_lib = importlib.import_module("asset_" + str(asset_type))
    #     eval('from "asset_" + str(asset_type) import AssetImpl')

    def read_value(self):
        return asset_wt.AssetImpl().read_value()
