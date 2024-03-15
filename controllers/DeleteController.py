from flask import Blueprint, render_template

from models.book_copy_model import BookCopy
from conn import db
from sqlalchemy.exc import SQLAlchemyError

from forms import DeleteBookForm

delete_controller = Blueprint("delete_controller", __name__)


@delete_controller.route("/", methods=['GET'])
def list_delete_book_by_id_page():
    form = DeleteBookForm()
    return render_template("delete_book.html", form=form), 200


@delete_controller.route("/", methods=['POST'])  # DELETE method doesnt work because html file doesnt support it
def delete_book_by_id():
    form = DeleteBookForm()
    if form.validate_on_submit():
        try:
            book_copy_id_to_delete = form.book_id.data
            # Query the BookCopy by id and delete it
            book_copy_to_delete = db.session.query(BookCopy).get(book_copy_id_to_delete)

            if book_copy_to_delete:
                db.session.delete(book_copy_to_delete)
                db.session.commit()
                print(f"BookCopy with id {book_copy_id_to_delete} deleted successfully.")
                return render_template("delete_book.html", form=form), 204
            else:
                print(f"BookCopy with id {book_copy_id_to_delete} not found.")
                return render_template("delete_book.html", form=form), 404

        except SQLAlchemyError as e:
            # Handle any potential database errors
            db.session.rollback()
            print(f"Error deleting BookCopy: {e}")
