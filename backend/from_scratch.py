from just_stats import db
from just_stats.models import Team

db.drop_all()
db.create_all()


all_teams = ["Arsenal","Aston Villa","Brighton & Hove Albion","Burnley","Chelsea","Crystal Palace","Everton","Fulham","Leeds United","Leicester City","Liverpool","Manchester City","Manchester United","Newcastle United","Sheffield United","Southampton","Tottenham Hotspur","West Bromwich Albion","West Ham United","Wolverhampton Wanderers"]

for team in all_teams:
	t = Team(name = team, points = 0, wins = 0, draws = 0, loses = 0, goals_scored = 0, goals_concended = 0)
	db.session.add(t)
	db.session.commit()