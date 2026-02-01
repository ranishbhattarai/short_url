import secrets
import string


# used to generate secure short keys for URLs
def generate_secure_short_key(length=6):
    from slinks.models import ShortLink

    while True:
        characters = string.ascii_letters + string.digits
        key = ''.join(secrets.choice(characters) for _ in range(length))

        # check if key already exists in the database
        if not ShortLink.objects.filter(short_key=key).exists():
            return key


    