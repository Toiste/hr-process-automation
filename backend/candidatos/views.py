from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Candidato
from .serializers import CandidatoSerializer
import requests
import os

class BuscarCandidatosGitHub(APIView):
    def get(self, request):
        local = request.query_params.get("local")
        if not local:
            return Response({"erro": "Parâmetro 'local' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        url = "https://api.github.com/search/users"
        params = {
            "q": f"location:{local}",
            "per_page": 10,
            "page": 1
        }
        headers = {
            "Accept": "application/vnd.github+json",
        }

        token = os.getenv("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"Bearer {token}"


        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        users = data.get("items", [])

        candidatos = [
            {
                "nome": user["login"],
                "github_link": user["html_url"],
                "avatar_url": user["avatar_url"],
                "id_github": user["id"]
            }
            for user in users
        ]

        return Response(candidatos)

# lembrar depois de implementar os endpoints
# um viewset para crud dos candidatos no bd
class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
