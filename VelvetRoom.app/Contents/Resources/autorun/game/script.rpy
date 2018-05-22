# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Jeef", color="#3C932A")


# The game starts here.

define config.name = _('The Velvet Room')

define gui.show_name = True

define config.version = "1.0"

define gui.about = _("Made by Capn Commie.")
#Rough start to test the engine and see what it can do
label start:
    play music "yeet.mp3"
    show asd
    scene velvetr



    python:
        a=['fool', 'magician', 'high priestess', 'empress', 'emperor', 'hierophant', 'lovers',
        'chariot', 'strength', 'hermit', 'wheel of fortune', 'justice', 'hanged man', 'death',
        'temperance', 'devil', 'tower', 'star', 'moon', 'sun', 'judgement', 'world']
        for i in range(1):
            from random import randint

            size=len(a)-1
            x= randint(0,size)
            first="1"
            first = (a[x])
            del a[x]

            size = len(a)-1
            x= randint(0,size)
            second="1"
            second = (a[x])
            del a[x]

            size=len(a)-1
            x= randint(0,size)
            third="1"
            third = (a[x])
            del a[x]

            size=len(a)-1
            x= randint(0,size)
            forth="1"
            forth = (a[x])
            del a[x]

            size=len(a)-1
            x= randint(0,size)
            fifth="1"
            fifth = (a[x])
            del a[x]

            size=len(a)-1
            x= randint(0,size)
            sixth="1"
            sixth = (a[x])
            del a[x]

            size=len(a)-1
            x= randint(0,size)
            seventh="1"
            seventh = (a[x])
            del a[x]

            size=len(a)-1
            x= randint(0,size)
            eighth="1"
            eighth = (a[x])
            del a[x]

            size=len(a)-1
            x= randint(0,size)
            ninth="1"
            ninth = (a[x])
            del a[x]

            size=len(a)-1
            x= randint(0,size)
            tenth="1"
            tenth  = (a[x])



jump test
label test:
    "Shuffling..."
    "Would You Like to Shuffle Again?"
    menu:
        "Yes":
            jump test
        "No":
            jump heh

label heh:
    "Your Current Situation is:"
    if first== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."


    if first== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if first== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if first== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if first== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if first== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if first== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if first== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if first== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if first== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if first== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if first== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if first== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if first== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if first== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if first== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if first== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if first== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if first== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if first== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if first== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if first== "world":
        show 22 at truecenter
        "The World"
        "The World represents an ending to a cycle of life, a pause in life before the next big cycle beginning with the fool. It is an indicator of a major and inexorable change, of tectonic breadth."
############################################
    "The Current Challenge is:"
    if second== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."

    if second== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if second== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if second== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if second== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if second== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if second== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if second== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if second== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if second== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if second== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if second== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if second== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if second== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if second== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if second== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if second== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if second== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if second== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if second== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if second== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if second== "world":
        show 22 at truecenter
        "The World"
        "The World represents an ending to a cycle of life, a pause in life before the next big cycle beginning with the fool. It is an indicator of a major and inexorable change, of tectonic breadth."
#####################################
    "The Basis of the Situation is:"
    if third== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."

    if third== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if third== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if third== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if third== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if third== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if third== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if third== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if third== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if third== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if third== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if third== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if third== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if third== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if third== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if third== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if third== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if third== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if third== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if third== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if third== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if third== "world":
        show 22 at truecenter
        "The World"
        "The World represents an ending to a cycle of life, a pause in life before the next big cycle beginning with the fool. It is an indicator of a major and inexorable change, of tectonic breadth."
####################################
    "The Relevant Past is:"
    if forth== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."

    if forth== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if forth== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if forth== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if forth== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if forth== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if forth== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if forth== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if forth== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if forth== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if forth== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if forth== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if forth== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if forth== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if forth== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if forth== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if forth== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if forth== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if forth== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if forth== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if forth== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if forth== "world":
        show 22 at truecenter
        "The World"
        "The World represents an ending to a cycle of life, a pause in life before the next big cycle beginning with the fool. It is an indicator of a major and inexorable change, of tectonic breadth."
