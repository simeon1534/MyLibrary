from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, NumberRange


class AddBookForm(FlaskForm):
    author = StringField('Author',
                         validators=[DataRequired(), Length(min=1, max=255)])

    book_name = StringField('Book Name',
                            validators=[DataRequired(), Length(min=1, max=255)])

    description = TextAreaField('Description',
                                validators=[Optional(), Length(max=255)],
                                render_kw={"placeholder": "Optional"}
                                )
    category = SelectField('Category')

    isbn = StringField('ISBN',
                       validators=[Optional(), Length(max=30)],
                       render_kw={"placeholder": "Optional"}
                       )

    year_published = IntegerField('Year',
                                  validators=[DataRequired(), NumberRange(min=0, max=9999)],
                                  render_kw={"min": "0", "max": "9999"})

    publisher = StringField('Publisher',
                            validators=[DataRequired(), Length(min=1, max=255)])

    series = StringField('Series',
                         validators=[Optional(), Length(min=1, max=255)],
                         render_kw={"placeholder": "Optional"}
                         )

    def process_data(self):
        for field in self:
            print(field.data)
            if field.data == '':
                field.data = None


class DeleteBookForm(FlaskForm):
    book_id = StringField('Id',
                          validators=[DataRequired(), Length(min=1, max=255)])
