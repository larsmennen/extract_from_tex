# Extract from tex

Small command-line Python application to extract theorems, definitions, lemmas, etc. from a LaTeX file (by using regular expressions) and write them to a CSV file.

## Installation

You need Python >= 3.5 installed.

```bash
pip install git+https://github.com/larsmennen/extract_from_tex
```

## Example usage

Let's say you have the following file `input.tex`:

```latex
\documentclass{article}
\usepackage{amsmath,amssymb}
\usepackage{amsthm}
\usepackage{thmtools}

\declaretheoremstyle[
spaceabove=6pt, spacebelow=6pt,
headfont=\normalfont\bfseries,
notefont=\mdseries, notebraces={(}{)},
bodyfont=\normalfont,
postheadspace=1em,
numberwithin=section
]{exstyle}
\declaretheoremstyle[
spaceabove=6pt, spacebelow=6pt,
headfont=\normalfont\bfseries,
notefont=\mdseries, notebraces={(}{)},
bodyfont=\normalfont,
postheadspace=1em,
headpunct={},
qed=$\blacktriangleleft$,
numbered=no
]{solstyle}
\declaretheorem[style=exstyle]{example}
\declaretheorem[style=solstyle]{solution}
\declaretheorem{theorem}
\declaretheorem{thm}
\declaretheorem{definition}

\begin{document}
	
	\section{Test section}
	
	text text text
	\begin{example}
		text text text
	\end{example}
	text text text
	
	text text text
	\begin{solution}
		text text text
	\end{solution}
	text text text
	
	\begin{theorem}
		Bla bla
	\end{theorem}
	
	\begin{thm}[name=Infinity theorem,label=thm:infinity]That's a long theorem.\end{thm}
	
	\begin{definition}[My definition]My definition of \LaTeX    \end{definition}
	
\end{document}
```

Then simply run:
```bash
extract_from_tex input.text output.csv
```
which should show:
```
Found 2 valid elements of type theorem.
Found 1 valid elements of type definition.
Found 0 valid elements of type corollary.
Found 0 valid elements of type lemma.
```
and `output.csv` should be:
```
theorem;;Bla bla
theorem;Infinity theorem;That's a long theorem.
definition;My definition;My definition of \LaTeX 
```