##################################
    "The Present is:"
    if fifth== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."

    if fifth== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if fifth== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if fifth== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if fifth== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if fifth== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if fifth== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if fifth== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if fifth== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if fifth== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if fifth== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if fifth== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if fifth== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if fifth== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if fifth== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if fifth== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if fifth== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if fifth== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if fifth== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if fifth== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if fifth== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if fifth== "world":
        show 22 at truecenter
        "The World"
        "The World represents an ending to a cycle of life, a pause in life before the next big cycle beginning with the fool. It is an indicator of a major and inexorable change, of tectonic breadth."
#################################
    "The Near Future is:"
    if sixth== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."

    if sixth== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if sixth== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if sixth== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if sixth== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if sixth== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if sixth== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if sixth== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if sixth== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if sixth== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if sixth== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if sixth== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if sixth== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if sixth== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if sixth== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if sixth== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if sixth== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if sixth== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if sixth== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if sixth== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if sixth== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if sixth== "world":
        show 22 at truecenter
        "The World"
        "The World represents an ending to a cycle of life, a pause in life before the next big cycle beginning with the fool. It is an indicator of a major and inexorable change, of tectonic breadth."
#################################
    "Your Power in the Situation is:"
    if seventh== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."

    if seventh== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if seventh== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if seventh== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if seventh== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if seventh== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if seventh== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if seventh== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if seventh== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if seventh== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if seventh== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if seventh== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if seventh== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if seventh== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if seventh== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if seventh== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if seventh== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if seventh== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if seventh== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if seventh== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if seventh== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if seventh== "world":
        show 22 at truecenter
        "The World"
        "The World represents an ending to a cycle of life, a pause in life before the next big cycle beginning with the fool. It is an indicator of a major and inexorable change, of tectonic breadth."
#################################
    "The Effect on People Around you is:"
    if eighth== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."

    if eighth== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if eighth== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if eighth== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if eighth== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if eighth== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if eighth== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if eighth== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if eighth== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if eighth== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if eighth== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if eighth== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if eighth== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if eighth== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if eighth== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if eighth== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if eighth== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if eighth== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if eighth== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if eighth== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if eighth== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if eighth== "world":
        show 22 at truecenter
        "The World"
        "The World represents an ending to a cycle of life, a pause in life before the next big cycle beginning with the fool. It is an indicator of a major and inexorable change, of tectonic breadth."
#######################################
    "Your Hopes and Fears are:"
    if ninth== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."

    if ninth== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if ninth== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if ninth== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if ninth== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if ninth== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if ninth== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if ninth== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if ninth== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if ninth== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if ninth== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if ninth== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if ninth== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if ninth== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if ninth== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if ninth== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if ninth== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if ninth== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if ninth== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if ninth== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if ninth== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if ninth== "world":
        show 22 at truecenter
        "The World"
        "The World represents an ending to a cycle of life, a pause in life before the next big cycle beginning with the fool. It is an indicator of a major and inexorable change, of tectonic breadth."
