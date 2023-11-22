from django.shortcuts import render

from .forms import DateForm
from .models import Transaction
from .services import make_tuple_of_lists


def index(request):
    if request.method == 'POST':
        dateform = DateForm(request.POST)
        if dateform.is_valid():
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            filtered_by_dates = Transaction.items.filter_by_dates(
                start_date,
                end_date,
            )

            if filtered_by_dates:
                aggregated_cat_amount = (
                    Transaction.items.aggregate_cat_amount(
                        start_date,
                        end_date,
                    )
                )
                cat_labels, cat_data = make_tuple_of_lists(
                    aggregated_cat_amount
                )

                aggregated_sub_amount = Transaction.items.aggregate_sub_amount(
                    start_date,
                    end_date,
                )
                sub_labels, sub_data = make_tuple_of_lists(
                    aggregated_sub_amount
                )

                aggregated_payment_method_amount = (
                    Transaction.items.aggregate_payment_method_amount(
                        start_date,
                        end_date,
                    )
                )
                pay_labels, pay_data = make_tuple_of_lists(
                    aggregated_payment_method_amount
                )

                got_expenses_by_day = Transaction.items.get_expenses_by_day(
                    start_date,
                    end_date,
                )
                exp_labels, exp_data = make_tuple_of_lists(
                    got_expenses_by_day
                )
                exp_labels = [dt.strftime('%d-%m-%Y') for dt in exp_labels]

                total_amount_for_period = (
                    Transaction.items.get_total_amount_for_period(
                        start_date,
                        end_date
                    )['total_amount']
                )

                return render(
                    request, 'main/index.html', {
                        'cat_labels': cat_labels,
                        'cat_data': cat_data,
                        'sub_labels': sub_labels,
                        'sub_data': sub_data,
                        'pay_labels': pay_labels,
                        'pay_data': pay_data,
                        'exp_labels': exp_labels,
                        'exp_data': exp_data,
                        'form': dateform,
                        'filtered_by_dates': filtered_by_dates,
                        'total_amount_for_period': total_amount_for_period,
                    }
                )

    dateform = DateForm()
    return render(request, 'main/index.html', {'form': dateform})
