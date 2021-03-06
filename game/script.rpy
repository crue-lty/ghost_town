define g = Character("", kind=nvl, what_outlines=[(1,"#d47e00",0,0)]) #girl
define m = Character("", kind=nvl, what_outlines=[(1,"#0a1932",0,0)]) #guy
define narrator = Character(kind=nvl)
image filmoverlay:
    "film 1.png"
    0.1
    "film 2.png"
    0.1
    "film 3.png"
    0.1
    "film 4.png"
    0.1
    "film 5.png"
    0.1
    "film 6.png"
    0.1
    repeat

# image filmcomposite = LiveComposite(
    # (1280,800),
    # (0,0), "filmoverlay"
    # (0,0), "main underlay.png")


image bg black = "#000"
image bg white = "#fff"
transform nvlbgshow:
    alpha 0.0
    xpos 0.0
    xanchor 0.5
    parallel:
        linear 1.0 alpha 1.0
    parallel:
        easein_quad 1.0 xpos 0.5

label hideitall: #because the scene statement sucks #actually I'm not sure if it really sucks as much as I thought but I think I'll leave this be #at least for now
    hide girl
    hide guy
    hide bg
    hide nvlbg
    hide black
    hide white
    return


label start:
    scene bg black
    scene bg snow
    show girl 2
    with dissolve
    show nvlbg at nvlbgshow
    g "It's... It's been a long time."
    g "He hasn't been around since yesterday... I'm... A bit worried."
    g "He always comes. He said he would. He would take care. Of me."
    g "I don't know his name, but how does it matter? He's the only one who... Who wouldn't turn away from me."
    show girl 1 with dissolve
    nvl clear
    g "It's really cold tonight..."
    g "I hope he'll come today too... He..."
    scene bg snow path
    show guy 4
    with dissolve
    pause 1.0
    scene bg snow closeup
    show girl 3
    with dissolve
    show guy 1:
        alpha 0.0
        truecenter
        xpos 0.6
        parallel:
            easein_quad 1.0 xpos 0.5
        parallel:
            linear 0.5 alpha 1.0
    show nvlbg at nvlbgshow
    nvl clear
    g "I knew you wouldn't leave me! I knew, I knew, I knew... I'm so glad. You don't even know."
    m "I told you I would be with you until you pass away. And I'm not a person to break promises, I assure you, sunny."
    m "I brought you the usual necessities; food, twigs for a fire too. And... a special thing!"
    g "You... You really didn't have to!... I'm not worth the bother, you know..."
    show guy 2 with dissolve
    m "I hope it'll fit you just fine. I think... it's something of your liking, too."
    g "I can't believe this, I. T-thank you. Thank you so much!"
    show girl 4 with dissolve
    g "I love it."
    show bg snow closeup dark
    with dissolve
    g "I know it's rude of me to ask, since you help me out so much, but... {w}Can you tell me... {w}How long, uhhh... {w}Until the day?"
    m "My sweet child, soon enough you will know. Fret not, I have not forgotten. All my preparations are heading to the end."
    m "There's one thing itching my mind, sunny... You've never truly told me how it all happened."
    m "Or maybe you did - you know how an old man's memory can rot away..."
    g "It's hard for me to speak about it, but... for you, I will... I will try to remember."
    m "Don't push yourself too far, child. Take it slow, alright?"
    show bg black as black:
        alpha 0.0
        linear 0.5 alpha 1.0
    g "You probably don't know me, since you're a foreigner, but..."
    call hideitall from _call_hideitall
    show bg white with None
    scene bg factory view1 #todo: add animations
    show filmoverlay
    show filmunderlay
    show nvlbg
    with Dissolve(2.0)
    nvl clear
    g "I'm the daughter of the richest man on the city that's past that trail."
    g "The factories around the city are the main source of income for my father."
    g "He never told me much about them, but I think these were coal and lead mines. These need big chimneys, you know?"
    m "I'm a safety inspector for the council, so my job is to make sure these rules are followed properly, for the well-being of the population."
    m "That is correct, lead mines are quite harmful. They need good ventilation so as to avoid poisoning people with the fumes."
    g "Ah, the fumes-"
    m "I apologize for my interruption, so please continue your story."
    #show girl 4 but more scared
    g "That must be why..."
    g "You see, this town has been getting worse and worse after the factories started running."
    show bg field with dissolve
    g "The people started getting sick and dying, especially the workers."
    g "These fumes... {w}they came from the chimneys, and you could tell that whoever went down the mine would get sicker day by day."
    g "They told me about what was happening... They... They tried to warn me..."
    #her eyes get watery
    show bg mines2 with dissolve
    m "Who tried to warn you? The workers that came out of the mines?"
    g "No... it was the ones who didn't make it out."
    g "I saw them every day."
    g "At home, or outside, they were always there."
    g "I'm sure they were looking for me, because I was the only one who could see them."
    #show capitalist dad oink oink
    show bg factory view1 with dissolve
    g "But my dad never listened."
    g "I told him about all the people who were suffering and dying because of him, but it was pointless."
    g "He didn't care at all... I...  I couldn't take it..."
    #girl cries and falls down
    scene bg black with Dissolve(2.0)
    nvl clear
    show bg snow closeup dark
    show girl 5
    show guy 3
    with dissolve
    show nvlbg at nvlbgshow
    m "He really does seem like a wrongful person, I'm sorry sunny."
    m "Maybe you should rest a bit? You look tired.{w} I promise I'll come again, alright?"
    #they get comfier
    m "The fire will soon be gone too so please, darling."
    g "...Thank you so much for taking care of me."
    g "I'll try to rest, but..."
    g "Please take me with you as soon as you can."
    g "I don't want to keep sleeping out in the cold."
    scene bg black with dissolve
    nvl clear
    # change of scenes, it's the morning now
    pause 1.0
    call hideitall from _call_hideitall_1
    show bg white with None
    scene bg snow closeup
    show girl 5
    with Dissolve(2.0)
    show nvlbg at nvlbgshow
    nvl clear
    g "He's gone again..."
    g "It's a little warmer than yesterday, but it's still very cold."
    g "I really hope he'll be back soon today..."
    scene bg black with dissolve
    pause 1.0
    scene bg snow closeup
    show girl 2
    show guy 2
    with Dissolve(1.0)
    show nvlbg at nvlbgshow
    #girl lies down on the snow
    #change of scenes maybe?
    nvl clear
    #guy wakes her up kneeling
    m "How did you sleep, my dear?"
    g "Not so well... {w}It's really cold..."
    g "And there's a storm coming up."
    g "I don't wanna be here when the storm arrives."
    g "It's dangerous."
    g "Please."
    g "You have to take me home with you."
    #maybe the guy changes expressions?
    m "I'm almost ready, my dear."
    m "I promise the wait will be fruitful."
    m "Soon we won't have to worry about any of this."
    m "I'll take good care of you once you're with me."
    m "For now, all I can do is keep you company."
    g "Thank you so much."
    g "I think I'd be dead by now if it wasn't for you."
    m "Don't worry about it, precious."
    m "Please eat what from what I've brought and gain strength."
    m "It's not much, but it should get you through today."
    m "I promise we'll leave by tomorrow's night."
    g "It feels like such a long time..."
    #she lies down again
    g "I just hope the ghosts will stop bothering me once I'm there."
    #he seems surprised
    m "Ghosts?"
    m "What ghosts?"
    g "I thought... {w}I had told you about it yesterday..."
    g "Didn't I?"
    m "You shouldn't tell me if it awakens bad feelings in your heart, young lady."
    g "No! You don't understand."
    g "I want you to know."
    g "You need to protect me."
    m "..."
    m "I see."
    m "In that case, please tell me."
    m "Who are these ghosts?{w} Why were they bothering you?"
    g "They... {w}They were the victims of my father."
    g "I don't know if they were looking for revenge,{w} or for justice, but..." #maybe make dramatic scene change during this sentence
    nvl clear
    scene bg black with dissolve
    g "But..."
    nvl clear
    "Hey."
    #she tries to ignore the ghost, as the world materializes around her
    "Young lady, please look at me."
    "Please look at us."
    "Look at what your father has done to us."
    "We need your help."
    "Please, we beg you."
    "I beg you." #repeat this a bunch of times from different people for psychological effect
    g "What do you want?"
    g "Why does it have to be me?"
    "You're blessed with a very unique ability, young lady."
    "You're the only one who can carry our will forward."
    "Will you help us save this town from the evil that governs it?"
    "Will you help us finally rest in peace?"
    menu:
        "Yes.":
            $helped=1
            g "..."
            g "Okay."
            "Thank you, young lady."
            "We just need you to do a very simple thing."
            "We are aware that mechanics might not be the most fit task for a person like you, but you're the only hope we have left."
            #change of scenes, mechanical noises (maybe showing the underside of the car)
            nvl clear
            g "And that's all?"
            "Yes, that is all we need from you."
            g "Will you leave me in peace now?"
            "Oh,  soon enough. We just need the mechanism to go into effect."
            #another change of scenes
            nvl clear
            "Young lady, young lady! There's an emergency!"
            "Someone has tried to assassinate your father!"
            g "What?! {w}How?"
            "An explosion happened on his car just now."
            "It was far too powerful to be accidental."
            "Thankfully, it was parked in the new mining site, so no one was around when it happened."
            "But just a bit of bad luck, and your father wouldn't be here right now."
            g "I... I think I need a minute alone..."
            "I can understand, young lady. {w}I know how shocking hearing something like this can be."
            "But I want you to know that we have already contacted some of the best detectives in the country to find out who the culprit is."
            "I'm sure in just a few days we will know for sure who rigged your father's car, so you don't have to worry about it."
            "They won't receive any mercy from us, or from the sheriff."
            #she breaks down even more (I don't know if I should add some dialogue here)
            "We will be waiting for you at the dining room."
            "There will be increased security in the whole area, so you we want to notify you about all the new changes, young lady."
            "Please come when you feel more composed."
            #another change of scenes, now the girl is alone in the room
            g "This can't be happening..."
            g "I can't believe what I've done."
            g "It's all my fault."
            g "I'll never be able to look at my father to the face again."
            g "What will he do when he finds out it was me?"
            g "What will everyone do when they find out it was me?"
            g "I can't stay here any longer..."
            #change of scenes to the snow
        "No.":
            $helped=0
            g "I don't want to."
            g "I won't do this to my father."
            g "I know what you want from me, but I refuse."
            g "You won't get anywhere by talking to me."
            "We won't be able to rest until justice has been served, young lady."
            g "Can't you find someone else?"
            "We are tied to this house."
            "And you're the only one in here who can hear us."
            g "If you can't leave, then I'll do."
            g "I don't want to see any of you ever again in my life."
            "The winter is coming near. You will not survive."
            g "I will find shelter somewhere away from you."
            #change of scenes to the snow
            pass
    nvl clear
    #it's already nighttime
    m "I have nothing but respect for you, young lady."
    m "It takes a great bravery to take such a decision."
    m "There is a question that troubles my mind, however; and I hope you don't feel I've disrespected you by asking this."
    m "Why do you wish to come with me, instead of going back to your home?"
    m "I'm sure your family will understand how you were forced into doing this, against your will."
    g "I don't think so..."
    g "I don't think my family will ever forgive me."
    g "My father is known for ruling with an iron fist - not only in business but in our family as well."
    g "It's the way he is."
    g "If he were to know, he would likely kick me out of the home in an even more shameful way."
    g "I think... {w}I think it's best for me to disappear. {w}So no one can find me again."
    g "Do you live far away from here?"
    m "Not really."
    m "But you could say I'm free to go where I feel like, so you don't have to worry about it."
    m "If that is your wish, I will make sure that you don't have to encounter your father again."
    #man sits down probably
    m "I know what it feels like to flee from your crimes."
    "..."
    nvl clear
    g "Will you stay with me tonight?"
    m "I'm afraid I can't today, young lady."
    m "But I promise you'll come with me tomorrow."
    m "Everything is ready."
    m "It's almost time."
    #she lies down maybe?
    g "Thank you."
    g "Thank you so much."
    g "I think I'd probably be dead already without your help."
    m "Don't you worry, my dear."
    m "You will be safe with me."
    m "We just need to wait until tomorrow, okay?"
    #she gets uhhh  a little comfier
    "..."
    g "Please come back quickly tomorrow."
    g "I can feel the storm coming closer."
    g "It's very dangerous if it hits and I'm still here."
    m "I can understand, young lady."
    m "I promise I will come for you as soon as I can."
    m "Goodnight, my dear. {w}It's quite late."
    g "Goodnight."
    nvl clear

    #change of scenes, the snow sound gets stronger, now there's more snow on the screen and stuff

    g "He said he would come today..."
    g "He will come, right?"
    g "He won't leave me here, in the storm..."

    # the storm gets even stronger
    nvl clear
    if helped==True:
        jump goodEnding
    else:
        jump badEnding
    return






