# Declare characters

define c = Character("YOU")
define m = Character("MOM")
define d = Character("DAD")
define f = Character("ALICE")
define ls = Character("LITTLE BROTHER")
define n = Character("NEIGHBOR")
define t1 = Character("MS. FLORE")
define t2 = Character("MR. WILLIAMS")

# The game starts here.

label start:
    play music "audio/Music/rainy.mp3"
    scene bg sky with fade

    "The sun shone brightly in the sky as the sound of birds chirping filled the
    air."
    "Silence filled the street as many people were still sleeping. It was early
    in the morning."
    "Today is the start of a brand new day. You wondered what awaits."

    "Ready to start your day?"

    menu:
        "Yes":
            jump yes
        "No":
            jump no

label no:

    "It is midterms week and you know that skipping your classes will affect
    your performance on your exams."
    "Your parents will definitely be against the idea of you skipping for sure.
    They care a lot about your academics and have high expectations of you. You
    don’t want to disappoint them."
    "In other words, you have no other choice."

    menu:
        "Start the day":
            jump yes

# Scene 1 : Intro
label yes:

    "Let's begin!"

    scene bg bedroom with fade
    show clock 7pm

    show happy you at top

    "You wake up with full energy."
    "Surprisingly, you were able to get decent sleep the night before, a rare
    occurrence."
    "You did not have much planned for today except to review and study for your
    math midterm which you have to take tomorrow morning."
    "You want to utilize all the time you have since there is still material that
    you don’t understand and your grade for the class…isn’t looking the best."

    hide happy you

    menu:
        "Check Task List":
            jump taskExam

        "Next":
            jump Scene2

    stop music

label taskExam:
    show task exam
    pause 1.0

    menu:
        "Close Task List":
            jump Scene2

# Scene 2 : Getting Ready
label Scene2:

    scene bg bathroom with fade
    show clock 7pm
    show happy you at top

    "You got yourself out of bed and went to the bathroom."
    "You quickly brushed your teeth, washed your face, and changed to your
    school uniform before heading downstairs to the kitchen."
    "Another day of decisions. Another day of uncertainties."
    "You became a bit nervous, not knowing what to expect."

    hide happy you

    menu:
        "Head downstairs to the kitchen":
            jump Scene3

# Scene 3: Kitchen
label Scene3:

    scene bg kitchen with fade
    show clock 7pm

    "As you make your way to the kitchen, your mom comes and greets you."
    "Your dad is drinking coffee at the table, reading his newspapers as usual."
    "Your little brother was already awake and eating his breakfast."

    show happy mom at top
    m "Good morning! How was your sleep?"
    hide happy mom

    show happy you at top
    c "Good morning. It was okay."
    hide happy you

    show happy mom at top
    m "That's good to hear! You'll need enough energy for your midterms this
    week."
    hide happy mom

    "Hearing the mention of “midterms,” your dad looks up from his newspapers
    and directs his eyes at you."

    show dad at top
    d "How is studying coming along?"
    hide dad

    show unsure you at top
    c "Uhh...it's going okay."
    hide unsure you

    show dad at top
    d "Your grade in your math class isn’t doing so well, is it? You better use
    all of your time to study and pass the midterm. I’m expecting you to get
    high marks."
    hide dad

    show unsure you at top
    c "Yeah, I know."
    hide unsure you

    show happy mom at top
    m "Breakfast is already ready on the table. Eat up so you’ll have enough
    energy to study!"
    hide happy mom

    "Your parents both care deeply about your academic life and tend to push
    their ideals onto you. You’re used to it though and have always just
    listened to them. You wanted to be a good daughter and make them proud after
    all."

    show happy you at top
    c "Thank you, mom."
    hide happy you

    "As you finish up your breakfast and prepare to leave, your mother stops you
    and asks for a favor."

    show happy mom at top
    m "Can you come home early today to cook dinner for your little brother?
    Dad and I are going to be busy with work and won’t be home until late.
    I went grocery shopping earlier so there are a lot of ingredients in the
    fridge."
    hide happy mom

    menu:
        "Agree to cook dinner":
            jump yesCook
        "Tell her you are busy":
            jump noCook

    stop music

