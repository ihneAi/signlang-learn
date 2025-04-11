from django.db import models

class BaseModel(models.Model):
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} description: {self.description}"


class Lesson(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.TextField()

    def __str__(self):
        return f"Lesson title: {self.title}, {super().__str__()}"


class Topic(BaseModel):
    topic_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.TextField()
    picture = models.TextField()

    def __str__(self):
        return (
            f"Topic id: {self.topic_id}, Lesson id: {self.lesson.id}, "
            f"name: {self.name}, {super().__str__()}, picture url: {self.picture}"
        )
