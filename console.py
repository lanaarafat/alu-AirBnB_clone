#!/usr/bin/python3

""" console """

import cmd
import re
import sys
from shlex import split 
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


