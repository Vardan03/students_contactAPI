from typing import Any
from django.core.management import BaseCommand
import datetime

from app.models import Student

class Command(BaseCommand):
    """
        create Student
    """

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Create Student")


        students = [
            {
                'name': 'Vardan',
                'surname': 'Hovhannisyan',
                'lastname': "Armen",
                'contacts': [
                    {
                        'type': 'phone',
                        'value': '+7 999 999 99 99'
                    }
                ],
                'updatedAt': datetime.date.today(),
                'createdAt': datetime.date.today(),
            }
        ]

        for st in students:
            student, created = Student.objects.get_or_create(
                name=st['name'],
                surname=st['surname'],
                lastname=st['lastname'],
                contacts=st['contacts'],
                updatedAt=st['updatedAt'],
                createdAt=st['createdAt'],
                )
            self.stdout.write(f"Created student {student.name}")

        self.stdout.write(self.style.SUCCESS("Students created"))           




