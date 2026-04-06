from django.db import models

# Create your models here.


from django.contrib.auth.models import User


class Challenge(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    participants = models.ManyToManyField(User, through='ChallengeParticipation', blank=True, related_name='challenges', verbose_name="Участники")

    class Meta:
        verbose_name = "Челлендж"
        verbose_name_plural = "Челленджи"

    def __str__(self):
        return self.title

class ChallengeParticipation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, verbose_name="Челлендж")
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата присоединения")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    proof_image = models.ImageField(upload_to='proofs/', null=True, blank=True, verbose_name="Фото-подтверждение")

    class Meta:
        verbose_name = "Участие"
        verbose_name_plural = "Участники челленджей"
        unique_together = ('user', 'challenge')

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"
