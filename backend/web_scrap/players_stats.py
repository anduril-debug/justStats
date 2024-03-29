from bs4 import BeautifulSoup 
import requests


def get_players_stats(link):

	r = requests.get("https://fbref.com"+link)
	soup = BeautifulSoup(r.content, 'html.parser')

	tables = soup.find_all('table', class_="stats_table")
	real_tables = [tables[0], tables[7]]


	team1 = []
	team2 = []


	for i in range(2):
		if i == 0:
			rows = real_tables[i].find_all('tr')
			team1 = rows[2:-1]
		elif i == 1:
			rows = real_tables[i].find_all('tr')
			team2 = rows[2:-1]


	team1_players = []
	team2_players = []


	for player in team1:
		tmp_d = {}
		tmp_d["name"] = player.a.text if player.a else ""
		tmp_d["nationality"] = player.span.text if player.span else ""
		tmp_d["position"] = player.find(attrs = {"data-stat" : "position" }).text if player.find(attrs = {"data-stat" : "position" }) else ""
		tmp_d["shirt_number"] = player.find(attrs = {"data-stat" : "shirtnumber" }).text if player.find(attrs = {"data-stat" : "shirtnumber" }) else ""
		tmp_d["age"] = player.find(attrs = {"data-stat" : "age" }).text if player.find(attrs = {"data-stat" : "age" }) else ""
		tmp_d["minutes_played"] = player.find(attrs = {"data-stat" : "minutes" }).text if player.find(attrs = {"data-stat" : "minutes" }) else "0"
		tmp_d["goals"] = player.find(attrs = {"data-stat" : "goals" }).text if player.find(attrs = {"data-stat" : "goals" }) else "0"
		tmp_d["assists"] = player.find(attrs = {"data-stat" : "assists" }).text if player.find(attrs = {"data-stat" : "assists" }) else "0"
		tmp_d["penalties_made"] = player.find(attrs = {"data-stat" : "pens_made" }).text if player.find(attrs = {"data-stat" : "pens_made" }) else "0"
		tmp_d["penalties_att"] = player.find(attrs = {"data-stat" : "pens_att" }).text if player.find(attrs = {"data-stat" : "pens_att" }) else "0"	
		tmp_d["total_shots"] = player.find(attrs = {"data-stat" : "shots_total" }).text if player.find(attrs = {"data-stat" : "shots_total" }) else "0"
		tmp_d["shots_on_target"] = player.find(attrs = {"data-stat" : "shots_on_target" }).text if player.find(attrs = {"data-stat" : "shots_on_target" }) else "0"
		tmp_d["cards_yellow"] = player.find(attrs = {"data-stat" : "cards_yellow" }).text if player.find(attrs = {"data-stat" : "cards_yellow" }) else "0"
		tmp_d["cards_red"] = player.find(attrs = {"data-stat" : "cards_red" }).text if player.find(attrs = {"data-stat" : "cards_red" }) else "0"
		tmp_d["touches"] = player.find(attrs = {"data-stat" : "touches" }).text if player.find(attrs = {"data-stat" : "touches" }) else "0"
		tmp_d["pressures"] = player.find(attrs = {"data-stat" : "pressures" }).text if player.find(attrs = {"data-stat" : "pressures" }) else "0"
		tmp_d["tackles"] = player.find(attrs = {"data-stat" : "tackles" }).text if player.find(attrs = {"data-stat" : "tackles" }) else "0"
		tmp_d["interceptions"] = player.find(attrs = {"data-stat" : "interceptions" }).text if player.find(attrs = {"data-stat" : "interceptions" }) else "0"
		tmp_d["blocks"] = player.find(attrs = {"data-stat" : "blocks" }).text if player.find(attrs = {"data-stat" : "blocks" }) else "0"	
		tmp_d["passes_completed"] = player.find(attrs = {"data-stat" : "passes_completed" }).text if player.find(attrs = {"data-stat" : "passes_completed" }) else "0"
		tmp_d["passes"] = player.find(attrs = {"data-stat" : "passes" }).text if player.find(attrs = {"data-stat" : "passes" }) else "0"	
		tmp_d["passes_pct"] = player.find(attrs = {"data-stat" : "passes_pct" }).text if player.find(attrs = {"data-stat" : "passes_pct" }) else "0"	
		tmp_d["passes_progressive_distance"] = player.find(attrs = {"data-stat" : "passes_progressive_distance" }).text if player.find(attrs = {"data-stat" : "passes_progressive_distance" }) else "0"
		tmp_d["carries"] = player.find(attrs = {"data-stat" : "carries" }).text if player.find(attrs = {"data-stat" : "carries" }) else "0"
		tmp_d["carry_progressive_distance"] = player.find(attrs = {"data-stat" : "carry_progressive_distance" }).text if player.find(attrs = {"data-stat" : "carry_progressive_distance" }) else "0"
		tmp_d["dribbles_completed"] = player.find(attrs = {"data-stat" : "dribbles_completed" }).text if player.find(attrs = {"data-stat" : "dribbles_completed" }) else "0"
		tmp_d["dribbles"] = player.find(attrs = {"data-stat" : "dribbles" }).text if player.find(attrs = {"data-stat" : "dribbles" }) else "0"



		for k,v in tmp_d.items():
			if v == '' or v == ' ' or v == False or v == None:
				tmp_d[k] = ""

		team1_players.append(tmp_d)


	for player in team2:
		tmp_d = {}
		tmp_d["name"] = player.a.text if player.a else ""
		tmp_d["nationality"] = player.span.text if player.span else ""
		tmp_d["position"] = player.find(attrs = {"data-stat" : "position" }).text if player.find(attrs = {"data-stat" : "position" }) else ""
		tmp_d["shirt_number"] = player.find(attrs = {"data-stat" : "shirtnumber" }).text if player.find(attrs = {"data-stat" : "shirtnumber" }) else ""
		tmp_d["age"] = player.find(attrs = {"data-stat" : "age" }).text if player.find(attrs = {"data-stat" : "age" }) else ""
		tmp_d["minutes_played"] = player.find(attrs = {"data-stat" : "minutes" }).text if player.find(attrs = {"data-stat" : "minutes" }) else "0"
		tmp_d["goals"] = player.find(attrs = {"data-stat" : "goals" }).text if player.find(attrs = {"data-stat" : "goals" }) else "0"
		tmp_d["assists"] = player.find(attrs = {"data-stat" : "assists" }).text if player.find(attrs = {"data-stat" : "assists" }) else "0"
		tmp_d["penalties_made"] = player.find(attrs = {"data-stat" : "pens_made" }).text if player.find(attrs = {"data-stat" : "pens_made" }) else "0"
		tmp_d["penalties_att"] = player.find(attrs = {"data-stat" : "pens_att" }).text if player.find(attrs = {"data-stat" : "pens_att" }) else "0"	
		tmp_d["total_shots"] = player.find(attrs = {"data-stat" : "shots_total" }).text if player.find(attrs = {"data-stat" : "shots_total" }) else "0"
		tmp_d["shots_on_target"] = player.find(attrs = {"data-stat" : "shots_on_target" }).text if player.find(attrs = {"data-stat" : "shots_on_target" }) else "0"
		tmp_d["cards_yellow"] = player.find(attrs = {"data-stat" : "cards_yellow" }).text if player.find(attrs = {"data-stat" : "cards_yellow" }) else "0"
		tmp_d["cards_red"] = player.find(attrs = {"data-stat" : "cards_red" }).text if player.find(attrs = {"data-stat" : "cards_red" }) else "0"
		tmp_d["touches"] = player.find(attrs = {"data-stat" : "touches" }).text if player.find(attrs = {"data-stat" : "touches" }) else "0"
		tmp_d["pressures"] = player.find(attrs = {"data-stat" : "pressures" }).text if player.find(attrs = {"data-stat" : "pressures" }) else "0"
		tmp_d["tackles"] = player.find(attrs = {"data-stat" : "tackles" }).text if player.find(attrs = {"data-stat" : "tackles" }) else "0"
		tmp_d["interceptions"] = player.find(attrs = {"data-stat" : "interceptions" }).text if player.find(attrs = {"data-stat" : "interceptions" }) else "0"
		tmp_d["blocks"] = player.find(attrs = {"data-stat" : "blocks" }).text if player.find(attrs = {"data-stat" : "blocks" }) else "0"	
		tmp_d["passes_completed"] = player.find(attrs = {"data-stat" : "passes_completed" }).text if player.find(attrs = {"data-stat" : "passes_completed" }) else "0"
		tmp_d["passes"] = player.find(attrs = {"data-stat" : "passes" }).text if player.find(attrs = {"data-stat" : "passes" }) else "0"	
		tmp_d["passes_pct"] = player.find(attrs = {"data-stat" : "passes_pct" }).text if player.find(attrs = {"data-stat" : "passes_pct" }) else "0"	
		tmp_d["passes_progressive_distance"] = player.find(attrs = {"data-stat" : "passes_progressive_distance" }).text if player.find(attrs = {"data-stat" : "passes_progressive_distance" }) else "0"
		tmp_d["carries"] = player.find(attrs = {"data-stat" : "carries" }).text if player.find(attrs = {"data-stat" : "carries" }) else "0"
		tmp_d["carry_progressive_distance"] = player.find(attrs = {"data-stat" : "carry_progressive_distance" }).text if player.find(attrs = {"data-stat" : "carry_progressive_distance" }) else "0"
		tmp_d["dribbles_completed"] = player.find(attrs = {"data-stat" : "dribbles_completed" }).text if player.find(attrs = {"data-stat" : "dribbles_completed" }) else "0"
		tmp_d["dribbles"] = player.find(attrs = {"data-stat" : "dribbles" }).text if player.find(attrs = {"data-stat" : "dribbles" }) else "0"



		for k,v in tmp_d.items():
			if v == '' or v == ' ' or v == False or v == None:
				tmp_d[k] = ""

		team2_players.append(tmp_d)

	result = { 
			"team1" : team1_players, 
			"team2" : team2_players
			}

	return result




