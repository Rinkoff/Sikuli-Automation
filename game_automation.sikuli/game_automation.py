start_button  = "1693385227022.png"
play_button = "play_button.png"

#Open the game
type(Key.WIN)
type("Chrome")
type(Key.ENTER)
sleep(1)
type("https://www.crazygames.com/game/switch")
type(Key.ENTER)

#Start game
if exists(start_button):
    click(start_button)


if exists(play_button,40):
    click(play_button)

click(Pattern("1693385795725.png").targetOffset(35,24))
            
while exists(Pattern("1693387507980.png").similar(0.60)) and  exists(Pattern("1693387345285.png").similar(0.60)):
    click(Pattern("1693386034997.png").targetOffset(96,248))
        



    

