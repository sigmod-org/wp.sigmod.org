# Link check of blog.sigmod.org

Checked on 2026-11-06: every link, image and embed on all 207 built pages (12,036 references, 554 distinct external addresses). Internal links, anchors and all 259 local images were checked against the build; external addresses were requested over HTTP, failures were retried with curl, and dead ones were looked up in the Wayback Machine.

**Status (2026-11-06):** every **Fix** below is done; the two lost images are stored
with the blog (`wp-content/uploads/external/`); every **Dead** link now points to its
Wayback Machine copy nearest the post's date (or, for the two IEEE articles, to their
DOI), in posts and in archived comments. Left as they are: the dead links with no
archived copy (a 2012 GitHub homework page and an ICS-FORTH home page), and the
**Unreachable** and **Blocked** ones. Edited posts carry `keep_local_edits: true`.

- **Fix** — mistakes in the post itself (typos, missing `http://`, pasted Word images).
- **Dead** — the page or site is gone (404, unknown domain, redirected to a 404 page or home page).
- **Unreachable** — no answer to this check (timeout or refused); may only be down for a while.
- **Blocked** — the site refused an automated check (mostly ACM DL / doi.org, LinkedIn, Facebook); these usually work in a browser.

## [The ACM SIGMOD Blog](https://blog.sigmod.org/2012/02/10/bl2/)

- **Dead:** http://eric.univ-lyon2.fr/~jdarmont/ — dead (404) → [archived copy](https://web.archive.org/web/20210805115119/https://eric.univ-lyon2.fr/~jdarmont/)

## [From 100 Students to 100,000](https://blog.sigmod.org/2012/02/24/from-100-students-to-100000/)

- **Unreachable:** http://ai.stanford.edu/%7Ekoller/ — Stanford's server didn't answer this check; probably fine → [archived copy](https://web.archive.org/web/20260926080721/http://ai.stanford.edu/~koller/)
- **Dead:** http://www.wacom.com/en/Products/Cintiq.aspx — dead (404) → [archived copy](https://web.archive.org/web/20120915052109/http://www.wacom.com/en/products/cintiq.aspx)
- **Dead:** https://www.ai-class.com/ — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20130723032929/https://www.ai-class.com/)
- **Dead:** http://www.cs.stanford.edu/people/ang/ — dead (404) → [archived copy](https://web.archive.org/web/20180704013224/http://www.cs.stanford.edu/people/ang//)
- **Dead:** http://www.ml-class.org/ — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20110923173848/http://www.ml-class.org:80/)
- **Unreachable:** http://infolab.stanford.edu/%7Eullman/ — Stanford's server didn't answer this check; probably fine → [archived copy](https://web.archive.org/web/20261008181852/http://infolab.stanford.edu/~ullman/)
- **Dead:** http://www.db-class.org/ — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20230604141724/http://db-class.org/)
- **Unreachable:** http://infolab.stanford.edu/~widom/ — Stanford's server didn't answer this check; probably fine → [archived copy](https://web.archive.org/web/20140928050516/http://infolab.stanford.edu:80/~widom/)

## [MADlib: An Open-Source Library for Scalable Analytics](https://blog.sigmod.org/2012/04/06/madlib-an-open-source-library-for-scalable-analytics/)

- **Fix:** `"http://www.eecs.berkeley.edu/Pubs/TechRpts/2012/EECS-2012-38.html"` — link wrapped in extra quotes, so it points inside the blog
- **Dead:** http://github.com/cs186/sp12/blob/master/hw2/README.md — dead (404) → no archived copy
- **Dead:** http://www.sigmod.org/sigmod-awards/sigmod-awards — dead (404) → [archived copy](https://web.archive.org/web/20160329031904/http://www.sigmod.org/sigmod-awards/sigmod-awards)
- **Dead:** http://money.cnn.com/galleries/2010/technology/1007/gallery.smartest_people_tech.fortune/27.html — dead (503) → [archived copy](https://web.archive.org/web/20140221024604/http://money.cnn.com:80/galleries/2010/technology/1007/gallery.smartest_people_tech.fortune/27.html)
- **Dead:** http://www.technologyreview.com/computing/25089/ — dead (404) → [archived copy](https://web.archive.org/web/20120422015147/http://www.technologyreview.com:80/computing/25089/)
- **Dead:** http://www.platfora.com — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20181128132154/https://www.platfora.com/)