label noCook:
    play music "audio/Music/help.mp3"

    show sad mom at top
    m "I really can’t come home early at all. Just cook something simple and then
    you can go back to your studies. I’m sorry for asking you so suddenly but
    you would help me out a lot."
    hide sad mom

    show you shadow at top
    "You see your mom sigh in frustration. Clearly, she is stressed with work."
    "You start to feel bad for declining her request."
    "It is just cooking dinner. It shouldn’t take too much time. Surely, you can
    do this for your mom right? You’re the big sister after all, you should take
    care of your sibling. It would help your parents out a lot."
    "What kind of daughter would you be if you can’t even help with something as
    simple as this?"
    hide you shadow

    show happy you at top
    c "Actually, I can help cook dinner. You don't have to worry about it."
    hide happy you

    menu:
        "Agree to cook dinner":
            jump yesCook

    stop music

label yesCook:

    show happy mom at top
    m "Thank you so much! Have a good day at school!"
    hide happy mom

    "You feel a sense of joy knowing that you were able to help out your mom."

    jump updateTask1

label updateTask1:
    play music "audio/Music/help.mp3"

    scene bg black with fade

    "A new task has been added to your Task List."

    menu:
        "Check Task List":
            jump taskDinner

label taskDinner:
    show task dinner
    pause 1.5

    menu:
        "Close Task List":
            jump Scene4

    stop music

# Scene 3 : School
label Scene4:
    play music "audio/Music/rainy.mp3"

    scene bg classroom1 with fade
    show clock 8pm

    "You arrived at school just in time and made your way to your first class
    as the late bell rings. It was your art class."
    "The sound of chatter and laughter fills your ears as you open the classroom
    door and walk in."
    "Your friend Alice waves at you with a smile as you sit down at your desk."

    show happy alice at top
    f "Good morning! You actually came to school on time today."
    hide happy alice

    "You rolled your eyes at her as you began to take out your sketchbook and art
    tools."
    "She wasn’t wrong though. You haven’t been getting a lot of sleep due to
    studying which results in you oversleeping in the morning."
    "Today was just a rare day that you actually woke up on time and had energy."

    show happy alice at top
    f "What do you have planned today?"
    hide happy alice

    show unsure you at top
    c "I have to go home early to cook dinner and then just study all evening
    for the math midterm tomorrow."
    hide unsure you at top

    show happy alice at top
    f "Oh yeah, the math midterm is tomorrow. I almost forgot. I bet you’ve
    already started studying for it huh?"
    hide happy alice

    show unsure you at top
    c "Yeah…my dad has been nagging at me nonstop to study. I barely have time
    for anything else."
    hide unsure you at top

    show happy alice at top
    f "Yeah I can see that. You always go straight home after school so you
    never get to hang out with everyone. I can’t even remember the last time we
    hung out!"
    hide happy alice

    stop music

    play music "audio/Music/help.mp3"
    show you shadow at top
    "It really has been a while since you hung out with your friends. It’s not
    like you didn’t want to. You couldn’t."
    "Your parents are strict about how you choose to spend your spare time. They
    expect you to go straight home after school so that you can focus on your
    studies. As a result, you rarely have time to do things that you want and
    enjoy."
    "Even though it makes you sad, there is nothing you can do about it. You
    need to abide by your parents’ rules since you are a good daughter and your
    parents’ opinions matter to you."
    hide you shadow
    stop music

    play music "audio/Music/rainy.mp3"
    show happy alice at top
    f "I was going to ask if you wanted to come with everyone to the new dessert
    shop that opened last week but I guess you can’t because you have to go home
    and cook dinner right? Maybe next time?"
    hide happy alice

    show unsure you at top
    c "Yeah…sorry I won’t be able to join. Hopefully next time."
    hide unsure you at top

    "For a second, you felt really sad. You actually really wanted to join your
    friends because it sounded like fun."

    show happy alice at top
    f "Sounds good! Anyways! It seems like you’re mostly free for today so can
    I ask you for a favor?"
    hide happy alice

    "You start becoming a bit anxious. Is this another task?"

    show unsure you at top
    c "What is it?"
    hide unsure you at top

    show happy alice at top
    f "You know that group project for biology class? I know I still have to
    finish my part for the powerpoint but I have really important plans today
    and I don’t think I can finish it by tonight. Can you please just finish it
    for me? Obviously, I will still present it."
    hide happy alice

    "You think for a bit. If you decide to help finish Alice’s part, that means
    you would have to do more research and spend time finalizing the entire
    presentation."
    "It will definitely take some time and you still have to study for your math
    midterm, which you know you need a decent amount of time for."
    "Regardless, the project has to be completed by tonight or your grade will
    be affected. Presentations are tomorrow, after all."
    "Your mind races as you try to make your decision."

    menu:
        "Agree to finish Alice's part for the project":
            jump yesAlice
        "Tell Alice you're busy":
            jump noAlice

    stop music

