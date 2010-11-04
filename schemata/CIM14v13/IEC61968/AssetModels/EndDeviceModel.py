# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61968.AssetModels.AssetModel import AssetModel

class EndDeviceModel(AssetModel):
    """Documentation for particular end device product model made by a manufacturer.
    """

    def __init__(self, EndDeviceTypeAsset=None, EndDeviceAssets=None, *args, **kw_args):
        """Initializes a new 'EndDeviceModel' instance.

        @param EndDeviceTypeAsset:
        @param EndDeviceAssets: All end device assets being of this model.
        """
        self._EndDeviceTypeAsset = None
        self.EndDeviceTypeAsset = EndDeviceTypeAsset

        self._EndDeviceAssets = []
        self.EndDeviceAssets = [] if EndDeviceAssets is None else EndDeviceAssets

        super(EndDeviceModel, self).__init__(*args, **kw_args)

    def getEndDeviceTypeAsset(self):
        
        return self._EndDeviceTypeAsset

    def setEndDeviceTypeAsset(self, value):
        if self._EndDeviceTypeAsset is not None:
            filtered = [x for x in self.EndDeviceTypeAsset.EndDeviceModels if x != self]
            self._EndDeviceTypeAsset._EndDeviceModels = filtered

        self._EndDeviceTypeAsset = value
        if self._EndDeviceTypeAsset is not None:
            self._EndDeviceTypeAsset._EndDeviceModels.append(self)

    EndDeviceTypeAsset = property(getEndDeviceTypeAsset, setEndDeviceTypeAsset)

    def getEndDeviceAssets(self):
        """All end device assets being of this model.
        """
        return self._EndDeviceAssets

    def setEndDeviceAssets(self, value):
        for x in self._EndDeviceAssets:
            x._EndDeviceModel = None
        for y in value:
            y._EndDeviceModel = self
        self._EndDeviceAssets = value

    EndDeviceAssets = property(getEndDeviceAssets, setEndDeviceAssets)

    def addEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj._EndDeviceModel = self
            self._EndDeviceAssets.append(obj)

    def removeEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj._EndDeviceModel = None
            self._EndDeviceAssets.remove(obj)
