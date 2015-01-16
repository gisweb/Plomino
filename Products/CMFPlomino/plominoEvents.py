from five import grok
from zope.component.interfaces import IObjectEvent
from zope.component.interfaces import ObjectEvent
class IPlominoSaveEvent(IObjectEvent):
  pass
class PlominoSaveEvent(ObjectEvent):
  grok.implements(IPlominoSaveEvent)
  def __init__(self,object):
    self.object = object
class IPlominoCreateEvent(IObjectEvent):
  pass
class PlominoCreateEvent(ObjectEvent):
  grok.implements(IPlominoCreateEvent)
  def __init__(self,object):
    self.object = object
