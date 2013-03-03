# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'story_database_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'story_database', ['Category'])

        # Adding model 'TagTranslation'
        db.create_table(u'story_database_tag_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('translated_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Tag'])),
        ))
        db.send_create_signal(u'story_database', ['TagTranslation'])

        # Adding unique constraint on 'TagTranslation', fields ['language_code', 'master']
        db.create_unique(u'story_database_tag_translation', ['language_code', 'master_id'])

        # Adding model 'Tag'
        db.create_table(u'story_database_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'story_database', ['Tag'])

        # Adding model 'VideoTranslation'
        db.create_table(u'story_database_video_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subheadline', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('single_line_description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('vimeo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('poster_frame', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Video'])),
        ))
        db.send_create_signal(u'story_database', ['VideoTranslation'])

        # Adding unique constraint on 'VideoTranslation', fields ['language_code', 'master']
        db.create_unique(u'story_database_video_translation', ['language_code', 'master_id'])

        # Adding model 'Video'
        db.create_table(u'story_database_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'])),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'story_database', ['Video'])

        # Adding model 'Poster_Frame'
        db.create_table(u'story_database_poster_frame', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('poster_frame', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'story_database', ['Poster_Frame'])

        # Adding model 'InteractiveTranslation'
        db.create_table(u'story_database_interactive_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subheadline', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('single_line_description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('infographic_files', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.Interactive'])),
        ))
        db.send_create_signal(u'story_database', ['InteractiveTranslation'])

        # Adding unique constraint on 'InteractiveTranslation', fields ['language_code', 'master']
        db.create_unique(u'story_database_interactive_translation', ['language_code', 'master_id'])

        # Adding model 'Interactive'
        db.create_table(u'story_database_interactive', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'], null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'story_database', ['Interactive'])

        # Adding M2M table for field tag on 'Interactive'
        db.create_table(u'story_database_interactive_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('interactive', models.ForeignKey(orm[u'story_database.interactive'], null=False)),
            ('tag', models.ForeignKey(orm[u'story_database.tag'], null=False))
        ))
        db.create_unique(u'story_database_interactive_tag', ['interactive_id', 'tag_id'])

        # Adding model 'StoryPageTranslation'
        db.create_table(u'story_database_storypage_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subheadline', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('single_line_description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('quote', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quote_attribution', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.StoryPage'])),
        ))
        db.send_create_signal(u'story_database', ['StoryPageTranslation'])

        # Adding unique constraint on 'StoryPageTranslation', fields ['language_code', 'master']
        db.create_unique(u'story_database_storypage_translation', ['language_code', 'master_id'])

        # Adding model 'StoryPage'
        db.create_table(u'story_database_storypage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'], null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Video'])),
        ))
        db.send_create_signal(u'story_database', ['StoryPage'])

        # Adding M2M table for field tags on 'StoryPage'
        db.create_table(u'story_database_storypage_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('storypage', models.ForeignKey(orm[u'story_database.storypage'], null=False)),
            ('tag', models.ForeignKey(orm[u'story_database.tag'], null=False))
        ))
        db.create_unique(u'story_database_storypage_tags', ['storypage_id', 'tag_id'])

        # Adding M2M table for field related_stories on 'StoryPage'
        db.create_table(u'story_database_storypage_related_stories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_storypage', models.ForeignKey(orm[u'story_database.storypage'], null=False)),
            ('to_storypage', models.ForeignKey(orm[u'story_database.storypage'], null=False))
        ))
        db.create_unique(u'story_database_storypage_related_stories', ['from_storypage_id', 'to_storypage_id'])

        # Adding M2M table for field interactives on 'StoryPage'
        db.create_table(u'story_database_storypage_interactives', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('storypage', models.ForeignKey(orm[u'story_database.storypage'], null=False)),
            ('interactive', models.ForeignKey(orm[u'story_database.interactive'], null=False))
        ))
        db.create_unique(u'story_database_storypage_interactives', ['storypage_id', 'interactive_id'])

        # Adding model 'FeaturedStory'
        db.create_table(u'story_database_featuredstory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'story_database', ['FeaturedStory'])

        # Adding model 'FeaturedStoryItem'
        db.create_table(u'story_database_featuredstoryitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('featured_story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.FeaturedStory'])),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.StoryPage'])),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'story_database', ['FeaturedStoryItem'])

        # Adding model 'Menu'
        db.create_table(u'story_database_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'story_database', ['Menu'])

        # Adding model 'MenuItem'
        db.create_table(u'story_database_menuitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Menu'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_es', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.StoryPage'])),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'story_database', ['MenuItem'])


    def backwards(self, orm):
        # Removing unique constraint on 'StoryPageTranslation', fields ['language_code', 'master']
        db.delete_unique(u'story_database_storypage_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'InteractiveTranslation', fields ['language_code', 'master']
        db.delete_unique(u'story_database_interactive_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'VideoTranslation', fields ['language_code', 'master']
        db.delete_unique(u'story_database_video_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'TagTranslation', fields ['language_code', 'master']
        db.delete_unique(u'story_database_tag_translation', ['language_code', 'master_id'])

        # Deleting model 'Category'
        db.delete_table(u'story_database_category')

        # Deleting model 'TagTranslation'
        db.delete_table(u'story_database_tag_translation')

        # Deleting model 'Tag'
        db.delete_table(u'story_database_tag')

        # Deleting model 'VideoTranslation'
        db.delete_table(u'story_database_video_translation')

        # Deleting model 'Video'
        db.delete_table(u'story_database_video')

        # Deleting model 'Poster_Frame'
        db.delete_table(u'story_database_poster_frame')

        # Deleting model 'InteractiveTranslation'
        db.delete_table(u'story_database_interactive_translation')

        # Deleting model 'Interactive'
        db.delete_table(u'story_database_interactive')

        # Removing M2M table for field tag on 'Interactive'
        db.delete_table('story_database_interactive_tag')

        # Deleting model 'StoryPageTranslation'
        db.delete_table(u'story_database_storypage_translation')

        # Deleting model 'StoryPage'
        db.delete_table(u'story_database_storypage')

        # Removing M2M table for field tags on 'StoryPage'
        db.delete_table('story_database_storypage_tags')

        # Removing M2M table for field related_stories on 'StoryPage'
        db.delete_table('story_database_storypage_related_stories')

        # Removing M2M table for field interactives on 'StoryPage'
        db.delete_table('story_database_storypage_interactives')

        # Deleting model 'FeaturedStory'
        db.delete_table(u'story_database_featuredstory')

        # Deleting model 'FeaturedStoryItem'
        db.delete_table(u'story_database_featuredstoryitem')

        # Deleting model 'Menu'
        db.delete_table(u'story_database_menu')

        # Deleting model 'MenuItem'
        db.delete_table(u'story_database_menuitem')


    models = {
        u'story_database.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'story_database.featuredstory': {
            'Meta': {'object_name': 'FeaturedStory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'story_database.featuredstoryitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'FeaturedStoryItem'},
            'featured_story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.FeaturedStory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.StoryPage']"}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'story_database.interactive': {
            'Meta': {'object_name': 'Interactive'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.Tag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'story_database.interactivetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'InteractiveTranslation', 'db_table': "u'story_database_interactive_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infographic_files': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['story_database.Interactive']"}),
            'single_line_description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'story_database.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'story_database.menuitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'MenuItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Menu']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_es': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.StoryPage']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'story_database.poster_frame': {
            'Meta': {'object_name': 'Poster_Frame'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'poster_frame': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'story_database.storypage': {
            'Meta': {'object_name': 'StoryPage'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactives': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['story_database.Interactive']", 'symmetrical': 'False'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'related_stories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['story_database.StoryPage']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.Tag']", 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Video']"})
        },
        u'story_database.storypagetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'StoryPageTranslation', 'db_table': "u'story_database_storypage_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['story_database.StoryPage']"}),
            'quote': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quote_attribution': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'single_line_description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'story_database.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'story_database.tagtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'TagTranslation', 'db_table': "u'story_database_tag_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['story_database.Tag']"}),
            'translated_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'story_database.video': {
            'Meta': {'object_name': 'Video'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Category']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'story_database.videotranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'VideoTranslation', 'db_table': "u'story_database_video_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['story_database.Video']"}),
            'poster_frame': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'single_line_description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'vimeo_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['story_database']