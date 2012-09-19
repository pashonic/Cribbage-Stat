Cribbage-Stat
=============

Description
-------
<p>I like playing the game <a href="http://en.wikipedia.org/wiki/Cribbage">Cribbage</a> and I wanted to find out what the average score is for a hand and where most of the points come from. Here is a sample output:</p>
 
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

<p>The above output represents scoring for the Show, scoring comes from picking 4 best cards out of 6 and counting the score for the 4 best cards plus a cut-card </p>

<p>I made a class that represents a set of playing cards which has methods for calucating the cribbage score no matter how many cards there are.</p>

Restrictions
-------
 *  Python 2.6 to 2.7

Usage
-------
Just Run it...<br>
python CribStat.py