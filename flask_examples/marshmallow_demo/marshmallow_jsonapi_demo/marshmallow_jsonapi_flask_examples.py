'''
Flask integration that avoids the need to hard-code URLs for links.

This includes a Flask-specific schema with custom Meta options and a relationship field for linking to related resources.
'''
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Comment:
    def __init__(self, id, body, author):
        self.id = id
        self.body = body
        self.author = author


class Post:
    def __init__(self, id, title, author, comments=None):
        self.id = id
        self.title = title
        self.author = author
        self.comments = [] if comments is None else comments


class PostSchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String()

    author = fields.Relationship(
        self_view='post_author',
        self_url_kwargs={'post_id': '<id>'},
        related_view='author_detail',
        related_url_kwargs={'author_id': '<author.id>'}
    )

    comments = fields.Relationship(
        related_view='post_comments',
        related_url_kwargs={'post_id': '<id>'},
        many=True,
        include_resource_linkage=True,
        type_='comments'
    )

    class Meta:
        type_ = 'posts'
        self_view = 'post_detail'
        self_view_kwargs = {'post_detail': '<id>'}
        self_view_many = 'post_list'
