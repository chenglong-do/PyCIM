# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" The specificatoin of limits associated with equipment and other operational entities.The specificatoin of limits associated with equipment and other operational entities.
"""

from cpsm.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_OperationalLimits"

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.A value associated with a specific kind of limit.
    """
    # <<< operational_limit
    # @generated
    def __init__(self, type='', operational_limit_set=None, **kw_args):
        """ Initialises a new 'OperationalLimit' instance.
        """
        # Used to specify high/low and limit levels.Used to specify high/low and limit levels. 
        self.type = type


        self._operational_limit_set = None
        self.operational_limit_set = operational_limit_set


        super(OperationalLimit, self).__init__(**kw_args)
    # >>> operational_limit

    # <<< operational_limit_set
    # @generated
    def get_operational_limit_set(self):
        """ The limit set to which the limit values belong.The limit set to which the limit values belong.
        """
        return self._operational_limit_set

    def set_operational_limit_set(self, value):
        if self._operational_limit_set is not None:
            filtered = [x for x in self.operational_limit_set.operational_limit_value if x != self]
            self._operational_limit_set._operational_limit_value = filtered

        self._operational_limit_set = value
        if self._operational_limit_set is not None:
            self._operational_limit_set._operational_limit_value.append(self)

    operational_limit_set = property(get_operational_limit_set, set_operational_limit_set)
    # >>> operational_limit_set


    def __str__(self):
        """ Returns a string representation of the OperationalLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< operational_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OperationalLimit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OperationalLimit", self.uri)
        if format:
            indent += ' ' * depth

        if self.operational_limit_set is not None:
            s += '%s<%s:OperationalLimit.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_set.uri)
        s += '%s<%s:OperationalLimit.type>%s</%s:OperationalLimit.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OperationalLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> operational_limit.serialize


class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.A set of limits associated with equipmnet.
    """
    # <<< operational_limit_set
    # @generated
    def __init__(self, equipment=None, operational_limit_value=None, **kw_args):
        """ Initialises a new 'OperationalLimitSet' instance.
        """

        self._equipment = None
        self.equipment = equipment

        self._operational_limit_value = []
        if operational_limit_value is not None:
            self.operational_limit_value = operational_limit_value
        else:
            self.operational_limit_value = []


        super(OperationalLimitSet, self).__init__(**kw_args)
    # >>> operational_limit_set

    # <<< equipment
    # @generated
    def get_equipment(self):
        """ The equpment to which the limit set applies.The equpment to which the limit set applies.
        """
        return self._equipment

    def set_equipment(self, value):
        if self._equipment is not None:
            filtered = [x for x in self.equipment.operational_limit_set if x != self]
            self._equipment._operational_limit_set = filtered

        self._equipment = value
        if self._equipment is not None:
            self._equipment._operational_limit_set.append(self)

    equipment = property(get_equipment, set_equipment)
    # >>> equipment

    # <<< operational_limit_value
    # @generated
    def get_operational_limit_value(self):
        """ Values of equipment limits.Values of equipment limits.
        """
        return self._operational_limit_value

    def set_operational_limit_value(self, value):
        for x in self._operational_limit_value:
            x._operational_limit_set = None
        for y in value:
            y._operational_limit_set = self
        self._operational_limit_value = value

    operational_limit_value = property(get_operational_limit_value, set_operational_limit_value)

    def add_operational_limit_value(self, *operational_limit_value):
        for obj in operational_limit_value:
            obj._operational_limit_set = self
            self._operational_limit_value.append(obj)

    def remove_operational_limit_value(self, *operational_limit_value):
        for obj in operational_limit_value:
            obj._operational_limit_set = None
            self._operational_limit_value.remove(obj)
    # >>> operational_limit_value


    def __str__(self):
        """ Returns a string representation of the OperationalLimitSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< operational_limit_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OperationalLimitSet.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OperationalLimitSet", self.uri)
        if format:
            indent += ' ' * depth

        if self.equipment is not None:
            s += '%s<%s:OperationalLimitSet.equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment.uri)
        for obj in self.operational_limit_value:
            s += '%s<%s:OperationalLimitSet.operational_limit_value rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OperationalLimitSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> operational_limit_set.serialize


class ActivePowerLimit(OperationalLimit):
    """ Limit on active power flow.Limit on active power flow.
    """
    # <<< active_power_limit
    # @generated
    def __init__(self, value=0.0, **kw_args):
        """ Initialises a new 'ActivePowerLimit' instance.
        """
        # Value of active power limit.Value of active power limit. 
        self.value = value



        super(ActivePowerLimit, self).__init__(**kw_args)
    # >>> active_power_limit


    def __str__(self):
        """ Returns a string representation of the ActivePowerLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< active_power_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ActivePowerLimit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ActivePowerLimit", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ActivePowerLimit.value>%s</%s:ActivePowerLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.operational_limit_set is not None:
            s += '%s<%s:OperationalLimit.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_set.uri)
        s += '%s<%s:OperationalLimit.type>%s</%s:OperationalLimit.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ActivePowerLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> active_power_limit.serialize