## [Computer science publication culture: where to go from here?](https://blog.sigmod.org/2012/07/17/computer-science-publication-culture-where-to-go-from-here/)

- **Dead:** http://www.sigmod.org/publications/sigmod-record/0212/tamer.pdf — dead (404) → [archived copy](https://web.archive.org/web/20240224134534/http://www.sigmod.org/publications/sigmod-record/0212/tamer.pdf)
- **Dead:** http://www.sigmod.org/publications/sigmod-record/0809/p36.korth.pdf — dead (404) → [archived copy](https://web.archive.org/web/20120728014330/http://www.sigmod.org/publications/sigmod-record/0809/p36.korth.pdf)
- **Dead:** http://www.cs.pitt.edu/~labrinid — dead (404) → [archived copy](https://web.archive.org/web/20260516022345/http://www.cs.pitt.edu/~labrinid/)
- **Unreachable:** http://www.cs.utexas.edu/~jsequeda — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20170518003251/http://www.cs.utexas.edu:80/~jsequeda/)

## [A Few More Words on Big Data](https://blog.sigmod.org/2012/08/07/a-few-more-words-on-big-data/)

- **Dead:** http://www.systems.ethz.ch/Talks — dead (404) → [archived copy](https://web.archive.org/web/20150914221730/https://www.systems.ethz.ch/talks)

## [Fifty Years of Databases](https://blog.sigmod.org/2012/12/11/tt/)

- **Fix:** `www.tomandmaria.com/tom` — missing `http://`, so it points inside the blog
- **Unreachable:** http://www.bitsavers.org/www.computer.museum.uq.edu.au/pdf/CPB-230 GE-225 Introduction To GECOM.pdf — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20240531171259/http://bitsavers.org/www.computer.museum.uq.edu.au/pdf/CPB-230%20GE-225%20Introduction%20To%20GECOM.pdf)
- **Dead:** http://www.computer.org/portal/web/csdl/doi/10.1109/85.988583 — dead (now redirects to an error or home page) → no archived copy
- **Dead:** http://www.computer.org/portal/web/csdl/doi/10.1109/MAHC.2009.110 — dead (now redirects to an error or home page) → [archived copy](https://web.archive.org/web/20251124061558/https://www.computer.org/portal/web/csdl/doi/10.1109/MAHC.2009.110)

## [Where’s the Data in the Big Data Wave?](https://blog.sigmod.org/2013/03/06/wheres-the-data-in-the-big-data-wave/)

- **Dead:** http://www.mmci.uni-saarland.de/en/start — dead (404) → [archived copy](https://web.archive.org/web/20200928015436/http://www.mmci.uni-saarland.de/en/start)

## [Stop publishing so much already!](https://blog.sigmod.org/2013/03/22/832/)

- **Dead:** http://www3.isi.edu/home — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20240702081510/https://www3.isi.edu/home)

## [Ontology-based Data Management](https://blog.sigmod.org/2013/05/14/ontology-based-data-management/)

- **Dead:** http://www.dis.uniroma1.it/~lenzerini — dead (404) → no archived copy

## [Hunting for the Value Gaps in Data Management, Services, and Analytics](https://blog.sigmod.org/2013/06/25/904/)

- **Unreachable:** http://aria.asu.edu/candan — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20210420213518/https://aria.asu.edu/candan/)

## [Observation: CSers do not value themselves, nor the results of their work?](https://blog.sigmod.org/2013/09/30/939/)

- **Unreachable:** http://i.stanford.edu/VIC/allVICcitations.pdf — Stanford's server didn't answer this check; probably fine → [archived copy](https://web.archive.org/web/20240806230026/http://i.stanford.edu/VIC/allVICcitations.pdf)
- **Unreachable:** http://infolab.stanford.edu/~gio/ — Stanford's server didn't answer this check; probably fine → [archived copy](https://web.archive.org/web/20260721004116/http://infolab.stanford.edu/~gio/)
- **Unreachable:** http://i.stanford.edu/VIC/index.html — Stanford's server didn't answer this check; probably fine → [archived copy](https://web.archive.org/web/20240713043257/http://i.stanford.edu/VIC/index.html)
- **Unreachable:** http://infolab.stanford.edu/pub/gio/2009/Wiederhold-Gupta-Neuhold.pdf — Stanford's server didn't answer this check; probably fine → [archived copy](https://web.archive.org/web/20240810232634/http://infolab.stanford.edu/pub/gio/2009/Wiederhold-Gupta-Neuhold.pdf)

