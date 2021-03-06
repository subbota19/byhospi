from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from service import hospital


class HospitalView(View):
    def post(self, request, id, *args, **kwargs):
        response = None
        if "description" in request.POST:
            response = hospital.edit_description_form(
                id, message=request.POST["description"]
            )
        if "comment" in request.POST:
            try:
                response = hospital.create_comment(
                    id, request.COOKIES["username"], comment=request.POST["comment"]
                )
            except KeyError:
                redirect("sign")
        if response["error"]:
            return redirect("map")
        return redirect("/hospital/{}".format(id))

    def get(self, request, id, *args, **kwargs):
        try:
            if not request.session.get(request.COOKIES["username"], None):
                return redirect("sign")
        except KeyError:
            return redirect("sign")
        response = hospital.get_info_about_hospital(id)
        try:
            response["is_admin"] = request.COOKIES["is_admin"]
        except KeyError:
            redirect("sign")
        if response["error"]:
            return redirect("map")
        return render(request, "hospital/hospital.html", response)
