from factory import SubFactory, Faker
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory

from ..models import Course, Lesson, Exercise, Achievement


class CourseFactory(DjangoModelFactory):
    title = Faker('sentence', nb_words=3, locale='ru_RU')
    status = 'published'  # if set to random tests will break
    # status = FuzzyChoice(choices=['draft', 'published'])

    class Meta:
        model = Course
        django_get_or_create = ['title']


class LessonFactory(DjangoModelFactory):
    course = SubFactory(CourseFactory)
    title = Faker('sentence', nb_words=4, locale='ru_RU')
    theory = Faker('text')
    status = 'published'  # if set to random tests will break

    class Meta:
        model = Lesson
        django_get_or_create = ['title']


class ExerciseFactory(DjangoModelFactory):
    lesson = SubFactory(LessonFactory)
    difficulty = FuzzyChoice(choices=[i for i in range(10)])
    condition = Faker('sentence', nb_words=4, locale='ru_RU')
    expression = '1 + 1'
    answer = '2'
    answers = ['2', '3', '5']

    class Meta:
        model = Exercise
        # django_get_or_create = ['title']


class AchievementFactory(DjangoModelFactory):
    name = Faker('sentence', nb_words=4, locale='ru_RU')
    description = Faker('text', locale='ru_RU')

    class Meta:
        model = Achievement
        django_get_or_create = ['name']
