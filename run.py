import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/add_reviews", methods=["GET", "POST"])
def add_reviews():
    if request.method == "POST":
        review = {
            "movie_name": request.form.get("movie_name"),
            "reviewer_name": request.form.get("reviewer_name"),
            "review_description": request.form.get("review_description")
        }
        mongo.db.reviews.insert_one(review)
        flash("Reviews added successfully")
        return redirect(url_for("get_reviews"))

    movies = mongo.db.movies.find().sort("movie_name", 1)
    return render_template("add_reviews.html", movies=movies)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "movie_name": request.form.get("movie_name"),
            "reviewer_name": request.form.get("reviewer_name"),
            "review_description": request.form.get("review_description")
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Reviews updated successfully")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    movies = mongo.db.movies.find().sort("movies_name", 1)
    return render_template("edit_review.html", review=review, movies=movies)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_reviews"))


@app.route("/get_movies")
def get_movies():
    movies = list(mongo.db.movies.find().sort("movie_name", 1))
    return render_template("movies.html", movies=movies)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)