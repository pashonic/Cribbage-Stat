Cribbage-Stat
=============

Description
-------
<p>I like playing the card game <a href="http://en.wikipedia.org/wiki/Cribbage">Cribbage</a>. I wanted to find out the following:</p>

 *  The average score for a hand during the "Show" play.
 *  Where most of the points come from. 
 
<p>Here is a sample output:</p>
 
``` 
Average Score: 8.1933 
15 Score:      48.67% 
Run Score:     23.01% 
Pair Score:    22.92% 
Flush Score:   3.54% 
Nob Score:     1.86% 
--------- 
Sample Count:  700000 
Run Time:      656.832999945 seconds
```

<p>The above output represents scoring for the "Show" play with a dealt sample count of 700000. Scoring comes from picking 4 best cards (that result in highest score) out of the randomly dealt 6 and counting the score for the 4 cards plus a extra cut-card.</p>

<p>My approach involved making class that represents a set of playing cards which has methods for calucating the cribbage score no matter how many cards there are. You could count the score of entire deck of cards but it would take a very long time.</p>

Restrictions
-------
 *  Python 2.6 to 2.7

Usage
-------
Just Run it...<br>
<b>python CribStat.py</b>