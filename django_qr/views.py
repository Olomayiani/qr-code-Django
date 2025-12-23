from django.shortcuts import render
from .forms import QRCodeForm
import qrcode


def generate_qr_code(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data["restaurant_name"]
            url = form.cleaned_data["url"]

            # generate qr code
            qr = qrcode.make(url)
            file_name = rest_name.replace

            qr.save("test_qr.png")

    else:
        form = QRCodeForm()
        context = {"form": form}
        return render(request, "generate_qr_code.html", context)
