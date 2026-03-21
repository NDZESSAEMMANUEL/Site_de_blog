from flask import Flask,render_template,redirect,request,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.secret_key = "ma_cle_secrete_super_secure_123"


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///produits.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    titre = db.Column(db.String(80),unique=True,nullable = False)
    auteur = db.Column(db.String(80),unique=True,nullable = False)
    categorie = db.Column(db.String(80),unique=True,nullable = False)
    date_creation = db.Column(db.String(20), nullable = False )

with app.app_context():
    produits = User.query.all()
    db.create_all()


@app.route('/')
def home():
    produits = User.query.all()
    return render_template('home.html',produits = produits)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        categorie = request.form['categorie']
        date = request.form['date']

        if not titre or not auteur or not categorie or not date:
            flash('tout les champs doivent etre remplis ','error')
            return redirect(url_for(create_post))
        new_user = User(titre = titre, auteur = auteur, categorie = categorie, date_creation = date)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Enregistrement Reussie', 'succes')
            return redirect(url_for('home'))
        except:
            db.session.rollback()
            flash('il y a eu une erreur','error')
    return render_template('create.html')

@app.route('/update/<int:id_post>', methods=['GET', 'POST'])
def modify_post(id_post):
    produit = User.query.get(id_post)

    if produit is None:
        return "Produit non trouvé", 404

    if request.method == 'POST':
        produit.titre = request.form['titre']
        produit.auteur = request.form['auteur']
        produit.categorie = request.form['categorie']
        produit.date_creation = request.form['date']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('modify.html', produit=produit)

@app.route('/delete/<int:id_post>')
def delete_post(id_post):
    produit = User.query.get(id_post)
    try:
        db.session.delete(produit)
        db.session.commit()
        flash("Produit supprimé avec succès", "success")
    except:
        db.session.rollback()
        flash("Erreur lors de la suppression", "error")

    return redirect(url_for('home'))

@app.route('/read/<int:id_post>')
def show_post(id_post):
    produit = User.query.get(id_post)

    if produit is None:
        return "produit non trouvé ",404
    return render_template('read.html',produit=produit)

@app.route('/search', methods=['GET', 'POST'])
def search():
    resultats = []
    produits = User.query.all()
    if request.method == 'POST':
        mot_cle = request.form['mot_cle'].lower() 
        resultats = [
            p for p in produits
            if mot_cle in p.titre.lower()
            or mot_cle in p.auteur.lower()
            or mot_cle in p.categorie.lower()
        ]

    return render_template('search.html', resultats=resultats)

   
 
if __name__ == "__main__":
    app.run(debug=True)