#################################
    "The Outcome is:"
    if tenth== "fool":
        show 0 at truecenter
        "Fool"
        "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe."

    if tenth== "magician":
        show 1 at truecenter
        "Magician"
        "When the Magician appears in a spread, it points to the talents, capabilities and resources at the querent's disposal to succeed."
        "The message is to tap into one's full potential rather than holding back, especially when there is a need to transform something."
    if tenth== "high priestess":
        show 2 at truecenter
        "High Priestess"
        "High Priestess is a card of mystery, stillness and passivity. This card suggests that it is time to retreat and reflect upon the situation and trust your inner instincts to guide you through it."
        "Things around you are not what they appear to be right now"
    if tenth== "empress":
        show 3 at truecenter
        "Empress"
        "The Empress is traditionally associated with maternal influence, it is the card if you are hoping to start a family. She can represent the creation of life, romance, art, or new business."
    if tenth== "emperor":
        show 4 at truecenter
        "Emperor"
        "This card is suggestive of stability and security in life. You are on top of things and everything in under your control. It is your hard work, discipline and self control that have bought you this far."
        "It means that you are in charge of your life now setting up your own rules and boundaries."
    if tenth== "hierophant":
        show 5 at truecenter
        "Hierophant"
        "Hierophant stands for tradition and convention. It can represent marriage in an arranged setup. It can also mean a teacher or counsellor who will help in learning / education of the querent."
    if tenth== "lovers":
        show 6 at truecenter
        "Lovers"
        "The Lovers represent relationships and choices. Its appearance in a spread indicates some decision about an existing relationship, a temptation of the heart, or a choice of potential partners"
    if tenth== "chariot":
        show 7 at truecenter
        "Chariot"
        "The Chariot is a card about overcoming conflicts and moving forward in a positive direction. One needs to keep going on and through sheer hard work and commitment he will be victorious."
    if tenth== "strength":
        show 8 at truecenter
        "Strength"
        "Strength predicts the triumphant conclusion to a major life problem, situation or temptation through strength of character. It is a very happy card if you are fighting illness or recovering from injury."
    if tenth== "hermit":
        show 9 at truecenter
        "Hermit"
        "The Hermit suggests that you are in a phase of introspection where you are drawing your attention inwards and looking for answers within."
        "You are in need of a period of inner reflection, away from the current demands of your position."
    if tenth== "wheel of fortune":
        show 10 at truecenter
        "Wheel of Fortune"
        "An element of change in the querent's life, such change being in station, position or fortune: such as the rich becoming poor, or the poor becoming rich."
    if tenth== "justice":
        show 11 at truecenter
        "Justice"
        "The Justice card indicates that the fairest decision will be made. Justice is the sword that cuts through a situation, and will not be swayed by outer beauty when deciding what is fair and just."
    if tenth== "hanged man":
        show 12 at truecenter
        "Hanged Man"
        "The Hanged Man is the card that suggests ultimate surrender, sacrifice, or being suspended in time."
    if tenth== "death":
        show 13 at truecenter
        "Death"
        "Implies an end, possibly of a relationship or interest, and therefore implies an increased sense of self-awareness."
    if tenth== "temperance":
        show 14 at truecenter
        "Temperance"
        "This card indicates that you should learn to bring about balance, patience and moderation in your life. You should take the middle road, avoiding extremes and maintain a sense of calm."
    if tenth== "devil":
        show 15 at truecenter
        "Devil"
        "It represents being seduced by the material world and physical pleasures."
        "Also living in fear, domination and bondage, being caged by an overabundance of luxury, discretion should be used in personal and business matters."
    if tenth== "tower":
        show 16 at truecenter
        "Tower"
        "The Tower is commonly interpreted as meaning danger, crisis, destruction, and liberation. It is associated with sudden unforseen change."
    if tenth== "star":
        show 18 at truecenter
        "Star"
        "You are likely to find yourself feeling inspired. It brings renewed hope and faith and a sense that you are truly blessed by the universe at this time."
    if tenth== "moon":
        show 19 at truecenter
        "Moon"
        "The Moon is a card of illusion and deception, and therefore often suggests a time when something is not as it appears to be. Perhaps a misunderstanding on your part, or a truth you cannot admit to yourself."
    if tenth== "sun":
        show 20 at truecenter
        "Sun"
        "The card portends good fortune, happiness, joy and harmony. It represents the universe coming together and agreeing with your path and aiding forward movement into something greater."
    if tenth== "judgement":
        show 21 at truecenter
        "Judgement"
        "This card is referred to as a time of resurrection and awakening, a time when a period of our life comes to an absolute end making way for dynamic new beginnings."
    if tenth== "world":
        show 22 at truecenter
        "The World"
