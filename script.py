from datacenter.models import Mark, Lesson, Chastisement, Schoolkid, Commendation
import random

def fix_marks(schoolkid):
    child_marks = Mark.objects.filter(schoolkid = schoolkid, points__in = [2,3]) 
    for child_mark in child_marks:
        child_mark.points = 5
        child_mark.save()

def remove_chastisements(schoolkid): 
    notes = Chastisement.objects.filter(schoolkid = schoolkid) 
    notes.delete()


def create_commendation(name, les):
    lst = ['Молодец!','Ты меня очень обрадовал!','С каждым разом у тебя получается всё лучше!','Я вижу, как ты стараешься!']
    text = random.choice(lst)                                                                                                                               
    schoolkid = Schoolkid.objects.get(full_name__contains = name)
    last_lesson_6a = Lesson.objects.filter(year_of_study = 6, group_letter = 'А', subject__title = les).order_by('-date').first()
    Commendation.objects.create(text = text, created = last_lesson_6a.date, schoolkid = schoolkid[0], subject = last_lesson_6a.subject, teacher = last_lesson_6a.teacher) 
