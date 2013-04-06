# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Stop.address'
        db.add_column(u'truck_stop', 'address',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Stop.zip'
        db.add_column(u'truck_stop', 'zip',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Stop.city'
        db.add_column(u'truck_stop', 'city',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Stop.state'
        db.add_column(u'truck_stop', 'state',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Stop.arrival'
        db.add_column(u'truck_stop', 'arrival',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Stop.departure'
        db.add_column(u'truck_stop', 'departure',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Stop.address'
        db.delete_column(u'truck_stop', 'address')

        # Deleting field 'Stop.zip'
        db.delete_column(u'truck_stop', 'zip')

        # Deleting field 'Stop.city'
        db.delete_column(u'truck_stop', 'city')

        # Deleting field 'Stop.state'
        db.delete_column(u'truck_stop', 'state')

        # Deleting field 'Stop.arrival'
        db.delete_column(u'truck_stop', 'arrival')

        # Deleting field 'Stop.departure'
        db.delete_column(u'truck_stop', 'departure')


    models = {
        u'truck.stop': {
            'Meta': {'object_name': 'Stop'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'arrival': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'departure': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'truck': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truck.Truck']"}),
            'zip': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'truck.truck': {
            'Meta': {'object_name': 'Truck'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['truck']