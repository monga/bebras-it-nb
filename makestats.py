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
    "if (!file.exists('img/d-{paese}.png')) {{\\n",
    "options(repr.plot.width=10, repr.plot.height=2)\\n",
    "p <- ggplot(d, aes(x=value))\\n",
    "p <- p + geom_histogram(binwidth=0.1*sd(d$value)) \\n",
    "p <- p + aes(y=..density..)\\n",
    "p <- p + facet_grid(. ~ category)\\n",
    "ggsave(filename = 'img/d-{paese}.png', plot = p, width = 10, height = 2)\\n",
    "rm(p)\\n",
    "}}\\n",
    "summary(d$value)"
   ]
  }},
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "![d-{paese}](img/d-{paese}.png)"
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
    "if (!file.exists('img/a-{paese}.png')) {{\\n",
    "options(repr.plot.width=10, repr.plot.height=2)\\n",
    "p <- ggplot(a, aes(x=value))\\n",
    "p <- p + geom_histogram(binwidth=0.1*sd(a$value)) \\n",
    "p <- p + aes(y=..density..)\\n",
    "p <- p + facet_grid(. ~ category)\\n",
    "ggsave(filename = 'img/a-{paese}.png', plot = p, width = 10, height = 2)\\n",
    "rm(p)\\n",
    "}}\\n",
    "summary(a$value)"
   ]
  }},
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "![a-{paese}](img/a-{paese}.png)"
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
    "if (!file.exists('img/g-{paese}.png')) {{\\n",
    "options(repr.plot.width=10, repr.plot.height=2)\\n",
    "p <- ggplot(g, aes(x=value))\\n",
    "p <- p + geom_histogram(binwidth=0.1*sd(g$value)) \\n",
    "p <- p + aes(y=..density..)\\n",
    "p <- p + facet_grid(. ~ category)\\n",
    "ggsave(filename = 'img/g-{paese}.png', plot = p, width = 10, height = 2)\\n",
    "rm(p)\\n",
    "}}\\n",
    "summary(g$value)"
   ]
  }},
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "![g-{paese}](img/g-{paese}.png)"
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
    "if (!file.exists('img/l-{paese}.png')) {{\\n",
    "data <- data.frame(x=seq(-5,5,.1))\\n",
    "options(repr.plot.width=6, repr.plot.height=6)\\n",
    "p <- ggplot(data, aes(x=x))\\n",
    "p <- p + scale_x_continuous()\\n",
    "p <- p + geom_hline(yintercept=0.5, linetype=\\"dashed\\")\\n",
    "p <- p + geom_vline(xintercept=0.0, linetype=\\"dashed\\")\\n",
    "dall <- data.frame()\\n",
    "for (i in 1:length(d$value)) {{\\n",
    " ldata <- bind_cols(data,  data.frame(a=rep(d$value[i], times=length(data$x)),\\n",
    "                                      b=rep(a$value[i], times=length(data$x)),\\n",
    "                                      c=rep(g$value[i], times=length(data$x)),\\n",
    "                                      category=rep(d$category[i], times=length(data$x))\\n",
    "                                   ))\\n",
    " ldata <- mutate(ldata, y = logistic(x, a, b, c))\\n",
    "  dall <- bind_rows(dall, ldata)\\n",
    "}}\\n",
    " p <- p + geom_point(data=dall, aes(x=x, y=y)) + geom_smooth(data=dall, aes(x=x, y=y))\\n",
    " p <- p + facet_grid(. ~ category)\\n",
    " ggsave(filename = 'img/l-{paese}.png', plot = p, width = 6, height = 6)\\n",
    " rm(data, dall, ldata, p)\\n",
    "}}"
   ]
  }},
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "![l-{paese}](img/l-{paese}.png)"
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

