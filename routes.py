from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from extensions import db
from models import Contact

contact_bp = Blueprint('contact', __name__)

# Home route
@contact_bp.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

# Search contacts
@contact_bp.route('/search', methods=['GET'])
def search_contacts():
    search_query = request.args.get('search', '').strip()
    if search_query:
        contacts = Contact.query.filter(
            Contact.name.ilike(f'%{search_query}%') |
            Contact.email.ilike(f'%{search_query}%') |
            Contact.address.ilike(f'%{search_query}%') |
            Contact.contact_number.ilike(f'%{search_query}%')
        ).all()
    else:
        contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts, search_query=search_query)

# Create contact
@contact_bp.route('/create', methods=['GET', 'POST'])
def create_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        contact_number = request.form['contact_number']

        new_contact = Contact(
            name=name, email=email, address=address, contact_number=contact_number
        )
        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for('contact.index'))
    return render_template('create.html')

# Update contact
@contact_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    contact = Contact.query.get_or_404(id)
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.email = request.form['email']
        contact.address = request.form['address']
        contact.contact_number = request.form['contact_number']

        db.session.commit()
        return redirect(url_for('contact.index'))
    return render_template('update.html', contact=contact)

# Delete contact
@contact_bp.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contact.index'))