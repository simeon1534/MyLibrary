import requests
from flask import Blueprint, render_template,   flash
import base64
from models.author_model import Author
from models.category_model import Category
from models.book_model import Book
from models.book_author_model import BookAuthor
from models.publisher_model import Publisher
from models.series_model import Series
from models.book_copy_model import BookCopy
from conn import db

from forms import AddBookForm

create_controller = Blueprint("create_controller", __name__)

@create_controller.route("/", methods=['GET'])
def list_add_book_page():
    categories = Category.query.all()
    category_names = [category.name for category in categories]

    form = AddBookForm()
    form.category.choices = category_names

    return render_template("add_book.html", form=form, categories=categories),200


@create_controller.route("/", methods=['POST'])
def add_book():
    categories = Category.query.all()
    category_names = [category.name for category in categories]

    form = AddBookForm()
    form.category.choices = category_names
    form.process_data()
    if form.validate_on_submit():
        author = Author(
            name=form.author.data
        )

        db.session.add(author)
        db.session.commit()

        category_id_form = [category.id for category in categories if category.name == form.category.data]
        book = Book(
            title=form.book_name.data,
            category_id=category_id_form,
            description=form.description.data
        )
        db.session.add(book)
        db.session.commit()

        book_author = BookAuthor(
            book_id=book.id, author_id=author.id
        )
        db.session.add(book_author)
        db.session.commit()

        publisher = Publisher(name=form.publisher.data)
        db.session.add(publisher)
        db.session.commit()

        series = Series(name=form.series.data, publisher_id=publisher.id)
        db.session.add(series)
        db.session.commit()

        response = requests.get(f"https://covers.openlibrary.org/b/isbn/{form.isbn.data}-M.jpg")
        image_data = response.content
        print(image_data)
        image_base64 = base64.b64encode(image_data)

        book_copy = BookCopy(year_published=form.year_published.data, book_id=book.id, isbn=form.isbn.data,
                             series_id=series.id, cover_base64=image_base64)
        db.session.add(book_copy)
        db.session.commit()
        categories = Category.query.all()
        flash('Successfully added')

    return render_template("add_book.html", form=form, categories=categories),201

    # old variant without validation in forms
    # return render_template("add_book.html", form=form)
    # if request.method == 'POST':
    #
    #     # Get data from the form
    #     author_name = request.form.get('User-Name')
    #     book_title = request.form.get('Book-Name')
    #     description = request.form.get('Description')
    #     category_id = int(request.form.get('category'))
    #     isbn = request.form.get('isbn')
    #     year_published = request.form.get('year')
    #     publisher = request.form.get('publisher')
    #     series = request.form.get('series')
    #
    #     # Create an Author object and add it to the database
    #     author = Author(name=author_name)
    #
    #     db.session.add(author)
    #     db.session.commit()
    #     authors = Author.query.all()
    #
    #     # Create a Book object and add it to the database
    #
    #     book = Book(
    #         title=book_title,
    #         category_id=category_id,
    #         description=description
    #
    #     )
    #     db.session.add(book)
    #     db.session.commit()
    #
    #     # Create a BookAuthor object and add it to the database
    #     book_author = BookAuthor(book_id=book.id, author_id=author.id)
    #     db.session.add(book_author)
    #     db.session.commit()
    #
    #     # Create a Publisher object and add it to the database
    #     publisher = Publisher(name=publisher)
    #     db.session.add(publisher)
    #     db.session.commit()
    #
    #     # Create a Series object and add it to the database
    #     series = Series(name=series, publisher_id=publisher.id)
    #     db.session.add(series)
    #     db.session.commit()
    #
    #     # Create a BookCopy object and add it to the database
    #     book_copy = BookCopy(year_published=year_published, book_id=book.id, isbn=isbn, series_id=series.id)
    #     db.session.add(book_copy)
    #     db.session.commit()
    #     categories = Category.query.all()
    #     return render_template("add_book_old.html", categories=categories)
    #
    # elif request.method == 'GET':
    #     categories = Category.query.all()
    #     return render_template("add_book_old.html", categories=categories)
