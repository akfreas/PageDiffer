# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RegisteredPerson'
        db.create_table(u'Differ_registeredperson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone_number', self.gf('django.db.models.fields.BigIntegerField')()),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'Differ', ['RegisteredPerson'])

        # Adding model 'DiffedSite'
        db.create_table(u'Differ_diffedsite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Differ', ['DiffedSite'])

        # Adding M2M table for field registered_users on 'DiffedSite'
        db.create_table(u'Differ_diffedsite_registered_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('diffedsite', models.ForeignKey(orm[u'Differ.diffedsite'], null=False)),
            ('registeredperson', models.ForeignKey(orm[u'Differ.registeredperson'], null=False))
        ))
        db.create_unique(u'Differ_diffedsite_registered_users', ['diffedsite_id', 'registeredperson_id'])


    def backwards(self, orm):
        # Deleting model 'RegisteredPerson'
        db.delete_table(u'Differ_registeredperson')

        # Deleting model 'DiffedSite'
        db.delete_table(u'Differ_diffedsite')

        # Removing M2M table for field registered_users on 'DiffedSite'
        db.delete_table('Differ_diffedsite_registered_users')


    models = {
        u'Differ.diffedsite': {
            'Meta': {'object_name': 'DiffedSite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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