# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Video_StoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_video_story_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'Infographics_StoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_infographics_story_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'Photo_StoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_photo_story_translation', ['language_code', 'master_id'])

        # Deleting model 'Infographics_Story'
        db.delete_table('story_database_infographics_story')

        # Removing M2M table for field sites on 'Infographics_Story'
        db.delete_table('story_database_infographics_story_sites')

        # Removing M2M table for field tags on 'Infographics_Story'
        db.delete_table('story_database_infographics_story_tags')

        # Deleting model 'Photo_StoryTranslation'
        db.delete_table('story_database_photo_story_translation')

        # Deleting model 'Infographics_StoryTranslation'
        db.delete_table('story_database_infographics_story_translation')

        # Deleting model 'Video_StoryTranslation'
        db.delete_table('story_database_video_story_translation')

        # Deleting model 'Video_Story'
        db.delete_table('story_database_video_story')

        # Removing M2M table for field sites on 'Video_Story'
        db.delete_table('story_database_video_story_sites')

        # Removing M2M table for field tags on 'Video_Story'
        db.delete_table('story_database_video_story_tags')

        # Deleting model 'Photo_Story'
        db.delete_table('story_database_photo_story')

        # Removing M2M table for field sites on 'Photo_Story'
        db.delete_table('story_database_photo_story_sites')

        # Removing M2M table for field tags on 'Photo_Story'
        db.delete_table('story_database_photo_story_tags')

        # Adding model 'PhotoStoryTranslation'
        db.create_table('story_database_photostory_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.PhotoStory'])),
        ))
        db.send_create_signal('story_database', ['PhotoStoryTranslation'])

        # Adding unique constraint on 'PhotoStoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_photostory_translation', ['language_code', 'master_id'])

        # Adding model 'InfographicStoryTranslation'
        db.create_table('story_database_infographicstory_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.InfographicStory'])),
        ))
        db.send_create_signal('story_database', ['InfographicStoryTranslation'])

        # Adding unique constraint on 'InfographicStoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_infographicstory_translation', ['language_code', 'master_id'])

        # Adding model 'VideoStoryTranslation'
        db.create_table('story_database_videostory_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('vimeo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.VideoStory'])),
        ))
        db.send_create_signal('story_database', ['VideoStoryTranslation'])

        # Adding unique constraint on 'VideoStoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_videostory_translation', ['language_code', 'master_id'])

        # Adding model 'InfographicStory'
        db.create_table('story_database_infographicstory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('infographic_package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.InfographicPackage'], null=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['InfographicStory'])

        # Adding M2M table for field sites on 'InfographicStory'
        db.create_table('story_database_infographicstory_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infographicstory', models.ForeignKey(orm['story_database.infographicstory'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('story_database_infographicstory_sites', ['infographicstory_id', 'site_id'])

        # Adding M2M table for field tags on 'InfographicStory'
        db.create_table('story_database_infographicstory_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infographicstory', models.ForeignKey(orm['story_database.infographicstory'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_infographicstory_tags', ['infographicstory_id', 'tag_id'])

        # Adding model 'PhotoStory'
        db.create_table('story_database_photostory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('photo_gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.PhotoGallery'], null=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['PhotoStory'])

        # Adding M2M table for field sites on 'PhotoStory'
        db.create_table('story_database_photostory_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photostory', models.ForeignKey(orm['story_database.photostory'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('story_database_photostory_sites', ['photostory_id', 'site_id'])

        # Adding M2M table for field tags on 'PhotoStory'
        db.create_table('story_database_photostory_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photostory', models.ForeignKey(orm['story_database.photostory'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_photostory_tags', ['photostory_id', 'tag_id'])

        # Adding model 'VideoStory'
        db.create_table('story_database_videostory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('story_database', ['VideoStory'])

        # Adding M2M table for field sites on 'VideoStory'
        db.create_table('story_database_videostory_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('videostory', models.ForeignKey(orm['story_database.videostory'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('story_database_videostory_sites', ['videostory_id', 'site_id'])

        # Adding M2M table for field tags on 'VideoStory'
        db.create_table('story_database_videostory_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('videostory', models.ForeignKey(orm['story_database.videostory'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_videostory_tags', ['videostory_id', 'tag_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'VideoStoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_videostory_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'InfographicStoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_infographicstory_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'PhotoStoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_photostory_translation', ['language_code', 'master_id'])

        # Adding model 'Infographics_Story'
        db.create_table('story_database_infographics_story', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('infographic_package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.InfographicPackage'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['Infographics_Story'])

        # Adding M2M table for field sites on 'Infographics_Story'
        db.create_table('story_database_infographics_story_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infographics_story', models.ForeignKey(orm['story_database.infographics_story'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('story_database_infographics_story_sites', ['infographics_story_id', 'site_id'])

        # Adding M2M table for field tags on 'Infographics_Story'
        db.create_table('story_database_infographics_story_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infographics_story', models.ForeignKey(orm['story_database.infographics_story'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_infographics_story_tags', ['infographics_story_id', 'tag_id'])

        # Adding model 'Photo_StoryTranslation'
        db.create_table('story_database_photo_story_translation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Photo_Story'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('story_database', ['Photo_StoryTranslation'])

        # Adding unique constraint on 'Photo_StoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_photo_story_translation', ['language_code', 'master_id'])

        # Adding model 'Infographics_StoryTranslation'
        db.create_table('story_database_infographics_story_translation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Infographics_Story'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('story_database', ['Infographics_StoryTranslation'])

        # Adding unique constraint on 'Infographics_StoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_infographics_story_translation', ['language_code', 'master_id'])

        # Adding model 'Video_StoryTranslation'
        db.create_table('story_database_video_story_translation', (
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Video_Story'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vimeo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('story_database', ['Video_StoryTranslation'])

        # Adding unique constraint on 'Video_StoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_video_story_translation', ['language_code', 'master_id'])

        # Adding model 'Video_Story'
        db.create_table('story_database_video_story', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['Video_Story'])

        # Adding M2M table for field sites on 'Video_Story'
        db.create_table('story_database_video_story_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video_story', models.ForeignKey(orm['story_database.video_story'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('story_database_video_story_sites', ['video_story_id', 'site_id'])

        # Adding M2M table for field tags on 'Video_Story'
        db.create_table('story_database_video_story_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video_story', models.ForeignKey(orm['story_database.video_story'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_video_story_tags', ['video_story_id', 'tag_id'])

        # Adding model 'Photo_Story'
        db.create_table('story_database_photo_story', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('photo_gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.PhotoGallery'], null=True, blank=True)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['Photo_Story'])

        # Adding M2M table for field sites on 'Photo_Story'
        db.create_table('story_database_photo_story_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo_story', models.ForeignKey(orm['story_database.photo_story'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('story_database_photo_story_sites', ['photo_story_id', 'site_id'])

        # Adding M2M table for field tags on 'Photo_Story'
        db.create_table('story_database_photo_story_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo_story', models.ForeignKey(orm['story_database.photo_story'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_photo_story_tags', ['photo_story_id', 'tag_id'])

        # Deleting model 'PhotoStoryTranslation'
        db.delete_table('story_database_photostory_translation')

        # Deleting model 'InfographicStoryTranslation'
        db.delete_table('story_database_infographicstory_translation')

        # Deleting model 'VideoStoryTranslation'
        db.delete_table('story_database_videostory_translation')

        # Deleting model 'InfographicStory'
        db.delete_table('story_database_infographicstory')

        # Removing M2M table for field sites on 'InfographicStory'
        db.delete_table('story_database_infographicstory_sites')

        # Removing M2M table for field tags on 'InfographicStory'
        db.delete_table('story_database_infographicstory_tags')

        # Deleting model 'PhotoStory'
        db.delete_table('story_database_photostory')

        # Removing M2M table for field sites on 'PhotoStory'
        db.delete_table('story_database_photostory_sites')

        # Removing M2M table for field tags on 'PhotoStory'
        db.delete_table('story_database_photostory_tags')

        # Deleting model 'VideoStory'
        db.delete_table('story_database_videostory')

        # Removing M2M table for field sites on 'VideoStory'
        db.delete_table('story_database_videostory_sites')

        # Removing M2M table for field tags on 'VideoStory'
        db.delete_table('story_database_videostory_tags')


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
        'story_database.infographicstory': {
            'Meta': {'object_name': 'InfographicStory'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infographic_package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.InfographicPackage']", 'null': 'True', 'blank': 'True'}),
            'internal_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.infographicstorytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'InfographicStoryTranslation', 'db_table': "'story_database_infographicstory_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.InfographicStory']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'story_database.photo': {
            'Meta': {'object_name': 'Photo'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
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
        'story_database.photostory': {
            'Meta': {'object_name': 'PhotoStory'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'photo_gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.PhotoGallery']", 'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.photostorytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PhotoStoryTranslation', 'db_table': "'story_database_photostory_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.PhotoStory']"}),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
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
        'story_database.videostory': {
            'Meta': {'object_name': 'VideoStory'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.videostorytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'VideoStoryTranslation', 'db_table': "'story_database_videostory_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['story_database.VideoStory']"}),
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