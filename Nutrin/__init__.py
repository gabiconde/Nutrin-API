from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from Nutrin.Model.Response import response

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# User
from Nutrin.User.Model.User import User
from Nutrin.User.Routes import *
from Nutrin.User.ErrorHandlers import *

#  Paciente
from Nutrin.Paciente.Model.Paciente import Paciente
from Nutrin.Paciente.Routes import *
from Nutrin.Paciente.ErrorHandlers import *

#  Consulta
from Nutrin.Consulta.Model.Consulta import Consulta
from Nutrin.Consulta.Model.TipoAtendimento import TipoAtendimento
from Nutrin.Consulta.Model.TipoEstado import TipoEstado
from Nutrin.Consulta.Model.Antropometria import Antropometria
from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin.Consulta.Model.Ocupado import Ocupado
from Nutrin.Consulta.Routes import *

# Alimentacao
from Nutrin.Alimentacao.Model.TipoRefeicao import TipoRefeicao
from Nutrin.Alimentacao.Model.Refeicao import Refeicao
from Nutrin.Alimentacao.Model.Anamnese import Anamnese
from Nutrin.Alimentacao.Routes import *
from Nutrin.Alimentacao.ErrorHandlers import *
