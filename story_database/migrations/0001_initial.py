# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StoryTranslation'
        db.create_table('story_database_story_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Story'])),
        ))
        db.send_create_signal('story_database', ['StoryTranslation'])

        # Adding unique constraint on 'StoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_story_translation', ['language_code', 'master_id'])

        # Adding model 'Story'
        db.create_table('story_database_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('story_database', ['Story'])

        # Adding M2M table for field sites on 'Story'
        db.create_table('story_database_story_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['story_database.story'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('story_database_story_sites', ['story_id', 'site_id'])

        # Adding M2M table for field tags on 'Story'
        db.create_table('story_database_story_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['story_database.story'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_story_tags', ['story_id', 'tag_id'])

        # Adding model 'Video_StoryTranslation'
        db.create_table('story_database_video_story_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('vimeo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Video_Story'])),
        ))
        db.send_create_signal('story_database', ['Video_StoryTranslation'])

        # Adding unique constraint on 'Video_StoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_video_story_translation', ['language_code', 'master_id'])

        # Adding model 'Video_Story'
        db.create_table('story_database_video_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
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

        # Adding model 'Infographics_StoryTranslation'
        db.create_table('story_database_infographics_story_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Infographics_Story'])),
        ))
        db.send_create_signal('story_database', ['Infographics_StoryTranslation'])

        # Adding unique constraint on 'Infographics_StoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_infographics_story_translation', ['language_code', 'master_id'])

        # Adding model 'Infographics_Story'
        db.create_table('story_database_infographics_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('infographic_package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.InfographicPackage'], null=True, blank=True)),
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
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Photo_Story'])),
        ))
        db.send_create_signal('story_database', ['Photo_StoryTranslation'])

        # Adding unique constraint on 'Photo_StoryTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_photo_story_translation', ['language_code', 'master_id'])

        # Adding model 'Photo_Story'
        db.create_table('story_database_photo_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('internal_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('photo_gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.PhotoGallery'], null=True, blank=True)),
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

        # Adding model 'Video'
        db.create_table('story_database_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vimeo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
        ))
        db.send_create_signal('story_database', ['Video'])

        # Adding M2M table for field tags on 'Video'
        db.create_table('story_database_video_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['story_database.video'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_video_tags', ['video_id', 'tag_id'])

        # Adding model 'InfographicPackage'
        db.create_table('story_database_infographicpackage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('story_database', ['InfographicPackage'])

        # Adding model 'PhotoGallery'
        db.create_table('story_database_photogallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('story_database', ['PhotoGallery'])

        # Adding M2M table for field photos on 'PhotoGallery'
        db.create_table('story_database_photogallery_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photogallery', models.ForeignKey(orm['story_database.photogallery'], null=False)),
            ('photo', models.ForeignKey(orm['story_database.photo'], null=False))
        ))
        db.create_unique('story_database_photogallery_photos', ['photogallery_id', 'photo_id'])

        # Adding model 'Photo'
        db.create_table('story_database_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Photo'])

        # Adding model 'Video_Background'
        db.create_table('story_database_video_background', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('h264_background', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('ogg_background', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('jpg_background', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Video_Background'])

        # Adding model 'TagTranslation'
        db.create_table('story_database_tag_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_translation', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Tag'])),
        ))
        db.send_create_signal('story_database', ['TagTranslation'])

        # Adding unique constraint on 'TagTranslation', fields ['language_code', 'master']
        db.create_unique('story_database_tag_translation', ['language_code', 'master_id'])

        # Adding model 'Tag'
        db.create_table('story_database_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('story_database', ['Tag'])


    def backwards(self, orm):
        # Removing unique constraint on 'TagTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_tag_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'Photo_StoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_photo_story_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'Infographics_StoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_infographics_story_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'Video_StoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_video_story_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'StoryTranslation', fields ['language_code', 'master']
        db.delete_unique('story_database_story_translation', ['language_code', 'master_id'])

        # Deleting model 'StoryTranslation'
        db.delete_table('story_database_story_translation')

        # Deleting model 'Story'
        db.delete_table('story_database_story')

        # Removing M2M table for field sites on 'Story'
        db.delete_table('story_database_story_sites')

        # Removing M2M table for field tags on 'Story'
        db.delete_table('story_database_story_tags')

        # Deleting model 'Video_StoryTranslation'
        db.delete_table('story_database_video_story_translation')

        # Deleting model 'Video_Story'
        db.delete_table('story_database_video_story')

        # Removing M2M table for field sites on 'Video_Story'
        db.delete_table('story_database_video_story_sites')

        # Removing M2M table for field tags on 'Video_Story'
        db.delete_table('story_database_video_story_tags')

        # Deleting model 'Infographics_StoryTranslation'
        db.delete_table('story_database_infographics_story_translation')

        # Deleting model 'Infographics_Story'
        db.delete_table('story_database_infographics_story')

        # Removing M2M table for field sites on 'Infographics_Story'
        db.delete_table('story_database_infographics_story_sites')

        # Removing M2M table for field tags on 'Infographics_Story'
        db.delete_table('story_database_infographics_story_tags')

        # Deleting model 'Photo_StoryTranslation'
        db.delete_table('story_database_photo_story_translation')

        # Deleting model 'Photo_Story'
        db.delete_table('story_database_photo_story')

        # Removing M2M table for field sites on 'Photo_Story'
        db.delete_table('story_database_photo_story_sites')

        # Removing M2M table for field tags on 'Photo_Story'
        db.delete_table('story_database_photo_story_tags')

        # Deleting model 'Video'
        db.delete_table('story_database_video')

        # Removing M2M table for field tags on 'Video'
        db.delete_table('story_database_video_tags')

        # Deleting model 'InfographicPackage'
        db.delete_table('story_database_infographicpackage')

        # Deleting model 'PhotoGallery'
        db.delete_table('story_database_photogallery')

        # Removing M2M table for field photos on 'PhotoGallery'
        db.delete_table('story_database_photogallery_photos')

        # Deleting model 'Photo'
        db.delete_table('story_database_photo')

        # Deleting model 'Video_Background'
        db.delete_table('story_database_video_background')

        # Deleting model 'TagTranslation'
        db.delete_table('story_database_tag_translation')

        # Deleting model 'Tag'
        db.delete_table('story_database_tag')


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
        }
    }

    complete_apps = ['story_database']