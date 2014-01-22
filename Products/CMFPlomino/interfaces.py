# -*- coding: utf-8 -*-
from zope.interface.interface import Attribute
from zope.interface import Interface

class IBootstrapView(Interface):
    """ """

    def getColumnsClasses(view=None):
        """ A helper method to return the clases for the columns of the site
            it should return a dict with three elements:'one', 'two', 'content'
            Each of them should contain the classnames for the first (leftmost)
            second (rightmost) and middle column
        """

class IPlominoDatabase(Interface):
    """ Marker interface for .PlominoDatabase.PlominoDatabase
    """

class IPlominoAction(Interface):
    """ Marker interface for .PlominoAction.PlominoAction
    """

class IPlominoForm(Interface):
    """ Marker interface for .PlominoForm.PlominoForm
    """

class IPlominoField(Interface):
    """ Marker interface for .PlominoField.PlominoField
    """

class IPlominoView(Interface):
    """ Marker interface for .PlominoView.PlominoView
    """

class IPlominoColumn(Interface):
    """ Marker interface for .PlominoColumn.PlominoColumn
    """

class IPlominoDocument(Interface):
    """ Marker interface for .PlominoDocument.PlominoDocument
    """

class IPlominoHidewhen(Interface):
    """ Marker interface for .PlominoHidewhen.PlominoHidewhen
    """

class IPlominoAgent(Interface):
    """ Marker interface for .PlominoAgent.PlominoAgent
    """

class IPlominoUtils(Interface):
    """ Marker interface for PlominoUtils
    """

class IPlominoCache(Interface):
    """ Marker interface for PlominoCache
    """

class IXMLImportExportSubscriber(Interface):
    """ Provides import/export to/from XML.
       Subscribers to IXMLExportEvent MUST implement this interface"""
    def __call__():
        """ Attaches an XML string representing custom exportable properties
           to the 'xml_strings' attribute of the event
        """
    def import_xml(xml_string):
        """ Applies information contained in XML string 
        (as returned by __call__).
        """

        
class IPlominoSafeDomains(Interface):
    """Marker interface for PlominoSafeDomains
    """