label yesAlice:

    show happy alice at top
    f "You're the best! I owe you one!"
    hide happy alice

    jump taskUpdate2

label noAlice:
    play music "audio/Music/help.mp3"
    show sad alice at top
    f "We’ve been friends for so long! Why can’t you just help me a little? You
    don’t even have that much planned today, unlike me. Can’t you just do it?
    You’ll be doing me a huge favor!"
    hide sad alice

    show you shadow at top
    "You sigh and look down at the desk. Now you feel bad and guilty for
    deciding not to help Alice."
    "Maybe Alice is right. Maybe you aren't being a good friend."
    "You don't have that much planned today besides cooking dinner and
    studying for the math exam. She did say her plans were important."
    "Surely, you can take some time out to finish up the project and help her out.
    That's what a good friend would do right? You wanted to do whatever you can to
    support and help her."
    "It will probably just take you an hour to finish everything. You should
    have enough time to study for your math exam."
    hide you shadow

    show unsure you at top
    c "Actually, I can help."
    hide unsure you

    menu:
        "Agree to finish Alice's part for the project":
            jump yesAlice

label taskUpdate2:
    play music "audio/Music/help.mp3"
    scene bg black with fade

    "A new task has been added to your Task List."
    "Was it so hard to say no?"

    menu:
        "Check Task List":
            jump taskAlice

label taskAlice:
    show task alice
    pause 2.0

    menu:
        "Close Task List":
            jump Scene5

    stop music

# Scene 5 : Art Teacher
label Scene5:
    play music "audio/Music/rainy.mp3"
    scene bg classroom1 with fade
    show clock 10pm

    "You stared blankly at the painting in front of you until you realized that
    class had already ended and you were the last student in the room."
    "You packed up your supplies and began to head out the door when your art
    teacher suddenly stopped you."

    show happy flore at top
    t1 "Hey! Can I talk to you for a minute?"
    hide happy flore

    show unsure you at top
    c "What is it, Ms. Flore?"
    hide unsure you

    show happy flore at top
    t1 "Our school is participating in an art competition and the student who
    wins the most votes from judges will be able to have their art featured in
    the art gallery!"
    t1 "I wanted to let you know and ask if you wanted to participate! Your
    artworks are marvelous and you definitely have the potential! Are you
    interested?"
    hide happy flore

    play music "audio/Music/help.mp3"
    show you shadow at top
    "You think for a bit."
    "You had always loved art and it was one of your dreams to become a freelance
    artist in the future."
    "This is such a good opportunity for you to possibly have your artwork
    featured in an art gallery. So many people would be able to see your work!
    This was almost like a dream come true."
    "However, you knew your parents would never agree to this. They believed that
    being a freelance artist is a waste of time and is not a career with a stable
    income."
    "In their minds, occupations such as a doctor, lawyer and computer scientist
    are the most promising. Therefore, they have high expectations of you and
    expect you to excel in your academics in order to reach those positions."
    "Because of their focus on academics, your parents have not allowed you to
    join any extracurricular activities and even limited the time you can spend
    with your friends."
    "Your parents are also constantly busy with work and you often have to take
    care after your siblings. As a result, your social life has been negatively
    affected and you have missed out on a lot of opportunities and experiences."
    "Rather than rebelling or defying your parents, you decided to listen to your
    parents and live up to their expectations. You want to be a good daughter
    and make them proud."
    "Family has always been first and you were raised with the belief that your
    sense of duty is to assist your family members and consider their needs."
    "Therefore, you knew that if you spent your time working on the artwork for
    the competition, your parents would have an issue with it. They would rather
    you spend that time studying and working harder on your academics. And you
    will be too busy taking care of your siblings to draw anyways."
    "Despite it being your ultimate dream, maybe being a freelance artist just
    wasn’t meant to be for you."
    "You looked at Ms. Flore and shook your head."
    hide you shadow

    show sad you at top
    c "I’m sorry but I might have to back out of this one. I need to focus more
    on my studies and I don’t think I’ll have time to work on an artwork for the
    competition. Thank you for asking me and letting me know though, Ms. Flore."
    hide sad you

    show sad flore at top
    "Ms. Flore looked a bit disappointed but nodded her head with a smile."
    hide sad flore

    stop music

    play music "audio/Music/rainy.mp3"
    show happy flore at top
    t1 "That’s fine! I completely understand. The deadline for the competition
    is in about a month so you have plenty of time if you decide to change your
    mind!"
    hide happy flore

    show sad you at top
    c "Okay, got it. Thank you."
    hide sad you

    show happy flore at top
    t1 "Of course!"
    hide happy flore

    "You planned to go to the vending machine in the cafeteria to get some snacks
    before going to your next class. You knew you were going to feel hungry later
    and you needed something to replenish your energy. As you begin to walk towards
    the door, Ms. Flore stops you."

    show happy flore at top
    t1 "Oh! Before you go, do you mind dropping off this folder to Mr. Williams?
    I have to get these grades in by the end of today so I have my hands full.
    You can find his room on the third floor."
    hide happy flore

    "You knew for sure that you won’t be able to buy your snack if you decide to
    help Ms. Flore out. You wouldn’t make it to your next class on time."
    "Which is more important to you? Replenishing your energy or being helpful
    to your teacher?"

    menu:
        "Agree to help Ms. Flore":
            jump yesFlore
        "Tell Ms. Flore you're busy":
            jump noFlore

label yesFlore:
    show happy flore at top
    t1 "Thank you so much! I appreciate it help!"
    hide happy flore

    jump taskUpdate3

label noFlore:
    play music "audio/Music/help.mp3"
    show sad flore at top
    t1 "Oh, is that so? I was hoping you could help me out really quick. But,
    it’s okay! I should’ve planned ahead of time and delivered it myself. It’s
    just been quite busy for me, you know?"
    hide sad flore

    show you shadow at top
    "You start to feel bad."
    "It's not like you desperately needed the snack. It was just something you
    wanted to give yourself some energy."
    "Surely, you can power through the day and sacrifice a bit."
    "Ms. Flore has helped you out a lot in this class and you wanted to return
    the favor by helping her out. It was just delivering papers, nothing difficult."
    "She will definitely appreciate you more if you help."
    hide you shadow

    show unsure you at top
    c "Actually, I can help you Ms. Flore."
    hide unsure you

    menu:
        "Agree to help Ms. Flore":
            jump yesFlore

label taskUpdate3:
    play music "audio/Music/help.mp3"
    scene bg black with fade

    "A new task has been added to your Task List."
    "Was it so hard to say no?"

    menu:
        "Check Task List":
            jump taskWilliam

label taskWilliam:
    show task william
    pause 2.5

    menu:
        "Close Task List":
            jump Scene6

    stop music

label Scene6:
    play music "audio/Music/rainy.mp3"
    scene bg hallway with fade
    show clock 10pm

    "You take the folder and walk upstairs to the third floor. You have decided
    to give up your snack since there is only a few minutes to transition between
    your classes. You will not have enough time. You walked down the hallway and
    into the literature room."

    jump Scene7

# Scene 7 : William
label Scene7:
    scene bg classroom2 with fade
    show clock 10pm

    "As you enter the classroom, Mr. Williams greets you with a smile."

    show happy williams at top
    t2 "Hi! How can I help you?"
    hide happy williams

    show unsure you at top
    c "Hi Mr. Williams. I’m here to drop off some papers from Ms. Flore."
    hide unsure you

    show happy williams at top
    t2 "Oh that’s right! I was supposed to get those from her but I got busy
    reparing for my semester plans."
    t2 "I’m guessing she also got busy seeing you’re the delivery person, huh?
    Anyways, thank you so much! Enjoy the rest of your day!"
    hide happy williams

    "How does he appear to have so much energy? I'm already exhausted and the
    day has only just begun."

    show happy you at top
    c "You’re welcome. I hope you enjoy the rest of your day too, Mr. Williams."
    hide happy you

    "You walk out of the classroom and close the door behind you as you make your
    way down to your next class."
    "You let out a sigh of relief since Mr. Williams did not request anything
    from you."
    "Knowing you, you would have probably accepted yet another task."

    jump taskUpdate4

label taskUpdate4:
    scene bg black with fade

    "No new task has been added."
    "But that's because no one asked you to do anything for them this time."

    jump Scene8

# Scene 8 : End School
label Scene8:
    scene bg school with fade
    show clock 5pm

    "You finally finished all your classes. It has been a long day and you’re
    exhausted."
    "However, you still have much to do from your Task List."
    "It is already 5pm and you have to go back home to cook dinner."

    jump Scene9

