# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MenuIcon.page'
        db.delete_column('menu_icons_menuicon', 'page_id')

        # Adding field 'MenuIcon.public_extension'
        db.add_column('menu_icons_menuicon', 'public_extension',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['menu_icons.MenuIcon'], unique=True, related_name='draft_extension', null=True),
                      keep_default=False)

        # Adding field 'MenuIcon.extended_object'
        db.add_column('menu_icons_menuicon', 'extended_object',
                      self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['cms.Page'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MenuIcon.page'
        db.add_column('menu_icons_menuicon', 'page',
                      self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['cms.Page'], null=True),
                      keep_default=False)

        # Deleting field 'MenuIcon.public_extension'
        db.delete_column('menu_icons_menuicon', 'public_extension_id')

        # Deleting field 'MenuIcon.extended_object'
        db.delete_column('menu_icons_menuicon', 'extended_object_id')


    models = {
        'cms.page': {
            'Meta': {'unique_together': "(('publisher_is_draft', 'application_namespace'), ('reverse_id', 'site', 'publisher_is_draft'))", 'object_name': 'Page', 'ordering': "('tree_id', 'lft')"},
            'application_namespace': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'application_urls': ('django.db.models.fields.CharField', [], {'null': 'True', 'db_index': 'True', 'blank': 'True', 'max_length': '200'}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'languages': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'db_index': 'True', 'blank': 'True', 'default': 'None'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'null': 'True', 'db_index': 'True', 'blank': 'True', 'max_length': '80'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']", 'related_name': "'children'", 'null': 'True', 'blank': 'True'}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['cms.Placeholder']"}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.Page']", 'unique': 'True', 'related_name': "'publisher_draft'", 'null': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'db_index': 'True', 'blank': 'True', 'max_length': '40'}),
            'revision_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'djangocms_pages'", 'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'INHERIT'", 'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'xframe_options': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50'})
        },
        'menu_icons.menuicon': {
            'Meta': {'object_name': 'MenuIcon'},
            'extended_object': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['cms.Page']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_icon_font_awesome': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '48'}),
            'menu_icon_image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'menu_icon_url': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'public_extension': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['menu_icons.MenuIcon']", 'unique': 'True', 'related_name': "'draft_extension'", 'null': 'True'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'", 'object_name': 'Site', 'ordering': "('domain',)"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['menu_icons']