## [The Curses of Heterogeneity in Big Data](https://blog.sigmod.org/2013/10/30/the-curses-of-heterogeneity-in-big-data/)

- **Dead:** http://www3.isi.edu/home — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20240702081510/https://www3.isi.edu/home)

## [Are Databases ready for Gestural Workloads?](https://blog.sigmod.org/2013/12/11/are-databases-ready-for-gestural-workloads/)

- **Dead:** http://db.cse.ohio-state.edu/gestureDB.html — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20201202060020/http://db.cse.ohio-state.edu/gestureDB.html)

## [Systems & Databases: Let’s Break Down the Walls](https://blog.sigmod.org/2014/02/24/systems-databases-lets-break-down-the-walls/)

- **Dead:** http://www.informatik.uni-trier.de/~ley/pers/hd/b/Bernstein:Philip_A=.html — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20141225023710/http://www.informatik.uni-trier.de:80/~ley/pers/hd/b/Bernstein:Philip_A=.html)

## [Is Query Optimization a “Solved” Problem?](https://blog.sigmod.org/2014/04/10/nn/)

- **Unreachable:** http://publib.boulder.ibm.com/infocenter/dzichelp/v2r2/index.jsp?topic=%2Fcom.ibm.db2z10.doc.comref%2Fsrc%2Ftpc%2Fdb2z_bindoptreopt.htm — no answer (timeout or refused) → no archived copy
- **Dead:** http://www.cs.columbia.edu/~wfan/PAPERS/Tech08Reopt.pdf — dead (404) → [archived copy](https://web.archive.org/web/20120103124104/http://www.cs.columbia.edu/~wfan/PAPERS/Tech08Reopt.pdf)
- **Dead:** http://researcher.ibm.com/researcher/view.php?person=us-lohmang — dead (404) → [archived copy](https://web.archive.org/web/20230325083149/https://researcher.ibm.com/researcher/view.php?person=us-lohmang)
- **Dead:** http://www.socc2013.org/ — dead (404) → [archived copy](https://web.archive.org/web/20210412060454/http://www.socc2013.org/)
- **Unreachable:** http://conceptoriented.com — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20181230002706/http://conceptoriented.com/)

## [Exploratory search: New name for an old hat?](https://blog.sigmod.org/2014/06/21/data-exploration-new-name-for-an-old-hat/)

- **Unreachable:** http://aria.asu.edu/candan — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20210420213518/https://aria.asu.edu/candan/)
- **Dead:** http://www.ics.forth.gr/~tzitzik — dead (now redirects to an error or home page) → [archived copy](https://web.archive.org/web/20130515091828/http://www.ics.forth.gr:80/~tzitzik/)

## [Quality Experiments Crowdsourced](https://blog.sigmod.org/2014/08/27/crowdsourced/)

- **Dead:** http://www.aub.edu.lb/fas/cs/people/Pages/se58.aspx — dead (404) → [archived copy](https://web.archive.org/web/20170910062321/http://www.aub.edu.lb:80/fas/cs/people/Pages/se58.aspx)

## [Big Data Is Opening the Door To Revolutions: Databases Should Be Next](https://blog.sigmod.org/2014/11/08/big-data-is-opening-the-door-to-revolutions-databases-should-be-next/)

- **Dead:** http://www.michaelbrodie.com/michael_brodie.asp — dead (404) → [archived copy](https://web.archive.org/web/20141220151328/http://www.michaelbrodie.com/michael_brodie.asp)

## [The elephant in the room: getting value from Big Data](https://blog.sigmod.org/2015/02/08/the-elephant-in-the-room-getting-value-from-big-data/)

- **Dead:** http://dbweb.enst.fr/events/webdb2015 — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20161225031934/http://dbweb.enst.fr/events/webdb2015/)
- **Dead:** http://allenai.org/semantic-scholar.html — dead (404) → [archived copy](https://web.archive.org/web/20190916221803/https://allenai.org/semantic-scholar.html)
- **Dead:** http://allenai.org/content/publications/clark_divvala.pdf — dead (404) → [archived copy](https://web.archive.org/web/20160315183127/http://allenai.org/content/publications/clark_divvala.pdf)
- **Dead:** https://stics.mpi-inf.mpg.de/ — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20210901034108/https://stics.mpi-inf.mpg.de/)
- **Dead:** http://www.telecom-paristech.fr/nc/formation-et-innovation-dans-le-numerique.html — dead (404) → [archived copy](https://web.archive.org/web/20160328161549/http://www.telecom-paristech.fr/nc/formation-et-innovation-dans-le-numerique.html)

