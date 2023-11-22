from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import Transaction


@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
        "subcategory",
        "payment_method",
        "amount",
        "created_at",
    )

    list_filter = (
        "category",
        "subcategory",
        "payment_method",
        ("created_at", DateRangeFilter),
    )
