# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StoryCategoryHeaderTranslation'
        db.create_table(u'story_database_storycategoryheader_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category_description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['story_database.StoryCategoryHeader'])),
        ))
        db.send_create_signal(u'story_database', ['StoryCategoryHeaderTranslation'])

        # Adding unique constraint on 'StoryCategoryHeaderTranslation', fields ['language_code', 'master']
        db.create_unique(u'story_database_storycategoryheader_translation', ['language_code', 'master_id'])

        # Adding model 'StoryCategoryHeader'
        db.create_table(u'story_database_storycategoryheader', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('background_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'story_database', ['StoryCategoryHeader'])

        # Adding field 'StoryPage.story_category_header'
        db.add_column(u'story_database_storypage', 'story_category_header',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.StoryCategoryHeader'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'StoryCategoryHeaderTranslation', fields ['language_code', 'master']
        db.delete_unique(u'story_database_storycategoryheader_translation', ['language_code', 'master_id'])

        # Deleting model 'StoryCategoryHeaderTranslation'
        db.delete_table(u'story_database_storycategoryheader_translation')

        # Deleting model 'StoryCategoryHeader'
        db.delete_table(u'story_database_storycategoryheader')

        # Deleting field 'StoryPage.story_category_header'
        db.delete_column(u'story_database_storypage', 'story_category_header_id')


    models = {
        u'story_database.articlechapter': {
            'Meta': {'object_name': 'ArticleChapter'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pano_head': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'related_stories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.ArticlePage']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.Video']", 'null': 'True', 'blank': 'True'})
        },
        u'story_database.articlechaptertranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ArticleChapterTranslation', 'db_table': "u'story_database_articlechapter_translation'"},
            'body_text': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactives': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.Interactive']", 'null': 'True', 'blank': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['story_database.ArticleChapter']"}),
            'quote': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quote_attribution': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'story_database.articlepage': {
            'Meta': {'object_name': 'ArticlePage'},
            'article_chapter': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['story_database.ArticleChapter']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'story_database.articlepagetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ArticlePageTranslation', 'db_table': "u'story_database_articlepage_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translation'", 'null': 'True', 'to': u"orm['story_database.ArticlePage']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
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
            'poster_frame': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.PosterFrame']", 'null': 'True', 'blank': 'True'}),
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
        u'story_database.storycategoryheader': {
            'Meta': {'object_name': 'StoryCategoryHeader'},
            'background_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'story_database.storycategoryheadertranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'StoryCategoryHeaderTranslation', 'db_table': "u'story_database_storycategoryheader_translation'"},
            'category_description': ('django.db.models.fields.TextField', [], {}),
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['story_database.StoryCategoryHeader']"})
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
            'story_category_header': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['story_database.StoryCategoryHeader']", 'null': 'True', 'blank': 'True'}),
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