class ApparentPowerLimit(OperationalLimit):
    """ Apparent power limit.Apparent power limit.
    """
    # <<< apparent_power_limit
    # @generated
    def __init__(self, value=0.0, **kw_args):
        """ Initialises a new 'ApparentPowerLimit' instance.
        """
        # The apparent power limit.The apparent power limit. 
        self.value = value



        super(ApparentPowerLimit, self).__init__(**kw_args)
    # >>> apparent_power_limit


    def __str__(self):
        """ Returns a string representation of the ApparentPowerLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< apparent_power_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ApparentPowerLimit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ApparentPowerLimit", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ApparentPowerLimit.value>%s</%s:ApparentPowerLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.operational_limit_set is not None:
            s += '%s<%s:OperationalLimit.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_set.uri)
        s += '%s<%s:OperationalLimit.type>%s</%s:OperationalLimit.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ApparentPowerLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> apparent_power_limit.serialize


class VoltageLimit(OperationalLimit):
    """ Operational limit applied to voltage.Operational limit applied to voltage.
    """
    # <<< voltage_limit
    # @generated
    def __init__(self, value=0.0, **kw_args):
        """ Initialises a new 'VoltageLimit' instance.
        """
        # Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKindLimit on voltage. High or low limit depends on the OperatoinalLimit.limitKind 
        self.value = value



        super(VoltageLimit, self).__init__(**kw_args)
    # >>> voltage_limit


    def __str__(self):
        """ Returns a string representation of the VoltageLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< voltage_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the VoltageLimit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "VoltageLimit", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:VoltageLimit.value>%s</%s:VoltageLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.operational_limit_set is not None:
            s += '%s<%s:OperationalLimit.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_set.uri)
        s += '%s<%s:OperationalLimit.type>%s</%s:OperationalLimit.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "VoltageLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> voltage_limit.serialize


class CurrentLimit(OperationalLimit):
    """ OIoeratuibak kimit on current.OIoeratuibak kimit on current.
    """
    # <<< current_limit
    # @generated
    def __init__(self, value=0.0, **kw_args):
        """ Initialises a new 'CurrentLimit' instance.
        """
        # Limit on current flow.Limit on current flow. 
        self.value = value



        super(CurrentLimit, self).__init__(**kw_args)
    # >>> current_limit


    def __str__(self):
        """ Returns a string representation of the CurrentLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< current_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CurrentLimit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CurrentLimit", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:CurrentLimit.value>%s</%s:CurrentLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.operational_limit_set is not None:
            s += '%s<%s:OperationalLimit.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_set.uri)
        s += '%s<%s:OperationalLimit.type>%s</%s:OperationalLimit.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurrentLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> current_limit.serialize


# <<< operational_limits
# @generated
# >>> operational_limits