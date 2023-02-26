curl -XPOST -H "Content-type: application/json" -d '{ 
  "name": "Fave",
  "target_genre": 462977,
  "my_genre": 462978,
  "career_stage": "mid-level",
  "target_country": "US"
}' 'https://msdocs-python-webapp-quickstart-rrr.azurewebsites.net/collaborators' > response.json