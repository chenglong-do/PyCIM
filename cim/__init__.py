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



# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/CIM-generic"

class Element(object):
    # <<< element
    # @generated
    def __init__(self, uuid='', **kw_args):
        """ Initialises a new 'Element' instance.
        """
 
        self.uuid = uuid



        super(Element, self).__init__(**kw_args)
    # >>> element


    def __str__(self):
        """ Returns a string representation of the Element.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< element.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Element.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Element", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Element")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> element.serialize


class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.
    """
    # <<< iec61970_cimversion
    # @generated
    def __init__(self, date='', version='', **kw_args):
        """ Initialises a new 'IEC61970CIMVersion' instance.
        """
        # The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008. 
        self.date = date

        # Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition. 
        self.version = version



        super(IEC61970CIMVersion, self).__init__(**kw_args)
    # >>> iec61970_cimversion


    def __str__(self):
        """ Returns a string representation of the IEC61970CIMVersion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< iec61970_cimversion.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IEC61970CIMVersion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IEC61970CIMVersion", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:IEC61970CIMVersion.date>%s</%s:IEC61970CIMVersion.date>' % \
            (indent, ns_prefix, self.date, ns_prefix)
        s += '%s<%s:IEC61970CIMVersion.version>%s</%s:IEC61970CIMVersion.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "IEC61970CIMVersion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> iec61970_cimversion.serialize


# <<< cim
# @generated
# >>> cim