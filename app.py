from flask import Flask, render_template, request, redirect, url_for, flash
from category import Category

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Para mensagens flash

# Simulação de banco de dados em memória
categories = []

def find_category(cat_id):
    for cat in categories:
        if cat.id == cat_id:
            return cat
    return None

@app.route("/")
def index():
    return render_template("index.html", categories=categories)

@app.route("/category/add", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        category = Category(name=name, description=description)
        categories.append(category)
        flash("Categoria criada com sucesso!", "success")
        return redirect(url_for("index"))
    return render_template("add_category.html")

@app.route("/category/<cat_id>")
def category_details(cat_id):
    cat = find_category(cat_id)
    if not cat:
        flash("Categoria não encontrada.", "danger")
        return redirect(url_for("index"))
    return render_template("category_details.html", cat=cat)

@app.route("/category/<cat_id>/edit", methods=["GET", "POST"])
def edit_category(cat_id):
    cat = find_category(cat_id)
    if not cat:
        flash("Categoria não encontrada.", "danger")
        return redirect(url_for("index"))
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        cat.update(name=name, description=description)
        flash("Categoria atualizada!", "info")
        return redirect(url_for("category_details", cat_id=cat.id))
    return render_template("edit_category.html", cat=cat)

@app.route("/category/<cat_id>/activate")
def activate_category(cat_id):
    cat = find_category(cat_id)
    if cat:
        cat.activate()
        flash("Categoria ativada!", "success")
    return redirect(url_for("index"))

@app.route("/category/<cat_id>/deactivate")
def deactivate_category(cat_id):
    cat = find_category(cat_id)
    if cat:
        cat.deactivate()
        flash("Categoria desativada!", "warning")
    return redirect(url_for("index"))

@app.route("/category/<cat_id>/delete", methods=["POST"])
def delete_category(cat_id):
    cat = find_category(cat_id)
    if cat:
        categories.remove(cat)
        flash("Categoria removida!", "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)