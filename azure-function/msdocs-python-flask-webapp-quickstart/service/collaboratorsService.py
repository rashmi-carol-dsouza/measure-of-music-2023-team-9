import requests
import random
genres = [
    {
      "id": 478636,
      "name": "Soundtracks",
      "color": "hsl(165.9794274707042, 100%, 75%)"
    },
    {
      "id": 468670,
      "name": "Bachata",
      "color": "hsl(70.61443936872638, 100%, 75%)"
    },
    {
      "id": 462989,
      "name": "Arabic Folk",
      "color": "hsl(310.1453989493647, 100%, 75%)"
    },
    {
      "id": 462988,
      "name": "Arabic Classical",
      "color": "hsl(286.64081724236354, 100%, 75%)"
    },
    {
      "id": 462987,
      "name": "Arabic Dance",
      "color": "hsl(130.74045018654826, 100%, 75%)"
    },
    {
      "id": 462986,
      "name": "Arabic Rock",
      "color": "hsl(44.45126440830749, 100%, 75%)"
    },
    {
      "id": 462985,
      "name": "Arabic Hip-Hop/Rap",
      "color": "hsl(188.54469271729883, 100%, 75%)"
    },
    {
      "id": 462984,
      "name": "Arabic Pop",
      "color": "hsl(305.9983456282773, 100%, 75%)"
    },
    {
      "id": 462983,
      "name": "Arabic Children's Music",
      "color": "hsl(162.52084517618914, 100%, 75%)"
    },
    {
      "id": 462982,
      "name": "African Folk",
      "color": "hsl(22.44131963588665, 100%, 75%)"
    },
    {
      "id": 462981,
      "name": "African Classical",
      "color": "hsl(219.54875894350207, 100%, 75%)"
    },
    {
      "id": 462980,
      "name": "African Dance",
      "color": "hsl(86.44380634907179, 100%, 75%)"
    },
    {
      "id": 462979,
      "name": "African Rock",
      "color": "hsl(67.61864239427183, 100%, 75%)"
    },
    {
      "id": 462978,
      "name": "African Hip-Hop/Rap",
      "color": "hsl(301.64237848191505, 100%, 75%)"
    },
    {
      "id": 462977,
      "name": "African Pop",
      "color": "hsl(169.09841336321202, 100%, 75%)"
    },
    {
      "id": 462976,
      "name": "African Children's Music",
      "color": "hsl(62.678053744034806, 100%, 75%)"
    },
    {
      "id": 462975,
      "name": "Indian Folk",
      "color": "hsl(326.9978743290937, 100%, 75%)"
    },
    {
      "id": 462974,
      "name": "Indian Classical",
      "color": "hsl(88.45869457160843, 100%, 75%)"
    },
    {
      "id": 462973,
      "name": "Indian Dance",
      "color": "hsl(159.9302811641032, 100%, 75%)"
    },
    {
      "id": 462972,
      "name": "Indian Rock",
      "color": "hsl(281.29104975940095, 100%, 75%)"
    },
    {
      "id": 462971,
      "name": "Indian Hip-Hop/Rap",
      "color": "hsl(256.70298354516325, 100%, 75%)"
    },
    {
      "id": 462970,
      "name": "Indian Pop",
      "color": "hsl(301.9585700686657, 100%, 75%)"
    },
    {
      "id": 462969,
      "name": "Indian Children's Music",
      "color": "hsl(120.43638650856943, 100%, 75%)"
    },
    {
      "id": 462968,
      "name": "European Folk",
      "color": "hsl(257.60000627151584, 100%, 75%)"
    },
    {
      "id": 462967,
      "name": "European Dance",
      "color": "hsl(225.47006297591997, 100%, 75%)"
    },
    {
      "id": 462966,
      "name": "European Rock",
      "color": "hsl(36.764719344167354, 100%, 75%)"
    },
    {
      "id": 462965,
      "name": "European Hip-Hop/Rap",
      "color": "hsl(19.616119630160547, 100%, 75%)"
    },
    {
      "id": 462964,
      "name": "European Pop",
      "color": "hsl(85.12714159390642, 100%, 75%)"
    },
    {
      "id": 462963,
      "name": "European Children's Music",
      "color": "hsl(133.94331396375998, 100%, 75%)"
    },
    {
      "id": 462962,
      "name": "Latin Folk",
      "color": "hsl(331.4505471326921, 100%, 75%)"
    },
    {
      "id": 462961,
      "name": "Latin Classical",
      "color": "hsl(96.96215369617983, 100%, 75%)"
    },
    {
      "id": 462960,
      "name": "Latin Dance",
      "color": "hsl(207.95931401916135, 100%, 75%)"
    },
    {
      "id": 462959,
      "name": "Latin Rock",
      "color": "hsl(218.493874943216, 100%, 75%)"
    },
    {
      "id": 462958,
      "name": "Latin Hip-Hop/Rap",
      "color": "hsl(3.2492083776829705, 100%, 75%)"
    },
    {
      "id": 462957,
      "name": "Latin Pop",
      "color": "hsl(70.38050658985406, 100%, 75%)"
    },
    {
      "id": 462956,
      "name": "Latin Children's Music",
      "color": "hsl(238.89532757382173, 100%, 75%)"
    },
    {
      "id": 462955,
      "name": "Arabic",
      "color": "hsl(326.9132331058097, 100%, 75%)"
    },
    {
      "id": 462954,
      "name": "African",
      "color": "hsl(272.5789332890529, 100%, 75%)"
    },
    {
      "id": 462953,
      "name": "Indian",
      "color": "hsl(183.83447177406958, 100%, 75%)"
    },
    {
      "id": 462952,
      "name": "European",
      "color": "hsl(36.94321696610898, 100%, 75%)"
    },
    {
      "id": 462951,
      "name": "Latin",
      "color": "hsl(184.0278669298706, 100%, 75%)"
    },
    {
      "id": 462950,
      "name": "Delta Blues",
      "color": "hsl(296.9468577438898, 100%, 75%)"
    },
    {
      "id": 462949,
      "name": "Motown",
      "color": "hsl(122.87950626113155, 100%, 75%)"
    },
    {
      "id": 462948,
      "name": "Ghazals",
      "color": "hsl(57.68898054459255, 100%, 75%)"
    },
    {
      "id": 462947,
      "name": "Dancehall",
      "color": "hsl(65.86287897542691, 100%, 75%)"
    },
    {
      "id": 462946,
      "name": "Grunge",
      "color": "hsl(32.887318549531976, 100%, 75%)"
    },
    {
      "id": 462945,
      "name": "Drum & Bass",
      "color": "hsl(322.7706324633507, 100%, 75%)"
    },
    {
      "id": 462944,
      "name": "Trap",
      "color": "hsl(228.49778572792044, 100%, 75%)"
    },
    {
      "id": 462943,
      "name": "Doo Wop",
      "color": "hsl(178.9030074854908, 100%, 75%)"
    },
    {
      "id": 462942,
      "name": "Chicago Blues",
      "color": "hsl(329.8635242599039, 100%, 75%)"
    },
    {
      "id": 462941,
      "name": "Hard Rock",
      "color": "hsl(214.50436812159984, 100%, 75%)"
    },
    {
      "id": 462940,
      "name": "Gangsta Rap",
      "color": "hsl(37.817405180774635, 100%, 75%)"
    },
    {
      "id": 462939,
      "name": "Comedy",
      "color": "hsl(212.01197494104585, 100%, 75%)"
    },
    {
      "id": 462938,
      "name": "Indie Pop",
      "color": "hsl(269.9113884949446, 100%, 75%)"
    },
    {
      "id": 462937,
      "name": "Alternative Rap",
      "color": "hsl(330.24137444453316, 100%, 75%)"
    },
    {
      "id": 462936,
      "name": "Opera",
      "color": "hsl(155.0821165638998, 100%, 75%)"
    },
    {
      "id": 462935,
      "name": "Dubstep",
      "color": "hsl(114.00065663278846, 100%, 75%)"
    },
    {
      "id": 462934,
      "name": "Gospel",
      "color": "hsl(68.95298721861997, 100%, 75%)"
    },
    {
      "id": 462933,
      "name": "Funk",
      "color": "hsl(101.16288854213329, 100%, 75%)"
    },
    {
      "id": 462932,
      "name": "Spoken Word",
      "color": "hsl(255.25796829515812, 100%, 75%)"
    },
    {
      "id": 462931,
      "name": "Ambient",
      "color": "hsl(108.70026456154807, 100%, 75%)"
    },
    {
      "id": 462930,
      "name": "Indie Rock",
      "color": "hsl(259.62402468683996, 100%, 75%)"
    },
    {
      "id": 462929,
      "name": "Punk",
      "color": "hsl(264.78322199508506, 100%, 75%)"
    },
    {
      "id": 462928,
      "name": "Folk",
      "color": "hsl(345.88519123878785, 100%, 75%)"
    },
    {
      "id": 462927,
      "name": "Trance",
      "color": "hsl(248.73450167960155, 100%, 75%)"
    },
    {
      "id": 462926,
      "name": "Vocal",
      "color": "hsl(162.93858492867315, 100%, 75%)"
    },
    {
      "id": 462925,
      "name": "K-Pop",
      "color": "hsl(15.681815312136616, 100%, 75%)"
    },
    {
      "id": 462924,
      "name": "J-Pop",
      "color": "hsl(10.22099728918568, 100%, 75%)"
    },
    {
      "id": 462923,
      "name": "Bluegrass",
      "color": "hsl(316.7134349049446, 100%, 75%)"
    },
    {
      "id": 462922,
      "name": "Rockabilly",
      "color": "hsl(75.79608649489316, 100%, 75%)"
    },
    {
      "id": 462921,
      "name": "Neo-Soul",
      "color": "hsl(93.80923408158557, 100%, 75%)"
    },
    {
      "id": 462920,
      "name": "Soft Rock",
      "color": "hsl(312.60732624872827, 100%, 75%)"
    },
    {
      "id": 462919,
      "name": "Standards",
      "color": "hsl(91.03150722274785, 100%, 75%)"
    },
    {
      "id": 462918,
      "name": "Hard Bop",
      "color": "hsl(359.8684807517035, 100%, 75%)"
    },
    {
      "id": 462917,
      "name": "Classic Rock",
      "color": "hsl(297.14071178994107, 100%, 75%)"
    },
    {
      "id": 462916,
      "name": "Industrial",
      "color": "hsl(70.66750090625028, 100%, 75%)"
    },
    {
      "id": 462915,
      "name": "New Wave",
      "color": "hsl(4.647941371890427, 100%, 75%)"
    },
    {
      "id": 462914,
      "name": "Swing",
      "color": "hsl(265.90096438230074, 100%, 75%)"
    },
    {
      "id": 462913,
      "name": "Dirty South",
      "color": "hsl(275.4631443975922, 100%, 75%)"
    },
    {
      "id": 462912,
      "name": "Smooth Jazz",
      "color": "hsl(6.819268681481132, 100%, 75%)"
    },
    {
      "id": 462911,
      "name": "Psychedelic",
      "color": "hsl(98.66896408833016, 100%, 75%)"
    },
    {
      "id": 462910,
      "name": "Musicals",
      "color": "hsl(207.0194500676419, 100%, 75%)"
    },
    {
      "id": 462909,
      "name": "Choral",
      "color": "hsl(269.0968643968863, 100%, 75%)"
    },
    {
      "id": 462908,
      "name": "Big Band",
      "color": "hsl(290.4407881576486, 100%, 75%)"
    },
    {
      "id": 462907,
      "name": "Oldies",
      "color": "hsl(278.7885354337543, 100%, 75%)"
    },
    {
      "id": 462906,
      "name": "East Coast Rap",
      "color": "hsl(8.817775371990022, 100%, 75%)"
    },
    {
      "id": 462905,
      "name": "Others",
      "color": "hsl(50.919437534778496, 100%, 75%)"
    },
    {
      "id": 462904,
      "name": "Salsa",
      "color": "hsl(141.86449280196305, 100%, 75%)"
    },
    {
      "id": 462903,
      "name": "Holiday",
      "color": "hsl(75.41064800843134, 100%, 75%)"
    },
    {
      "id": 462902,
      "name": "Instrumental",
      "color": "hsl(289.01439910611697, 100%, 75%)"
    },
    {
      "id": 462901,
      "name": "Easy Listening",
      "color": "hsl(74.47446441906085, 100%, 75%)"
    },
    {
      "id": 462900,
      "name": "Blues",
      "color": "hsl(20.68888526396953, 100%, 75%)"
    },
    {
      "id": 462899,
      "name": "Alternative Rock",
      "color": "hsl(148.57495283786687, 100%, 75%)"
    },
    {
      "id": 462898,
      "name": "Metal",
      "color": "hsl(254.94872281680875, 100%, 75%)"
    },
    {
      "id": 462897,
      "name": "Techno",
      "color": "hsl(274.79686788647894, 100%, 75%)"
    },
    {
      "id": 462896,
      "name": "Reggae",
      "color": "hsl(190.29478782729146, 100%, 75%)"
    },
    {
      "id": 462895,
      "name": "Country",
      "color": "hsl(48.84548952332932, 100%, 75%)"
    },
    {
      "id": 462894,
      "name": "New Age",
      "color": "hsl(257.94718575901226, 100%, 75%)"
    },
    {
      "id": 462893,
      "name": "Jazz",
      "color": "hsl(335.2902238371677, 100%, 75%)"
    },
    {
      "id": 462892,
      "name": "Classical",
      "color": "hsl(108.91485557045833, 100%, 75%)"
    },
    {
      "id": 462891,
      "name": "Singer/Songwriter",
      "color": "hsl(268.23790093286027, 100%, 75%)"
    },
    {
      "id": 462890,
      "name": "House",
      "color": "hsl(91.79402006550062, 100%, 75%)"
    },
    {
      "id": 462889,
      "name": "R&B/Soul",
      "color": "hsl(155.76504281123735, 100%, 75%)"
    },
    {
      "id": 462888,
      "name": "Alternative",
      "color": "hsl(120.62157773263625, 100%, 75%)"
    },
    {
      "id": 462887,
      "name": "Electronic",
      "color": "hsl(356.0379598956621, 100%, 75%)"
    },
    {
      "id": 462886,
      "name": "Orchestral",
      "color": "hsl(225.64368869262753, 100%, 75%)"
    },
    {
      "id": 462885,
      "name": "Dance",
      "color": "hsl(115.80598605955544, 100%, 75%)"
    },
    {
      "id": 462884,
      "name": "Rock",
      "color": "hsl(261.85862796182573, 100%, 75%)"
    },
    {
      "id": 462883,
      "name": "Hip-Hop/Rap",
      "color": "hsl(253.6184990012036, 100%, 75%)"
    },
    {
      "id": 462882,
      "name": "Pop",
      "color": "hsl(112.08652169651975, 100%, 75%)"
    },
    {
      "id": 462881,
      "name": "Children's Music",
      "color": "hsl(231.3153951631632, 100%, 75%)"
    },
    {
      "id": 462880,
      "name": "Samba",
      "color": "hsl(258.61586208736287, 100%, 75%)"
    },
    {
      "id": 462879,
      "name": "Christian",
      "color": "hsl(107.22490483556956, 100%, 75%)"
    },
    {
      "id": 462878,
      "name": "Klezmer",
      "color": "hsl(48.4464390393346, 100%, 75%)"
    },
    {
      "id": 462877,
      "name": "Sertanejo",
      "color": "hsl(297.8461249464192, 100%, 75%)"
    },
    {
      "id": 462876,
      "name": "Merengue",
      "color": "hsl(236.32790638485832, 100%, 75%)"
    },
    {
      "id": 462875,
      "name": "Cumbia",
      "color": "hsl(15.608801686689127, 100%, 75%)"
    },
    {
      "id": 462874,
      "name": "Polka",
      "color": "hsl(331.600439839617, 100%, 75%)"
    },
    {
      "id": 462873,
      "name": "Reggaeton",
      "color": "hsl(94.58441615588254, 100%, 75%)"
    },
    {
      "id": 462872,
      "name": "Afrobeat",
      "color": "hsl(157.4803782060952, 100%, 75%)"
    },
    {
      "id": 462871,
      "name": "Forro",
      "color": "hsl(245.73778901370298, 100%, 75%)"
    },
    {
      "id": 462870,
      "name": "Flamenco",
      "color": "hsl(57.54187686199268, 100%, 75%)"
    },
    {
      "id": 462869,
      "name": "Celtic",
      "color": "hsl(142.50812044535556, 100%, 75%)"
    },
    {
      "id": 462868,
      "name": "Schlager",
      "color": "hsl(165.36433207786604, 100%, 75%)"
    },
    {
      "id": 462867,
      "name": "Worldbeat",
      "color": "hsl(106.1819754033437, 100%, 75%)"
    },
    {
      "id": 462866,
      "name": "Bollywood",
      "color": "hsl(255.23834661214067, 100%, 75%)"
    },
    {
      "id": 462865,
      "name": "Cantopop",
      "color": "hsl(140.35690838571688, 100%, 75%)"
    },
    {
      "id": 462864,
      "name": "Russelater",
      "color": "hsl(216.06737144607166, 100%, 75%)"
    },
    {
      "id": 462863,
      "name": "Mandopop",
      "color": "hsl(16.990741090530975, 100%, 75%)"
    },
    {
      "id": 462862,
      "name": "Devotional & Spiritual",
      "color": "hsl(109.84808312930349, 100%, 75%)"
    }
  ]



def getCollaborators(data, accessToken):
    url = f'https://api.chartmetric.com/api/artist/list/filter?tagId={data["target_genre"]}&code2={data["target_country"]}&career_stage={data["career_stage"]}&limit=10'
    response = requests.get(
            url,
            headers = {'Authorization': 'Bearer ' + accessToken,
                       'content-Type': 'application/json',
                       'Accept': 'application/json'},
        )
    response_json = response.json()["obj"]
    my_genre_api = data["my_genre"]
    target_genre_api = data["target_genre"]
    my_genre = ""
    target_genre = ""

    for genre in genres:
        if my_genre_api == genre["id"]:
            my_genre = genre["name"]
        if target_genre_api == genre["id"]:
            target_genre = genre["name"]
    
    collaborators = {}
    collaborators["collaborators"] = response_json["obj"]
    for collaborator in collaborators["collaborators"]:
        collaborator_genre = collaborator["genres"]
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