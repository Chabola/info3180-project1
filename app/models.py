from . import db


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    no_room = db.Column(db.Integer)
    no_bathroom = db.Column(db.Integer)
    location = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2))
    type = db.Column(db.String(255))
    description = db.Column(db.String(255))
    photo = db.Column(db.String(255))

    def __init__(self, title, no_room, no_bathroom, location, price, type, description, photo):
        self.title = title
        self.no_room = no_room
        self.no_bathroom = no_bathroom
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo
