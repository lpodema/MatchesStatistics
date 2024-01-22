from random import randint
import requests
from matches.service import create_match, join_match, finish_match
from players.service import create_player, get_players_by_quantity, get_playerbase_number


def new_and_existing_players_qty(player_quantity):
    playerbase = get_playerbase_number()
    new_players_quantity = randint(0, player_quantity)

    required_existing_players = player_quantity - new_players_quantity

    if playerbase < required_existing_players:
        new_players_quantity += (required_existing_players - playerbase)
        required_existing_players = playerbase
    existing_players = min(playerbase, required_existing_players)
    return existing_players, new_players_quantity


def create_new_players(new_players_quantity):
    new_players = []
    response = requests.get(f'https://randomuser.me/api/?format=json&results={new_players_quantity}').json()
    for new_player in response['results']:
        player_instance = create_player({'nickname': new_player['login']['username'],
                                         'thumbnail': new_player['picture']['thumbnail'],
                                         'med': new_player['picture']['medium'],
                                         'large': new_player['picture']['large']
                                         })
        new_players.append(player_instance)
    return new_players


def define_players():
    player_qty = randint(0, 10)

    new_players_instances = []
    existing_players_qty, new_players_qty = new_and_existing_players_qty(player_qty)

    existing_players_instances = list(get_players_by_quantity(existing_players_qty))

    if new_players_qty > 0:
        new_players_instances = create_new_players(new_players_qty)

    return new_players_instances + existing_players_instances


def play_loop():
    match = create_match()
    total_players = define_players()
    for player in total_players:
        join_match(match, player)
    finish_match(match)
