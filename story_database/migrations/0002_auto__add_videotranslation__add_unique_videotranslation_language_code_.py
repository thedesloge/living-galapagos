# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VideoTranslation'
        db.create_table('story_database_video_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('vimeo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Video'])),
        ))
        db.send_create_signal('story_database', ['VideoTranslation'])

        # Adding unique constraint on 'VideoTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_video_translation', ['language_code', 'master_id'])

        # Adding model 'PhotoTranslation'
        db.create_table('story_database_photo_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Photo'])),
        ))
        db.send_create_signal('story_database', ['PhotoTranslation'])

        # Adding unique constraint on 'PhotoTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_photo_translation', ['language_code', 'master_id'])

        # Adding model 'InfographicPackageTranslation'
        db.create_table('story_database_infographicpackage_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('infographic_bundle', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.InfographicPackage'])),
        ))
        db.send_create_signal('story_database', ['InfographicPackageTranslation'])

        # Adding unique constraint on 'InfographicPackageTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_infographicpackage_translation', ['language_code', 'master_id'])

        # Adding model 'PhotoGalleryTranslation'
        db.create_table('story_database_photogallery_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.PhotoGallery'])),
        ))
        db.send_create_signal('story_database', ['PhotoGalleryTranslation'])

        # Adding unique constraint on 'PhotoGalleryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_photogallery_translation', ['language_code', 'master_id'])

        # Deleting field 'Video.vimeo_id'
        db.delete_column('story_database_video', 'vimeo_id')

        # Deleting field 'Video.description'
        db.delete_column('story_database_video', 'description')

        # Deleting field 'Video.title'
        db.delete_column('story_database_video', 'title')


    def backwards(self, orm):
        # Removing unique constraint on 'PhotoGalleryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_photogallery_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'InfographicPackageTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_infographicpackage_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'PhotoTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_photo_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'VideoTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_video_translation', ['language_code', 'master_id'])

        # Deleting model 'VideoTranslation'
        db.delete_table('story_database_video_translation')

        # Deleting model 'PhotoTranslation'
        db.delete_table('story_database_photo_translation')

        # Deleting model 'InfographicPackageTranslation'
        db.delete_table('story_database_infographicpackage_translation')

        # Deleting model 'PhotoGalleryTranslation'
        db.delete_table('story_database_photogallery_translation')

        # Adding field 'Video.vimeo_id'
        db.add_column('story_database_video', 'vimeo_id',
                      self.gf('django.db.models.fields.IntegerField')(default=datetime.datetime(2012, 8, 10, 0, 0)),
                      keep_default=False)

        # Adding field 'Video.description'
        db.add_column('story_database_video', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Video.title'
        db.add_column('story_database_video', 'title',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2012, 8, 10, 0, 0), max_length=100, unique=True),
                      keep_default=False)


    models = {
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'story_database.infographicpackage': {
            'Meta': {'object_name': 'InfographicPackage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.infographicpackagetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'InfographicPackageTranslation', 'db_table': "'story_database_infographicpackage_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infographic_bundle': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.InfographicPackage']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'story_database.infographics_story': {
            'Meta': {'object_name': 'Infographics_Story'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infographic_package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.InfographicPackage']", 'null': 'True', 'blank': 'True'}),
            'internal_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.infographics_storytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'Infographics_StoryTranslation', 'db_table': "'story_database_infographics_story_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.Infographics_Story']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'story_database.photo': {
            'Meta': {'object_name': 'Photo'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.photo_story': {
            'Meta': {'object_name': 'Photo_Story'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'photo_gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.PhotoGallery']", 'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.photo_storytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'Photo_StoryTranslation', 'db_table': "'story_database_photo_story_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.Photo_Story']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'story_database.photogallery': {
            'Meta': {'object_name': 'PhotoGallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Photo']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.photogallerytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PhotoGalleryTranslation', 'db_table': "'story_database_photogallery_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.PhotoGallery']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'story_database.phototranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PhotoTranslation', 'db_table': "'story_database_photo_translation'"},
            'caption': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.Photo']"})
        },
        'story_database.story': {
            'Meta': {'object_name': 'Story'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.storytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'StoryTranslation', 'db_table': "'story_database_story_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.Story']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'story_database.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.tagtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'TagTranslation', 'db_table': "'story_database_tag_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.Tag']"}),
            'tag_translation': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'story_database.video': {
            'Meta': {'object_name': 'Video'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'story_database.video_background': {
            'Meta': {'object_name': 'Video_Background'},
            'h264_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jpg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ogg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.video_story': {
            'Meta': {'object_name': 'Video_Story'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.video_storytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'Video_StoryTranslation', 'db_table': "'story_database_video_story_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.Video_Story']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vimeo_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'story_database.videotranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'VideoTranslation', 'db_table': "'story_database_video_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.Video']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vimeo_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['story_database']