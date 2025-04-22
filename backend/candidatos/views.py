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
        linguagem = request.query_params.get("linguagem")
        qtd_repos_min = request.query_params.get("qtd_repos_min")
        seguidores_min = request.query_params.get("seguidores_min")

        if not local:
            return Response({"erro": "Parâmetro 'local' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        search_url = "https://api.github.com/search/users"
        search_params = {
            "q": f"location:{local}",
            "per_page": 10,
            "page": 1
        }

        headers = {
            "Accept": "application/vnd.github+json",
        }

        user_search_response = requests.get(search_url, params=search_params, headers=headers)
        user_data = user_search_response.json()
        users = user_data.get("items", [])

        candidatos = []

        for user in users:
            user_detail_response = requests.get(user["url"], headers=headers)
            user_detail = user_detail_response.json()

            if qtd_repos_min and user_detail.get("public_repos", 0) < int(qtd_repos_min):
                continue

            if seguidores_min and user_detail.get("followers", 0) < int(seguidores_min):
                continue

            if linguagem:
                repos_response = requests.get(user["repos_url"], headers=headers)
                repos = repos_response.json()

                linguagens_do_usuario = [repo.get("language") for repo in repos if repo.get("language")]
                if linguagem not in linguagens_do_usuario:
                    continue

            candidatos.append({
                "nome": user["login"],
                "github_link": user["html_url"],
                "avatar_url": user["avatar_url"],
                "id_github": user["id"],
                "repositorios": user_detail.get("public_repos"),
                "seguidores": user_detail.get("followers")
            })

        return Response(candidatos)

# lembrar depois de implementar os endpoints
# um viewset para crud dos candidatos no bd
class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
