from django.db import models
from django.db.models import Sum
from django.db.models.functions import TruncDate


class CustomManager(models.Manager):
    def filter_by_dates(self, start_date, end_date):
        return self.filter(created_at__gte=start_date,
                           created_at__lte=end_date).order_by('id')

    def aggregate_cat_amount(self, start_date, end_date):
        return self.filter(
            created_at__gte=start_date,
            created_at__lte=end_date).values('category').annotate(
            total_amount=Sum('amount')).order_by('-total_amount')

    def aggregate_sub_amount(self, start_date, end_date):
        return self.filter(
            created_at__gte=start_date,
            created_at__lte=end_date).values('subcategory').annotate(
            total_amount=Sum('amount')).order_by('-total_amount')

    def aggregate_payment_method_amount(self, start_date, end_date):
        return self.filter(
            created_at__gte=start_date,
            created_at__lte=end_date).values(
                'payment_method').annotate(total_amount=Sum('amount'))

    def get_expenses_by_day(self, start_date, end_date):
        return self.filter(
            created_at__gte=start_date,
            created_at__lte=end_date).annotate(day=TruncDate(
                'created_at')).values('day').annotate(total_amount=Sum(
                 'amount')).order_by('day')


class Transaction(models.Model):
    category = models.CharField(blank=True, null=True)
    subcategory = models.CharField(blank=True, null=True)
    payment_method = models.CharField(blank=True, null=True)
    amount = models.DecimalField(blank=True, null=True, max_digits=10,
                                 decimal_places=2)
    created_at = models.DateField(blank=True, null=True)

    objects = models.Manager()
    items = CustomManager()

    class Meta:
        managed = False
        db_table = 'transaction'
