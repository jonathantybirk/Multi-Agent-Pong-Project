from ai import *

# LOOP
while not EXIT:
    # Input
    keys = pg.key.get_pressed()

    # Exit
    for event in pg.event.get():
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            EXIT = True

    # Draw background (and clear screen)
    app.fill(backgroundColor)
    drawGrid()

    # Players
    for player in players:
        player.control()
        player.move(player.movement[1])
        player.draw()

    # Ball
    ball.collide()
    ball.move()
    ball.lose()
    ball.draw()

    # Misc
    pg.display.update()
    pg.time.Clock().tick(5)