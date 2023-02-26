import requests
import random

def get_compatibility_score(target_genre,my_genre,collaborator_genre):
    if target_genre in collaborator_genre and my_genre in collaborator_genre:
        score = ran



def getCollaborators(data, accessToken):
    url = f'https://api.chartmetric.com/api/artist/list/filter?tagId={data["target_genre"]}&code2={data["target_country"]}&career_stage={data["career_stage"]}&limit=10'
    response = requests.get(
            url,
            headers = {'Authorization': 'Bearer ' + accessToken,
                       'content-Type': 'application/json',
                       'Accept': 'application/json'},
        )
    response_json = response.json()["obj"]
    my_genre = data["my_genre"]
    target_genre = data["target_genre"]
    collaborators = {}
    collaborators["collaborators"] = response_json["obj"]
    for collaborator in collaborators["collaborators"]:
        collaborator_genre = [collaborator["genres"]]
        print(collaborator_genre)
        print(target_genre)
        print(my_genre)
        high_compatibility = target_genre in collaborator_genre and my_genre in collaborator_genre
        mid_compatibility = target_genre in collaborator_genre or my_genre in collaborator_genre
        if high_compatibility:
            score = random.randint(80,96)
        elif mid_compatibility:
            score = random.randint(60,75)
        else:
            score = random.randint(35,55)
        collaborator["compatibility_score"] = score
    return collaborators