# Scene 9: Neighbor
label Scene9:
    scene bg street with fade
    show clock 5pm

    "On your way home, you walked past the convenience store. As you turn the
    corner, you bump into your elderly neighbor who was walking her dog."

    show happy neighbor at top
    n "Oh my, you surprised me! Are you just coming back from school?"
    hide happy neighbor

    show unsure you at top
    c "Yes, I’m heading home right now. I have to cook dinner for my little
    brother because my parents are coming late from work tonight."
    hide unsure you

    show happy neighbor at top
    n "What a good child! And good timing! I was just walking my dog, Rosie.
    But I need to buy something from the convenience store and I completely
    forgot that pets aren't allowed in! Do you mind helping me watch after Rosie
    for a bit? I won’t take long!"
    hide happy neighbor

    "You noticed the sky getting darker. You should really be heading home soon."
    "You still have to cook, finish up Alice's part of the project and study for
    the math exam. The time you have remaining is running out."
    "What should you do? Help out your neighbor or go home and focus on your tasks?"

    menu:
        "Help out your elderly neighbor":
            jump yesNeighbor
        "Tell your neighbor you're busy":
            jump noNeighbor

label yesNeighbor:
    show happy neighbor at top
    n "Thank you so much!"
    hide happy neighbor

    jump taskUpdate5

label noNeighbor:
    play music "audio/Music/help.mp3"

    show sad neighbor at top
    n "Oh really? Darn...I really wanted to buy the fresh strawberries today. I
    guess I will have to wait until tomorrow."
    n "I was planning to make some strawberry tarts for my husband since it is his birthday tomorrow and
    strawberries are his favorite fruit."
    n "I guess I will just have to wake up earlier to buy it..."
    hide sad neighbor

    show you shadow at top
    "You felt bad for declining her request after hearing that."
    "Your neighbor and her husband have always been friendly to you and your
    family since you've moved in. They definitely have helped a lot."
    "You were also taught to treat your elders with respect so not offering to
    help her might make you appear rude."
    "You should return the favor after all that they have done for you. You want
    to maintain a good relationship with them."
    "It shouldn't be too much of a problem to look after Rosie. Surely, you can
    help out."
    hide you shadow

    show unsure you at top
    c "Actually, I can help."
    hide unsure you

    menu:
        "Help out your elderly neighbor":
            jump yesNeighbor

label taskUpdate5:
    play music "audio/Music/help.mp3"
    scene bg black with fade

    "A new task has been added to your Task List."
    "Was it so hard to say no?"

    menu:
        "Check Task List":
            jump taskDog

label taskDog:
    show task william2
    pause 3.0

    menu:
        "Close Task List":
            jump Scene10

# Scene 10: Street Wait
label Scene10:
    play music "audio/Music/help.mp3"
    scene bg street with fade
    show clock 520pm

    "You fidget around as you continue to wait for your neighbor to come out. It
    has already been 20 minutes and you haven't seen her."
    "You began to grow agitated since you could've been home, working on your
    assignments right now."
    "But, you shouldn't complain. You did this to yourself. You made the decision."
    "After waiting a few more minutes, your neighbor finally came out."
    stop music

    play music "audio/Music/rainy.mp3"
    show happy neighbor at top
    n "I’m so sorry, that took a bit longer than I expected! Thank you for
    looking after Rosie. I'll make sure to give you some of the strawberry tarts
    tomorrow for your help! Get home safely and have a good night!"
    hide happy neighbor

    "Seeing her carrying the two grocery bags, you decided to help out. It would
    be difficult for her to carry the bags and hold the leash for her dog at the
    same time. You wanted to be respectful and you were walking the same way
    anyway."

    show unsure you at top
    c "I’ll go ahead and walk you home, those grocery bags must be heavy. I’ll
    carry them for you."
    hide unsure you

    show happy neighbor at top
    n "Why, thank you! You are such a good child, indeed!"
    hide happy neighbor

    "You carried the grocery bags and walked your elderly neighbor back to her
    house."
    "After dropping her off, you headed back to your own house. It was getting
    colder and the sky was now pitch black. You are completely exhausted...but
    you still have more to do."

    jump Scene11

