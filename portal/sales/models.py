import uuid
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Tkp_new(models.Model):
    unique_id_tkp = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField("Организация (Клиент)", max_length=200)
    data_create_tkp = models.DateField("Дата ТКП", default=date.today)
    time_update_tkp = models.DateTimeField(auto_now=True)
    summa_tkp = models.DecimalField("Сумма ТКП", max_digits=19, decimal_places=2, default=0, help_text="указывать сумму в рублях с НДС")
    kontakt_tkp = models.CharField("Контактное лицо", max_length=200, help_text="указывать полное имя")
    kontakt_tel = models.BigIntegerField("Телефон контактного лица")
    city_client = models.CharField("Населённый пункт", max_length=200)
    description_tkp = models.CharField("Оборудование, содержание/предложение", max_length=200)
    tkpdf = models.FileField(upload_to='tkps/%Y-%m-%d/', null=True, blank=True)
    tender_tkp = models.BooleanField("Тендер", default=False)
    notes_tkp = models.CharField("Примечание", max_length=200, blank=True, default='')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    members = models.ManyToManyField(User, related_name="members", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tkp_detail', args=[str(self.id)])
