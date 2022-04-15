import sqlalchemy
from sqlalchemy import String, Integer

from .base import metadata
import datetime

posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("shortcode", sqlalchemy.String, unique=True),
    sqlalchemy.Column("created_time", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("timestamp", sqlalchemy.Integer),
    sqlalchemy.Column("product_type", sqlalchemy.String),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("text_lang", sqlalchemy.String),
    sqlalchemy.Column("text_tagged_users", sqlalchemy.ARRAY(Integer)),
    sqlalchemy.Column("text_tags", sqlalchemy.ARRAY(String)),
    sqlalchemy.Column("attached_media_display_url", sqlalchemy.String),
    sqlalchemy.Column("attached_media_content", sqlalchemy.ARRAY(String)),
    sqlalchemy.Column("attached_media_tagged_users", sqlalchemy.ARRAY(String)),
    sqlalchemy.Column("is_video", sqlalchemy.Boolean),
    sqlalchemy.Column("is_comments_disabled", sqlalchemy.Boolean),
    sqlalchemy.Column("like_count", sqlalchemy.Integer),
    sqlalchemy.Column("comments_count", sqlalchemy.Integer),
    sqlalchemy.Column("video_views_count", sqlalchemy.Integer),
    sqlalchemy.Column("video_plays_count", sqlalchemy.Integer),
    sqlalchemy.Column("related_posts", sqlalchemy.ARRAY(String)),
    sqlalchemy.Column("sponsors", sqlalchemy.ARRAY(Integer)),
    sqlalchemy.Column("owner_id", sqlalchemy.Integer, unique=True),
    sqlalchemy.Column("location_id", sqlalchemy.Integer, unique=True),
)
