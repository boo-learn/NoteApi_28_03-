from api import api, app, docs
from api.resources import note
from api.resources.user import UserResource, UsersListResource
from api.resources.auth import TokenResource
from api.resources.tag import TagResource, TagsListResource
from config import Config

# CRUD

# Create --> POST
# Read --> GET
# Update --> PUT
# Delete --> DELETE
api.add_resource(UsersListResource,
                 '/users')  # GET, POST
api.add_resource(UserResource,
                 '/users/<int:user_id>')  # GET, PUT, DELETE

api.add_resource(TokenResource,
                 '/auth/token')  # GET

api.add_resource(note.NotesListResource,
                 '/notes',  # GET, POST
                 )
api.add_resource(note.NotesListByUserResource,
                 '/users/<user_id>/notes')  # GET
api.add_resource(note.NoteResource,
                 '/notes/<int:note_id>',  # GET, PUT, DELETE
                 )
api.add_resource(note.NoteSetTagsResource,
                 '/notes/<int:note_id>/set_tags',  # GET, PUT, DELETE
                 )
api.add_resource(TagsListResource,
                 '/tags',  # GET, POST
                 )
api.add_resource(TagResource,
                 '/tags/<int:tag_id>',  # GET, PUT, DELETE
                 )
# GET: /notes/filter?private=false
# GET: /notes/filter?username=<un>&private=false
# GET: /notes/filter?tag=good&username=Ivan
api.add_resource(note.NotesFilterResource,
                 '/notes/filter',  # GET
                 )
api.add_resource(note.NoteRestoreResource,
                 '/notes/<int:note_id>/restore',  # GET
                 )

docs.register(UserResource)
docs.register(UsersListResource)
docs.register(note.NoteResource)
docs.register(note.NotesListResource)
docs.register(TagResource)
docs.register(TagsListResource)
docs.register(note.NoteSetTagsResource)
docs.register(note.NotesListByUserResource)
docs.register(note.NotesFilterResource)
docs.register(note.NoteRestoreResource)
if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
