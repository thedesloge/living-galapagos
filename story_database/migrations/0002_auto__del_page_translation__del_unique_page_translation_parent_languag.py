# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Tag_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_tag_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Page_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_page_translation', ['parent_id', 'language_code'])

        # Deleting model 'Page_Translation'
        db.delete_table('story_database_page_translation')

        # Deleting model 'Page'
        db.delete_table('story_database_page')

        # Deleting model 'Tag_Translation'
        db.delete_table('story_database_tag_translation')


    def backwards(self, orm):
        # Adding model 'Page_Translation'
        db.create_table('story_database_page_translation', (
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Featured Video', null=True, to=orm['story_database.Video'], blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Page'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('single_line_description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('story_database', ['Page_Translation'])

        # Adding unique constraint on 'Page_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_page_translation', ['parent_id', 'language_code'])

        # Adding model 'Page'
        db.create_table('story_database_page', (
            ('video_background', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Video_Background'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Page'])

        # Adding model 'Tag_Translation'
        db.create_table('story_database_tag_translation', (
            ('translation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Tag'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('story_database', ['Tag_Translation'])

        # Adding unique constraint on 'Tag_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_tag_translation', ['parent_id', 'language_code'])


    models = {
        'story_database.site': {
            'Meta': {'object_name': 'Site'},
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'story_database.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.video': {
            'Meta': {'object_name': 'Video'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'vimeo_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'story_database.video_background': {
            'Meta': {'object_name': 'Video_Background'},
            'h264_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jpg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ogg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['story_database']