# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Stop.city'
        db.alter_column(u'truck_stop', 'city', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Stop.zip'
        db.alter_column(u'truck_stop', 'zip', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Stop.state'
        db.alter_column(u'truck_stop', 'state', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Stop.address'
        db.alter_column(u'truck_stop', 'address', self.gf('django.db.models.fields.CharField')(max_length=500))

    def backwards(self, orm):

        # Changing field 'Stop.city'
        db.alter_column(u'truck_stop', 'city', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Stop.zip'
        db.alter_column(u'truck_stop', 'zip', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Stop.state'
        db.alter_column(u'truck_stop', 'state', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Stop.address'
        db.alter_column(u'truck_stop', 'address', self.gf('django.db.models.fields.TextField')())

    models = {
        u'truck.stop': {
            'Meta': {'object_name': 'Stop'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'arrival': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'departure': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'truck': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truck.Truck']"}),
            'zip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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