# A script to sort through the ISBNs in books3
## What this repo contains
This repo has simple scripts in it to clean the ISBNs in the books3 database and filter them by the country each ISBN is registered to. At the moment all it does it list the Norwegian ISBNs. I would like to expand this so we can visualise the distribution of books by the country the ISBN was registered in (I assume the books are mostly in English and mostly American, but would like to see). By pulling in data via the ISBNs a lot of other analysis would also be possible - what is the gender distribution? What time periods were these books published in? 

## What is books3?
There have been multiple news stories (starting with [The Atlantic](https://www.theatlantic.com/technology/archive/2023/08/books3-ai-meta-llama-pirated-books/675063/)) about the books in "[the Pile]([url](https://pile.eleuther.ai))", a large training dataset used to train AI language models, including Meta's. 
The Pile includes books3, which was [announced by Shawn Presser on Twitter in 2020](https://twitter.com/theshawwn/status/1320282152689336320). In the thread, Presser writes that [books3 is "all of Bibliotik"](https://twitter.com/theshawwn/status/1320282152689336320?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1320282152689336320%7Ctwgr%5Ee0362aac7d3b6a2ce864009a36fb587f409211f8%7Ctwcon%5Es1_c10&ref_url=https%3A%2F%2Froamresearch.com%2F%3Fserver-port%3D3333%2Fapp%2Fjilltxt%2Fpage%2FlNtAwnbG_). Bibliotik is a "shadow library" like libgen, Z-library or Sci-Hub. Presser converted the Bibliotik data to txt files and released it online so people could use it to train AI models. 
Books3 and the Pile have been taken offline, but I found this Github repo by psmedia, [https://github.com/psmedia/Books3Info](https://github.com/psmedia/Books3Info), which consists of a list of the ISBN numbers that were in books3, which is exactly what The Atlantic have used in their search engine. I haven't verified this as I don't have the books3 file. I will note that there are only 131402 lines in the list of ISBNs I'm using, and the Atlantic writes that their searchable set includes 186,000 books.

## What it could be used for
This seems to be a fruitful way we could understand more about the datasets that are used to train large language models.
I would welcome contributions or for anyone to take this and run with it - mostly I just want to see the data rather than read about it in newspapers that don't give us the full information. For instance, the Norwegian newspaper wrote "at least 30 Norwegian authors have been illegally used for training AI" - this data finds 42 ISBN numbers registered in Norway, which is only 0.03% of the total training dataset. I suppose that's not bad given that only 0.06% of the world's population lives in Norway. 

## How to use the script
You need to have installed Python. Download the files to your computer and type ´python3 analyse_isbns.py´ from the command line in the directory you put the files in. This will print out the 42 Norwegian ISBN numbers in `books3`. If you know some Python code you can alter the code to see the ISBNs from another country. 

# How ISBNs are formatted
The first three digits of a 13 digit ISBN are all the same (at least for books, there's a different number for sheet music for instance). The next digits are the country number, also called the **group number**.The tricky thing is that these group numbers can be different lengths. [This wikipedia page has an overview](https://en.wikipedia.org/wiki/List_of_ISBN_registration_groups). 0 or 1 are English (no difference between UK, USA, Australia etc), 2 is France, 3 is German, 4 is Japan etc. Most countries have longer numbers, so Norway is 82, and Botswana is 99968. 
The rest of the ISBN identifies the publishing house, so it would be possible to do something clever by finding the location each publishing house is registered to for instance find Australian books. The final digits are the publisher's unique number for the specific book and control digits at the end.

# What are the Norwegian books in books3?
Here are the 42 ISBNs registered in Norway. You could use [isbntools](https://github.com/xlcnd/isbntools) to find their authors and titles - but when I tried it wasn't able to find them, so I think it needs to use a different service - maybe Norwegian ISBNs aren't covered in the libraries it's using? If someone knows an easy way to convert these to a list of authors and titles I would love to know. Otherwise you can paste each ISBN into google and it pops up but that's boring.
9788203372674
9788281433229
9788232802418
9788203359835
9788203359149
9788202603663
9788202638467
9788203264245
9788241916601
9788253041001
9788253041537
9788203298233
9788248912545
9788253037141
9788202302597
9788203375309
9788202440398
9788205503595
9788282261241
9788203356674
9788249510962
9788293671763
9788293671121
9788203252440
9788203375460
9788248919216
9788205492806
9788232802029
9788203362781
9788203365157
9788203373039
9788253038827
9788279651284
9788282655002
9788282261302
9788283132380
9788249514694
9788203196829
9788248918233
9788203361654
9788203351501
9788293670582

# References
- Norli, Camilla. “Norske Bøker Brukt Til å Trene AI-Roboter: − Det Er Fullstendig Uakseptabelt.” VG, September 27, 2023. https://www.vg.no/rampelys/bok/i/kEjA3A/norske-boeker-brukt-til-aa-trene-ai-roboter-det-er-fullstendig-uakseptabelt.
- Reisner, Alex. “Revealed: The Authors Whose Pirated Books Are Powering Generative AI.” The Atlantic, August 19, 2023. https://www.theatlantic.com/technology/archive/2023/08/books3-ai-meta-llama-pirated-books/675063/
- ———. “These 183,000 Books Are Fueling the Biggest Fight in Publishing and Tech.” The Atlantic, September 25, 2023. https://www.theatlantic.com/technology/archive/2023/09/books3-database-generative-ai-training-copyright-infringement/675363/.
- [Norwegian explanation of how ISBN numbers work](https://www.nb.no/tjenester/standardnummerering/isbn/#oppbygging-av-isbn)

