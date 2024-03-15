from flask import Blueprint, render_template
from conn import db
from models.author_model import Author
from models.book_author_model import BookAuthor
from models.book_copy_model import BookCopy
from models.book_model import Book
from models.category_model import Category
from models.publisher_model import Publisher
from models.series_model import Series

home_controller = Blueprint("home_controller", __name__)


@home_controller.route("/", methods=['GET'])
def home():
    # blob_image = BookCopy.cover_base64
    # decoded_image = base64.b64decode(blob_image)
    # print(decoded_image)
    results = db.session.query(
        Book.title,
        Book.description,
        Author.name,
        Category.name,
        BookCopy.year_published,
        BookCopy.isbn,
        Publisher.name,
        Series.name,
        BookCopy.id,
        BookCopy.cover_base64
    ) \
        .join(BookAuthor, Book.id == BookAuthor.book_id) \
        .join(Author, BookAuthor.author_id == Author.id) \
        .join(Category, Book.category_id == Category.id) \
        .join(BookCopy, Book.id == BookCopy.book_id) \
        .join(Series, BookCopy.series_id == Series.id) \
        .join(Publisher, Series.publisher_id == Publisher.id) \
        .order_by(BookCopy.id)\
        .all()

    # From byte to string
    decoded_results = []
    for result in results:
        decoded_result = list(result)
        if result[9]:  # Assuming the base64 data is in the 9th index
            decoded_result[9] = result[9].decode('utf-8')  # Decode bytes to string
        decoded_results.append(decoded_result)

    print(decoded_results)
    return render_template('home.html', results=decoded_results)
