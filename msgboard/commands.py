'''
#6 step
IMPORTANT create commands
'''
import click
from faker import Faker
from flask_folder import app, db
from flask_folder.model import Message

@app.cli.command()
@click.option('--drop', is_flag=True, help='create after drop.')
def initdb(drop):
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')
    
@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    db.drop_all()
    db.create_all()
    
    fake=Faker()
    click.echo('Generating fake messages...')
    
    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
            )
        db.session.add(message)
        
    db.session.commit()
    click.echo('%d fake messages created.' % count)
    