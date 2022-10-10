from factory import SubFactory, Faker, post_generation
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory

from ..models import Course, Lesson, Exercise


class CourseFactory(DjangoModelFactory):
    title = Faker('name', locale='ru_RU')
    status = FuzzyChoice(choices=['draft', 'published'])

    class Meta:
        model = Course
        django_get_or_create = ['title']


class LessonFactory(DjangoModelFactory):
    course = SubFactory(CourseFactory)
    title = Faker('name', locale='ru_RU')
    theory = Faker('text')
    status = FuzzyChoice(choices=['draft', 'published'])

    class Meta:
        model = Lesson
        django_get_or_create = ['title']


class ExerciseFactory(DjangoModelFactory):
    lesson = SubFactory(LessonFactory)
    difficulty = FuzzyChoice(choices=[i for i in range(10)])

    class Meta:
        model = Exercise
        # django_get_or_create = ['title']
