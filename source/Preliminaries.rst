.. include:: ../rst_prolog.txt


Preliminaries
=============

How I Came To Write This Book
-----------------------------

As I retired in 2005, I began playing bridge online.  The players were no
longer using the Goren system of bidding that I had read about as a child.
Although I had played a small amount of party bridge as an adult I had avoided
bridge after seeing the cream of my class of mathematicians at U.C. Berkeley
flunk out when they played bridge at the Student Union all day and night.  So
then, about to retire, I found myself with only a bare-bones document on
OKBridge to explain this mysterious "Standard American Yellow Card" (SAYC) and
the more advanced extension of it, "Two Over One Game Force", not to mention
the seemingly endless collection of conventions, bids that did not mean what
they appeared to mean.

I set out to remedy the situation for myself.  I soon realized others were in
the same boat, especially people in other countries for whom bridge books were
expensive. So I made it my goal to provide an Open Source book that helps a
bridge player get from intermediate to advanced. I have constantly revised my
set of explanations as my own understanding has grown. 

In 2024 I was fortunate to place in the top 10 in the world in the Realbridge.online 
bidding contest.  I wish my cardplay and defense would keep up!

The Bidding Rules Have Two Branches
-----------------------------------

The first part of this book presents the Two Over One Game Force (2/1) system
that is popular in North America. The more basic Standard American Yellow Card
(SAYC) is subsumed in that system. Here is what I mean.

Let's suppose I deal and I open a heart. The next person passes and you, my partner,
bid two diamonds.  You have made a two-level bid over my higher-ranked suit. In the
2/1 system, that bid promises an opening hand, which means that together we have 
enough points for game.  Hence we are in a "game-forcing" auction, meaning that 
neither of us can pass short of 3N or a four-level bid.

By contrast, suppose you deal and pass, and the next opponent passes. I bid a heart,
and you reply two diamonds. You already passed, so you cannot have an opening hand,
and so your bid cannot "force to game".  Obviously, whatever our bidding rules are
going to be in this situation, they have to be different now. As it happens, the rules
we will use are the older SAYC set of rules that historically preceded the adoption 
of 2/1. We also need to use those rules when the opponent to the left of the opener 
makes a bid before the responder can speak.

You will still find people playing SAYC. The predecessor to that was "Goren",
the system popularized by Charles Goren and that I learned as a child 70 years ago.
The name SAYC originated in a convention card the American Contract Bridge
League (ACBL) created for an event in which everyone was to play the same
convention card. Apparently the sample cards were yellow in color.
Few people play SAYC as it was written. In cases where the standard is
sometimes or often ignored, I'll point that out. 


How to Use This Book
--------------------

You can use this book for initial learning, or as a reference. For that reason
it has an index. It frustrates me no end that most bridge books do not. There
is also a glossary of bridge terms. In electronic manifestations of this book,
there are many operable links in the text. What this book lacks is the kind of
things that are in good books written by professionals: extensive examples, and
quizzes. I list some of my favorite sources in :ref:`Resources <bibliography>`.

Bridge has three big topics: bidding, declarer play, and defense. An expert
friend who has read my notes commented that the defensive part of your
notes ought to be as big as the bidding section. Indeed, your side is on
defense half of the time. Few of us measure up -- for some reason, learning
another convention that comes up twice a year is more compelling than the
basics of carding that happens on every hand.

While I want to present the major conventions so you will know what your
opponents are up to, do not take this as advice to master them, rather than
spending equal time on the other two-thirds of bridge.

.. _expected_conventions:

.. index::
   pair:convention;expected with 2/1
   
Here's a guide to what follows. First we cover 2/1's key bids, competitive
bidding, and basic slam bidding. The 2/1 system really has two
parts: the two-over-one and 1N-forcing bids and their followups; and this set of
expected conventions:

