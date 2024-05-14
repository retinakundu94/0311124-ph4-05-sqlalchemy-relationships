from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
# wait what the heck is an association proxy?

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# BUILD OUT THE FOLLOWING MODELS

# YOU WILL NEED ADDITIONAL COLUMNS FOR THE FOREIGN KEYS


# VideoGame #########
# id        integer #
# name     string  #
#####################

class VideoGame():
    pass


# Publication #######
# id        integer #
# name      string  #
#####################

class Publication():
    pass


# Rating ############
# id        integer #
# rating    integer  #
#####################

class Review():
    pass