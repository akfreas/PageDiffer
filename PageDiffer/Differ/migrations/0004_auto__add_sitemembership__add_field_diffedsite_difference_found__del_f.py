# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteMembership'
        db.create_table(u'Differ_sitemembership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Differ.RegisteredPerson'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Differ.DiffedSite'])),
            ('paid', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('notified', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'Differ', ['SiteMembership'])

        # Adding field 'DiffedSite.difference_found'
        db.add_column(u'Differ_diffedsite', 'difference_found',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Removing M2M table for field registered_users on 'DiffedSite'
        db.delete_table('Differ_diffedsite_registered_users')

        # Deleting field 'RegisteredPerson.paid'
        db.delete_column(u'Differ_registeredperson', 'paid')


    def backwards(self, orm):
        # Deleting model 'SiteMembership'
        db.delete_table(u'Differ_sitemembership')

        # Deleting field 'DiffedSite.difference_found'
        db.delete_column(u'Differ_diffedsite', 'difference_found')

        # Adding M2M table for field registered_users on 'DiffedSite'
        db.create_table(u'Differ_diffedsite_registered_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('diffedsite', models.ForeignKey(orm[u'Differ.diffedsite'], null=False)),
            ('registeredperson', models.ForeignKey(orm[u'Differ.registeredperson'], null=False))
        ))
        db.create_unique(u'Differ_diffedsite_registered_users', ['diffedsite_id', 'registeredperson_id'])

        # Adding field 'RegisteredPerson.paid'
        db.add_column(u'Differ_registeredperson', 'paid',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


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