# Scene 11 : Kitchen Late
label Scene11:
    scene bg kitchen with fade
    show clock 7pm

    "At last, you finally arrived home."
    "Your little brother was sitting on the couch, watching TV."

    show brother at top
    ls "Welcome back! I’m starving!"
    hide brother

    show unsure you at top
    c "I’ll go cook some fried rice with soup on the side. Wait for a few minutes, okay?"
    hide unsure you

    show brother at top
    ls "Okay!"
    hide brother

    "You cooked dinner and called your little brother to come eat. That took you
    about half an hour and it was already 7PM."
    "After you both finished eating, you washed the dishes and cleaned up after
    him. After everything was cleaned up, you went upstairs to the bathroom to
    wash up."

    jump Scene12

# Scene 12: Bedroom Study
label Scene12:
    scene bg bedroom with fade
    show clock 8pm

    "After you showered, you checked the time and was surprised to see that it
    was already 8 PM."
    "You immediately start to work on Alice’s part of the project."
    "An hour passed and you are still working on the project."
    "You can feel yourself growing extremely lethargic. Your eyes have been
    struggling to stay open and your stomach would not stop growling since you
    skipped dinner and didn't have a snack today. All you want to do is sleep."
    "But, you have to finish this project by tonight. No exceptions."

    pause 1.5

    "3 hours later..."
    show clock 11pm with fade

    pause 0.5

    "You finally finished Alice’s part and finalized the entire project."
    "You stretched and looked at the time. It was now 11 PM."
    "That took you way longer than you expected."

    jump taskUpdateFinal

label taskUpdateFinal:
    scene bg black with fade

    menu:
        "Check Task List":
            jump taskLast

label taskLast:
    show task last
    pause 3.0

    menu:
        "Close Task List":
            jump Scene13

label Scene13:
    play music "audio/Music/help.mp3"
    scene bg bedroom with fade
    show clock 11pm

    "Isn’t it funny?"
    "You started off the day with only one task to do: studying for your math exam."
    "But how did it end up being the last one that is still not complete?"
    "You can feel your body growing weak. The energy that you had started the day
    with has long depleted. You knew you needed sufficient time and energy to
    study for your math exam today. Was it so hard to say no to other people’s
    requests?"
    show shadow one at top
    "Well…for the most part, you couldn’t help but to agree because you are a
    filial daughter. The idea of filial piety is the devotion or
    respect that you would present to your parents or elders."
    hide shadow one
    show shadow two at top
    "You’ve been this way all your life. Helping your parents out while
    sacrificing your own needs and dreams."
    "Despite being in high-school, you’ve never joined any clubs before and you
    barely have time to hang out with your friends. You always spent your time
    either studying or looking after your little brother because your parents are
    often busy with work."
    hide shadow two
    show shadow three at top
    "Even when it’s not family, you tend to feel “forced” to help out elders or
    those who are older than you out of respect. It is what you have been taught
    to do all your life, after all."
    hide shadow three
    show shadow four at top
    "It has always been family first…and you are too afraid to say no."
    "Saying no would have made you feel guilty and bad. But why?"
    "Why is it so hard to say no? Why do you tend to put others first?"
    hide shadow four
    show shadow five at top
    "Is it because you don’t want to appear disrespectful? Do you feel as if
    it’s your duty?"
    "Is it because you don’t want to disappoint others or hurt their feelings?
    Fear of conflict?"
    "Is it because you want to feel accepted and a sense of belonging in the
    community? Is it because you genuinely want to help them?"
    hide shadow five
    show shadow six at top
    "But to what extent and at what expense?"
    "You feeling stressed out? Burnt out? Your mental and physical health
    deteriorating? Neglecting your own needs?"
    hide shadow six
    show shadow seven at top
    "Your social life has deteriorated and you cannot work towards a future that
    you want because of your acts of filial piety and your focus on others."
    hide shadow seven
    show shadow eight at top
    "Finding a balance between helping others and tending to your own needs is
    important. You need to learn to put yourself first. You need to decide what
    is best for you."
    "But today, you did not find that balance. You are completely burnt out.
    Exhausted. And you missed a good opportunity that would’ve helped you towards
    the career that you wanted in the future."

    pause 1
    hide clock 11pm
    show clock 12am

    hide shadow eight
    show shadow nine at top
    "It is now 12:00 AM."
    "You still can’t take a break. You still need to study for your math exam."
    hide shadow nine

    pause 1

    show you shadow at top

    menu:
        "Pass Out":
            jump endScreen
        "Pass Out":
            jump endScreen
        "Pass Out":
            jump endScreen
        "Pass Out":
            jump endScreen
        "Pass Out":
            jump endScreen

label endScreen:
    "The End."