## [Information Hunting: The Many Faces of Recommendations for Data Exploration](https://blog.sigmod.org/2015/03/10/1580/)

- **Dead:** http://ics.forth.gr/~kstef/ — dead (now redirects to an error or home page) → no archived copy
- **Dead:** http://ics.forth.gr/~kondylak — dead (now redirects to an error or home page) → [archived copy](https://web.archive.org/web/20120510004756/http://www.ics.forth.gr:80/~kondylak/)

## [A Decade at Google](https://blog.sigmod.org/2015/09/20/a-decade-at-google/)

- **Fix:** `http://______________` — placeholder left in the post
- **Dead:** https://research.google.com/tables — dead (now redirects to an error or home page) → [archived copy](https://web.archive.org/web/20191216072754/https://research.google.com/tables)
- **Dead:** http://jinglei.ren.systems — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20180226111302/http://jinglei.ren.systems:80/)

## [Thinking Spatial](https://blog.sigmod.org/2016/10/06/thinking-spatial/)

- **Fix:** `www.cs.umn.edu/~mokbel` — missing `http://`, so it points inside the blog

## [SIGMOD 2017 Announcement](https://blog.sigmod.org/2017/01/19/sigmod-2017-announcement/)

- **Fix:** `http://philbe@microsoft.com` — an email address written as a web link
- **Dead:** http://researcher.watson.ibm.com/researcher/view.php?person=us-dolby — dead (404) → [archived copy](https://web.archive.org/web/20230102093856/https://researcher.watson.ibm.com/researcher/view.php?person=us-dolby)
- **Unreachable:** http://www.shawconferencecentre.com/upcoming-events/ — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20180726030056/https://www.shawconferencecentre.com/upcoming-events/)

## [The data chatbots are coming](https://blog.sigmod.org/2017/02/09/the-data-chatbots-are-coming/)

- **Unreachable:** http://www.cs.utexas.edu/~ml/papers/chill-mlw-97.pdf — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20251012004948/https://www.cs.utexas.edu/~ml/papers/chill-mlw-97.pdf)

## [Courting ML: Witnessing the Marriage of Relational & Web Data Systems to Machine Learning](https://blog.sigmod.org/2018/02/14/courting-ml-witnessing-the-marriage-of-relational-web-data-systems-to-machine-learning/)

- **Dead:** https://bigdata.uni-saarland.de/predictweather/ — dead (404) → [archived copy](https://web.archive.org/web/20240803033407/https://bigdata.uni-saarland.de/predictweather/)
- **Dead:** http://www.deeptunedb.com/ — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20240125025155/http://deeptunedb.com/)

## [A Tribute to José Alfredo Blakeley](https://blog.sigmod.org/2018/03/10/a-tribute-to-jose-alfredo-blakeley/)

- **Unreachable:** http://i.stanford.edu/~gio — Stanford's server didn't answer this check; probably fine → [archived copy](https://web.archive.org/web/20260826153640/http://i.stanford.edu/~gio/)

## [Data cleaning is a machine learning problem that needs data systems help!](https://blog.sigmod.org/2018/04/18/data-cleaning-is-a-machine-learning-problem-that-needs-data-systems-help/)

- **Dead:** https://sites.google.com/site/anhaidgroup/projects/magellan — dead (404) → [archived copy](https://web.archive.org/web/20210227000121/https://sites.google.com/site/anhaidgroup/projects/magellan)
- **Dead:** https://hazyresearch.github.io/snorkel/ — dead (404) → [archived copy](https://web.archive.org/web/20191022163704/https://hazyresearch.github.io/snorkel/)
- **Unreachable:** http://interact.osu.edu/gesturedb/ — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20230530174409/https://interact.osu.edu/gesturedb/)
- **Dead:** https://www.census.gov/srd/csrmreports/byyear.html — dead (404) → [archived copy](https://web.archive.org/web/20170127165543/http://www.census.gov/srd/csrmreports/byyear.html)
- **Dead:** https://www.census.gov/srd/papers/pdf/RRS2018-05.pdf — dead (404) → [archived copy](https://web.archive.org/web/20210323072437/https://www.census.gov/srd/papers/pdf/RRS2018-05.pdf)

