# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SiteHash.page_content'
        db.add_column(u'Differ_sitehash', 'page_content',
                      self.gf('django.db.models.fields.TextField')(default='<html></html>'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SiteHash.page_content'
        db.delete_column(u'Differ_sitehash', 'page_content')


    models = {
        u'Differ.diffedsite': {
            'Meta': {'object_name': 'DiffedSite'},
            'difference_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'registered_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Differ.RegisteredPerson']", 'through': u"orm['Differ.SiteMembership']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Differ.registeredperson': {
            'Meta': {'object_name': 'RegisteredPerson'},
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_number': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'Differ.sitehash': {
            'Meta': {'object_name': 'SiteHash'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'md5hash': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page_content': ('django.db.models.fields.TextField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Differ.DiffedSite']"})
        },
        u'Differ.sitemembership': {
            'Meta': {'object_name': 'SiteMembership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'paid': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Differ.RegisteredPerson']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Differ.DiffedSite']"})
        }
    }

    complete_apps = ['Differ']