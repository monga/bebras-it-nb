#!/usr/bin/python
# -*- coding: utf-8 -*-

STAT="""
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "###  {titolo}\\n",
    "\\n",
    "![{nome}](screenshot/{file})"
   ]
  }},
  {{
   "cell_type": "code",
   "execution_count": null,
   "metadata": {{
    "collapsed": false
   }},
   "outputs": [],
   "source": [
    "q <- '{paese}'\\n",
    "d <- quiz_difficulty %>% dplyr::filter(bebras_id == q) %>% select(value, category)\\n",
    "a <- quiz_discrimination %>% dplyr::filter(bebras_id == q) %>% select(value, category)\\n",
    "g <- quiz_guessing %>% dplyr::filter(bebras_id == q) %>% select(value, category)"
   ]
  }},
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "#### Difficoltà"
   ]
  }},
  {{
   "cell_type": "code",
   "execution_count": null,
   "metadata": {{
    "collapsed": false
   }},
   "outputs": [],
   "source": [
    "options(repr.plot.width=10, repr.plot.height=2)\\n",
    "p <- ggplot(d, aes(x=value))\\n",
    "p <- p + geom_histogram(binwidth=0.1*sd(d$value)) \\n",
    "p <- p + aes(y=..density..)\\n",
    "p <- p + facet_grid(. ~ category)\\n",
    "p\\n",
    "summary(d$value)"
   ]
  }},
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "#### Differenziazione"
   ]
  }},
  {{
   "cell_type": "code",
   "execution_count": null,
   "metadata": {{
    "collapsed": false
   }},
   "outputs": [],
   "source": [
    "options(repr.plot.width=10, repr.plot.height=2)\\n",
    "p <- ggplot(a, aes(x=value))\\n",
    "p <- p + geom_histogram(binwidth=0.1*sd(a$value)) \\n",
    "p <- p + aes(y=..density..)\\n",
    "p <- p + facet_grid(. ~ category)\\n",
    "p\\n",
    "summary(a$value)"
   ]
  }},
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "#### Guessing"
   ]
  }},
  {{
   "cell_type": "code",
   "execution_count": null,
   "metadata": {{
    "collapsed": false
   }},
   "outputs": [],
   "source": [
    "options(repr.plot.width=10, repr.plot.height=2)\\n",
    "p <- ggplot(g, aes(x=value))\\n",
    "p <- p + geom_histogram(binwidth=0.1*sd(g$value)) \\n",
    "p <- p + aes(y=..density..)\\n",
    "p <- p + facet_grid(. ~ category)\\n",
    "p\\n",
    "summary(g$value)"
   ]
  }},
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "#### Curva Item-Response"
   ]
  }},
 {{
   "cell_type": "code",
   "execution_count": null,
   "metadata": {{
    "collapsed": false
   }},
   "outputs": [],
   "source": [
    "data <- data.frame(x=seq(-5,5,.1))\\n",
    "options(repr.plot.width=6, repr.plot.height=6)\\n",
    "p <- ggplot(data, aes(x=x))\\n",
    "p <- p + scale_x_continuous()\\n",
    "p <- p + geom_hline(yintercept=0.5, linetype=\\"dashed\\")\\n",
    "for (i in 1:length(d$value)) {{\\n",
    "  p <- p + geom_line(aes(y=logistic(x, a=d$value[i], b=a$value[i], c=g$value[i])))\\n",
    "}}\\n",
    "p"
   ]
  }},
"""

import glob, sys

OFFSET = {"kilo": 0, "mega": 5, "giga": 10, "tera": 15, "peta": 20}

with open("qnames.R") as names:
    pars = {}
    for n in names:
        for a in n.split(','):
            for b in a.split("'"):
                for c in b.split('"'):
                    if '2015' in c:
                        pars['titolo'] = c.strip()
                        pars['nome'] = pars['titolo'].split('_')[4]
                        pars['paese'] = pars['titolo'].split('_')[3]
                        cat = pars['titolo'].split('_')[1].lower()
                        key = 5*(ord(pars['titolo'].split('_')[2][0]) - ord('A')) + int(pars['titolo'].split('_')[2][1]) - OFFSET[cat]
                        key = cat + "%02d" % key
                        files = glob.glob("./screenshot/" + key + "-*")
                        if len(files) == 1:
                            pars['file'] = files[0].split("/")[2]
                            print STAT.format(**pars)
                        elif len(files) > 1:
                            print files
                            assert(False)