## [Visual Data Exploration: A Fertile Ground for Data Management Research](https://blog.sigmod.org/2018/06/25/2342/)

- **Unreachable:** http://db.cs.duke.edu/papers/pvldb15-WuHarbYangYu-object_centric_vis.pdf — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20230607094423/http://db.cs.duke.edu/papers/pvldb15-WuHarbYangYu-object_centric_vis.pdf)
- **Dead:** http://www.cs.umd.edu/~leilani/static/papers/forecache_cr_sigmod2016.pdf — dead (404) → [archived copy](https://web.archive.org/web/20210416181118/http://www.cs.umd.edu/~leilani/static/papers/forecache_cr_sigmod2016.pdf)
- **Dead:** http://www.bewitched.com/projects/querysketch/wattenberg-chi2001.pdf — dead (404) → [archived copy](https://web.archive.org/web/20210423040721/http://www.bewitched.com/projects/querysketch/wattenberg-chi2001.pdf)
- **Dead:** https://idl.cs.washington.edu/papers/voyager/ — dead (404) → [archived copy](https://web.archive.org/web/20240519182639/https://idl.cs.washington.edu/papers/voyager/)
- **Dead:** http://vis.stanford.edu/papers/profiler — dead (404) → [archived copy](https://web.archive.org/web/20260611233417/http://vis.stanford.edu/papers/profiler)
- **Unreachable:** https://vgc.poly.edu/~fchirigati/papers/chirigati-sigmod2016.pdf — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20220121050100/https://vgc.poly.edu/~fchirigati/papers/chirigati-sigmod2016.pdf)

## [ML/AI Systems and Applications: Is the SIGMOD/VLDB Community Losing Relevance?](https://blog.sigmod.org/2018/08/21/2454/)

- **Dead:** https://bigdata.uni-saarland.de/people/dittrich.php — dead (404) → [archived copy](https://web.archive.org/web/20241207105954/https://bigdata.uni-saarland.de/people/dittrich.php)
- **Dead:** https://edtosavetheworld.files.wordpress.com/2014/05/paradigms.png **(image)** — dead (404) → [archived copy](https://web.archive.org/web/20230202185548/https://edtosavetheworld.files.wordpress.com/2014/05/paradigms.png)
- **Dead:** https://www.kaggle.com/surveys/2017 — dead (404) → [archived copy](https://web.archive.org/web/20260101010259/https://www.kaggle.com/surveys/2017)
- **Dead:** http://visit.crowdflower.com/rs/416-ZBE-142/images/CrowdFlower_DataScienceReport_2016.pdf — dead (503) → [archived copy](https://web.archive.org/web/20180801063101/http://visit.crowdflower.com/rs/416-ZBE-142/images/CrowdFlower_DataScienceReport_2016.pdf)
- **Dead:** http://bigdata.csail.mit.edu/node/185 — dead (400) → [archived copy](https://web.archive.org/web/20190603015351/http://bigdata.csail.mit.edu:80/node/185)
- **Unreachable:** https://www.sysml.cc — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20260905024646/https://www.sysml.cc/)
- **Dead:** https://edtosavetheworld.com/2014/05/28/1-thomas-kuhn-the-structure-of-scientific-revolutions — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20220517053541/https://edtosavetheworld.com/2014/05/28/1-thomas-kuhn-the-structure-of-scientific-revolutions/)
- **Dead:** http://first-the-trousers.com/hello-world/ — dead (now redirects to an error or home page) → [archived copy](https://web.archive.org/web/20230902012510/https://first-the-trousers.com/hello-world/)
- **Dead:** https://www.kaggle.com/surveys/2017/ — dead (404) → [archived copy](https://web.archive.org/web/20260101010259/https://www.kaggle.com/surveys/2017)

## [Privacy Challenges in the Post-GDPR World: A Data Management Perspective](https://blog.sigmod.org/2018/10/09/2554/)

- **Unreachable:** https://eugdpr.org/ — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20261026044718/https://eugdpr.org/)
- **Dead:** https://rise.cs.berkeley.edu/projects/ground/ — dead (404) → [archived copy](https://web.archive.org/web/20260606101457/https://rise.cs.berkeley.edu/Projects/ground/)
- **Unreachable:** https://datahub.csail.mit.edu/www/ — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20230110132526/https://datahub.csail.mit.edu/www/)
- **Unreachable:** https://www.wirewheel.io/ — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20250403070715/https://wirewheel.io/)

