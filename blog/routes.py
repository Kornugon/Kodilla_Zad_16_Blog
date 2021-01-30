from flask import render_template
from blog import app, db
from blog.models import Entry, db

from faker import Faker


def generate_entries(how_many=10):
    fake = Faker()

    for _ in range(how_many):
        post = Entry(
            title=fake.sentence(),
            body='\n'.join(fake.paragraphs(15)),
            is_published=True
        )
        db.session.add(post)
    db.session.commit()



@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    #generate_entries(how_many=10)
    return render_template("homepage.html", all_posts=all_posts)