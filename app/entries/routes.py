from flask import Blueprint, render_template
from app.models import Entry, Tag
from .helpers import object_list

entries = Blueprint('entries', __name__, template_folder='templates')


@entries.route('/')
def index():
    entries = Entry.query.order_by(Entry.created_timestamp.desc())
    return object_list('entries/index.html', entries)


@entries.route('/tags/')
def tag_index():
    tags = Tag.query.order_by(Tag.name)
    return object_list('entries/tag_index.html', tags)


@entries.route('/tags/<slug>/')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    entries = tag.entries.order_by(Entry.created_timestamp.desc())
    return object_list('entries/tag_detail.html', entries, tag=tag)


@entries.route('/<slug>/')
def detail(slug):
    entry = Entry.query.filter(Entry.slug == slug).first_or_404()
    return render_template('entries/detail.html', entry=entry)