## [Simulating Infection Spread](https://blog.sigmod.org/2020/04/21/simulating-infection-spread/)

- **Dead:** https://vectorinstitute.ai/wp-content/uploads/2020/03/arxiv-mappingai.pdf — dead (404) → [archived copy](https://web.archive.org/web/20231216224341/https://vectorinstitute.ai/wp-content/uploads/2020/03/arxiv-mappingai.pdf)
- **Unreachable:** https://www.washingtonpost.com/graphics/2020/world/corona-simulator/?mod=article_inline — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20220818182315/https://www.washingtonpost.com/graphics/2020/world/corona-simulator/?mod=article_inline)

## [Humans’ Role in-the-Loop](https://blog.sigmod.org/2020/12/21/3138/)

- **Dead:** https://agp.iem.technion.ac.il/incognitomatch/ — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20210413225638/https://agp.iem.technion.ac.il/incognitomatch/)

## [Enabling Responsible Data Science in Practice](https://blog.sigmod.org/2021/01/20/enabling-responsible-data-science-in-practice/)

- **Fix:** `https://towardsdatascience.com/a-gentle-introduction-to-the-discussion-on-algorithmic- fairness-740bbb469b6` — a space inside the address breaks it
- **Fix:** `https://cacm.acm.org/magazines/2020/5/244336-a-snapshot-of-the-frontiers-of-fairness- in-machine-learning/full` — a space inside the address breaks it
- **Fix:** `https://www.vox.com/2017/1/18/14304964/data-facial-recognition-trouble-recognizing- black-white-faces-diversit` — a space inside the address breaks it
- **Dead:** https://aif360.mybluemix.net/ — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20230525081324/https://aif360.mybluemix.net/)
- **Dead:** https://towardsdatascience.com/a-tutorial-on-fairness-in-machine-learning-3ff8ba1040cb — dead (now redirects to an error or home page) → [archived copy](https://web.archive.org/web/20231127085221/https://towardsdatascience.com/a-tutorial-on-fairness-in-machine-learning-3ff8ba1040cb)
- **Dead:** https://www.equivant.com/response-to-propublica-demonstrating-accuracy-equity-and-predictive-parity/ — dead (404) → [archived copy](https://web.archive.org/web/20240624143309/https://www.equivant.com/response-to-propublica-demonstrating-accuracy-equity-and-predictive-parity/)
- **Dead:** https://blog.einstein.ai/double-hard-debias-tailoring-word-embeddings-for-gender-bias-mitigation/ — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20210805141331/https://blog.einstein.ai/double-hard-debias-tailoring-word-embeddings-for-gender-bias-mitigation/)
- **Dead:** https://www.cs.uic.edu/~indexlab/mithra.htm — dead (404) → [archived copy](https://web.archive.org/web/20210516090141/https://www.cs.uic.edu/~indexlab/mithra.htm)

## [Automation of Data Prep, ML, and Data Science: New Cure or Snake Oil?](https://blog.sigmod.org/2021/11/10/automation-of-data-prep-ml-and-data-science-new-cure-or-snake-oil/)

- **Unreachable:** https://visit.figure-eight.com/rs/416-ZBE-142/images/CrowdFlower_DataScienceReport_2016.pdf — no answer (timeout or refused) → [archived copy](https://web.archive.org/web/20250117044233/http://visit.figure-eight.com/rs/416-ZBE-142/images/CrowdFlower_DataScienceReport_2016.pdf)

## [Data Science for Social Good: the STAR Mission](https://blog.sigmod.org/2022/01/26/data-science-for-social-good-the-star-mission/)

- **Dead:** http://wwwnew2.hklii.hk/predictor — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20230317123604/http://wwwnew2.hklii.hk/predictor)

## [Natural Language-Based Exploration with Databases in Chatbot](https://blog.sigmod.org/2022/02/23/natural-language-based-exploration-with-databases-in-chatbot/)

- **Dead:** http://www.sqlbot.co.kr/ — dead (domain no longer exists) → [archived copy](https://web.archive.org/web/20250915190928/https://www.sqlbot.co.kr/)

## [From Curbing Epidemics to Investing: We can Help!](https://blog.sigmod.org/2022/08/03/from-curbing-epidemics-to-investing-we-can-help/)

- **Fix:** `url:https://doi.org/10.14778/3415478.3415499` — `url:` in front of the address
- **Fix:** `https://doi.org/10.1145/3093754.3093761.` — full stop included in the link, which makes it a 404

