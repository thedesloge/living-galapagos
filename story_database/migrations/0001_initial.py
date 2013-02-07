# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table('story_database_site', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('story_database', ['Site'])

        # Adding model 'Resources'
        db.create_table('story_database_resources', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('resource_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['Resources'])

        # Adding model 'Category'
        db.create_table('story_database_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('story_database', ['Category'])

        # Adding model 'Category_Translation'
        db.create_table('story_database_category_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Category'])),
            ('translation', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Category_Translation'])

        # Adding unique constraint on 'Category_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_category_translation', ['parent_id', 'language_code'])

        # Adding model 'Background_Video'
        db.create_table('story_database_background_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'])),
            ('h264_background', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('ogg_background', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('jpg_background', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Background_Video'])

        # Adding model 'Tag'
        db.create_table('story_database_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('story_database', ['Tag'])

        # Adding model 'Tag_Translation'
        db.create_table('story_database_tag_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Tag'])),
            ('translation', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Tag_Translation'])

        # Adding unique constraint on 'Tag_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_tag_translation', ['parent_id', 'language_code'])

        # Adding model 'Video'
        db.create_table('story_database_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vimeo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('related_content_thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
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

        # Adding model 'Poster_Frame'
        db.create_table('story_database_poster_frame', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('poster_frame', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Poster_Frame'])

        # Adding model 'Photo'
        db.create_table('story_database_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'], null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
        ))
        db.send_create_signal('story_database', ['Photo'])

        # Adding M2M table for field tags on 'Photo'
        db.create_table('story_database_photo_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo', models.ForeignKey(orm['story_database.photo'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_photo_tags', ['photo_id', 'tag_id'])

        # Adding model 'Photo_Translation'
        db.create_table('story_database_photo_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Photo'])),
            ('caption', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('story_database', ['Photo_Translation'])

        # Adding unique constraint on 'Photo_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_photo_translation', ['parent_id', 'language_code'])

        # Adding model 'Photo_Gallery'
        db.create_table('story_database_photo_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'], null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
        ))
        db.send_create_signal('story_database', ['Photo_Gallery'])

        # Adding M2M table for field photos on 'Photo_Gallery'
        db.create_table('story_database_photo_gallery_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo_gallery', models.ForeignKey(orm['story_database.photo_gallery'], null=False)),
            ('photo', models.ForeignKey(orm['story_database.photo'], null=False))
        ))
        db.create_unique('story_database_photo_gallery_photos', ['photo_gallery_id', 'photo_id'])

        # Adding M2M table for field tag on 'Photo_Gallery'
        db.create_table('story_database_photo_gallery_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo_gallery', models.ForeignKey(orm['story_database.photo_gallery'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_photo_gallery_tag', ['photo_gallery_id', 'tag_id'])

        # Adding model 'Photo_Gallery_Translation'
        db.create_table('story_database_photo_gallery_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Photo_Gallery'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('story_database', ['Photo_Gallery_Translation'])

        # Adding unique constraint on 'Photo_Gallery_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_photo_gallery_translation', ['parent_id', 'language_code'])

        # Adding model 'Infographic'
        db.create_table('story_database_infographic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'], null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
        ))
        db.send_create_signal('story_database', ['Infographic'])

        # Adding M2M table for field tag on 'Infographic'
        db.create_table('story_database_infographic_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infographic', models.ForeignKey(orm['story_database.infographic'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_infographic_tag', ['infographic_id', 'tag_id'])

        # Adding model 'Infographic_Translation'
        db.create_table('story_database_infographic_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Infographic'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('is_interactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('infographic_files', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Infographic_Translation'])

        # Adding unique constraint on 'Infographic_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_infographic_translation', ['parent_id', 'language_code'])

        # Adding model 'Related_Content'
        db.create_table('story_database_related_content', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['Related_Content'])

        # Adding M2M table for field tag on 'Related_Content'
        db.create_table('story_database_related_content_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('related_content', models.ForeignKey(orm['story_database.related_content'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_related_content_tag', ['related_content_id', 'tag_id'])

        # Adding model 'Related_Content_Translation'
        db.create_table('story_database_related_content_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Related_Content'])),
        ))
        db.send_create_signal('story_database', ['Related_Content_Translation'])

        # Adding unique constraint on 'Related_Content_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_related_content_translation', ['parent_id', 'language_code'])

        # Adding M2M table for field videos on 'Related_Content_Translation'
        db.create_table('story_database_related_content_translation_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('related_content_translation', models.ForeignKey(orm['story_database.related_content_translation'], null=False)),
            ('video', models.ForeignKey(orm['story_database.video'], null=False))
        ))
        db.create_unique('story_database_related_content_translation_videos', ['related_content_translation_id', 'video_id'])

        # Adding M2M table for field infographics on 'Related_Content_Translation'
        db.create_table('story_database_related_content_translation_infographics', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('related_content_translation', models.ForeignKey(orm['story_database.related_content_translation'], null=False)),
            ('infographic', models.ForeignKey(orm['story_database.infographic'], null=False))
        ))
        db.create_unique('story_database_related_content_translation_infographics', ['related_content_translation_id', 'infographic_id'])

        # Adding M2M table for field photo_galleries on 'Related_Content_Translation'
        db.create_table('story_database_related_content_translation_photo_galleries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('related_content_translation', models.ForeignKey(orm['story_database.related_content_translation'], null=False)),
            ('photo_gallery', models.ForeignKey(orm['story_database.photo_gallery'], null=False))
        ))
        db.create_unique('story_database_related_content_translation_photo_galleries', ['related_content_translation_id', 'photo_gallery_id'])

        # Adding model 'Story'
        db.create_table('story_database_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('menu_order', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Site'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'], null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
        ))
        db.send_create_signal('story_database', ['Story'])

        # Adding M2M table for field tags on 'Story'
        db.create_table('story_database_story_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['story_database.story'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_story_tags', ['story_id', 'tag_id'])

        # Adding model 'Story_Translation'
        db.create_table('story_database_story_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Story'])),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('subheadline', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('single_line_description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('quote', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quote_attribution', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('poster_frame', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Poster_Frame'], null=True, blank=True)),
            ('featured_video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Video'], null=True, blank=True)),
            ('related_content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Related_Content'], null=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['Story_Translation'])

        # Adding unique constraint on 'Story_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_story_translation', ['parent_id', 'language_code'])

        # Adding model 'Research'
        db.create_table('story_database_research', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['Research'])

        # Adding model 'Research_Translation'
        db.create_table('story_database_research_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Research'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('institute', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['Research_Translation'])

        # Adding unique constraint on 'Research_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_research_translation', ['parent_id', 'language_code'])

        # Adding model 'Featured_Story'
        db.create_table('story_database_featured_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Story'], unique=True)),
        ))
        db.send_create_signal('story_database', ['Featured_Story'])

        # Adding model 'About_Page'
        db.create_table('story_database_about_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Site'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('story_database', ['About_Page'])

        # Adding model 'About_Page_Translation'
        db.create_table('story_database_about_page_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.About_Page'])),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('subheadline', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('about_text', self.gf('django.db.models.fields.TextField')()),
            ('quote', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quote_attribution', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('featured_video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Video'], null=True, blank=True)),
            ('related_content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Related_Content'], null=True, blank=True)),
        ))
        db.send_create_signal('story_database', ['About_Page_Translation'])

        # Adding unique constraint on 'About_Page_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_about_page_translation', ['parent_id', 'language_code'])

        # Adding model 'Title_Card'
        db.create_table('story_database_title_card', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Story'])),
        ))
        db.send_create_signal('story_database', ['Title_Card'])

        # Adding model 'Title_Card_Translation'
        db.create_table('story_database_title_card_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translation', to=orm['story_database.Title_Card'])),
            ('title_card', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Title_Card_Translation'])

        # Adding unique constraint on 'Title_Card_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_title_card_translation', ['parent_id', 'language_code'])


    def backwards(self, orm):
        # Removing unique constraint on 'Title_Card_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_title_card_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'About_Page_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_about_page_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Research_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_research_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Story_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_story_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Related_Content_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_related_content_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Infographic_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_infographic_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Photo_Gallery_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_photo_gallery_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Photo_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_photo_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Tag_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_tag_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Category_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_category_translation', ['parent_id', 'language_code'])

        # Deleting model 'Site'
        db.delete_table('story_database_site')

        # Deleting model 'Resources'
        db.delete_table('story_database_resources')

        # Deleting model 'Category'
        db.delete_table('story_database_category')

        # Deleting model 'Category_Translation'
        db.delete_table('story_database_category_translation')

        # Deleting model 'Background_Video'
        db.delete_table('story_database_background_video')

        # Deleting model 'Tag'
        db.delete_table('story_database_tag')

        # Deleting model 'Tag_Translation'
        db.delete_table('story_database_tag_translation')

        # Deleting model 'Video'
        db.delete_table('story_database_video')

        # Removing M2M table for field tags on 'Video'
        db.delete_table('story_database_video_tags')

        # Deleting model 'Poster_Frame'
        db.delete_table('story_database_poster_frame')

        # Deleting model 'Photo'
        db.delete_table('story_database_photo')

        # Removing M2M table for field tags on 'Photo'
        db.delete_table('story_database_photo_tags')

        # Deleting model 'Photo_Translation'
        db.delete_table('story_database_photo_translation')

        # Deleting model 'Photo_Gallery'
        db.delete_table('story_database_photo_gallery')

        # Removing M2M table for field photos on 'Photo_Gallery'
        db.delete_table('story_database_photo_gallery_photos')

        # Removing M2M table for field tag on 'Photo_Gallery'
        db.delete_table('story_database_photo_gallery_tag')

        # Deleting model 'Photo_Gallery_Translation'
        db.delete_table('story_database_photo_gallery_translation')

        # Deleting model 'Infographic'
        db.delete_table('story_database_infographic')

        # Removing M2M table for field tag on 'Infographic'
        db.delete_table('story_database_infographic_tag')

        # Deleting model 'Infographic_Translation'
        db.delete_table('story_database_infographic_translation')

        # Deleting model 'Related_Content'
        db.delete_table('story_database_related_content')

        # Removing M2M table for field tag on 'Related_Content'
        db.delete_table('story_database_related_content_tag')

        # Deleting model 'Related_Content_Translation'
        db.delete_table('story_database_related_content_translation')

        # Removing M2M table for field videos on 'Related_Content_Translation'
        db.delete_table('story_database_related_content_translation_videos')

        # Removing M2M table for field infographics on 'Related_Content_Translation'
        db.delete_table('story_database_related_content_translation_infographics')

        # Removing M2M table for field photo_galleries on 'Related_Content_Translation'
        db.delete_table('story_database_related_content_translation_photo_galleries')

        # Deleting model 'Story'
        db.delete_table('story_database_story')

        # Removing M2M table for field tags on 'Story'
        db.delete_table('story_database_story_tags')

        # Deleting model 'Story_Translation'
        db.delete_table('story_database_story_translation')

        # Deleting model 'Research'
        db.delete_table('story_database_research')

        # Deleting model 'Research_Translation'
        db.delete_table('story_database_research_translation')

        # Deleting model 'Featured_Story'
        db.delete_table('story_database_featured_story')

        # Deleting model 'About_Page'
        db.delete_table('story_database_about_page')

        # Deleting model 'About_Page_Translation'
        db.delete_table('story_database_about_page_translation')

        # Deleting model 'Title_Card'
        db.delete_table('story_database_title_card')

        # Deleting model 'Title_Card_Translation'
        db.delete_table('story_database_title_card_translation')


    models = {
        'story_database.about_page': {
            'Meta': {'object_name': 'About_Page'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.about_page_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'About_Page_Translation'},
            'about_text': ('django.db.models.fields.TextField', [], {}),
            'featured_video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Video']", 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.About_Page']"}),
            'quote': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quote_attribution': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'related_content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Related_Content']", 'null': 'True', 'blank': 'True'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'story_database.background_video': {
            'Meta': {'object_name': 'Background_Video'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Category']"}),
            'h264_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jpg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ogg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.category_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Category_Translation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.Category']"}),
            'translation': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'story_database.featured_story': {
            'Meta': {'object_name': 'Featured_Story'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Story']", 'unique': 'True'})
        },
        'story_database.infographic': {
            'Meta': {'object_name': 'Infographic'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.infographic_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Infographic_Translation'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infographic_files': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'is_interactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.Infographic']"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'story_database.photo': {
            'Meta': {'object_name': 'Photo'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.photo_gallery': {
            'Meta': {'object_name': 'Photo_Gallery'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['story_database.Photo']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'story_database.photo_gallery_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Photo_Gallery_Translation'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.Photo_Gallery']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'story_database.photo_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Photo_Translation'},
            'caption': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Photo']"})
        },
        'story_database.poster_frame': {
            'Meta': {'object_name': 'Poster_Frame'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'poster_frame': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.related_content': {
            'Meta': {'object_name': 'Related_Content'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.related_content_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Related_Content_Translation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infographics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Infographic']", 'null': 'True', 'blank': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.Related_Content']"}),
            'photo_galleries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Photo_Gallery']", 'null': 'True', 'blank': 'True'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Video']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.research': {
            'Meta': {'object_name': 'Research'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.research_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Research_Translation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.Research']"}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'story_database.resources': {
            'Meta': {'object_name': 'Resources'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resource_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'story_database.site': {
            'Meta': {'object_name': 'Site'},
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'story_database.story': {
            'Meta': {'object_name': 'Story'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Category']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'menu_order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'story_database.story_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Story_Translation'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured_video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Video']", 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.Story']"}),
            'poster_frame': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Poster_Frame']", 'null': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quote_attribution': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'related_content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Related_Content']", 'null': 'True', 'blank': 'True'}),
            'single_line_description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'story_database.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.tag_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Tag_Translation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.Tag']"}),
            'translation': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'story_database.title_card': {
            'Meta': {'object_name': 'Title_Card'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Story']"})
        },
        'story_database.title_card_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Title_Card_Translation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translation'", 'to': "orm['story_database.Title_Card']"}),
            'title_card': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'story_database.video': {
            'Meta': {'object_name': 'Video'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Category']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'related_content_thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'vimeo_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['story_database']