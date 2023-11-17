from flask import Flask,render_template,abort
# from portfolio.models import Class

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/Habit-tracking.jpg", # shown in homepage
        "hero": "img/Habit-tracking.jpg", # shown at top of each project page
        "categories": ["python", "web"], # technologies that we used 
        "slug": "habit-tracking", # url endpoint
        "prod": "https://udemy.com", # project hosted
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/Personal-finance.jpg",
        "hero": "img/Personal-finance.jpg",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
        "prod": "https://www.investopedia.com/terms/p/personal-financial-statement.asp"
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.jpg",
        "hero": "img/rest-api-docs.jpg",
        "categories": ["writing"],
        "slug": "api-docs",
        "prod": "https://learning.postman.com/docs/getting-started/importing-and-exporting/importing-from-swagger/"
    },
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html", 
        project=slug_to_project[slug]
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404