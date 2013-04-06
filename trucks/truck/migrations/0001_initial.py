# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Truck'
        db.create_table(u'truck_truck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'truck', ['Truck'])

        # Adding model 'Stop'
        db.create_table(u'truck_stop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('truck', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truck.Truck'])),
        ))
        db.send_create_signal(u'truck', ['Stop'])


    def backwards(self, orm):
        # Deleting model 'Truck'
        db.delete_table(u'truck_truck')

        # Deleting model 'Stop'
        db.delete_table(u'truck_stop')


    models = {
        u'truck.stop': {
            'Meta': {'object_name': 'Stop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'truck': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truck.Truck']"})
        },
        u'truck.truck': {
            'Meta': {'object_name': 'Truck'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['truck']