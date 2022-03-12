from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re
app = Flask(__name__)

data = {
    "1": {
        "title": "In Moscow's Shadows 60: Ukraine: Nuclear Options, National Morale, and How Kyiv Can Save Moscow",
        "description": "What can one say about the unfolding horror in Ukraine. In this podcast I alight on a few specific issues: Putin's nuclear signalling (at least I hope that's all it is), the idiocy of 'No Fly Zones' in this context, Russian morale, and how, if Putin is re-booting the Brezhnev franchise, this could in the long-term let Russia finally complete its reform process.",
        "podcast_name": "In Moscow's Shadows",
        "podcast_image_url": "https://www.buzzsprout.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCS2s4QUFFPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--08d007e30c66de2aed803375943958aff047c375/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2QzNKbGMybDZaVWtpRFRZd01IZzJNREJlQmpzR1ZEb01aM0poZG1sMGVVa2lDMk5sYm5SbGNnWTdCbFE2QzJWNGRHVnVkRWtpRERZd01IZzJNREFHT3daVU9neHhkV0ZzYVhSNWFWVTZEMk52Ykc5eWMzQmhZMlZKSWdselVrZENCanNHVkE9PSIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--8a9b4b1bc245a46b538f72d4d9b2ab0a7fbe8ac1/IMSPodcastLogo.jpg",
        "episode_link": "https://www.buzzsprout.com/1026985/10152168-in-moscow-s-shadows-60-ukraine-nuclear-options-national-morale-and-how-kyiv-can-save-moscow",
        "id": 1,
        "date": "02/27/2022",
        "url": "https://www.buzzsprout.com/1026985/10152168-in-moscow-s-shadows-60-ukraine-nuclear-options-national-morale-and-how-kyiv-can-save-moscow.mp3",
    },
    "2": {
        "title": "What Putin Wants",
        "description": "Russia's newly-belligerent stance has rocked the democratic West on its heels, from the annexation of the Crimea to the sponsoring of extremist digital disinformation to - almost certainly - the stacking of elections in the US and UK. And it all stems from the paranoid, Machiavellian, espionage-steeped mindset of one man: Vladimir Putin. On this edition, Arthur talks to exiled journalists, foreign correspondents including Luke Harding of The Guardian and Russia analysts to unpick the question that baffles even Russians themselves: What does Putin want? Пожалуйста, наслаждайтесь нашим подкастом. Спасибо! 'There was no liberal Putin. There was no white album.'- LUKE HARDING 'Russia is the world champion at national suicide. It's a deeply, deeply self-destructive country.' - PETER POMERANTSEV 'Putin doesn't even see Ukraine as a country… They think, this was always ours, what is the US doing interfering?' - ARTYOM LISS 'The plan is to make Russia great again… Neither London nor Washington nor Paris has come up with an adequate way to deal with him.' - LUKE HARDING",
        "podcast_name": "Doomsday Watch with Arthur Snell",
        "podcast_image_url": "https://img.resized.co/shuffle/eyJkYXRhIjoie1widXJsXCI6XCJodHRwczpcXFwvXFxcL21lZ2FwaG9uZS5pbWdpeC5uZXRcXFwvcG9kY2FzdHNcXFwvMDI0MDE5MDgtM2NjYy0xMWVjLWJiYjUtMTc3MmNlODAzMDAzXFxcL2ltYWdlXFxcL0RPT01TREFZX1dBVENIX0FydGh1cl9tYWluX3RpbGUucG5nP2l4bGliPXJhaWxzLTIuMS4yJm1heC13PTMwMDAmbWF4LWg9MzAwMCZmaXQ9Y3JvcCZhdXRvPWZvcm1hdCxjb21wcmVzc1wiLFwid2lkdGhcIjpudWxsLFwiaGVpZ2h0XCI6bnVsbCxcImRlZmF1bHRcIjpcImh0dHBzOlxcXC9cXFwvd3d3LmdvbG91ZG5vdy5jb21cXFwvaW1hZ2VzXFxcL2xvZ28uc3ZnXCIsXCJvcHRpb25zXCI6W119IiwiaGFzaCI6IjRmNzcwZGRkNGEyOGU1ZTU4NjY2M2MzYTQzNjRmYjY4ZGQ3OTM2N2UifQ==/doomsday-watch-arthur-main-tile-png-ixlib-rails-2-1.2&max-w=3000&max-h=3000&fit=crop&auto=format,compress",
        "episode_link": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vZG9vbXNkYXl3YXRjaA/episode/YWQ5YTkwMWUtNDZjZi0xMWVjLTkzYWEtNGY0MzVmYWFjMjhi?sa=X&ved=0CAUQkfYCahcKEwiYxaCn8bX2AhUAAAAAHQAAAAAQCg&hl=en",
        "id": 2,
        "date": "11/23/2021",
        "url": "https://traffic.megaphone.fm/PMO1944155127.mp3?updated=1637063647",
    },
    "3": {
        "title": "It's not about Russia. It's about Putin",
        "description": "Since December, the biggest question facing foreign policymakers in the US and Europe has been as simple as it has been hard to really believe: Is Russia going to invade Ukraine? Russian President Vladimir Putin has ordered massive numbers of troops, tanks, artillery, and more to the border with Ukraine, as well as in Crimea (a region that Russia seized from Ukraine in 2014) and in Belarus (a close ally of Russia and northern neighbor of Ukraine). He has also issued demands that Ukraine not be admitted into NATO, and that NATO not deploy forces to member states close to Russia like Poland and the Baltic states. These are bold demands that some view as designed for Ukraine and the West to reject, allowing Putin to claim that diplomacy has failed and an invasion is necessary. For the moment, though, diplomatic efforts between the US, EU members, Ukraine, and Russia continue, and some experts are more optimistic that the situation can resolve without what could be Europe's first major land war in decades. One of them is Mark Galeotti, director of Mayak Intelligence, a professor at University College London, and an expert on Russian security affairs. We spoke on Zoom recently for an episode of Vox’s podcast The Weeds. A transcript, heavily truncated and edited for length and clarity, follows.",
        "podcast_name": "The Weeds",
        "podcast_image_url": "https://megaphone.imgix.net/podcasts/c3f826bc-e112-11e8-90b5-2f1c4d81c4e2/image/uploads_2F1585578364123-rcztsm1b6y-c1e630a7dd426cff08760d32dd9846b2_2FTile_3000x3000.png?ixlib=rails-2.1.2&max-w=3000&max-h=3000&fit=crop&auto=format,compress",
        "episode_link": "https://www.vox.com/22917832/vladimir-putin-ukraine-military-invasion",
        "id": 3,
        "date": "02/6/2022",
        "url": "https://www.podtrac.com/pts/redirect.mp3/pdst.fm/e/chtbl.com/track/524GE/traffic.megaphone.fm/VMP8280337054.mp3",
    },
    "4": {
        "title": "11 DAYS IN: RUSSIA’S INVASION STUMBLES FORWARD",
        "description": "Russia bungled its invasion plan but is nonetheless making progress in the face of fierce Ukrainian resistance. But can the Russian military stay combat effective? What lessons can we learn from the war so far? What role is urban warfare playing in this fight? What do the troubles faced by the Russian military and security services in Ukraine portend for the regime of Vladimir Putin? And what exactly is going on with that long column of Russian forces north of Kyiv? In our last episode, Michael Kofman sat down with Ryan to break down the first few days of the war. In this episode, he brings us up to speed and breaks down the state-of-play.",
        "podcast_name": "War On The Rocks",
        "podcast_image_url": "https://2k8r3p1401as2e1q7k14dguu-wpengine.netdna-ssl.com/wp-content/themes/warontherocks/assets/img/podcasts/war-on-the-rocks.jpg",
        "episode_link": "https://warontherocks.com/2022/03/11-days-in-russias-invasion-stumbles-forward/",
        "id": 4,
        "date": "03/07/2022",
        "url": "https://content.libsyn.com/p/d/3/f/d3f658815750cbd4/WOTR_March_7.mp3",
    }
}

