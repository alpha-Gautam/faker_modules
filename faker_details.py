from faker import Faker
import pandas as pd

faker = Faker('en_IN')

data = {
    # Personal
    "name": faker.name(),
    "first_name": faker.first_name(),
    "last_name": faker.last_name(),
    
    # Contact
    "email": faker.email(),
    "phone": faker.phone_number(),
    "address": faker.address(),
    
    # Geographic
    "country": faker.country(),
    "city": faker.city(),
    "postcode": faker.postcode(),
    "latitude": faker.latitude(),
    "longitude": faker.longitude(),
    
    # Internet
    "username": faker.user_name(),
    "url": faker.url(),
    "ipv4": faker.ipv4(),
    "domain": faker.domain_name(),
    
    # Financial
    "credit_card": faker.credit_card_number(),
    "iban": faker.iban(),
    "currency": faker.currency_code(),
    
    # Business
    "company": faker.company(),
    "job": faker.job(),
    "catch_phrase": faker.catch_phrase(),
    
    # Date/Time
    "date": faker.date(),
    "datetime": faker.date_time(),
    "future_date": faker.future_date(),
    
    # Text
    "text": faker.text(),
    "sentence": faker.sentence(),
    "word": faker.word(),
    
    # Colors
    "color": faker.color_name(),
    "hex_color": faker.hex_color(),
    
    # Technical
    "uuid": faker.uuid4(),
    "file_name": faker.file_name(),
    "mime_type": faker.mime_type(),
    
    # Automotive
    "license_plate": faker.license_plate(),
    
    # Identifiers
    "ssn": faker.ssn(),
    "isbn": faker.isbn13()
}