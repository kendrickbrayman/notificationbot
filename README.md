# notification_bot
Groupme bot for keeping track of beer dye stats

## commands
!add - adds a new player to the database `!add [player name]`

!stats - shows stats for a player `!stats [player name]`

!game - updates the database after a game ```!game [winner1] [winner2] [#drinks] [loser1] [loser2] [#drinks]```

!racks - accesses information about rack purchases. Three different modes:
- `!racks` -- shows top 7 rack purchasers
- `!racks -f` -- shows ranking of all players in database
- `!racks [player name]` -- increases rack count by 1 and displays season count

!update - updates a single player's main stats `!update [player name] [w/l] [#drinks]`

!updateq - quiet updates a single player's main stats (no confirmation message) `!updateq [player name] [w/l] [#drinks]`

!updatef - full update to one player's full stats `!updatef [player name] [w/l] [#tosses] [#points] [#catches] [#drops] [#drinks]`
