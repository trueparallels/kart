#!/usr/bin/python3.6
import json
import prettytable
import lib.rank as ranking
import lib.common.web as webutil
import lib.common.slack as slackutil


def handle():
    # retrieve the rankings
    rankings = ranking.average_individual()

    # initialize the text table
    table = prettytable.PrettyTable(['Rank', 'Player', 'Character', 'Average'])

    # add each ranking entry to the table
    for index, player in enumerate(rankings):
        table.add_row([(index + 1), player['name'], player['character'], player['average']])

    # covert the table to format that Slack will understand
    table_string = '```' + table.get_string(border=True) + '```'
    slack_response = slackutil.ephemeral_response(table_string)

    return webutil.respond_success_json(json.dumps(slack_response))
