# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'ArticlePageTranslation', fields ['language_code', 'master']
        db.delete_unique(u'story_database_articlepage_translation', ['language_code', 'master_id'])

        # Deleting model 'ArticlePage'
        db.delete_table(u'story_database_articlepage')

        # Removing M2M table for field tags on 'ArticlePage'
        db.delete_table('story_database_articlepage_tags')

        # Removing M2M table for field interactives on 'ArticlePage'
        db.delete_table('story_database_articlepage_interactives')

        # Deleting model 'ArticlePageTranslation'
        db.delete_table(u'story_database_articlepage_translation')


    def backwards(self, orm):
        # Adding model 'ArticlePage'
        db.create_table(u'story_database_articlepage', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'], null=True, blank=True)),
            ('chapter_graphic', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('chapter_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('top_nav', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('chapter_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('top_image', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chapter_subtitle', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'story_database', ['ArticlePage'])

        # Adding M2M table for field tags on 'ArticlePage'
        db.create_table(u'story_database_articlepage_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articlepage', models.ForeignKey(orm[u'story_database.articlepage'], null=False)),
            ('tag', models.ForeignKey(orm[u'story_database.tag'], null=False))
        ))
        db.create_unique(u'story_database_articlepage_tags', ['articlepage_id', 'tag_id'])

        # Adding M2M table for field interactives on 'ArticlePage'
        db.create_table(u'story_database_articlepage_interactives', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articlepage', models.ForeignKey(orm[u'story_database.articlepage'], null=False)),
            ('interactive', models.ForeignKey(orm[u'story_database.interactive'], null=False))
        ))
        db.create_unique(u'story_database_articlepage_interactives', ['articlepage_id', 'interactive_id'])

        # Adding model 'ArticlePageTranslation'
        db.create_table(u'story_database_articlepage_translation', (
            ('subheadline', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.ArticlePage'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('quote', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('single_line_description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote_attribution', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'story_database', ['ArticlePageTranslation'])

        # Adding unique constraint on 'ArticlePageTranslation', fields ['language_code', 'master']
        db.create_unique(u'story_database_articlepage_translation', ['language_code', 'master_id'])


    models = {
        u'story_database.backgroundvideo': {
            'Meta': {'object_name': 'BackgroundVideo'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Category']"}),
            'h264_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jpg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ogg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'story_page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.StoryPage']", 'null': 'True', 'blank': 'True'})
        },
        u'story_database.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'story_database.categorytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'CategoryTranslation', 'db_table': "u'story_database_category_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['story_database.Category']"}),
            'translation': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'story_database.credit': {
            'Meta': {'object_name': 'Credit'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['story_database.Role']", 'symmetrical': 'False'})
        },
        u'story_database.credittranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'CreditTranslation', 'db_table': "u'story_database_credit_translation'"},
            'bio': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['story_database.Credit']"})
        },
        u'story_database.featuredstory': {
            'Meta': {'object_name': 'FeaturedStory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'story_database.featuredstoryitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'FeaturedStoryItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.FeaturedStory']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.StoryPage']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'story_database.interactive': {
            'Meta': {'object_name': 'Interactive'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.Credit']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infographic_files': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'is_spanish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.Tag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
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
        u'story_database.posterframe': {
            'Meta': {'object_name': 'PosterFrame'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_spanish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'poster_frame': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'story_database.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'story_database.storypage': {
            'Meta': {'object_name': 'StoryPage'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactives': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.Interactive']", 'null': 'True', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'related_stories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.StoryPage']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.Tag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Video']", 'null': 'True', 'blank': 'True'})
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
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
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Credit']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'story_database.videotranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'VideoTranslation', 'db_table': "u'story_database_video_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['story_database.Video']"}),
            'poster_frame': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.PosterFrame']", 'null': 'True', 'blank': 'True'}),
            'single_line_description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_card': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'vimeo_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['story_database']