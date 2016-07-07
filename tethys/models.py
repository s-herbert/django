from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import requests
import xml.etree.ElementTree as ElementTree

class TethysServer(models.Model):
	port = models.PositiveIntegerField(default=9779)
	url = models.URLField(default='localhost')
	
	

class Container(models.Model):
	name = models.CharField(max_length=100, unique=True)
	count = models.PositiveIntegerField(default = 0)
	server = models.ForeignKey(TethysServer,on_delete=models.CASCADE)
	last_updated = models.DateTimeField(blank=True,null=True)
	last_modified = models.DateTimeField(blank=True,null=True)
	
	
	def refresh(self):
		COUNT_ELEMENT = 0 #index of the <Count> for the collection
		self.last_updated = timezone.now()
		
		tethys_query_url = "http://"+self.server.url + ":" + str(self.server.port) +"//XQuery"
		#get count and docsfor this self.name and server
		xquery ='''
		let $alldocs:= for $doc in collection("%s")
			return substring(base-uri($doc),10) 
		return 
		<Results>
			<Count>{count($alldocs)}</Count>
			{
			for $d in $alldocs 
				order by $d
				return <Document>{$d}</Document>
			}
		</Results>
		'''%self.name
		params = {"XQuery":xquery}
		result = requests.post(tethys_query_url, params)
		
		#parse xml
		tree = ElementTree.fromstring(result.text)
		self.count = int(tree[COUNT_ELEMENT].text)
		documents = [doc.text.replace(self.name+'/','') for doc in tree.iter('Document')]
		self.document_set.all().delete()
		for doc in documents:
			self.document_set.create(name=doc, container=self)
		self.save()
		return result
	
	
	def __str__(self):
		return self.name
		
		
class Document(models.Model):
	name = models.CharField(max_length=200)
	added = models.DateTimeField(blank=True,null=True)
	container = models.ForeignKey(Container,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
	
