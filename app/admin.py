from flask_admin import Admin
from .models import db,Entry,Tag
from flask_admin.contrib.sqla import ModelView


class EntryModelView(ModelView):
    pass

class TagModelView(ModelView):
    pass

administrator = Admin(name="Admin Panel")


administrator.add_view(EntryModelView(Entry,db.session))
administrator.add_view(TagModelView(Tag,db.session))
