import datetime as dt
import numpy as np
import pandas as pd
# Import SQLAlchemy to access SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Flask Dependency
from flask import Flask, jsonify