- :ref:`Reverse Drury <Reverse_Drury>`,
- :ref:`Fourth Suit Forcing <FSF>`,
- :ref:`New Minor Forcing <NMF>`, 
- :ref:`Inverted Minors <inverted_minors>`, and
- :ref:`Roman Keycard Blackwood <RKC>`.

There is no real connection between the 2/1 bids and this set of conventions except that
most players of 2/1 also play those conventions.  As you are learning you'll
need to tell potential partners which of these conventions you haven't mastered
yet. Fourth Suit Forcing and New Minor Forcing are so close in spirit that you
should learn them at the same time. Roman Keycard Blackwood is likely to be
high on the want list from your partner.

.. warning::
   Do not agree to play a convention unless you have a solid knowledge of it, including
   not just the initial bids but the followups, including what to do if the opponents
   interfere.  Everyone now and then fails to recognize that a bid is conventional,
   both when they make it and when partner makes it, but each such error cancels out
   a year's worth of benefits from playing it.

I believe that new players should learn 2/1 from the beginning, adding in the
conventions just mentioned ASAP. You have to learn the SAYC meanings as well,
since they apply when opener is a passed hand or there is interference. That's
the approach we're taking here.

There are many aspects of bidding, including the vital areas of competing for
part scores and making game tries, that are not explicitly in these systems at
all. 

Until we get to the Advanced chapters, I will not present many alternative ways of
doing things.  I didn't like, when I was learning, books that said I could do this or
that, when I had no basis in experience to make an informed choice.

Casual Partners
---------------

Even a person with the most dedicated partner plays with someone else once in a
while; this is especially true online. Therefore, you have to learn two things:
your system, and the system you can count on a stranger to know. For casual
face-to-face play, an intermediate pair who agrees on SAYC or 2/1 still needs
to fill in some details as they fill out the card.

I like to be in a position to say, "Let's play your card"; armed with this
book, you'll know what most of their stuff means already. My philosophy is that
this way, at most one person is confused: me.

Many online sites have a definition somewhere of one or more  systems that you
can expect people to use there -- but frankly not many people bother to read
them.

If you are learning to play using robots online, be sure to check what the
robot thinks bids mean. None of the various robots play vanilla systems.

Contributing
------------

I encourage others to help me build a community resource by furnishing corrections and 
additions. The source for the book is written in "reStructuredText" and uses a system 
called  "Sphinx" to render the book into web pages, e-books and PDF files. 

Sphinx is the standard system used to document computer programs written in the popular
Python computer language, so it is heavily used, is free, and has the advantage that 
the source is a simple, readable text file with a very natural markup system.  

Send corrections by indicating section and nearby content, rather than by
page number, as the latter depends on the rendering device, unless using the PDF. 
Since the book is revised fairly often, the only "versioning" I am doing is the date, 
so please include that date (visible near the top of the opening page in the web version)
with your corrections.

You can contribute additions such as examples and quizzes for chapters
by sending a plain text file. Extra points for using reStructuredText markup. 
Use Bridge Books in the subject and mail to me at ``pfdubois@gmail.com``.

Acknowledgments
---------------

Thank you to my long-time teacher, Mike Moss, who taught me almost everything I
know. Lately I have greatly profited by taking lessons from Marc Smith. I have
also learned from expert players including Marty Bergen, Rob Barrington, Gavin
Wolpert, Howard Schutzman, Oliver Clarke, Alex Martelli, and Jim and Pat Leary;
and received encouragement from my fellow learners and partners, especially
Douglas Schmickrath, David Silberman, Julia Beatty, Ally Whiteneck, and John
Engstrom.

I am definitely a #Gavinista. Gavin's set of video lessons at wolpertbridge.com covers 
everything; if you learn better from people than from books, this might be the best 
path for you.

About The Author
----------------

I am a retired mathematician and computational scientist. I founded the first successful
system for computational steering in 1984, which has become the main way scientific 
computation is done now. My professional biography is available, along with this book, at 
https://pfdubois.com. 


