#################################################################################
#                                                                               #
#                               Eric BREHAULT - 2006                            #
#                                                                               #
#################################################################################

from Products.Archetypes.public import *
from Products.CMFCore import CMFCorePermissions
from Products.Archetypes.utils import make_uuid
from AccessControl import ClassSecurityInfo

from Products.CMFPlomino.config import *

from PlominoIndex import PlominoIndex

class PlominoDatabase(BaseFolder):
	""" Plomino DB """
	schema = BaseFolderSchema + Schema(
		StringField('Description',
		widget=TextAreaWidget(label='Description')
		))
	
	content_icon = "PlominoDatabase.gif"
	
	__allow_access_to_unprotected_subobjects__ = 1
	
	security = ClassSecurityInfo()
	
	actions = (
		{
		'id': 'view',
		'name': 'View',
		'action': 'string:${object_url}/OpenDatabase',
		'permissions': (CMFCorePermissions.View,)
		},
		{
		'id': 'forms',
		'name': 'Forms',
		'action': 'string:${object_url}/DatabaseForms',
		'permissions': (CMFCorePermissions.View,)
		},
		{
		'id': 'views',
		'name': 'Views',
		'action': 'string:${object_url}/DatabaseViews',
		'permissions': (CMFCorePermissions.View,)
		},
		{
		'id': 'acl',
		'name': 'ACL',
		'action': 'string:${object_url}/DatabaseACL',
		'permissions': (CMFCorePermissions.View,)
		},)
	
	def __init__(self, oid, **kw):
		BaseFolder.__init__(self, oid, **kw)
		self.ACL_initialized=0
		index = PlominoIndex()
		self._setObject(index.getId(), index)
		design = {}
		design['views'] = {}
		self._design = design
		
	def getForms(self):
		""" return the database forms list """
		return self.getFolderContents(contentFilter = {'portal_type' : ['PlominoForm']})
		
	def getViews(self):
		""" return the database views list """
		return self.getFolderContents(contentFilter = {'portal_type' : ['PlominoView']})
	
	def getForm(self, formname):
		""" return a PlominoForm """
		f = self.getFolderContents(contentFilter = {'portal_type' : ['PlominoForm'], 'title' : formname})
		return self._getOb(f[0].id)
			
	def getView(self, viewname):
		""" return a PlominoView """
		#v = self.getFolderContents(contentFilter = {'portal_type' : ['PlominoView'], 'title' : viewname})
		#return self._getOb(v[0].id)
		views = self._design['views']
		if views.has_key(viewname):
			v = views[viewname]
			if hasattr(v, '__of__'):
				v = v.__of__(self)
			return v
		else:
			return None
		
	security.declareProtected(CREATE_PERMISSION, 'createDocument')
	def createDocument(self):
		""" create a unique ID and invoke PlominoDocument factory """
		newid = make_uuid()
		self.invokeFactory( type_name='PlominoDocument', id=newid)
		doc = self._getOb( newid )
		doc.setParentDatabase(self)
		return doc
		
	def getRoles(self):
		""" return the database roles list """
		roles = self.valid_roles()
		return roles
		
	def initializeACL(self):
		""" create the default Plomino access rights """
		self._addRole("PlominoReader")
		self.manage_role("PlominoReader", permissions=[
			READ_PERMISSION,
			CMFCorePermissions.View])
		self._addRole("PlominoAuthor")
		self.manage_role("PlominoAuthor", permissions=[
			READ_PERMISSION,
			EDIT_PERMISSION,
			REMOVE_PERMISSION,
			CREATE_PERMISSION,
			ADD_CONTENT_PERMISSION,
			CMFCorePermissions.View])
		self._addRole("PlominoEditor")
		self.manage_role("PlominoEditor", permissions=[
			READ_PERMISSION,
			EDIT_PERMISSION,
			REMOVE_PERMISSION,
			CREATE_PERMISSION,
			ADD_CONTENT_PERMISSION,
			CMFCorePermissions.View])
		self._addRole("PlominoDesigner")
		self.manage_role("PlominoDesigner", permissions=[
			READ_PERMISSION,
			EDIT_PERMISSION,
			REMOVE_PERMISSION,
			CREATE_PERMISSION,
			DESIGN_PERMISSION,
			ADD_CONTENT_PERMISSION,
			ADD_DESIGN_PERMISSION,
			CMFCorePermissions.View])
		self._addRole("PlominoManager")
		self.manage_role("PlominoManager", permissions=[
			READ_PERMISSION,
			EDIT_PERMISSION,
			REMOVE_PERMISSION,
			CREATE_PERMISSION,
			DESIGN_PERMISSION,
			ADD_CONTENT_PERMISSION,
			ADD_DESIGN_PERMISSION,
			ACL_PERMISSION,
			CMFCorePermissions.View])
		self.ACL_initialized=1
	
		
	security.declareProtected(CMFCorePermissions.View, 'updateACL')
	def updateACL(self, REQUEST):
		""" update the ACL settings """
		if self.ACL_initialized==0:
			self.initializeACL()
		REQUEST.RESPONSE.redirect('../OpenDatabase')
		
	security.declareProtected(CMFCorePermissions.View, 'getIndex')
	def getIndex(self):
		""" return the database index """
		return self._getOb('plomino_index')
			
	def declareDesign(self, design_type, design_name, design_obj):
		""" declare a design element """
		design = self._design
		elements = design[design_type]
		elements[design_name] = design_obj
		design[design_type] = elements
		self._design = design
	
	def undeclareDesign(self, design_type, design_name):
		""" undeclare a design element """
		design = self._design
		elements = design[design_type]
		del elements[design_name]
		design[design_type] = elements
		self._design = design
		
registerType(PlominoDatabase, PROJECTNAME)