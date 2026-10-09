from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from database import conectar
import database


auth_bp = Blueprint("auth", __name__)
 

# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:
#

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
      nome = request.form['nome']
      email = request.form['email']
      senha = request.form['senha']
      senha_hash = generate_password_hash(senha)
      with conectar() as conexao:
        cursor = conexao.cursor()
        
        cursor.execute(
          """INSERT INTO usuarios (nome, email, senha_hash) VALUES (?,?, ?)""",
          (nome,email, senha_hash,)
        )
        flash('cadastro realizado')
      return redirect(url_for("auth.login"))

    return render_template("registro.html")



@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if 'usuario_id' in session:
        flash("Você já está logado.")
        return redirect(url_for("/"))

    if request.method == "POST":

        email = request.form['email']
        senha = request.form['senha']

        with conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                'SELECT * FROM usuarios WHERE email = ?',
                (email,)
            )

            usuario = cursor.fetchone()

        if usuario and check_password_hash(usuario[3], senha):
            session['usuario_id'] = usuario[0]
            flash("Login realizado com sucesso.")
            return redirect('/')

        flash("E-mail ou senha incorretos.")
        return redirect(url_for("auth.login"))

    return render_template("login.html")



@auth_bp.route("/logout")
def logout():
    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)
    flash("Logout realizado com sucesso.")
    return redirect(url_for("index"))