label goodEnding:
    #guy comes closer and holds her hand
    m "I came here for you, young lady."
    m "I said I wouldn't abandon you."
    #her eyes light up, her fingers are purple already
    g "I'm cold..."
    g "I'm so cold..."
    g "Please bring me with you..."
    m "Soon enough, my dear."
    m "Please relax."
    #he takes her blanket out (?)
    g "I-I'm... going to freeze..."
    m "We'll be together soon, my dear."
    #change of music and tone of the scene (it gets dark at first then it becomes light, almost ethereal)
    nvl clear
    g "...what happened?"
    g "I'm not... I don't feel cold anymore."
    m "I know, my dear."
    m "Let's go home."

    #here goes the Emotional Slideshow(TM)
    jump credits
    return


label badEnding:
    #she wakes up in the snow
    #the breeze is even stronger
    g "Where is him?"
    g "He said he'd come back, right?"
    g "He said he would come for me..."
    g "Where is... {w}Where is the bonfire? {w}Where is the coat he brought for me?"
    g "I'm hungry... {w}Have I really eaten anything?"
    g "Was he real?"
    g "Was... {w}Was any of it real?"

    #Emotional Slideshow 2.0: now it's sad
    jump credits
    return

label credits:
    nvl clear
    scene bg white with dissolve
    "these are the credits"
    $renpy.pause(1.0,hard=True)
    return