# ROUTES

def search_data(term):
    results = []
    for (key, item) in data.items():
        title = item["title"].lower()
        title = re.sub('[!,*)@#%(&$_?.^]', '', title)
        description = item["description"].lower()
        description = re.sub('[!,*)@#%(&$_?.^]', '', description)
        if (term in title) or (term in description) or (term in item["podcast_name"]):
            results.append(item)
    return results

@app.route('/')
def home():
    display = [data["1"], data["2"], data["3"]]
    return render_template('home.html', data=display)

@app.route('/detail/<id>', methods=['GET', 'POST'])
def detail(id=None):
    if request.method == 'POST':
        return render_template("detail.html", data=item)
    else:
        item = data[id]
        return render_template("detail.html", data=item)

@app.route('/search/<term>')
def search(term: None):
    search_term = re.sub('[!,*)@#%(&$_?.^]', '', term)
    results = search_data(search_term)
    print(term)
    return render_template('search.html', data=results, search=term)

@app.route('/add')
def add():
    ids = data.keys()
    return render_template('form.html', data=[], possible_id=len(ids) + 1)

@app.route('/additem', methods=["GET", "POST"])
def additem():
    global data
    json_data = request.get_json()
    data[str(json_data["id"])] = json_data
    ids = data.keys()
    print(data)
    print(ids)
    updated_id = len(ids) + 1
    return jsonify(data = [], possible_id=updated_id)

@app.route('/edit/<id>', methods=["GET", "POST"])
def edit(id=None):
    if request.method == "POST":
         global data
         json_data = request.get_json()
         data[str(json_data["id"])] = json_data
         return jsonify(data = [data])
    item = data[id]
    return render_template('form.html', data=item)
    

if __name__ == '__main__':
    app.run(debug = True)