## [Returning Top-K : Preference Aggregation or Sortition, or is there a Better Middle Ground?](https://blog.sigmod.org/2022/10/26/returning-top-k-preference-aggregation-or-sortition-or-is-there-a-better-middle-ground/)

- **Fix:** `http://​​https://stanford.library.sydney.edu.au/...` — two invisible characters and a doubled `http://` in front of the address

## [Auditing bias of recourse in classifiers (part II)](https://blog.sigmod.org/2024/09/25/auditing-bias-of-recourse-in-classifiers-part-ii/)

- **Fix:** 8 missing images: small math symbols pasted from Word (4 point to the author's own computer, `file:///Users/christsapelas/...`, and 4 have no address). From the text they are probably ∈, ∃ and ∧, and 𝒢 for the set of groups; best confirmed with the authors or the paper.
- **Fix:** `#_ftn1` — Word footnote/comment link with nothing to jump to
- **Fix:** `#_msocom_1` — Word footnote/comment link with nothing to jump to
- **Fix:** `#_bookmark6` — Word footnote/comment link with nothing to jump to

## Blocked automated checks

These answered 403/999/401/400 to the checker; spot-check in a browser if needed.

- [The ACM SIGMOD Blog](https://blog.sigmod.org/2012/02/10/bl2/): <http://www.facebook.com/profile.php?id=10727687>
- [From 100 Students to 100,000](https://blog.sigmod.org/2012/02/24/from-100-students-to-100000/): <http://www.facebook.com/profile.php?id=1561831993>, <http://twitter.com/tonysidaway>
- [MADlib: An Open-Source Library for Scalable Analytics](https://blog.sigmod.org/2012/04/06/madlib-an-open-source-library-for-scalable-analytics/): <http://fellows.acm.org/fellow_citation.cfm?id=4354833&srt=year&year=2009>, <http://www.sloan.org/fellowships>
- [Big Data: It’s Not Just the Analytics](https://blog.sigmod.org/2012/05/05/big-data-its-not-just-the-analytics/): <http://cra.org/ccc/docs/init/bigdatawhitepaper.pdf>, <http://www.cra.org/>
- [Computer science publication culture: where to go from here?](https://blog.sigmod.org/2012/07/17/computer-science-publication-culture-where-to-go-from-here/): <http://dx.doi.org/10.1145/1538788.1538789>, <http://dx.doi.org/10.1145/1506409.1506410>, <http://www.cra.org/scholarlypub/>, <http://www.facebook.com/profile.php?id=1381017262>
- [Fifty Years of Databases](https://blog.sigmod.org/2012/12/11/tt/): <http://dl.acm.org/citation.cfm?id=1387145>, <http://dl.acm.org/citation.cfm?id=1387148>, <http://amturing.acm.org/award_winners/codd_1000892.cfm>, <http://dl.acm.org/citation.cfm?id=362534>, <http://dl.acm.org/citation.cfm?id=1141882>
- [Stop publishing so much already!](https://blog.sigmod.org/2013/03/22/832/): <http://www.facebook.com/profile.php?id=688762663>, <http://www.metacase.com/blogs/stevek/blogView>, <http://www.facebook.com/profile.php?id=747718481>, <http://www.ecs.soton.ac.uk/people/dt2>
- [Hunting for the Value Gaps in Data Management, Services, and Analytics](https://blog.sigmod.org/2013/06/25/904/): <http://www.facebook.com/profile.php?id=622018639>
- [Are Databases ready for Gestural Workloads?](https://blog.sigmod.org/2013/12/11/are-databases-ready-for-gestural-workloads/): <http://www.canalys.com/newsroom/smart-phones-overtake-client-pcs-2011>, <http://www.forbes.com/sites/louiscolumbus/2013/09/12/idc-87-of-connected-devices-by-2017-will-be-tablets-and-smartphones/>
- [Systems & Databases: Let’s Break Down the Walls](https://blog.sigmod.org/2014/02/24/systems-databases-lets-break-down-the-walls/): <http://www.pnas.org/content/early/2012/09/14/1211286109>
- [Is Query Optimization a “Solved” Problem?](https://blog.sigmod.org/2014/04/10/nn/): <http://www.linkedin.com/in/stephendillon/>
- [Quality Experiments Crowdsourced](https://blog.sigmod.org/2014/08/27/crowdsourced/): <http://blogs.wsj.com/digits/2010/07/23/using-flickr-photos-as-a-travel-guide/>
- [Big Data Is Opening the Door To Revolutions: Databases Should Be Next](https://blog.sigmod.org/2014/11/08/big-data-is-opening-the-door-to-revolutions-databases-should-be-next/): <http://doi.acm.org/10.1145/2674026.2674035>, <http://doi.acm.org/10.1145/2623330.2623667>
- [The elephant in the room: getting value from Big Data](https://blog.sigmod.org/2015/02/08/the-elephant-in-the-room-getting-value-from-big-data/): <http://doi.acm.org/10.1145/2623330.2623623>
- [Data systems that are easy to design*](https://blog.sigmod.org/2015/06/08/1617/): <http://stratos.seas.harvard.edu/>
- [A Decade at Google](https://blog.sigmod.org/2015/09/20/a-decade-at-google/): <http://dl.acm.org/citation.cfm?id=1453916>
- [Wisdom: a “double V” for Big Data](https://blog.sigmod.org/2016/02/18/wisdom-a-double-v-for-big-data/): <http://doi.acm.org/10.1145/2814710.2814714>
- [A Tribute to José Alfredo Blakeley](https://blog.sigmod.org/2018/03/10/a-tribute-to-jose-alfredo-blakeley/): <https://www.linkedin.com/in/peter-chen-43bba0/>
- [Visual Data Exploration: A Fertile Ground for Data Management Research](https://blog.sigmod.org/2018/06/25/2342/): <https://www.tableau.com/about/press-releases/2016/tableau-acquires-hyper>, <https://dl.acm.org/citation.cfm?doid=2694413.2694417>, <https://dl.acm.org/citation.cfm?id=304581>, <https://dl.acm.org/citation.cfm?id=2465355>, <https://dl.acm.org/citation.cfm?id=3209903>, <https://dl.acm.org/citation.cfm?id=253291>, <https://dl.acm.org/citation.cfm?id=2600592>, <https://dl.acm.org/citation.cfm?id=614285.614512>, <https://dl.acm.org/citation.cfm?id=2379788>, <https://dl.acm.org/citation.cfm?id=2807478>, <https://dl.acm.org/citation.cfm?id=2984588>
- [ML/AI Systems and Applications: Is the SIGMOD/VLDB Community Losing Relevance?](https://blog.sigmod.org/2018/08/21/2454/): <https://www.acm.org/hennessy-patterson-turing-lecture>
- [Privacy Challenges in the Post-GDPR World: A Data Management Perspective](https://blog.sigmod.org/2018/10/09/2554/): <https://dl.acm.org/citation.cfm?id=774552>, <https://dl.acm.org/citation.cfm?id=1217302>, <https://dl.acm.org/citation.cfm?id=2588581>, <https://dl.acm.org/citation.cfm?id=3035945>, <https://dl.acm.org/citation.cfm?id=564717>, <https://dl.acm.org/citation.cfm?id=2467797>
- [Automation of Data Prep, ML, and Data Science: New Cure or Snake Oil?](https://blog.sigmod.org/2021/11/10/automation-of-data-prep-ml-and-data-science-new-cure-or-snake-oil/): <https://towardsdatascience.com/automl-is-overhyped-1b5511ded65f>, <https://dl.acm.org/doi/10.1145/3316416.3316425>
- [Data Management For The Metaverse](https://blog.sigmod.org/2022/06/10/data-management-for-the-metaverse/): <https://www.bloomberg.com/professional/blog/metaverse-may-be-800-billion-market-next-tech-platform/>
- [From Curbing Epidemics to Investing: We can Help!](https://blog.sigmod.org/2022/08/03/from-curbing-epidemics-to-investing-we-can-help/): <https://doi.org/10.1145/2658840.2658843>, <https://doi.org/10.1145/3299881>, <https://doi.org/10.14778/2904483.2904489>, <https://doi.org/10.1145/3318464.3389765>, <https://doi.org/10.1145/2588555.2612667>, <https://doi.org/10.1145/3495257>, <https://doi.org/10.1145/3472749.3474794>
- [Why Uncertainty is Unavoidable and What We Can Do About That](https://blog.sigmod.org/2023/01/24/why-uncertainty-is-unavoidable-and-what-we-can-do-about-that/): <https://doi.org/10.1145/3375395.3387970>, <https://doi.org/10.1145/3299869.3319887>
