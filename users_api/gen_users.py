import random
import string
from typing import Tuple
from faker import Faker
import uuid
import re

fake = Faker()
Faker.seed(42)

VALID_PROB = 0.8
INVALID_TYPES = ("missing_at", "bad_domain", "illegal_char")
TLD_TYPES = ("com", "org", "net", "edu", "mil", "info", "biz", "co")


def rand_string(n, alphabet=string.ascii_lowercase):
    return "".join(random.choice(alphabet) for _ in range(n))


def generate_company_domain():
    company = fake.company()
    return re.sub(r"[^a-zA-Z]", "", company).lower()[:5], company


def invalid_email(kind: str) -> Tuple[str, str]:
    tld = random.choice(TLD_TYPES)
    user = fake.user_name()
    domain, company = generate_company_domain()
    if kind == "missing_at":
        return f"{user}{domain}.{tld}", user, company
    if kind == "bad_domain":
        return f"{user}@{domain}..{tld}", user, company
    if kind == "illegal_char":
        return f"{user}!@{domain}.{tld}", user, company
    raise ValueError(kind)


def maybe_email() -> str:
    return invalid_email(random.choice(INVALID_TYPES))


def gen_user(uid):
    loc = fake.local_latlng()
    lat, lng = float(loc[0]), float(loc[1])
    email, user, company = maybe_email()
    return {
        "id": uid,
        "name": fake.name(),
        "username": user,
        "email": email,
        "address": {
            "street": fake.street_name(),
            "suite": f"Apt. {random.randint(100, 999)}",
            "city": loc[2] if len(loc) > 2 else fake.city(),
            "zipcode": fake.postcode(),
            "geo": {"lat": f"{lat:.4f}", "lng": f"{lng:.4f}"},
        },
        "phone": fake.phone_number(),
        "website": fake.domain_name(),
        "company": {
            "name": company,
            "catchPhrase": fake.catch_phrase(),
            "bs": fake.bs(),
        },
    }


def stream_users(page=1, size=10):
    start_index = (page - 1) * size
    for i in range(size):
        user_position = start_index + i
        random.seed(42 + user_position)
        Faker.seed(42 + user_position)
        user_uuid = str(uuid.uuid4()).replace("-", "")[:8]
        yield gen_user(user_uuid)
    random.seed(42)
    Faker.seed(42)
