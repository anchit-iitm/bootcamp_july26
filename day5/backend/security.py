from flask_security import Security
from argon2 import PasswordHasher

security = Security()
ph = PasswordHasher()