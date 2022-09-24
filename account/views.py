from rest_framework.views import APIView
from rest_framework.response import Response
from resource_server.authentications import UserAuthentication


class AccountView(APIView):
    authentication_classes = [UserAuthentication,]

    def get(self, request):
        user = request.user
        info = dict()
        if user == 2:
            info["name"] = "Arun Kumar Mandal"
            info["occupation"] = "Engineer"
            info["address"] = "Kathmandu"
            info["phone"] = "9804093087"
        return Response(info)