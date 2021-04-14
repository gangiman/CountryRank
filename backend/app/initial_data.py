#!/usr/bin/env python3
import json

from app.db.session import get_db
from app.db.crud import create_user
from app.db.crud import create_rankings
from app.db.schemas import UserCreate
from app.db.schemas import RankingBase
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    first_user = create_user(
        db,
        UserCreate(
            email="avnotchenko@gmail.com",
            password="password",
            is_active=True,
            is_superuser=True,
        ),
    )

    with open('joined_init_rankings.json') as fh:
        data = json.loads(fh.read())
        for _record in data:
            create_rankings(db, RankingBase(
                name=_record['name'],
                created_date=data.today(),
                ranking=_record['ranking'],
                number_of_countries=_record['number_of_countries'],
                source=_record['source'],
                user_id=first_user.id
            ), first_user.id)


if __name__ == "__main__":
    print("Creating superuser avnotchenko@gmail.com")
    init()
    print("Superuser created")
