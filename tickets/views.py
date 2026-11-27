import logging

from django.shortcuts import redirect, render

from .forms import TicketForm
from .models import Ticket

logger = logging.getLogger(__name__)


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})


def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()  # status = «Жаңа» (әдепкі мән)
            logger.info("Өтінім сақталды: id=%s", ticket.pk)
            return redirect("ticket_list")
        logger.warning("Өтінім формасы тексеруден өтпеді")
    else:
        form = TicketForm()
    return render(request, "tickets/ticket_form.html", {"form": form})
