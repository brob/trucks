# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Truck.twitter'
        db.delete_column(u'truck_truck', 'twitter')


    def backwards(self, orm):
        # Adding field 'Truck.twitter'
        db.add_column(u'truck_truck', 'twitter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)


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