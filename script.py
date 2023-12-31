from datacenter.models import Mark, Lesson, Chastisement, Schoolkid, Commendation
import random


LAUDATORY_COMMENTS = ['Молодец!', 'Ты меня очень обрадовал!', 'С каждым разом у тебя получается всё лучше!', 'Я вижу, как ты стараешься!']


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        raise Schoolkid.DoesNotExist
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned
    return schoolkid


def fix_marks(name):
    child_marks = Mark.objects.filter(schoolkid=get_schoolkid(name), points__in=[2, 3])
    child_marks.update(points=5)


def remove_chastisements(name):
    notes = Chastisement.objects.filter(schoolkid=get_schoolkid(name))
    notes.delete()


def create_commendation(name, lesson):
    text = random.choice(LAUDATORY_COMMENTS)
    schoolkid = get_schoolkid(name)
    last_lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title=lesson).order_by('-date').first()
    if last_lesson is not None:
        Commendation.objects.create(text=text, created=last_lesson.date, schoolkid=schoolkid, subject=last_lesson.subject, teacher=last_lesson.teacher)
    else:
        print('Lesson Does Not Exist!')
