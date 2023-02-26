import requests

def getCollaborators(data, accessToken):
    url = f'https://api.chartmetric.com/api/artist/list/filter?tagId={data["target_genre"]}&code2={data["target_country"]}&career_stage={data["career_stage"]}&limit=10'
    response = requests.get(
            url,
            headers = {'Authorization': 'Bearer ' + accessToken,
                       'content-Type': 'application/json',
                       'Accept': 'application/json'},
        )
    return response.json()