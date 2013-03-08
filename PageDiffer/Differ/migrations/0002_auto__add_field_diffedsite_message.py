# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DiffedSite.message'
        db.add_column(u'Differ_diffedsite', 'message',
                      self.gf('django.db.models.fields.CharField')(default='Your site has changes.', max_length=155),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DiffedSite.message'
        db.delete_column(u'Differ_diffedsite', 'message')


    models = {
        u'Differ.diffedsite': {
            'Meta': {'object_name': 'DiffedSite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'registered_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Differ.RegisteredPerson']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Differ.registeredperson': {
            'Meta': {'object_name': 'RegisteredPerson'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone_number': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['Differ']