from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response
import mysql.connector

app = Flask(__name__)

infoMysql = {
    'host': 'localhost',
    'user': 'root',
    'password': 'senhadobanco',
    'database': 'SMCM'
}


@app.route('/teste', methods=['GET'])
def teste():
    return render_template('teste.html', dados=realizaConsulta("select * from Tbpessoa"))


@app.route('/base', methods=['GET'])
def index():
    return render_template('base.html')


@app.route('/consultas', methods=['GET'])
def consultas():
    q = "select Status_agend, Data_agend, Horario, (select p.nome from paciente p where p.ID = ID_paciente), " \
        "(select m.nome from medico m where m.ID = ID_medico), ID from agendamento "
    m = "select Nome from medico"
    return render_template('consultas.html', dados=realizaConsulta(q), medicos=realizaConsulta(m))


@app.route('/consultas/deletarConsulta/<string:ids>', methods=['GET'])
def deletarConsultas(ids):
    id_list = ids.split(',')
    print(id_list)


@app.route('/consultas/filtrarConsulta/<string:valores>', methods=['GET'])
def filtrarConsultas(valores):
    valores_list = valores.split(',')
    print(valores_list)


@app.route('/medicos', methods=['GET'])
def medicos():
    return render_template('medicos.html')


#####################cadastros###############################

@app.route('/cadastroMedico', methods=['GET'])
def cadastroMedico():
    return render_template('cadastroMedico.html')


@app.route('/cadastroPaciente', methods=['GET'])
def cadastroPaciente():
    return render_template('cadastroPaciente.html')


#####################functions para manipulacao de dados###############################


def realizaConsulta(query):
    # Configuração da conexão com o banco de dados
    cnx = mysql.connector.connect(**infoMysql)
    # Cria um cursor para executar a consulta
    cursor = cnx.cursor()
    # Executa a consulta
    cursor.execute(query)
    # Obtém os resultados
    resultado = cursor.fetchall()
    # Fecha a conexão com o banco de dados
    cursor.close()
    cnx.close()
    return resultado


if __name__ == "__main__":
    app.run(debug=False)
