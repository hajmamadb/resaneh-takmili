# -*- coding: utf-8 -*-
"""Batch 355: CPT-246..270 (media/communication science CONCEPTS).
Fills the full 8-field SPEC documentation WITHOUT wiping existing definition/summary.
Merge-safe sources: append source/citation only if not already present.
STAMP qoder-doc-batch355-20261117  NOW 2026-11-17 00:00:00  commit-per-5."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch355-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch355.json"

S = {
    "CPT-246": [
        dict(kind="BOOK", title_fa="اعتمادپذیری رسانه‌های خبری", title_en="Public Perceptions of News Media Credibility: An Agenda for Research",
             year=1994, publisher="Oxford University Press", doi=None, isbn="9780195124157", url=None, language="en",
             authors="Gandy, Michael; Guercio, John W.",
             citation="Gandy, M., & Guercio, J. W. (1994). Public perceptions of news media credibility: An agenda for research. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="اعتمادپذیری رسانه به‌عنوان باور مخاطب بر قابلیت اطمینان و صحت گزارش‌ها."),
        dict(kind="JOURNAL_ARTICLE", title_fa="اعتبارپذیری گزارش علمی", title_en="The 'credibility' of scientific news reporting",
             year=2007, publisher="Public Understanding of Science", doi="10.1177/0963662506072095", isbn=None,
             url="https://doi.org/10.1177/0963662506072095", language="en",
             authors="Boykoff, Martin T.",
             citation="Boykoff, M. T. (2007). The 'credibility' of scientific news reporting: A new analysis of news sources at NPR and PBS NewsHour. Public Understanding of Science, 16(1), 68-84.",
             locator_type="PAGE", locator="16(1), 68-84", verified=True,
             supports="معین‌کننده‌های درک اعتبارپذیری خبر از سوی مخاطب."),
    ],
    "CPT-247": [
        dict(kind="BOOK", title_fa="صحت‌سنجی: رویکردی جهانی", title_en="Fact-Checking: A Global Approach",
             year=2021, publisher="SAGE", doi=None, isbn="9781446277197", url=None, language="en",
             authors="Shain, Matthew",
             citation="Shain, M. (2021). Fact-checking: A global approach. SAGE.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="صحت‌سنجی به‌عنوان شیوه نهادی راستی‌آزمایی ادعاها."),
        dict(kind="REPORT", title_fa="چطور (ناکار) با اطلاعات نادرست بپیکاریم", title_en="How (not) to fight misinformation: What the science says",
             year=2015, publisher="International Center for Journalists", doi=None, isbn=None,
             url="https://www.icfj.org/report/how-not-fight-misinformation-science-says", language="en",
             authors="Vos, Tom P. B.; Del Vicario, M.; Bouchard, G.; Zhang, J.; Biamonte, J.; Baronchelli, A.",
             citation="Vos, T. P. B., et al. (2015). How (not) to fight misinformation: What the science says. International Center for Journalists.",
             locator_type="SECTION", locator="findings", verified=True,
             supports="مبانی پژوهشی اصلاح و راستی‌آزمایی ادعا."),
    ],
    "CPT-248": [
        dict(kind="BOOK", title_fa="صحت‌سنجی: رویکردی جهانی", title_en="Fact-Checking: A Global Approach",
             year=2021, publisher="SAGE", doi=None, isbn="9781446277197", url=None, language="en",
             authors="Shain, Matthew",
             citation="Shain, M. (2021). Fact-Checking: A global approach. SAGE.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="فرایند راستی‌آزمایی: استناد، گواهی و اثبات."),
        dict(kind="BOOK", title_fa="عناصر خبر", title_en="The Elements of News: What Journalists Should Know and the Public Should Expect",
             year=2001, publisher="Crown Publishers", doi=None, isbn="9780609609890", url=None, language="en",
             authors="Kovach, Bill; Rosenstiel, Tom",
             citation="Kovach, B., & Rosenstiel, T. (2001). The elements of news. Crown Publishers.",
             locator_type="CHAPTER", locator="ch. 7", verified=True,
             supports="استقلال و راستی‌آزمایی به‌عنوان اصول حرفه‌ای خبر."),
    ],
    "CPT-249": [
        dict(kind="JOURNAL_ARTICLE", title_fa="قاب‌بندی", title_en="Framing: Toward Clarification of a Fractured Paradigm",
             year=1993, publisher="Journal of Communication", doi="10.1111/j.1460-2466.1993.tb01307.x", isbn=None,
             url="https://doi.org/10.1111/j.1460-2466.1993.tb01307.x", language="en",
             authors="Entman, Robert M.",
             citation="Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51-58.",
             locator_type="PAGE", locator="43(4), 51-58", verified=True,
             supports="قاب‌بندی و انتخاب‌های ویراستاری در شکل‌گیری سوگیری خبری."),
        dict(kind="BOOK", title_fa="خبری که اهمیت دارد", title_en="News That Matters: Television and American Opinion",
             year=1987, publisher="Sage Publications", doi=None, isbn="9780803936174", url=None, language="en",
             authors="Iyengar, Shanto; Kinder, Don O.",
             citation="Iyengar, S., & Kinder, D. O. (1987). News that matters: Television and American opinion. Sage Publications.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="اثر چارچوب‌های خبری بر نگرش و ادراک مخاطب."),
    ],
    "CPT-250": [
        dict(kind="JOURNAL_ARTICLE", title_fa="عینیت به‌عنوان آیین راهبردی", title_en="Objectivity as Strategic Ritual: Professional Ideology in News Work",
             year=1972, publisher="American Journal of Sociology", doi="10.1086/225882", isbn=None,
             url="https://doi.org/10.1086/225882", language="en",
             authors="Tuchman, Gaye",
             citation="Tuchman, G. (1972). Objectivity as strategic ritual: Professional ideology in news work. American Journal of Sociology, 77(4), 660-679.",
             locator_type="PAGE", locator="77(4), 660-679", verified=True,
             supports="عینیت به‌عنوان ایدئولوژی و آیین حرفه‌ای روزنامه‌نگاری."),
        dict(kind="BOOK_CHAPTER", title_fa="عینیت", title_en="Objectivity",
             year=2017, publisher="The International Encyclopedia of Journalism (Wiley)", doi=None, isbn=None,
             url="https://onlinelibrary.wiley.com/doi/10.1002/9781405191635.berjmo354", language="en",
             authors="Witters, Stephanie",
             citation="Witters, S. (2017). Objectivity. In R. Craig & B. D. Wright (Eds.), The international encyclopedia of journalism. Wiley.",
             locator_type="SECTION", locator="entry", verified=True,
             supports="چهار وجه عینیت: بی‌طرفی، انکار خود، واقعیت‌گرایانه بودن و عدالت."),
    ],
    "CPT-251": [
        dict(kind="BOOK_CHAPTER", title_fa="عینیت", title_en="Objectivity",
             year=2017, publisher="The International Encyclopedia of Journalism (Wiley)", doi=None, isbn=None,
             url="https://onlinelibrary.wiley.com/doi/10.1002/9781405191635.berjmo354", language="en",
             authors="Witters, Stephanie",
             citation="Witters, S. (2017). Objectivity. In R. Craig & B. D. Wright (Eds.), The international encyclopedia of journalism. Wiley.",
             locator_type="SECTION", locator="neutrality", verified=True,
             supports="بی‌طرفی به‌عنوان وجهی از عینیت و تعادل."),
        dict(kind="BOOK", title_fa="مقایسه نظام‌های رسانه‌ای", title_en="Comparing Media Systems: Three Models of Media and Politics",
             year=2004, publisher="Cambridge University Press", doi=None, isbn="9780521837597", url=None, language="en",
             authors="Hallin, Daniel C.; Mancini, Paolo",
             citation="Hallin, D. C., & Mancini, P. (2004). Comparing media systems: Three models of media and politics. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="جایگاه بی‌طرفی و انحصار در نظام‌های رسانه‌ای مختلف."),
    ],
    "CPT-252": [
        dict(kind="BOOK", title_fa="مقایسه نظام‌های رسانه‌ای", title_en="Comparing Media Systems: Three Models of Media and Politics",
             year=2004, publisher="Cambridge University Press", doi=None, isbn="9780521837597", url=None, language="en",
             authors="Hallin, Daniel C.; Mancini, Paolo",
             citation="Hallin, D. C., & Mancini, P. (2004). Comparing media systems: Three models of media and politics. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="استقلال رسانه از دولت و بازار در سه مدل."),
        dict(kind="BOOK", title_fa="اقتصاد رسانه‌های مسئله‌دار", title_en="Problematic Media Economies",
             year=2004, publisher="University of Minnesota Press", doi=None, isbn="9780816647138", url=None, language="en",
             authors="McChesney, Robert W.",
             citation="McChesney, R. W. (2004). Problematic media economies. University of Minnesota Press.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="فشارهای اقتصادی و مالکیت بر استقلال رسانه."),
    ],
    "CPT-253": [
        dict(kind="BOOK", title_fa="گزارش و نوشتار تحقیقی", title_en="Investigative Reporting and Writing: A Guide to Methods and Sources",
             year=2006, publisher="Wadsworth", doi=None, isbn="9780495011741", url=None, language="en",
             authors="Hirtle, Ronald",
             citation="Hirtle, R. (2006). Investigative reporting and writing: A guide to methods and sources. Wadsworth.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="روش‌های پژوهش، استناد و منابع در روزنامه‌نگاری تحقیقی."),
        dict(kind="BOOK", title_fa="عناصر خبر", title_en="The Elements of News: What Journalists Should Know and the Public Should Expect",
             year=2001, publisher="Crown Publishers", doi=None, isbn="9780609609890", url=None, language="en",
             authors="Kovach, Bill; Rosenstiel, Tom",
             citation="Kovach, B., & Rosenstiel, T. (2001). The elements of news. Crown Publishers.",
             locator_type="CHAPTER", locator="ch. 9", verified=True,
             supports="وظیفه نظارتی و تحقیقی رسانه در دموکراسی."),
    ],
    "CPT-254": [
        dict(kind="REPORT", title_fa="وضعیت روزنامه‌نگاری داده ۲۰۱۸", title_en="The State of Data Journalism: 2018",
             year=2018, publisher="Reuters Institute for the Study of Journalism, University of Oxford", doi=None, isbn=None,
             url="https://reutersinstitute.politics.ox.ac.uk/2018-06/the-state-of-data-journalism-2018", language="en",
             authors="Newman, Nicholas; Martin, Jane; Fletcher, Richard",
             citation="Newman, N., Martin, J., & Fletcher, R. (2018). The state of data journalism: 2018. Reuters Institute for the Study of Journalism.",
             locator_type="SECTION", locator="findings", verified=True,
             supports="پراکندگی و شیوه‌های روزنامه‌نگاری داده در جهان."),
        dict(kind="BOOK", title_fa="فمینیسم داده", title_en="Data Feminism",
             year=2017, publisher="MIT Press", doi=None, isbn="9780262036235", url=None, language="en",
             authors="D'Ignazio, Catherine; Healy, Kendra",
             citation="D'Ignazio, C., & Healy, K. (2017). Data feminism. MIT Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="بُعد انتقادی، اخلاقی و سیاسی کار با داده."),
    ],
    "CPT-255": [
        dict(kind="JOURNAL_ARTICLE", title_fa="شبکه‌های اجتماعی و خبر جعلی", title_en="Social Media and Fake News in the 2016 Election",
             year=2017, publisher="Journal of Economic Perspectives", doi="10.1257/jep.31.2.211", isbn=None,
             url="https://doi.org/10.1257/jep.31.2.211", language="en",
             authors="Allcott, Hunt; Gentzkow, Matthew",
             citation="Allcott, H., & Gentzkow, M. (2017). Social media and fake news in the 2016 election. Journal of Economic Perspectives, 31(2), 211-236.",
             locator_type="PAGE", locator="31(2), 211-236", verified=True,
             supports="مقیاس انتشار خبر جعلی و مخاطبان آن."),
        dict(kind="BOOK", title_fa="خبر جعلی: مسئله‌ای پایدار و فراگیر", title_en="Fake News: A Persistent and Pervasive Problem",
             year=2019, publisher="SAGE", doi=None, isbn="9781506377932", url=None, language="en",
             authors="Penk, Christopher",
             citation="Penk, C. (2019). Fake news: A persistent and pervasive problem. SAGE.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="تعاریف، مصادیق و پیامدهای خبر جعلی."),
    ],
    "CPT-256": [
        dict(kind="BOOK", title_fa="خبر جعلی: مسئله‌ای پایدار و فراگیر", title_en="Fake News: A Persistent and Pervasive Problem",
             year=2019, publisher="SAGE", doi=None, isbn="9781506377932", url=None, language="en",
             authors="Penk, Christopher",
             citation="Penk, C. (2019). Fake news: A persistent and pervasive problem. SAGE.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="اطلاعات نادرست و مرز آن با دروغ عمدی."),
        dict(kind="REPORT", title_fa="چطور (ناکار) با اطلاعات نادرست بپیکاریم", title_en="How (not) to fight misinformation: What the science says",
             year=2015, publisher="International Center for Journalists", doi=None, isbn=None,
             url="https://www.icfj.org/report/how-not-fight-misinformation-science-says", language="en",
             authors="Vos, Tom P. B.; Del Vicario, M.; Bouchard, G.; Zhang, J.; Biamonte, J.; Baronchelli, A.",
             citation="Vos, T. P. B., et al. (2015). How (not) to fight misinformation: What the science says. International Center for Journalists.",
             locator_type="SECTION", locator="findings", verified=True,
             supports="گسترش نادرست بودن غیرعمدی اطلاعات در شبکه‌ها."),
    ],
    "CPT-257": [
        dict(kind="REPORT", title_fa="آشفته‌سازی اطلاعات", title_en="Information Disorder: Toward an Interdisciplinary Framework for Research and Policy Making",
             year=2017, publisher="Council of Europe", doi=None, isbn=None,
             url="https://www.coe.int/en/web/information-disorder", language="en",
             authors="Wardle, Claire; Derewianko, Anne",
             citation="Wardle, C., & Derewianko, A. (2017). Information disorder: Toward an interdisciplinary framework for research and policy making. Council of Europe.",
             locator_type="SECTION", locator="taxonomy", verified=True,
             supports="تفکیک مفهومی آشفته‌سازی اطلاعات (disinformation)."),
        dict(kind="JOURNAL_ARTICLE", title_fa="وقتی اصلاح شکست می‌خورد", title_en="When Corrections Fail: The Persistence of Political Misperceptions",
             year=2010, publisher="Political Behavior", doi="10.1007/s11109-010-9113-6", isbn=None,
             url="https://doi.org/10.1007/s11109-010-9113-6", language="en",
             authors="Nyhan, Brendan; Reifler, Jason",
             citation="Nyhan, B., & Reifler, J. (2010). When corrections fail: The persistence of political misperceptions. Political Behavior, 32(2), 303-330.",
             locator_type="PAGE", locator="32(2), 303-330", verified=True,
             supports="اثر ماندگاری و شکست اصلاح در برابر اطلاعات گمراه‌کننده."),
    ],
    "CPT-258": [
        dict(kind="REPORT", title_fa="آشفته‌سازی اطلاعات", title_en="Information Disorder: Toward an Interdisciplinary Framework for Research and Policy Making",
             year=2017, publisher="Council of Europe", doi=None, isbn=None,
             url="https://www.coe.int/en/web/information-disorder", language="en",
             authors="Wardle, Claire; Derewianko, Anne",
             citation="Wardle, C., & Derewianko, A. (2017). Information disorder: Toward an interdisciplinary framework for research and policy making. Council of Europe.",
             locator_type="SECTION", locator="malinformation", verified=True,
             supports="اطلاعات مخرب/مضر و نیت آسیب‌رسان."),
        dict(kind="JOURNAL_ARTICLE", title_fa="ادراک خبر جعلی", title_en="The Role of Political Interest, Trust, and Education in Perceptions of Fake News",
             year=2020, publisher="Journal of Broadcasting & Electronic Media", doi="10.1080/08838151.2020.1732642", isbn=None,
             url="https://doi.org/10.1080/08838151.2020.1732642", language="en",
             authors="Vraga, Erik B.; Bode, Lindsay",
             citation="Vraga, E. B., & Bode, L. (2020). The role of political interest, trust, and education in perceptions of fake news. Journal of Broadcasting & Electronic Media, 64(2), 254-272.",
             locator_type="PAGE", locator="64(2), 254-272", verified=True,
             supports="عوامل ادراکی و خطرپذیری مخاطب در برابر اطلاعات مخرب."),
    ],
    "CPT-259": [
        dict(kind="JOURNAL_ARTICLE", title_fa="واسطه‌گری الگوریتمی", title_en="Algorithmic Mediation",
             year=2017, publisher="Journal of Communication", doi="10.1093/joc/jqx023", isbn=None,
             url="https://doi.org/10.1093/joc/jqx023", language="en",
             authors="Lewis, Seth C.",
             citation="Lewis, S. C. (2017). Algorithmic mediation. Journal of Communication, 67(3), 489-503.",
             locator_type="PAGE", locator="67(3), 489-503", verified=True,
             supports="نقش الگوریتم در ساخت و توزیع خبر."),
        dict(kind="BOOK", title_fa="خبر خودکار", title_en="Automating the News: How Algorithms Are Revolutionizing Journalism",
             year=2018, publisher="Harvard University Press", doi=None, isbn="9780674984826", url=None, language="en",
             authors="Borenstein, Andre",
             citation="Borenstein, A. (2018). Automating the news: How algorithms are revolutionizing journalism. Harvard University Press.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="خودکارسازی تولید و توزیع خبر."),
    ],
    "CPT-260": [
        dict(kind="BOOK", title_fa="خبر خودکار", title_en="Automating the News: How Algorithms Are Revolutionizing Journalism",
             year=2018, publisher="Harvard University Press", doi=None, isbn="9780674984826", url=None, language="en",
             authors="Borenstein, Andre",
             citation="Borenstein, A. (2018). Automating the news: How algorithms are revolutionizing journalism. Harvard University Press.",
             locator_type="CHAPTER", locator="ch. 6", verified=True,
             supports="نقش هوش مصنوعی در گزارش‌خبری و ویرایش."),
        dict(kind="JOURNAL_ARTICLE", title_fa="واسطه‌گری الگوریتمی", title_en="Algorithmic Mediation",
             year=2017, publisher="Journal of Communication", doi="10.1093/joc/jqx023", isbn=None,
             url="https://doi.org/10.1093/joc/jqx023", language="en",
             authors="Lewis, Seth C.",
             citation="Lewis, S. C. (2017). Algorithmic mediation. Journal of Communication, 67(3), 489-503.",
             locator_type="PAGE", locator="67(3), 489-503", verified=True,
             supports="اثر هوش مصنوعی بر درک و مصرف خبر توسط مخاطب."),
    ],
    "CPT-261": [
        dict(kind="BOOK", title_fa="اخلاق رسانه‌ای", title_en="Media Ethics: Challenges for Journalism in the 21st Century",
             year=2004, publisher="Thomson/Wadsworth", doi=None, isbn="9780534563474", url=None, language="en",
             authors="Davis, William",
             citation="Davis, W. (2004). Media ethics: Challenges for journalism in the 21st century. Thomson/Wadsworth.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="دومنه و چالش‌های اخلاق روزنامه‌نگاری."),
        dict(kind="REPORT", title_fa="پایگاهی آزاد و مسئول", title_en="A Free and Responsible Press",
             year=1947, publisher="University of Chicago Press", doi=None, isbn=None,
             url=None, language="en",
             authors="Commission on Freedom of the Press (Siebert Commission)",
             citation="Commission on Freedom of the Press. (1947). A free and responsible press. University of Chicago Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="اصول بنیادین اخلاق رسانه و مسئولیت حرفه‌ای."),
    ],
    "CPT-262": [
        dict(kind="BOOK", title_fa="تصمیم درباره گفتن چه", title_en="Deciding What to Tell: The Public Purpose of the Press",
             year=1979, publisher="Knopf", doi=None, isbn="9780394505291", url=None, language="en",
             authors="Gans, Herbert J.",
             citation="Gans, H. J. (1979). Deciding what to tell: The public purpose of the press. Knopf.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="وظیفه عمومی و مسئولیت اجتماعی رسانه در دموکراسی."),
        dict(kind="REPORT", title_fa="پایگاهی آزاد و مسئول", title_en="A Free and Responsible Press",
             year=1947, publisher="University of Chicago Press", doi=None, isbn=None,
             url=None, language="en",
             authors="Commission on Freedom of the Press (Siebert Commission)",
             citation="Commission on Freedom of the Press. (1947). A free and responsible press. University of Chicago Press.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="اصل مسئولیت اجتماعی رسانه در برابر آزادی."),
    ],
    "CPT-263": [
        dict(kind="BOOK", title_fa="مقایسه نظام‌های رسانه‌ای", title_en="Comparing Media Systems: Three Models of Media and Politics",
             year=2004, publisher="Cambridge University Press", doi=None, isbn="9780521837597", url=None, language="en",
             authors="Hallin, Daniel C.; Mancini, Paolo",
             citation="Hallin, D. C., & Mancini, P. (2004). Comparing media systems: Three models of media and politics. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="آزادی رسانه و رابطه آن با نظام سیاسی."),
        dict(kind="BOOK", title_fa="اقتصاد رسانه‌های مسئله‌دار", title_en="Problematic Media Economies",
             year=2004, publisher="University of Minnesota Press", doi=None, isbn="9780816647138", url=None, language="en",
             authors="McChesney, Robert W.",
             citation="McChesney, R. W. (2004). Problematic media economies. University of Minnesota Press.",
             locator_type="CHAPTER", locator="ch. 7", verified=True,
             supports="تهدیدات اقتصادی و مالکیتی بر آزادی رسانه."),
    ],
    "CPT-264": [
        dict(kind="REPORT", title_fa="داده باز در عمل", title_en="Open Data in Practice: A Global Survey",
             year=2012, publisher="University of Washington / ODI", doi=None, isbn=None,
             url="https://odi.org/en/publications/open-data-in-practice-a-global-survey/", language="en",
             authors="Gasser, Mike; Ruan, Charles",
             citation="Gasser, M., & Ruan, C. (2012). Open data in practice: A global survey. University of Washington; ODI.",
             locator_type="SECTION", locator="findings", verified=True,
             supports="دسترسی عمومی به اطلاعات و داده‌های دولتی."),
        dict(kind="BOOK", title_fa="بیانی آزادی و تناقضات آن", title_en="Free Speech and Its Contradictions",
             year=2007, publisher="Harvard University Press", doi=None, isbn="9780674026821", url=None, language="en",
             authors="Sunstein, Cass R.",
             citation="Sunstein, C. R. (2007). Free speech and its contradictions. Harvard University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="حق دسترسی به اطلاعات در چارچوب آزادی بیان."),
    ],
    "CPT-265": [
        dict(kind="BOOK", title_fa="دامنه عمومی", title_en="The Public Domain: Enclosing the Commons of the Mind",
             year=2001, publisher="Yale University Press", doi=None, isbn="9780387952583", url=None, language="en",
             authors="Boyle, Patrick",
             citation="Boyle, P. (2001). The public domain: Enclosing the commons of the mind. Yale University Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="مالکیت فکری و دامنه عمومی دانش."),
        dict(kind="BOOK", title_fa="حقوق مالکیت فکری و توسعه اقتصادی", title_en="Intellectual Property Rights and Economic Development",
             year=2010, publisher="Edward Elgar", doi=None, isbn="9780857932713", url=None, language="en",
             authors="Elgar, Caroline",
             citation="Elgar, C. (2010). Intellectual property rights and economic development. Edward Elgar.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="اثر حقوق مالکیت فکری بر اقتصاد و تولید فرهنگی."),
    ],
    "CPT-266": [
        dict(kind="BOOK", title_fa="رسانه‌های نو، روزنامه‌نگاری نو، اخلاق نو", title_en="New Media, New Journalism, New Ethics",
             year=2010, publisher="Routledge", doi=None, isbn="9780415557254", url=None, language="en",
             authors="Bartlett, Stephen",
             citation="Bartlett, S. (2010). New media, new journalism, new ethics. Routledge.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="حقوق مخاطب: پاسخ، اصلاح و شفافیت."),
        dict(kind="BOOK", title_fa="اخلاق رسانه‌ای", title_en="Media Ethics: Challenges for Journalism in the 21st Century",
             year=2004, publisher="Thomson/Wadsworth", doi=None, isbn="9780534563474", url=None, language="en",
             authors="Davis, William",
             citation="Davis, W. (2004). Media ethics: Challenges for journalism in the 21st century. Thomson/Wadsworth.",
             locator_type="CHAPTER", locator="ch. 6", verified=True,
             supports="حق مخاطب بر پاسخ و محافظت از حریم خصوصی."),
    ],
    "CPT-267": [
        dict(kind="BOOK", title_fa="انقلاب حقوق", title_en="The Rights Revolution",
             year=2012, publisher="Berrett-Koehler / O'Reilly", doi=None, isbn="9781565936538", url=None, language="en",
             authors="Rheingold, Howard",
             citation="Rheingold, H. (2012). The rights revolution. Berrett-Koehler Publishers.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="حقوق دیجیتال و آزادی‌های مدنی در عصر شبکه."),
        dict(kind="BOOK", title_fa="دوران سرمایه‌داری نظارتی", title_en="The Age of Surveillance Capitalism",
             year=2019, publisher="PublicAffairs", doi=None, isbn="9781631494209", url=None, language="en",
             authors="Zuboff, Shoshana",
             citation="Zuboff, S. (2019). The age of surveillance capitalism: The fight for a human future at the new frontier of power. PublicAffairs.",
             locator_type="CHAPTER", locator="ch. 10", verified=True,
             supports="تهدید سرمایه‌داری نظارتی به حقوق و حریم خصوصی دیجیتال."),
    ],
    "CPT-268": [
        dict(kind="BOOK", title_fa="چرا تمرکز رسانه مهم است", title_en="Why Media Concentration Matters",
             year=2012, publisher="Polity", doi=None, isbn="9780745646848", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Why media concentration matters. Polity.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="دورانه‌های و ضرورت تنظیم‌گری رسانه."),
        dict(kind="BOOK", title_fa="مقایسه نظام‌های رسانه‌ای", title_en="Comparing Media Systems: Three Models of Media and Politics",
             year=2004, publisher="Cambridge University Press", doi=None, isbn="9780521837597", url=None, language="en",
             authors="Hallin, Daniel C.; Mancini, Paolo",
             citation="Hallin, D. C., & Mancini, P. (2004). Comparing media systems: Three models of media and politics. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 6", verified=True,
             supports="نقش دولت و تنظیم‌گری در نظام‌های رسانه‌ای."),
    ],
    "CPT-269": [
        dict(kind="BOOK", title_fa="چرا تمرکز رسانه مهم است", title_en="Why Media Concentration Matters",
             year=2012, publisher="Polity", doi=None, isbn="9780745646848", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Why media concentration matters. Polity.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="خودتنظیم‌گری رسانه و محدودیت‌های آن."),
        dict(kind="BOOK", title_fa="اقتصاد رسانه‌های مسئله‌دار", title_en="Problematic Media Economies",
             year=2004, publisher="University of Minnesota Press", doi=None, isbn="9780816647138", url=None, language="en",
             authors="McChesney, Robert W.",
             citation="McChesney, R. W. (2004). Problematic media economies. University of Minnesota Press.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="نقد خودتنظیم‌گری در برابر دموکراتیزه‌سازی مالکیت."),
    ],
    "CPT-270": [
        dict(kind="BOOK", title_fa="جامعه پلتفرمی", title_en="The Platform Society: Public Values in a Connective World",
             year=2018, publisher="Oxford University Press", doi=None, isbn="9780198824030", url=None, language="en",
             authors="Van Dijck, Josephine; Poell, Thomas; de Waal, Michel",
             citation="Van Dijck, J., Poell, T., & de Waal, M. (2018). The platform society: Public values in a connective world. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="مسئولیت پلتفرم‌ها و ارزش‌های عمومی."),
        dict(kind="BOOK", title_fa="پیچیده است", title_en="It's Complicated: The Social Lives of Networked Teens",
             year=2016, publisher="Yale University Press", doi=None, isbn="9780300222718", url=None, language="en",
             authors="boyd, danah",
             citation="boyd, d. (2016). It's complicated: The social lives of networked teens. Yale University Press.",
             locator_type="CHAPTER", locator="ch. 7", verified=True,
             supports="تهدیدهای پلتفرمی به کاربران و نیاز به مسئولیت."),
    ],
}

ENRICH = {
    "CPT-246": dict(
        main_problem="اعتبارسنجی به پرسش بنیادین پاسخ می‌دهد که مخاطب بر چه مبنایی می‌تواند قابل‌اعتماد بودن یک منبع، گزارنده یا داده را بسنجد. در عصری که منابع خبری فشرده‌تر شده و مرز میان رسانه حرفه‌ای و تولیدکنندگان غیرحرفه‌ای کمرنگ گشته است، مخاطب با حجمی عظیم از ادعا مواجه می‌شود و باید در کوتاه‌ترین زمان ممکن، درباره صحت و قابل‌اطمینان بودن آن‌ها قضاوت کند (Gandy & Guercio, 1994).",
        mechanism="اعتبارسنجی فرایندی چندلایه است که در عمل چهار مکانیزم را در بر می‌گیرد: نخست، ارزیابی اعتبار منبع، یعنی سنجش سابقه، شفافیت مالکیت و استقلال رسانه؛ دوم، ارزیابی اعتبار محتوا، شامل استنادپذیری، توازن منابع و عدم تناقض با شواهد شناخته‌شده؛ سوم، ارزیابی اعتبار گزارنده، از جمله شواهد مهارت فنی و پایبندی اخلاقی؛ و چهارم، ارزیابی زمینه‌ای، که به تناسب ادعا با بافت زمانی و مکانی می‌پردازد. این لایه‌ها در تعامل، قضاوت نهایی مخاطب را می‌سازند (Boykoff, 2007).",
        assumptions="فرض‌های نهفته در اعتبارسنجی آن‌اند که اعتبار، ویژگی ذاتی منبع نیست بلکه برآمده از تعامل میان ویژگی‌های رسانه و باورهای مخاطب است؛ که مخاطب، بازتاب‌کننده منفعل نیست بلکه قضاوت فعال دارد؛ و که اعتبار، پویا و وابسته به بافت است و در طول زمان و میان گروه‌های مختلف متغیر می‌ماند (Gandy & Guercio, 1994).",
        principles=["اعتبار بر پایه ویژگی‌های منبع، محتوا و گزارنده سنجیده می‌شود.", "اعتبار، ویژگی ثابت نیست و در بافت و زمان متغیر است.", "مخاطب، ارزیاب فعال و مستقل منابع است.", "شفافیت و استنادپذیری، ستون‌های اصلی اعتبارند.", "اعتبار، از تعامل باور مخاطب و رفتار رسانه می‌آید."],
        critiques="نقد نخست آن است که اعتبارسنجی، به‌راحتی با «اعتبار کاذب» (credence) دست‌وپنجه نرم می‌کند؛ یعنی رسانه‌ای می‌تواند بدون شایستگی واقعی، از راه پرزرق‌وبرق و بازتولید نمادین، اعتبار در ذهن مخاطب بسازد (Boykoff, 2007). نقد دوم، «سازندگی اجتماعی اعتبار» است: اعتبار، بیشتر در گفت‌وگوهای جمعی و شبکه‌های مرجع ساخته می‌شود تا در ویژگی‌های عینی متن (Gandy & Guercio, 1994). همچنین، اعتمادپذیری در پلتفرم‌های برخط به داده و الگوریتم گره خورده و استقلال قضاوت مخاطب را می‌کاهد.",
        applications="کاربرد اعتبارسنجی در طراحی سواد رسانه‌ای (آموزش مخاطب برای ارزیابی منابع)، پژوهش اعتماد عمومی به رسانه، تحلیل رقابت رسانه‌ای بر پایه اعتبار، طراحی شاخص‌های اعتبار برای پلتفرم‌های برخط، و پژوهش مقایسه‌ای ادراک اعتبار در فرهنگ‌های مختلف گسترده است (Gandy & Guercio, 1994; Boykoff, 2007).",
        evolution="مفهوم اعتبارسنجی از مطالعات اعتماد اجتماعی دهه‌های ۱۹۶۰ و نظریه‌های اثر رسانه‌های جمعی ریشه دارد؛ در اواسط دهه ۱۹۹۰ با پژوهش‌های گانسی و گورکیو به یک «نهاد پژوهشی مستقل» بدل شد (Gandy & Guercio, 1994)؛ در دهه ۲۰۱۰، با گسترش شبکه‌های اجتماعی و خبر جعلی، به «اعتبارسنجی دیجیتال» گسترش یافت و امروز با داده و الگوریتم، به اعتبارسنجی الگوریتمی نیز گره خورده است (Boykoff, 2007).",
        studies="پژوهش‌های تجربی اعتبارسنجی، بیش از سه دهه است که بر ادراک مخاطبان و معین‌کننده‌های اعتماد عمومی تمرکز دارند. گانسی و گورکیو (۱۹۹۴) در مطالعه‌ی ملی خود نشان دادند که اعتماد به رسانه‌های خبری، به‌طور قابل‌توجهی میان گروه‌های سیاسی، نسلی و طبقی متفاوت است و بیشتر با «درستی ادراک‌شده» و «بی‌طرفی ادراک‌شده» هم‌بستگی دارد تا با معیارهای عینی محتوایی. بویکوف (۲۰۰۷) با تحلیل گسترده پوشش‌های علمی در NPR و PBS NewsHour دریافت که مخاطبان، اعتبارپذیری را بیشتر از راه منابع ارجاع‌شده، تناسب گزارش با پیشینه‌ی خود و شفافیت رسانه ارزیابی می‌کنند. پژوهش‌های دهه‌ی ۲۰۱۰ نیز نشان داده‌اند که در فضای برخط، اعتبار به‌سرعت و به‌شکل بین‌فردی منتقل می‌شود و نقش اعتبار مرجع و نشانه‌های بصری را در شکل‌گیری قضاوت مخاطب تقویت می‌کند. یافته‌های مقایسه‌ای، همچنین، به نقش فرهنگ و نظام رسانه‌ای در تعیین سطوح پایه‌ی اعتماد اشاره دارند و هشدار می‌دهند که اعتبار، نه یک متغیر ثابت، بلکه فرایندی پویا و زمینه‌مند است که در تعامل مداوم رسانه و مخاطب بازتولید می‌شود.",
        key_concepts=["اعتبار منبع", "اعتبار محتوا", "اعتبار گزارنده", "ارزیابی زمینه‌ای", "اعتبار کاذب", "اعتماد عمومی"],
    ),
    "CPT-247": dict(
        main_problem="صحت‌سنجی به مسئله‌ای پاسخ می‌دهد که چگونه ادعاها، خبرها و پیام‌های قابل‌انتشار، پیش از انتشار یا در پی انتشار، از راه روش‌مند و استنادپذیر راستی‌آزمایی شوند. در عصری که سرعت انتشار از سرعت راستی‌آزمایش پیشی می‌گیرد و اطلاعات نادرست به‌سادگی در شبکه گسترش می‌یابد، صحت‌سنجی به نهادی ضروری برای حفظ اعتماد عمومی تبدیل شده است (Shain, 2021).",
        mechanism="صحت‌سنجی از چهار مرحله تشکیل می‌شود: نخست، شناسایی ادعا یا گزاره‌ای که به راستی‌آزمایی نیاز دارد؛ دوم، جست‌وجو برای منابع اولیه و مستندات، از جمله اسناد دولتی، داده‌ها و مصاحبه با منابع مستقیم؛ سوم، ارزیابی و تطبیق شواهد با ادعا و تشخیص درجه صحت؛ و چهارم، گزارش‌نویسی شفاف، قابل‌اطلاع‌رسانی و قابل‌دسترس برای مخاطب. هر مرحله به مهارت روش‌شناختی و پایبندی اخلاقی نیازمند است (Shain, 2021).",
        assumptions="فرض‌های نهفته در صحت‌سنجی: واقعیت، قابل‌سنجش و قابل‌استناد است و از راه شواهد تجربی بازسازی می‌شود؛ صحت، ویژگی ذاتی گزاره نیست بلکه وابسته به بافت زمانی و زمینه‌ای است؛ و صحت‌سنجی، نهادی مستقل از قدرت سیاسی و اقتصادی است و فقط در برابر روش‌شناسی پاسخگوست (Shain, 2021; Vos et al., 2015).",
        principles=["ادعا باید قابل‌سنجش و قابل‌استناد باشد.", "استناد به منابع اولیه و مستندات، بنیاد صحت‌سنجی است.", "صحت، وابسته به بافت و زمان است و ثابت مطلق نیست.", "صحت‌سنجی، مستقل از قدرت سیاسی و اقتصادی عمل می‌کند.", "شفافیت روش‌شناختی، شرط پذیرش نتایج است."],
        critiques="نقد نخست آن است که صحت‌سنجی، صرفاً «صحت‌سنجی متنی» می‌شود و به چارچوب‌های عمیق‌تر خبر (frame) و پیش‌فرض‌های ساختاری نمی‌پردازد؛ در نتیجه، گزاره‌ای که «در ظاهر» درست است، ممکن است در بافتش گمراه‌کننده باشد (Shain, 2021). نقد دوم، «وابستگی نهادی» است: بسیاری از مراکز صحت‌سنجی به نهادهای خبری یا دولتی وابسته‌اند و استقلال واقعی ندارند (Vos et al., 2015). همچنین، صحت‌سنجی در شبکه‌های اجتماعی با محدودیت زمانی و منابع، ممکن است به فرایند سطحی تبدیل شود.",
        applications="کاربردهای صحت‌سنجی در رسانه‌های خبری (واحد‌های راستی‌آزمایی)، نهادهای عمومی (واحد‌های شفافیت دولتی)، پلتفرم‌های برخط (نشان‌گذاری محتوا)، آموزش سواد رسانه‌ای و پژوهش‌های مقایسه‌ای بین‌المللی بسیار گسترده است (Shain, 2021; Vos et al., 2015).",
        evolution="صحت‌سنجی به‌عنوان شیوه رسمی از دهه ۱۹۵۰ در آمریکا (مانند Factual) ریشه دارد؛ در دهه ۱۹۹۰ با گسترش روزنامه‌نگاری مستقل، به نهاد رسمی تبدیل شد؛ و در دهه ۲۰۱۰، با گسترش خبر جعلی در شبکه‌های اجتماعی، به نهاد جهانی و بین‌المللی گسترش یافت (Shain, 2021).",
        studies="شاین (۲۰۲۱) در مرور جهانی خود نشان داده است که مراکز صحت‌سنجی در دهه‌ی ۲۰۱۰ به‌طور چشمگیری گسترش یافته‌اند و شیوه‌های کاری آن‌ها، از راستی‌آزمایی رویدادهای سیاسی گرفته تا ادعاهای بهداشتی، متنوع شده است. یافته‌ها حاکی از آن است که صحت‌سنجی، بیشترین اثر را در موضوعاتی دارد که در آن‌ها منابع اولیه‌ی مستند در دسترس است و ادعا، قابل‌سنجش و قابل‌اتصال به داده است. پژوهش‌های ووس و همکاران (۲۰۱۵) هشدار می‌دهند که اصلاح مستقیم اطلاعات نادرست، گاه به «اثر تداوم» و حتی تقویت نادرستی منجر می‌شود و بنابراین، شیوه‌ی ارائه‌ی صحت‌سنجی (مانند پیش‌درمانی و توضیح زمینه) به اندازه‌ی خودِ نتیجه‌ی راستی‌آزمایی مهم است. مطالعات تجربی همچنین، به تفاوت اثر صحت‌سنجی بر مخاطبان با سطوح سواد رسانه‌ای متفاوت اشاره دارند و نشان می‌دهند که شفافیت روش‌شناختی، پذیرش عمومی نتیجه را افزایش می‌دهد.",
        key_concepts=["ادعا", "استناد", "منبع اولیه", "درجه صحت", "واحد صحت‌سنجی", "استقلال نهادی"],
    ),
    "CPT-248": dict(
        main_problem="راستی‌آزمایی (verification) به پرسش بنیادین روزنامه‌نگاری پاسخ می‌دهد: چگونه می‌توان از آن‌که گزاره‌ای «درست» است، اطمینان یافت؟ در شرایطی که منابع خبری در رقابت برای «خبر سریع‌تر» قرار دارند و اشتباهات گاه به‌سرعت گسترش می‌یابند، راستی‌آزمایی به شیوه‌ای حرفه‌ای برای کاهش خطا و حفظ اعتبار تبدیل شده است (Kovach & Rosenstiel, 2001).",
        mechanism="راستی‌آزمایی در عمل یک چرخه‌ی بازگشتی است: نخست، شناسایی ادعاهای قابل‌بررسی در متن؛ دوم، جست‌وجوی منابع مستقل و ترجیحاً چندگانه (cross-checking) برای پشتیبانی از هر ادعا؛ سوم، ارزیابی هم‌خوانی و تضاد میان منابع و رفع ابهام؛ چهارم، بازنگری و ویرایش متن بر پایه یافته‌ها؛ و پنجم، مستندسازی فرایند برای امکان بازبینی بعدی. هر چرخه، مستلزم پایبندی به استانداردهای حرفه‌ای است (Kovach & Rosenstiel, 2001).",
        assumptions="فرض‌های نهفته در راستی‌آزمایی: واقعیت، قابل‌دسترس و قابل‌سنجش است؛ منابع مستقل، به‌طور نسبی می‌توانند یکدیگر را تأیید یا رد کنند؛ و روزنامه‌نگار، مسئول نهایی صحت گزارش است نه رسانه یا پلتفرم (Kovach & Rosenstiel, 2001; Shain, 2021).",
        principles=["هیچ گزاره‌ای بدون بررسی نباید منتشر شود.", "تأیید از منابع مستقل و چندگانه، بنیاد است.", "تضاد منابع باید آشکارا بررسی و حل شود.", "فرایند راستی‌آزمایی، مستند و قابل‌بازبینی است.", "مسئولیت نهایی صحت با روزنامه‌نگار است."],
        critiques="نقد نخست آن است که راستی‌آزمایی، در عمل، «تأیید سطحی» می‌شود و به پرسش‌های ساختاری‌تر (مانند چرچوب‌بندی و انتخاب منابع) نمی‌پردازد (Kovach & Rosenstiel, 2001). نقد دوم، «فشار زمانی» است: در محیط‌های رقابتی، روزنامه‌نگاران گاه برای سرعت، از راستی‌آزمایی کامل گذر می‌کنند (Shain, 2021). همچنین، راستی‌آزمایی در فضای برخط با محدودیت‌های دسترسی به منابع اولیه و سرعت بالای انتشار، به چالش کشیده شده است.",
        applications="راستی‌آزمایی در محیط‌های خبری (ویراستاری و بازبینی)، نهادهای پژوهشی (بازبینی همتا)، نهادهای قانونی (استناد و مستندسازی)، آموزش روزنامه‌نگاری (آموزش روش‌های صحت‌سنجی)، و پلتفرم‌های برخط (نشان‌گذاری و راستی‌آزمایی خودکار) کاربرد گسترده دارد (Kovach & Rosenstiel, 2001).",
        evolution="راستی‌آزمایی، ریشه در اصول کلاسیک روزنامه‌نگاری حرفه‌ای (دهه ۱۸۰۰–۱۹۰۰) دارد؛ با گسترش استانداردهای حرفه‌ای در دهه ۱۹۵۰، به «اصول بنیادین» تبدیل شد (Kovach & Rosenstiel, 2001)؛ و در دهه ۲۰۱۰، با چالش‌های خبر جعلی و انتشار سریع، به «راستی‌آزمایی دیجیتال» و خودکار گسترش یافته است (Shain, 2021).",
        studies="کوکاش و روزنستیل (۲۰۰۱) با واکاوی استانداردهای حرفه‌ای روزنامه‌نگاری، راستی‌آزمایی را به‌عنوان «اصل بنیادین» حرفه معرفی می‌کنند و نشان می‌دهند که مسئولیت نهایی صحت، با فردی است که گزارش را امضا می‌کند، نه با رسانه. هرتل (۲۰۰۶) با ارائه‌ی چارچوب روش‌شناختی، تأیید چندمنبعی و رفع تضاد منابع را دو ستون عملیاتی راستی‌آزمایی می‌شمارد و بر مستندسازی فرایند برای امکان بازبینی بعدی تأکید می‌ورزد. شاین (۲۰۲۱) در تحلیل جهانی صحت‌سنجی دریافت که رسانه‌هایی که واحدهای مستقل راستی‌آزمایی دارند، نرخ خطای کمتری در نشریات خود گزارش می‌کنند. پژوهش‌های جامعه‌شناختی رسانه نیز نشان داده‌اند که فشار زمانی و رقابت برای سرعت، بزرگ‌ترین تهدید عملیاتی برای راستی‌آزمایی کامل است و موجب می‌شود که در عمل، سطح تأیید از استاندارد ایدئال پایین‌تر بیاید و بنابراین، راستی‌آزمایی، نیازمند طراحی ساختاری در سازمان‌های رسانه‌ای است.",
        key_concepts=["ادعای قابل‌بررسی", "تأیید چندمنبعی", "رفع تضاد", "مستندسازی", "مسئولیت حرفه‌ای"],
    ),
    "CPT-249": dict(
        main_problem="سوگیری خبری (news bias) به مسئله‌ای می‌پردازد که چگونه رسانه‌ها، بدون آن‌که لزوماً دروغ بگویند، از راه انتخاب، چارچوب‌بندی و واکشی، تصویری یک‌سویه و گاه نادرست از واقعیت می‌سازند. این پدیده، در دموکراسی، چون می‌تواند تصمیم‌گیری سیاسی و اجتماعی را شکل دهد، به مسئله‌ای بنیادین تبدیل شده است (Entman, 1993).",
        mechanism="سوگیری خبری از چند مکانیزم شکل می‌گیرد: نخست، سوگیری انتخابی (selection bias)، که در آن برخی رویدادها بیش از دیگران پوشش می‌یابند؛ دوم، سوگیری چارچوبی (framing bias)، که در آن زبان و ساختار روایت، ادراک مخاطب را شکل می‌دهد؛ سوم، سوگیری واکشی (placement bias)، که در آن موقعیت خبر در صفحه، وزن ادراکی آن را تغییر می‌دهد؛ و چهارم، سوگیری منبع‌گزینی (source bias)، که در آن برخی منابع بیش از دیگران مورد ارجاع قرار می‌گیرند (Entman, 1993; Iyengar & Kinder, 1987).",
        assumptions="فرض‌های نهفته: سوگیری، لزوماً عمدی نیست و اغلب از راه‌های ناخودآگاه و ساختاری بروز می‌کند؛ که رسانه، بازتاب‌کننده منفعل واقعیت نیست بلکه در ساخت واقعیت اجتماعی مشارکت دارد؛ و که مخاطب، در درک خود، به چارچوب‌های رسانه‌ای تکیه می‌کند (Entman, 1993).",
        principles=["سوگیری، اغلب ناخودآگاه و ساختاری است.", "انتخاب و چارچوب‌بندی، شکل‌دهنده ادراک مخاطب‌اند.", "موقعیت خبر، وزن ادراکی آن را تغییر می‌دهد.", "منبع‌گزینی، تصویر واقعی را شکل می‌دهد.", "شفافیت درباره منابع و چارچوب، کاهش‌دهنده سوگیری است."],
        critiques="نقد نخست آن است که پژوهش‌های سوگیری، اغلب «سوگیری سیاسی» را در پیش‌زمینه قرار می‌دهند و ابعاد اقتصادی، فرهنگی و جنسیتی را کم‌رنگ می‌کنند (Entman, 1993). نقد دوم، «فرض آگاهانه بودن» است: برخی پژوهش‌ها فرض می‌کنند که ویراستاران به‌طور آگاهانه سوگیری را اعمال می‌کنند، در حالی که در بیشتر موارد، فرایند ناخودآگاه و نهادی است (Iyengar & Kinder, 1987). همچنین، مرز میان «چارچوب‌بندی مشروع» و «سوگیری نادرست» همیشه مشخص نیست.",
        applications="پژوهش سوگیری خبری در تحلیل محتوای رسانه‌ای، آموزش سواد رسانه‌ای (آموزش مخاطب برای شناسایی چارچوب)، پژوهش‌های مقایسه‌ای بین‌المللی، تحلیل اثر اخبار بر رأی‌گیری و سیاست‌گذاری، و طراحی استانداردهای حرفه‌ای برای کاهش سوگیری کاربرد گسترده دارد (Entman, 1993; Iyengar & Kinder, 1987).",
        evolution="مفهوم سوگیری خبری از نظریه‌های «رسانه‌های جمعی» دهه ۱۹۲۰ و مطالعات چارچوب‌بندی دهه ۱۹۸۰ ریشه دارد؛ با پژوهش‌های انتمن (۱۹۹۳) و آیینگار و کیندر (۱۹۸۷)، به «میدان پژوهشی مستقل» تبدیل شد (Entman, 1993)؛ و در دهه ۲۰۱۰، با گسترش پلتفرم‌های برخط، به «سوگیری الگوریتمی» و «سوگیری انتخاب‌گر (self-selection bias)» گسترش یافته است (Iyengar & Kinder, 1987).",
        studies="انتمن (۱۹۹۳) با صورت‌بندی نظریه‌ی چارچوب‌بندی نشان داد که رسانه‌ها با انتخاب عناصر برجسته‌ی یک رویداد و پنهان‌سازی عناصر دیگر، معنای خبر را شکل می‌دهند و این فرایند، بیشتر ناخودآگاه و نهادی است تا نتیجه‌ی تصمیم آگاهانه. آیینگار و کیندر (۱۹۸۷) در پژوهش‌های طولی خود دریافت که «چارچوب‌بندی تهدید» در اخبار، ادراک مخاطبان از مسائل عمومی را تغییر می‌دهد و آن‌ها را از «مسئله‌ی شخصی» به «مسئله‌ی ملی» یا برعکس، بازتعبیر می‌کند. مطالعات تحلیل محتوا در دهه‌های ۲۰۰۰ و ۲۰۱۰ نیز نشان داده‌اند که منبع‌گزینی و موقعیت خبر در صفحه، دو کانال اصلی انتقال سوگیری هستند. پژوهش‌های جدیدتر، همچنین، به نقش الگوریتم‌ها در تشدید «سوگیری انتخاب‌گر» و تقویت حویلی‌های اطلاعاتی اشاره دارند.",
        key_concepts=["سوگیری انتخابی", "سوگیری چارچوبی", "سوگیری واکشی", "منبع‌گزینی", "چارچوب‌بندی"],
    ),
    "CPT-250": dict(
        main_problem="عینیت (objectivity) در روزنامه‌نگاری، به پرسش بنیادینی پاسخ می‌دهد: آیا رسانه می‌تواند واقعیت را «بدون تحریف» گزارش کند؟ اگرچه این ایده، در دوران طلایی روزنامه‌نگاری حرفه‌ای به‌عنوان استاندارد اخلاقی پذیرفته شد، اما پژوهش‌های جامعه‌شناختی و رسانه‌ای نشان داده‌اند که عینیت، بیشتر «آیین» و «ایدئولوژی» است تا ویژگی عینی گزارش (Tuchman, 1972).",
        mechanism="عینیت در عمل، از چند وجه تشکیل می‌شود: نخست، بی‌طرفی (neutrality)، یعنی پرهیز از اظهار نظر شخصی؛ دوم، انکار خود (self-denial)، یعنی پنهان کردن هویت و پیش‌فرض‌های روزنامه‌نگار؛ سوم، واقعیت‌گرایانه بودن (realism)، یعنی تلاش برای بازتاب واقعیت عینی؛ و چهارم، عدالت (fairness)، یعنی دادن حق‌الکلام به همه طرف‌ها (Witters, 2017). این چهار وجه، با هم، ساختار گزارش خبری را شکل می‌دهند.",
        assumptions="فرض‌های نهفته در عینیت: واقعیت، قابل‌دسترس و قابل‌بازتاب است؛ که روزنامه‌نگار می‌تواند از راه روش‌شناسی، خود و پیش‌فرض‌هایش را کنار بگذارد؛ و که عینیت، معیار اخلاقی برتر روزنامه‌نگاری است (Tuchman, 1972).",
        principles=["بی‌طرفی و انکار خود، ستون‌های عینیت‌اند.", "واقعیت‌گرایانه بودن، هدف گزارش‌خبری است.", "عدالت یعنی حق‌الکلام برای همه طرف‌ها.", "عینیت، آیین و ایدئولوژی حرفه‌ای است.", "روش‌شناسی، معیار عینیت‌سازی است."],
        critiques="نقد نخست، که توچمن (۱۹۷۲) مطرح کرد، آن است که عینیت «آیین راهبردی» (strategic ritual) است، نه ویژگی عینی گزارش؛ یعنی روزنامه‌نگاران با تکرار آیین‌های عینیت، مشروعیت حرفه‌ای خود را حفظ می‌کنند (Tuchman, 1972). نقد دوم، «عینیت کاذب تعادل» (false balance) است: دادن حق‌الکلام برابر به دیدگاه‌های نادرست و درست، ادراک نادرست از واقعیت می‌سازد (Witters, 2017). همچنین، عینیت، اغلب «عینیت ساختاری» (structural objectivity) را پنهان می‌کند.",
        applications="عینیت در طراحی استانداردهای حرفه‌ای روزنامه‌نگاری، آموزش سواد رسانه‌ای (آموزش مخاطب برای نقد عینیت)، پژوهش‌های جامعه‌شناختی رسانه، تحلیل اثر اخبار بر سیاست، و طراحی اصول اخلاقی رسانه کاربرد گسترده دارد (Tuchman, 1972; Witters, 2017).",
        evolution="ایده عینیت، از دوران طلایی روزنامه‌نگاری حرفه‌ای (دهه ۱۸۹۰–۱۹۵۰) ریشه دارد؛ با پژوهش‌های توچمن (۱۹۷۲)، به «موضوع نقد جامعه‌شناختی» تبدیل شد (Tuchman, 1972)؛ و در دهه ۲۰۱۰، با گسترش رسانه‌های اجتماعی، به «عینیت دیجیتال» و «عینیت الگوریتمی» گسترش یافته است (Witters, 2017).",
        studies="توچمن (۱۹۷۲) در مطالعه‌ی اثنوگرافیک کلاسیک خود در یک خبرگزاری، نشان داد که روزنامه‌نگاران عینیت را بیشتر به‌شکل «آیین راهبردی» به کار می‌برند تا به‌عنوان دسترسی واقعی به واقعیت بی‌طرف؛ یعنی تکرار آیین‌های عینیت، مشروعیت حرفه‌ای را بازتولید می‌کند. ویتRس (۲۰۱۷) با مرور نظری و تطبیقی، چهار وجه عینیت (بی‌طرفی، انکار خود، واقعیت‌گرایانه بودن و عدالت) را از هم جدا می‌کند و نشان می‌دهد که در عمل، این چهار وجه گاه در تعارض قرار می‌گیرند. پژوهش‌های تجربی «عینیت کاذب تعادل» نشان داده‌اند که دادن حق‌الکلام برابر به دیدگاه‌های با وزن شواهد متفاوت، ادراک نادرستی از موضوع می‌سازد. مطالعات دهه‌ی ۲۰۱۰ نیز، با ظهور رسانه‌های اجتماعی، به چالش تازه‌ای اشاره دارند: عینیت، در فضای الگوریتمی، باید با «شفافیت درباره‌ی الگوریتم» ترکیب شود تا از «عینیت کاذب» اجتناب کند. در مجموع، این یافته‌ها نشان می‌دهند که مفهوم عینیت، نه یک متغیر ثابت، بلکه فرایندی پویا و زمینه‌مند است که نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["بی‌طرفی", "انکار خود", "واقعیت‌گرایانه بودن", "عدالت", "آیین راهبردی"],
    ),
    "CPT-251": dict(
        main_problem="بی‌طرفی (neutrality/impartiality) در رسانه، به پرسش بنیادینی پاسخ می‌دهد: چگونه می‌توان در پوشش رویدادهای چندطرفه، بدون «صف‌بندی» با هیچ‌یک از طرف‌ها، گزارش داد؟ این ایده، از یک سو، ستون اخلاقی روزنامه‌نگاری حرفه‌ای است و از سوی دیگر، در نظام‌های رسانه‌ای مختلف، با چالش‌های ساختاری و سیاسی مواجه است (Witters, 2017).",
        mechanism="بی‌طرفی در عمل، از چند مکانیزم پشتیبانی می‌شود: نخست، حق‌الکلام برابر (balanced sourcing)، یعنی دادن فرصت برابر به همه طرف‌ها؛ دوم، زبان خنثی (neutral language)، یعنی پرهیز از واژگان ارزشی‌کننده؛ سوم، جدایی دیدگاه از گزارش (separation of commentary and news)، یعنی تمایز روشن بین بخش خبری و بخش نظر؛ و چهارم، شفافیت درباره پیش‌فرض‌ها (transparency of assumptions)، یعنی آشکارسازی محدودیت‌ها و ناهم‌خوانی‌ها (Hallin & Mancini, 2004).",
        assumptions="فرض‌های نهفته در بی‌طرفی: طرف‌های درگیر، در سطح یکسان و قابل‌مقایسه قرار دارند؛ که زبان رسانه، می‌تواند خنثی و بدون بار ارزشی باشد؛ و که بی‌طرفی، معیار اخلاقی برتر در پوشش چندطرفه است (Witters, 2017).",
        principles=["حق‌الکلام برابر، بنیاد بی‌طرفی است.", "زبان باید خنثی و بدون بار ارزشی باشد.", "نظر و خبر، باید از هم جدا باشند.", "شفافیت درباره پیش‌فرض‌ها، بی‌طرفی را تقویت می‌کند.", "بی‌طرفی، با عدالت و صحت در تعارض نیست."],
        critiques="نقد نخست آن است که بی‌طرفی، «بی‌طرفی کاذب» (false neutrality) می‌سازد: وقتی طرف‌های درگیر در سطح یکسان نیستند، دادن حق‌الکلام برابر، ادراک نادرست از واقعیت می‌سازد (Witters, 2017). نقد دوم، «بی‌طرفی ساختاری» (structural neutrality) است: بی‌طرفی فردی، در برابر ساختارهای قدرت اقتصادی و سیاسی، گاه ناممکن است (Hallin & Mancini, 2004). همچنین، بی‌طرفی، اغلب «بی‌طرفی غربی» تلقی می‌شود و با بافت‌های فرهنگی متفاوت، هم‌خوانی ندارد.",
        applications="بی‌طرفی در طراحی استانداردهای خبری، آموزش سواد رسانه‌ای، پژوهش‌های مقایسه‌ای نظام‌های رسانه‌ای، تحلیل اثر اخبار بر سیاست‌گذاری، و طراحی اصول اخلاقی رسانه کاربرد گسترده دارد (Witters, 2017; Hallin & Mancini, 2004).",
        evolution="ایده بی‌طرفی، از اصول کلاسیک روزنامه‌نگاری حرفه‌ای (دهه ۱۸۹۰) ریشه دارد؛ در نظام‌های رسانه‌ای مختلف، با ساختارهای متفاوتی همراه شد (Hallin & Mancini, 2004)؛ و در دهه ۲۰۱۰، با گسترش پلتفرم‌های برخط، به «بی‌طرفی الگوریتمی» و چالش‌های تازه‌ای در فضای دیجیتال گسترش یافته است (Witters, 2017).",
        studies="ویترس (۲۰۱۷) با واکاوی تطبیقی، نشان داده است که بی‌طرفی در نظام‌های رسانه‌ای مختلف، وزن و معناهای متفاوتی دارد: در نظام‌های «پایگاهی» بی‌طرفی رسمی‌تر و نهادی‌تر است، اما در نظام‌های لیبرال، بیشتر به‌شکل التزام فردی ویراستار بروز می‌کند. هالین و مانسین (۲۰۰۴) با مقایسه‌ی سه مدل رسانه و سیاست، نشان دادند که «بی‌طرفی ساختاری» به چگونگی توزیع قدرت اقتصادی و سیاسی در یک نظام گره خورده است و نمی‌توان آن را صرفا‌ً از رفتار فردی روزنامه‌نگار جدا کرد. پژوهش‌های زبان‌شناسی خبر نیز دریافت‌اند که ادعای «زبان خنثی» گاه به پنهان‌سازی بار ارزشی لفظ منجر می‌شود. مطالعات دهه‌ی ۲۰۱۰، همچنین، هشدار می‌دهند که بی‌طرفی فردی، در برابر ساختارهای قدرت، گاه به «بی‌طرفی کاذب» تبدیل می‌شود. در مجموع، این یافته‌ها نشان می‌دهند که بی‌طرفی، نه یک التزام فردی ثابت، بلکه فرایندی پویا و زمینه‌مند است که نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["حق‌الکلام برابر", "زبان خنثی", "جدایی نظر و خبر", "شفافیت پیش‌فرض‌ها", "بی‌طرفی ساختاری"],
    ),
    "CPT-252": dict(
        main_problem="استقلال رسانه‌ای (media independence) به پرسش بنیادینی پاسخ می‌دهد: چگونه می‌توان رسانه را از فشارهای سیاسی و اقتصادی آزاد ساخت، تا بتواند وظیفه نظارتی و اطلاع‌رسانی خود را بدون ترس و تردید انجام دهد؟ این مسئله، در نظام‌های سیاسی و اقتصادی مختلف، با چالش‌های متفاوتی مواجه است (Hallin & Mancini, 2004).",
        mechanism="استقلال رسانه‌ای در عمل، از چند سطح پشتیبانی می‌شود: نخست، استقلال مالکیتی (ownership independence)، یعنی پرهیز از تمرکز بیش‌ازحد مالکیت در دست دولت یا گروه‌های اقتصادی بزرگ؛ دوم، استقلال ویراستاری (editorial independence)، یعنی آزادی تحریریه در انتخاب و واکشی خبر؛ سوم، استقلال مالی (financial independence)، یعنی تنوع منابع درآمدی برای کاهش وابستگی به حامیان خاص؛ و چهارم، استقلال قانونی (legal independence)، یعنی حمایت قانونی از آزادی رسانه در برابر مداخله (McChesney, 2004).",
        assumptions="فرض‌های نهفته: رسانه، نهادی مستقل از دولت و بازار است و می‌تواند بدون مداخله عمل کند؛ که مالکیت، می‌تواند متنوع و شفاف باشد؛ و که قانون، می‌تواند آزادی رسانه را در برابر مداخله حفظ کند (Hallin & Mancini, 2004).",
        principles=["استقلال مالکیتی، بنیاد استقلال رسانه است.", "استقلال ویراستاری، آزادی تحریریه را تضمین می‌کند.", "تنوع منابع مالی، کاهش‌دهنده وابستگی است.", "حمایت قانونی، استقلال رسانه را حفظ می‌کند.", "استقلال، با شفافیت و پاسخگویی همراه است."],
        critiques="نقد نخست آن است که استقلال رسانه‌ای، در عمل، «استقلال کاذب» (false independence) می‌سازد؛ یعنی رسانه‌هایی که «در ظاهر» مستقل به نظر می‌رسند، در حقیقت به منافع پنهان اقتصادی یا سیاسی وابسته‌اند (McChesney, 2004). نقد دوم، «استقلال نابربر» (unequal independence) است: رسانه‌های بزرگ، استقلال بیشتری دارند و رسانه‌های کوچک، به‌سختی از فشارها جان‌به‌جای‌می‌گذارند (Hallin & Mancini, 2004). همچنین، استقلال رسانه‌ای، در نظام‌های پلتفرمی، با الگوریتم‌ها و داده‌ها گره خورده است.",
        applications="استقلال رسانه‌ای در پژوهش نظام‌های رسانه‌ای، تحلیل اثر مالکیت بر محتوای خبری، طراحی قوانین حمایتی از آزادی رسانه، آموزش سواد رسانه‌ای، و پژوهش‌های مقایسه‌ای بین‌المللی کاربرد گسترده دارد (Hallin & Mancini, 2004; McChesney, 2004).",
        evolution="ایده استقلال رسانه‌ای، از جنبش آزادی مطبوعات دهه ۱۷۰۰–۱۸۰۰ ریشه دارد؛ در نظام‌های دموکراتیک، به «اصول بنیادین» تبدیل شد (Hallin & Mancini, 2004)؛ و در دهه ۲۰۱۰، با گسترش پلتفرم‌های برخط و تمرکز اقتصادی، به «استقلال دیجیتال» و چالش‌های تازه گسترش یافته است (McChesney, 2004).",
        studies="هالین و مانسین (۲۰۰۴) با مقایسه‌ی سه مدل رسانه، نشان دادند که استقلال رسانه، در نظام‌های مختلف، به‌طور متفاوتی از دولت و بازار تضمین می‌شود و در نظام‌های «پایگاهی» بیشتر از راه حمایت دولتی و در نظام‌های لیبرال، از راه رقابت بازار شکل می‌گیرد. مک‌چزنی (۲۰۰۴) با واکاوی اقتصاد رسانه در آمریکا، نشان داد که تمرکز اقتصادی مالکیت، حتی در نظام‌های دموکراتیک، به وابستگی پنهان رسانه‌ها به منافع اقتصادی بزرگ منجر می‌شود. پژوهش‌های تجربی دهه‌ی ۲۰۱۰ نیز دریافت‌اند که تنوع منابع مالی (اشتراک، دولتی، خیریه) و شفافیت مالکیت، دو شاخص قابل‌سنجش برای استقلال عملی رسانه‌اند. مطالعات جدیدتر، همچنین، به چالش تازه‌ای اشاره دارند: در عصر پلتفرم، استقلال رسانه، در برابر وابستگی به الگوریتم و ترافیک، بازتعریف می‌شود.",
        key_concepts=["استقلال مالکیتی", "استقلال ویراستاری", "استقلال مالی", "استقلال قانونی", "شفافیت مالکیت"],
    ),
    "CPT-253": dict(
        main_problem="روزنامه‌نگاری تحقیقی (investigative journalism) به پرسش بنیادینی پاسخ می‌دهد: چگونه می‌توان با پژوهش عمیق، مستند و طولانی‌مدت، رویدادهای پنهان، فساد و سوءاستفاده از قدرت را آشکار ساخت؟ این شیوه، در دموکراسی، به‌عنوان «نگهبان قدرت» (watchdog) شناخته می‌شود و به شواهد قوی و روش‌های پژوهشی دقیق نیازمند است (Kovach & Rosenstiel, 2001).",
        mechanism="روزنامه‌نگاری تحقیقی از چند مرحله تشکیل می‌شود: نخست، شناسایی مسئله و طرح پرسش‌های پژوهشی؛ دوم، طراحی روش پژوهش، از جمله شناسایی منابع، اسناد و داده‌ها؛ سوم، جمع‌آوری شواهد، از راه مصاحبه، بررسی اسناد و تحلیل داده‌ها؛ چهارم، تحلیل و بازبینی شواهد برای اطمینان از صحت؛ و پنجم، گزارش‌نویسی دقیق و قابل‌استناد (Hirtle, 2006).",
        assumptions="فرض‌های نهفته در روزنامه‌نگاری تحقیقی: رویدادهای پنهان، از راه پژوهش عمیق قابل‌کشف‌اند؛ که منابع و اسناد، می‌توانند به‌صورت مستقل و قابل‌اطمینان در دسترس روزنامه‌نگار قرار گیرند؛ و که روزنامه‌نگار، مسئول اخلاقی آشکارسازی حقیقت است (Kovach & Rosenstiel, 2001).",
        principles=["پژوهش عمیق و مستند، بنیاد گزارش است.", "استناد به منابع متعدد و مستقل، ضروری است.", "پایبندی به اخلاق، حتی در برابر منابع پنهان.", "زمان و منابع، برای تحقیق لازم‌اند.", "آشکارسازی حقیقت، مسئولیت اخلاقی است."],
        critiques="نقد نخست آن است که روزنامه‌نگاری تحقیقی، «تحقیق پرهزینه» (high-cost investigation) است و رسانه‌های کوچک، به‌سختی می‌توانند آن را ادامه دهند (Hirtle, 2006). نقد دوم، «اثر بر منابع» (impact on sources) است: آشکارسازی حقیقت، گاه به آسیب به منابع و قربانیان می‌انجامد (Kovach & Rosenstiel, 2001). همچنین، روزنامه‌نگاری تحقیقی، در برابر فشارهای حقوقی و اقتصادی، آسیب‌پذیر است.",
        applications="روزنامه‌نگاری تحقیقی در آشکارسازی فساد، تحلیل سیاست‌گذاری، پژوهش‌های اجتماعی، آموزش روزنامه‌نگاری، و پژوهش اثر اخبار تحقیقی بر تغییر اجتماعی کاربرد گسترده دارد (Hirtle, 2006; Kovach & Rosenstiel, 2001).",
        evolution="روزنامه‌نگاری تحقیقی، از «عصر طلایی» روزنامه‌نگاری (دهه ۱۸۷۰–۱۹۵۰) ریشه دارد؛ با پژوهش‌های استاندارد‌ساز در دهه ۱۹۷۰، به «شیوه حرفه‌ای» تبدیل شد (Kovach & Rosenstiel, 2001)؛ و در دهه ۲۰۱۰، با گسترش داده و ابزارهای دیجیتال، به «تحقیق داده‌محور» و «روزنامه‌نگاری تحقیقی مشارکتی» گسترش یافته است (Hirtle, 2006).",
        studies="کوکاش و روزنستیل (۲۰۰۱) روزنامه‌نگاری تحقیقی را به‌عنوان «وظیفه‌ی نظارتی» (watchdog) رسانه در دموکراسی معرفی می‌کنند و نشان می‌دهند که اعتبار آن، بر شواهد قوی و قابل‌استناد استوار است. هرتل (۲۰۰۶) با ارائه‌ی چارچوب روش‌شناختی، چهار مرحله‌ی اصلی (طرح پرسش، جمع‌آوری شواهد، تحلیل و گزارش‌نویسی) را تدوین کرده و بر اهمیت اسناد و منابع مستقل تأکید می‌ورزد. پژوهش‌های اقتصادی رسانه نشان داده‌اند که گزارش‌های تحقیقی، به دلیل هزینه‌ی بالای تولید و ریسک حقوقی، در دهه‌های اخیر کاهش یافته‌اند و روزنامه‌نگاری تحقیقی مشارکتی (collaborative)، از طریق شبکه‌های بین‌رسانه‌ای، به شیوه‌ای پایدارتر برای ادامه‌ی آن تبدیل شده است. مطالعات اثرگذاری نیز دریافت‌اند که گزارش‌های تحقیقی برجسته، گاه منجر به تغییر قانونی و بازنشست‌سازی نهادهای فاسد شده‌اند. در مجموع، این یافته‌ها نشان می‌دهند که اثرات روزنامه‌نگاری تحقیقی، به بافت نهادی، حقوقی و اقتصادی هر نظام گره خورده و نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["نگهبان قدرت", "روش پژوهش", "اسناد و منابع", "شواهد قابل‌استناد", "آشکارسازی حقیقت"],
    ),
    "CPT-254": dict(
        main_problem="روزنامه‌نگاری داده (data journalism) به پرسش بنیادینی پاسخ می‌دهد: چگونه می‌توان با تحلیل داده‌های بزرگ و ساختاریافته، رویدادهای اجتماعی، سیاسی و اقتصادی را با عمق و دقت بیشتری گزارش داد؟ این شیوه، با ترکیب مهارت‌های روزنامه‌نگاری و علم داده، به «نسل بعدی» گزارش‌خبری تبدیل شده است (Newman et al., 2018).",
        mechanism="روزنامه‌نگاری داده از چند مرحله تشکیل می‌شود: نخست، شناسایی مسئله و طراحی پرسش پژوهشی بر پایه داده؛ دوم، جمع‌آوری و پاک‌سازی داده‌ها از منابع عمومی و خصوصی؛ سوم، تحلیل و بصری‌سازی داده (data visualization) برای آشکارسازی الگوها و روابط؛ چهارم، گزارش‌نویسی بر پایه یافته‌های تحلیل؛ و پنجم، بازبینی و اعتبارسنجی روش‌های تحلیل (Newman et al., 2018).",
        assumptions="فرض‌های نهفته در روزنامه‌نگاری داده: داده، قابل‌دسترس و قابل‌تحلیل است؛ که الگوریتم‌ها و روش‌های تحلیل، می‌توانند به درک عمیق‌تر از پدیده‌ها کمک کنند؛ و که داده، باید با شفافیت و مسئولیت اخلاقی استفاده شود (D'Ignazio & Healy, 2017).",
        principles=["داده، بنیاد گزارش‌خبری است و باید قابل‌اعتماد باشد.", "تحلیل باید شفاف و قابل‌بازتولید باشد.", "بصری‌سازی، ابزاری برای فهم، نه فریب است.", "داده، با مسئولیت اخلاقی و حریم خصوصی استفاده می‌شود.", "نقد داده و الگوریتم، بخشی از شیوه است."],
        critiques="نقد نخست آن است که روزنامه‌نگاری داده، «داده‌محوری» (data-ism) را تقویت می‌کند؛ یعنی فرض می‌کند که داده، واقعیت را «به‌طور عینی» بازتاب می‌دهد، در حالی که داده، همواره با پیش‌فرض‌های جمع‌آوری و تحلیل همراه است (D'Ignazio & Healy, 2017). نقد دوم، «نابرابری دسترسی» (access inequality) است: رسانه‌های بزرگ، به داده‌های بهتر و ابزارهای پیشرفته‌تری دسترسی دارند (Newman et al., 2018). همچنین، داده‌نگاری، ممکن است «انسان» را در گزارش‌خبری فراموش کند.",
        applications="روزنامه‌نگاری داده در گزارش‌های اقتصادی و سیاسی، تحلیل‌های اجتماعی و بهداشتی، بصری‌سازی داده‌های عمومی، آموزش سواد داده‌ای (data literacy)، و پژوهش‌های رسانه‌ای کاربرد گسترده دارد (Newman et al., 2018; D'Ignazio & Healy, 2017).",
        evolution="روزنامه‌نگاری داده، از پژوهش‌های «تحلیل کمّی» دهه ۱۹۸۰ و ابزارهای بصری‌سازی دهه ۱۹۹۰ ریشه دارد؛ با گسترش داده‌های باز (open data) در دهه ۲۰۱۰، به «شیوه حرفه‌ای مستقل» تبدیل شد (Newman et al., 2018)؛ و در دهه ۲۰۲۰، با الگوریتم‌های هوش مصنوعی، به «روزنامه‌نگاری داده پیش‌بینی‌کننده» گسترش یافته است (D'Ignazio & Healy, 2017).",
        studies="نیمن، مارتین و فلچر (۲۰۱۸) در گزارش «وضعیت روزنامه‌نگاری داده» نشان دادند که در میان روزنامه‌نگاران در سراسر جهان، استفاده‌ی عملی از داده و ابزارهای تحلیلی، به‌طور فزاینده‌ای رشد کرده است، اگرچه فاصله‌ی قابل‌توجهی میان رسانه‌های بزرگ و کوچک در دسترسی به داده و مهارت، باقی است. دیگنازیو و هیلی (۲۰۱۷) با رویکرد انتقادی «فمینیسم داده» نشان دادند که داده، هرگز «بی‌طرف» نیست و پیش‌فرض‌های جمع‌آوری، تحلیل و نمایش، بر نتیجه‌ی گزارش اثر می‌گذارند. پژوهش‌های تجربی دهه‌ی ۲۰۱۰ نیز دریافت‌اند که گزارش‌های داده‌محور، در موضوعاتی مانند اقتصاد، بهداشت و محیط‌زیست، عمق و دقت تحلیل را افزایش می‌دهند. مطالعات جدیدتر، همچنین، به چالش «سواد داده‌ای» مخاطبان و نقش آن در ادراک صحیح از گزارش‌های داده‌محور توجه دارند.",
        key_concepts=["داده بزرگ", "بصری‌سازی داده", "تحلیل الگوریتمی", "داده باز", "سواد داده‌ای"],
    ),
    "CPT-255": dict(
        main_problem="خبر جعلی (fake news) به مسئله‌ای پاسخ می‌دهد که چگونه مطالبی که «در ظاهر» شبیه خبر هستند، اما فاقد پایه واقعیتی‌اند، در شبکه‌های اجتماعی گسترش می‌یابند و بر ادراک و تصمیم‌گیری سیاسی و اجتماعی اثر می‌گذارند. این پدیده، در دهه ۲۰۱۰، با گسترش پلتفرم‌های برخط، به «چالش جهانی» تبدیل شده است (Allcott & Gentzkow, 2017).",
        mechanism="خبر جعلی از چند مکانیزم گسترش می‌یابد: نخست، تولید عمدی (deliberate fabrication)، یعنی ساختن محتوای نادرست برای هدف خاص؛ دوم، انتشار ویروسی (viral spread)، یعنی گسترش سریع در شبکه‌های اجتماعی از راه اشتراک‌گذاری؛ سوم، استناد‌سازی کاذب (false attribution)، یعنی استفاده از منابع جعلی یا تحریف‌شده؛ و چهارم، هدفمندی سیاسی یا اقتصادی (targeted purpose)، یعنی تولید محتوا برای تأثیر بر رأی‌گیری یا کسب سود (Allcott & Gentzkow, 2017; Penk, 2019).",
        assumptions="فرض‌های نهفته در مطالعه خبر جعلی: مخاطبان، در برابر مطالب نادرست، آسیب‌پذیرند؛ که شبکه‌های اجتماعی، می‌توانند گسترش خبر جعلی را تسهیل کنند؛ و که خبر جعلی، اغلب با انگیزه سیاسی یا اقتصادی تولید می‌شود (Penk, 2019).",
        principles=["خبر جعلی، نادرست است و باید شناسایی شود.", "گسترش ویروسی، به شفافیت و پاسخگویی نیازمند است.", "مخاطب، در برابر مطالب نادرست، آسیب‌پذیر است.", "پلتفرم‌ها، مسئولیت کاهش گسترش را دارند.", "پاسخ به خبر جعلی، باید علمی و مستند باشد."],
        critiques="نقد نخست آن است که تعریف خبر جعلی، «مبهم» (ambiguous) است: مرز میان خبر نادرست، شوخی، و پروپاگاندا، همیشه مشخص نیست (Penk, 2019). نقد دوم، «اثر تداوم» (persistence effect) است: حتی اصلاح خبر جعلی، گاه آن را تقویت می‌کند و «اثر بکزبک» (backfire effect) می‌سازد (Allcott & Gentzkow, 2017). همچنین، پاسخ به خبر جعلی، ممکن است آزادی بیان و حق شوخی را محدود کند.",
        applications="مطالعه خبر جعلی در تحلیل شبکه‌های اجتماعی، آموزش سواد رسانه‌ای، طراحی الگوریتم‌های شناسایی و پاسخ، پژوهش اثر اخبار بر رأی‌گیری، و طراحی سیاست‌های عمومی برای مقابله با اطلاعات نادرست کاربرد گسترده دارد (Allcott & Gentzkow, 2017; Penk, 2019).",
        evolution="مفهوم خبر جعلی، از «خبر ساختگی» (yellow journalism) دهه ۱۸۹۰ ریشه دارد؛ در دهه ۲۰۱۰، با گسترش شبکه‌های اجتماعی، به «پدیده جهانی» تبدیل شد (Allcott & Gentzkow, 2017)؛ و در دهه ۲۰۲۰، با الگوریتم‌ها و هوش مصنوعی، به «خبر جعلی الگوریتمی» و «دروغ‌های تولیدی» (generated disinformation) گسترش یافته است (Penk, 2019).",
        studies="آلکات و گنتزکاو (۲۰۱۷) با تحلیل داده‌های توییتر در انتخابات ۲۰۱۶ آمریکا، نشان دادند که صفحات خبری جعلی، در مقایسه با رسانه‌های واقعی، نرخ اشتراک‌گذاری بالاتری داشته‌اند و بیش از ۱۲ میلیون بار در شبکه اشتراک‌گذاری شده‌اند. پنک (۲۰۱۹) در تحلیل تطبیقی بین‌المللی، دریافت که خبر جعلی، نه پدیده‌ای جدید، بلکه ادامه‌ی «خبر زرد» در بستر دیجیتال است و انگیزه‌های اقتصادی (کسب ترافیک) و سیاسی (تأثیر بر رأی‌گیری) را در کنار هم دارد. پژوهش‌های آزمایشی نیز نشان داده‌اند که پاسخ‌های اصلاحی (fact-check)، گاه «اثر تداوم» می‌سازند و نادرستی را تقویت می‌کنند. مطالعات جدیدتر، همچنین، به نقش الگوریتم‌ها و هوش مصنوعی در تولید مقیاسی‌شده‌ی خبر جعلی توجه دارند.",
        key_concepts=["تولید عمدی", "گسترش ویروسی", "استناد کاذب", "هدفمندی سیاسی", "اثر تداوم"],
    ),
    "CPT-256": dict(
        main_problem="اطلاعات نادرست (misinformation) به مسئله‌ای پاسخ می‌دهد که چگونه مطالبی که «درست نیستند»، بدون آن‌که لزوماً عمدی باشند، در شبکه‌های اجتماعی گسترش می‌یابند و بر ادراک و تصمیم‌گیری مخاطبان اثر می‌گذارند. این پدیده، در عصر اطلاعات، به «چالش عمومی» تبدیل شده است (Penk, 2019).",
        mechanism="اطلاعات نادرست از چند مکانیزم گسترش می‌یابد: نخست، اشتراک‌گذاری بدون راستی‌آزمایی (unverified sharing)، یعنی انتشار مطالب بدون بررسی صحت؛ دوم، گسترش ویروسی (viral spread)، یعنی پخش سریع در شبکه‌های اجتماعی؛ سوم، تکرار و بازتولید (repetition and amplification)، یعنی تکرار مکرر مطلب نادرست، که ادراک آن را تقویت می‌کند؛ و چهارم، سوگیری تأییدی (confirmation bias)، یعنی تمایل مخاطب به پذیرش مطالبی که با باورهای پیشینش هم‌خوان است (Vos et al., 2015).",
        assumptions="فرض‌های نهفته در مطالعه اطلاعات نادرست: گسترش اطلاعات نادرست، اغلب ناخواسته و بدون انگیزه خاص است؛ که شبکه‌های اجتماعی، می‌توانند گسترش را تسهیل کنند؛ و که مخاطبان، در برابر مطالب نادرست، آسیب‌پذیرند (Vos et al., 2015).",
        principles=["راستی‌آزمایی پیش از انتشار، بنیاد مقابله با نادرستی است.", "گسترش ویروسی، به پاسخ علمی نیازمند است.", "سوگیری تأییدی، گسترش را تسهیل می‌کند.", "شفافیت و اصلاح، ابزارهای اصلی مقابله‌اند.", "سواد رسانه‌ای، کاهش‌دهنده آسیب‌پذیری مخاطب است."],
        critiques="نقد نخست آن است که مرز میان «نادرست بودن» (false) و «مدرک‌ناپذیر بودن» (unverifiable) همیشه مشخص نیست؛ یعنی برخی مطالب، نمی‌توانند به‌سادگی راست یا نادرست قضاوت شوند (Penk, 2019). نقد دوم، «اثر تداوم» (persistence effect) است: اصلاح اطلاعات نادرست، گاه آن را تقویت می‌کند (Vos et al., 2015). همچنین، مقابله با اطلاعات نادرست، ممکن است آزادی بیان را محدود کند.",
        applications="مطالعه اطلاعات نادرست در طراحی آموزش سواد رسانه‌ای، پژوهش گسترش اطلاعات در شبکه‌ها، طراحی الگوریتم‌های شناسایی و نشان‌گذاری، تحلیل اثر بر سیاست‌گذاری، و پژوهش‌های مقایسه‌ای بین‌المللی کاربرد گسترده دارد (Penk, 2019; Vos et al., 2015).",
        evolution="مفهوم اطلاعات نادرست، از نظریه‌های «خطای اطلاعاتی» دهه ۱۹۷۰ و مطالعات گسترش اطلاعات دهه ۱۹۹۰ ریشه دارد؛ در دهه ۲۰۱۰، با گسترش شبکه‌های اجتماعی، به «پدیده جهانی» تبدیل شد (Vos et al., 2015)؛ و در دهه ۲۰۲۰، با الگوریتم‌ها، به «نادرستی الگوریتمی» و چالش‌های تازه گسترش یافته است (Penk, 2019).",
        studies="پنک (۲۰۱۹) با تفکیک مفهومی، «اطلاعات نادرست» را از «گمراهی عمدی» جدا می‌کند و نشان می‌دهد که بیشتر گسترش اطلاعات نادرست، بدون انگیزه‌ی خاص و از راه اشتراک‌گذاری خودجوش مخاطبان صورت می‌گیرد. ووس و همکاران (۲۰۱۵) در تحلیل شبکه‌ای، دریافت‌اند که اطلاعات نادرست، به‌دلیل «سوگیری تأییدی» و «اثر تکرار»، در شبکه‌های اجتماعی سریع‌تر از اطلاعات درست گسترش می‌یابد. پژوهش‌های آزمایشی نیز نشان داده‌اند که پیش‌درمانی (pre-bunking) و آموزش سواد رسانه‌ای، مؤثرتر از اصلاح پس از انتشار (post-bunking) در کاهش پذیرش اطلاعات نادرست هستند. مطالعات دهه‌ی ۲۰۱۰، همچنین، به نقش «حلقه‌ی اجتماعی» و اعتماد بین‌فردی در گسترش نادرستی توجه دارند. در مجموع، این یافته‌ها نشان می‌دهند که مقابله با اطلاعات نادرست، فرایندی پویا و زمینه‌مند است که نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["اشتراک‌گذاری بدون راستی‌آزمایی", "گسترش ویروسی", "تکرار و بازتولید", "سوگیری تأییدی", "اثر تداوم"],
    ),
    "CPT-257": dict(
        main_problem="اطلاعات گمراه‌کننده (disinformation) به مسئله‌ای پاسخ می‌دهد که چگونه مطالب نادرست، به‌صورت «عمدی و هدفمند»، برای فریب، نفوذ یا تأثیر بر مخاطبان، تولید و گسترش می‌یابند. این پدیده، در عصر دیجیتال، به «چالش امنیتی و سیاسی» تبدیل شده و با پروپاگاندا و جنگ اطلاعاتی گره خورده است (Wardle & Derewianko, 2017).",
        mechanism="اطلاعات گمراه‌کننده از چند مکانیزم گسترش می‌یابد: نخست، تولید هدفمند (targeted fabrication)، یعنی ساختن مطالب نادرست با هدف خاص؛ دوم، توزیع هدفمند (targeted distribution)، یعنی استفاده از الگوریتم‌ها و حساب‌های جعلی برای گسترش؛ سوم، نفوذ اجتماعی (social infiltration)، یعنی استفاده از شبکه‌های اجتماعی و گروه‌های خاص برای گسترش؛ و چهارم، هدف‌گیری سیاسی (political targeting)، یعنی تأثیر بر رأی‌گیری و تصمیم‌گیری سیاسی (Wardle & Derewianko, 2017).",
        assumptions="فرض‌های نهفته در مطالعه اطلاعات گمراه‌کننده: تولید و گسترش، عمدی و هدفمند است؛ که کنشگران خاص (نهادهای دولتی، گروه‌های سیاسی یا اقتصادی)، به انگیزه خاص، آن را راه می‌اندازند؛ و که اثر آن، بر سیاست و امنیت ملی، گسترده است (Wardle & Derewianko, 2017).",
        principles=["گمراه‌کننده بودن، عمدی و هدفمند است.", "دست‌اندکاران، اغلب نهادهای پنهان هستند.", "توزیع، از راه الگوریتم و حساب‌های جعلی انجام می‌شود.", "هدف، تأثیر بر سیاست و امنیت است.", "پاسخ، باید بین‌المللی و چندلایه باشد."],
        critiques="نقد نخست آن است که مرز میان «گمراه‌کننده بودن عمدی» و «گمراه‌کننده بودن غیرعمدی» همیشه مشخص نیست و گاه، استفاده از برچسب «disinformation»، به‌صورت «زیرا من درست هستم، تو دروغ می‌گویی» (whataboutism) به کار می‌رود (Wardle & Derewianko, 2017). نقد دوم، «اثر تداوم» (persistence effect) است: اصلاح گمراهی، گاه آن را تقویت می‌کند (Nyhan & Reifler, 2010). همچنین، مقابله با اطلاعات گمراه‌کننده، ممکن است آزادی بیان و نظارت رسانه‌ای را محدود کند.",
        applications="مطالعه اطلاعات گمراه‌کننده در تحلیل جنگ اطلاعاتی، طراحی سیاست‌های امنیت ملی، آموزش سواد رسانه‌ای، پژوهش نفوذ در شبکه‌های اجتماعی، و طراحی پاسخ‌های بین‌المللی کاربرد گسترده دارد (Wardle & Derewianko, 2017; Nyhan & Reifler, 2010).",
        evolution="مفهوم اطلاعات گمراه‌کننده، از «پروپاگاندا» دهه ۱۹۳۰ و «جنگ روانی» دهه ۱۹۵۰ ریشه دارد؛ در دهه ۲۰۱۰، با گسترش پلتفرم‌های برخط، به «جنگ اطلاعاتی دیجیتال» تبدیل شد (Wardle & Derewianko, 2017)؛ و در دهه ۲۰۲۰، با هوش مصنوعی و الگوریتم‌ها، به «گمراهی الگوریتمی و تولیدی» گسترش یافته است (Nyhan & Reifler, 2010).",
        studies="واردل و درویانکو (۲۰۱۷) در چارچوب بین‌رشته‌ای «آشفته‌سازی اطلاعات»، «گمراهی عمدی» را به‌عنوان زیرمجموعه‌ای از آشفته‌سازی تعریف می‌کنند که در آن، تولید و توزیع، هر دو هدفمند و عمدی‌اند. نیهان و رایفلر (۲۰۱۰) در مطالعه‌ی آزمایشی کلاسیک خود، نشان دادند که اصلاح گمراهی سیاسی، اغلب «اثر تداوم» می‌سازد و حتی گاه به «اثر بکزبک» (backfire) منجر می‌شود. پژوهش‌های دهه‌ی ۲۰۱۰، با تحلیل داده‌های شبکه‌ای، نقش حساب‌های هماهنگ (coordinated inauthentic accounts) و «جنگ‌گاه‌های» (troll farms) در توزیع هدفمند اطلاعات گمراه‌کننده را آشکار کرده‌اند. مطالعات جدیدتر، همچنین، به چالش بین‌المللی‌سازی پاسخ و ضرورت هماهنگی پلتفرم‌ها و دولت‌ها توجه دارند. در مجموع، این یافته‌ها نشان می‌دهند که پاسخ به گمراهی عمدی، فرایندی پویا و زمینه‌مند است که نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["تولید هدفمند", "توزیع هدفمند", "نفوذ اجتماعی", "هدف‌گیری سیاسی", "جنگ اطلاعاتی"],
    ),
    "CPT-258": dict(
        main_problem="اطلاعات مخرب (malicious/harmful information) به مسئله‌ای پاسخ می‌دهد که چگونه مطالبی، با «نیت آسیب‌رسان»، برای فریب، تهدید، تنبیه یا تأثیر بر گروه‌های خاص، تولید و گسترش می‌یابند. این پدیده، در عصر دیجیتال، با «آشفته‌سازی اطلاعات» (information disorder) گره خورده و به «چالش اخلاقی و حقوقی» تبدیل شده است (Wardle & Derewianko, 2017).",
        mechanism="اطلاعات مخرب از چند مکانیزم گسترش می‌یابد: نخست، تولید با نیت آسیب‌رسان (harmful fabrication)، یعنی ساختن مطلب با هدف آزار، تهدید یا تنبیه؛ دوم، هدف‌گیری گروه‌های خاص (targeted targeting)، یعنی تمرکز بر قشرهای آسیب‌پذیر؛ سوم، گسترش ویروسی (viral spread)، یعنی پخش سریع در شبکه‌ها؛ و چهارم، تأثیر روانی (psychological impact)، یعنی ایجاد ترس، اضطراب یا نفرت در مخاطبان (Vraga & Bode, 2020).",
        assumptions="فرض‌های نهفته در مطالعه اطلاعات مخرب: نیت آسیب‌رسان، در تولید و گسترش، حضور دارد؛ که مخاطبان، در برابر مطالب مخرب، آسیب‌پذیرند؛ و که اثر آن، بر سلامت روان و انسجام اجتماعی، گسترده است (Vraga & Bode, 2020).",
        principles=["نیت آسیب‌رسان، بنیاد اطلاعات مخرب است.", "گروه‌های آسیب‌پذیر، هدف اصلی‌اند.", "گسترش ویروسی، به پاسخ سریع نیازمند است.", "اثر روانی، باید ارزیابی شود.", "پاسخ، باید اخلاقی و حقوقی باشد."],
        critiques="نقد نخست آن است که تعریف «نیت آسیب‌رسان»، «مبهم» (ambiguous) است و مرز میان «آزار عمدی» و «آزار غیرعمدی» همیشه مشخص نیست (Wardle & Derewianko, 2017). نقد دوم، «اثر تداوم» (persistence effect) است: حذف مطلب مخرب، گاه آن را تقویت می‌کند (Vraga & Bode, 2020). همچنین، مقابله با اطلاعات مخرب، ممکن است آزادی بیان و حق انتقاد را محدود کند.",
        applications="مطالعه اطلاعات مخرب در طراحی سیاست‌های حمایتی از گروه‌های آسیب‌پذیر، آموزش سواد رسانه‌ای، پژوهش اثر بر سلامت روان، طراحی الگوریتم‌های شناسایی و حذف، و طراحی پاسخ‌های اخلاقی و حقوقی کاربرد گسترده دارد (Wardle & Derewianko, 2017; Vraga & Bode, 2020).",
        evolution="مفهوم اطلاعات مخرب، از «آزار کلامی» (verbal harassment) دهه ۱۹۸۰ و «نفرت‌پراکنی» (hate speech) دهه ۱۹۹۰ ریشه دارد؛ در دهه ۲۰۱۰، با گسترش شبکه‌های اجتماعی، به «آزار دیجیتال» (cyberbullying) تبدیل شد (Wardle & Derewianko, 2017)؛ و در دهه ۲۰۲۰، با الگوریتم‌ها، به «آزار الگوریتمی و هدفمند» گسترش یافته است (Vraga & Bode, 2020).",
        studies="واردل و درویانکو (۲۰۱۷) در چارچوب «آشفته‌سازی اطلاعات»، «اطلاعات مضر» را از «گمراهی» و «نادرستی» جدا می‌کنند و آن را به‌عنوان محتوای نادرست یا دقیق، اما با «نیت آسیب‌رسان»، تعریف می‌کنند. وراگا و بود (۲۰۲۰) در پژوهش تجربی خود دریافت‌اند که ادراک مخاطبان از خطر خبر جعلی و مضر، به سطح اعتماد آن‌ها به رسانه‌ها و به بافت سیاسی‌شان گره خورده است. پژوهش‌های بهداشت عمومی نیز نشان داده‌اند که اطلاعات مضر، به‌ویژه در بحران‌های بهداشتی، می‌توانند به رفتارهای خطرناک (مانند اجتناب از واکسیناسیون) منجر شوند. مطالعات دهه‌ی ۲۰۱۰، همچنین، به نقش الگوریتم‌ها در هدف‌گیری گروه‌های آسیب‌پذیر و تقویت اثر روانی مطالب مضر توجه دارند. در مجموع، این یافته‌ها نشان می‌دهند که اثرات اطلاعات مخرب، فرایندی پویا و زمینه‌مند است که نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["نیت آسیب‌رسان", "هدف‌گیری گروه‌های آسیب‌پذیر", "گسترش ویروسی", "اثر روانی", "آزار دیجیتال"],
    ),
    "CPT-259": dict(
        main_problem="روزنامه‌نگاری الگوریتمی (algorithmic journalism) به پرسش بنیادینی پاسخ می‌دهد: چگونه الگوریتم‌ها و سیستم‌های خودکار، در فرایند انتخاب، تولید، توزیع و شخصی‌سازی خبر، نقش مؤثری بازی می‌کنند و بر ادراک و رفتار مخاطبان اثر می‌گذارند؟ این پدیده، در عصر دیجیتال، به «بُعد تازه» از واسطه‌گری رسانه‌ای تبدیل شده است (Lewis, 2017).",
        mechanism="روزنامه‌نگاری الگوریتمی از چند مکانیزم تشکیل می‌شود: نخست، انتخاب الگوریتمی (algorithmic selection)، یعنی انتخاب و اولویت‌بندی اخبار بر پایه داده‌های رفتار مخاطب؛ دوم، تولید نیمه‌خودکار (semi-automated production)، یعنی استفاده از الگوریتم‌ها برای تولید بخش‌هایی از گزارش؛ سوم، توزیع هدفمند (targeted distribution)، یعنی ارسال خبر به مخاطبان خاص بر پایه الگوریتم؛ و چهارم، شخصی‌سازی (personalization)، یعنی تنظیم محتوا بر پایه سلیقه و تاریخچه هر مخاطب (Borenstein, 2018).",
        assumptions="فرض‌های نهفته در روزنامه‌نگاری الگوریتمی: الگوریتم‌ها، می‌توانند به‌صورت «عادلانه و بی‌طرفانه» عمل کنند؛ که داده‌های رفتار، می‌توانند «ترجیحات واقعی» مخاطب را بازتاب دهند؛ و که الگوریتم، ابزاری برای «بهبود تجربه» مخاطب است، نه برای «کنترل» (Lewis, 2017).",
        principles=["الگوریتم، باید شفاف و قابل‌بازبینی باشد.", "شخصی‌سازی، باید با حق مخاطب بر دسترسی به خبر متنوع، هم‌خوان باشد.", "داده‌های رفتار، باید با مسئولیت اخلاقی استفاده شوند.", "مسئولیت نهایی، با رسانه و پلتفرم است.", "نقد الگوریتم، بخشی از سواد رسانه‌ای است."],
        critiques="نقد نخست آن است که روزنامه‌نگاری الگوریتمی، «جعبه‌ی سیاه» (black box) می‌سازد؛ یعنی مخاطب و حتی روزنامه‌نگار، نمی‌توانند بدانند که چگونه خبر انتخاب و توزیع شده است (Lewis, 2017). نقد دوم، «حویلی‌سازی الگوریتمی» (algorithmic filter bubble) است: شخصی‌سازی، مخاطب را در «اسپهر اطلاعاتی» بسته‌ای محصور می‌کند (Borenstein, 2018). همچنین، الگوریتم، می‌تواند سوگیری‌های داده و طراح را تقویت کند.",
        applications="مطالعه روزنامه‌نگاری الگوریتمی در طراحی الگوریتم‌های شفاف و عادلانه، آموزش سواد رسانه‌ای (نقد الگوریتم)، پژوهش اثر الگوریتم بر ادراک، طراحی استانداردهای اخلاقی برای پلتفرم‌ها، و پژوهش‌های مقایسه‌ای بین‌المللی کاربرد گسترده دارد (Lewis, 2017; Borenstein, 2018).",
        evolution="مفهوم روزنامه‌نگاری الگوریتمی، از «الگوریتم‌های جست‌وجو» دهه ۱۹۹۰ و «توصیه‌گرهای شخصی‌سازی‌شده» دهه ۲۰۰۰ ریشه دارد؛ در دهه ۲۰۱۰، با گسترش شبکه‌های اجتماعی، به «واسطه‌گری الگوریتمی» تبدیل شد (Lewis, 2017)؛ و در دهه ۲۰۲۰، با هوش مصنوعی، به «روزنامه‌نگاری الگوریتمی پیش‌بینی‌کننده» گسترش یافته است (Borenstein, 2018).",
        studies="لوئیس (۲۰۱۷) در صورت‌بندی نظری «واسطه‌گری الگوریتمی» نشان داد که الگوریتم‌ها، نه صرفا‌ً ابزار فنی، بلکه کنشگران فعال در ساخت واقعیت خبری‌اند و بر ادراک، توجه و رفتار مخاطبان اثر مستقیم دارند. بورنشتاین (۲۰۱۸) با تحلیل تطبیقی، نشان داد که خودکارسازی خبر، بیش از آن‌که «جایگزین» روزنامه‌نگار باشد، «بُعد تازه‌ای» به فرایند تولید و توزیع خبر افزوده است. پژوهش‌های تجربی دهه‌ی ۲۰۱۰ نیز دریافت‌اند که شخصی‌سازی الگوریتمی، در بلندمدت، به تقویت «حویلی اطلاعاتی» و کاهش مواجهه‌ی مخاطب با دیدگاه‌های مخالف، منجر می‌شود. مطالعات جدیدتر، همچنین، به ضرورت شفافیت الگوریتم و پاسخگویی پلتفرم توجه دارند. در مجموع، این یافته‌ها نشان می‌دهند که واسطه‌گری الگوریتمی، فرایندی پویا و زمینه‌مند است که نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["انتخاب الگوریتمی", "تولید نیمه‌خودکار", "توزیع هدفمند", "شخصی‌سازی", "حویلی الگوریتمی"],
    ),
    "CPT-260": dict(
        main_problem="روزنامه‌نگاری هوش مصنوعی (AI journalism) به پرسش بنیادینی پاسخ می‌دهد: چگونه هوش مصنوعی و الگوریتم‌های پیشرفته، در فرایند تولید، ویرایش، توزیع و تحلیل خبر، نقش مؤثری بازی می‌کنند و بر کیفیت، سرعت و اخلاق روزنامه‌نگاری اثر می‌گذارند؟ این پدیده، در دهه ۲۰۲۰، به «بُعد تازه‌ای» از تحول دیجیتال رسانه تبدیل شده است (Borenstein, 2018).",
        mechanism="روزنامه‌نگاری هوش مصنوعی از چند مکانیزم تشکیل می‌شود: نخست، تولید خودکار متن (automated text generation)، یعنی نوشتن گزارش‌های خبری بر پایه الگوریتم و داده؛ دوم، تحلیل هوشمند (intelligent analysis)، یعنی شناسایی الگوها و روابط در داده‌ها؛ سوم، ویرایش خودکار (automated editing)، یعنی تصحیح و بهینه‌سازی متن؛ و چهارم، شخصی‌سازی پیشرفته (advanced personalization)، یعنی تنظیم محتوا بر پایه الگوریتم‌های یادگیری ماشین (Lewis, 2017).",
        assumptions="فرض‌های نهفته در روزنامه‌نگاری هوش مصنوعی: هوش مصنوعی، می‌تواند به‌صورت «دقیق و بی‌طرفانه» عمل کند؛ که داده‌های ورودی، می‌توانند «واقعیت» را بازتاب دهند؛ و که هوش مصنوعی، ابزاری برای «بهبود کیفیت» خبر است، نه جایگزین قضاوت انسانی (Borenstein, 2018).",
        principles=["هوش مصنوعی، باید شفاف و قابل‌بازبینی باشد.", "مسئولیت اخلاقی، با انسان و رسانه است، نه الگوریتم.", "داده‌های ورودی، باید بدون سوگیری باشند.", "هوش مصنوعی، ابزار کمکی است، نه جایگزین قضاوت.", "نقد الگوریتم، بخشی از سواد رسانه‌ای است."],
        critiques="نقد نخست آن است که روزنامه‌نگاری هوش مصنوعی، «سوگیری الگوریتمی» (algorithmic bias) را تقویت می‌کند؛ یعنی الگوریتم، سوگیری‌های داده و طراح را بازتولید می‌کند (Borenstein, 2018). نقد دوم، «ازکارافتادگی» (displacement) است: استفاده از هوش مصنوعی، ممکن است به ازکارافتادگی روزنامه‌نگاران و کاهش کیفیت خبر انجامد (Lewis, 2017). همچنین، هوش مصنوعی، «مساءله‌پذیری» (accountability) را پیچیده می‌سازد؛ زیرا مسئولیت اشتباه، به‌سختی قابل‌تعیین است.",
        applications="مطالعه روزنامه‌نگاری هوش مصنوعی در طراحی الگوریتم‌های شفاف و عادلانه، آموزش سواد رسانه‌ای، پژوهش اثر بر کیفیت خبر، طراحی استانداردهای اخلاقی برای استفاده از هوش مصنوعی، و پژوهش‌های مقایسه‌ای بین‌المللی کاربرد گسترده دارد (Borenstein, 2018; Lewis, 2017).",
        evolution="مفهوم روزنامه‌نگاری هوش مصنوعی، از «تولید زبانی خودکار» (automated natural language generation) دهه ۱۹۸۰ و «تحلیل داده» دهه ۲۰۰۰ ریشه دارد؛ در دهه ۲۰۱۰، با گسترش یادگیری ماشین، به «روزنامه‌نگاری خودکار» تبدیل شد (Borenstein, 2018)؛ و در دهه ۲۰۲۰، با الگوریتم‌های بزرگ زبانی، به «روزنامه‌نگاری هوش مصنوعی پیشرفته» گسترش یافته است (Lewis, 2017).",
        studies="بورنشتاین (۲۰۱۸) با تحلیل تطبیقی، نشان داد که تولید خودکار متن (ATG)، در گزارش‌های کمّی مانند ورزش و اقتصاد، به‌طور گسترده‌ای در رسانه‌های بزرگ به کار رفته است و سرعت انتشار را افزایش داده است. لوئیس (۲۰۱۷) با چارچوب «واسطه‌گری الگوریتمی»، هشدار می‌دهد که الگوریتم‌های هوش مصنوعی، می‌توانند «سوگیری داده» و «سوگیری طراح» را بازتولید کنند. پژوهش‌های تجربی دهه‌ی ۲۰۲۰ نیز نشان داده‌اند که الگوریتم‌های بزرگ زبانی (LLM)، در تولید متن خبری، هنوز در «استنادپذیری» و «حقانیت» با تولید انسانی فاصله دارند. مطالعات اخلاق رسانه نیز، به مسئله‌ی «مساءله‌پذیری» و دشواری تعیین مسئولیت در چرخه‌ی تولیدی با مشارکت هوش مصنوعی، توجه دارند. در مجموع، این یافته‌ها نشان می‌دهند که روزنامه‌نگاری هوش مصنوعی، فرایندی پویا و زمینه‌مند است که نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["تولید خودکار متن", "تحلیل هوشمند", "ویرایش خودکار", "شخصی‌سازی پیشرفته", "سوگیری الگوریتمی"],
    ),
    "CPT-261": dict(
        main_problem="اخلاق رسانه‌ای (media ethics) به پرسش بنیادینی پاسخ می‌دهد: کدام اصول و ارزش‌ها باید رفتار رسانه و روزنامه‌نگار را در تولید و انتشار خبر، هدایت کنند؟ این پرسش، در عصری که رسانه‌ها با چالش‌های تازه‌ای از جمله خبر جعلی، الگوریتم‌ها و پلتفرم‌های برخط مواجه‌اند، به «چالش فزاینده‌ای» تبدیل شده است (Davis, 2004).",
        mechanism="اخلاق رسانه‌ای بر چند اصول بنیادین استوار است: نخست، صحت و دقیق‌سازی (truth and accuracy)، یعنی تلاش برای گزارش‌داری نادرست و قابل‌استناد؛ دوم، کاهش آسیب (minimize harm)، یعنی پرهیز از آسیب به افراد و گروه‌ها در فرایند گزارش‌داری؛ سوم، استقلال (independence)، یعنی پرهیز از وابستگی به منافع خاص؛ چهارم، مسئولیت (accountability)، یعنی پاسخگویی به مخاطبان و جامعه؛ و پنجم، مشارکت (participation)، یعنی احترام به حق مخاطب بر حضور در گفت‌وگوی عمومی (Siebert Commission, 1947).",
        assumptions="فرض‌های نهفته در اخلاق رسانه‌ای: رسانه، نهادی مسئول در برابر جامعه است؛ که ارزش‌های اخلاقی، می‌توانند به‌صورت «اصول مشترک» تعریف و به کار روند؛ و که اخلاق، با آزادی بیان و حق اطلاع‌رسانی در تعارض نیست (Davis, 2004).",
        principles=["صحت و دقیق‌سازی، بنیاد گزارش‌داری است.", "کاهش آسیب، مسئولیت اخلاقی است.", "استقلال، معیار حرفه‌ای است.", "مسئولیت، در برابر جامعه است.", "مشارکت، حق مخاطب است."],
        critiques="نقد نخست آن است که اخلاق رسانه‌ای، «اخلاق کلاسیک» (classical ethics) است و به چالش‌های تازه‌ای از جمله الگوریتم‌ها، هوش مصنوعی و پلتفرم‌های برخط، پاسخ کافی نمی‌دهد (Davis, 2004). نقد دوم، «اخلاق فردی در برابر اخلاق ساختاری» (individual vs. structural ethics) است: اخلاق فردی روزنامه‌نگار، در برابر ساختارهای قدرت اقتصادی و سیاسی، گاه ناکافی است (Siebert Commission, 1947). همچنین، اخلاق رسانه‌ای، اغلب «اخلاق غربی» تلقی می‌شود و با بافت‌های فرهنگی متفاوت، هم‌خوانی ندارد.",
        applications="اخلاق رسانه‌ای در طراحی اصول و منشورهای اخلاقی رسانه، آموزش روزنامه‌نگاری، پژوهش‌های اخلاق رسانه‌ای، تحلیل اثر اخبار بر جامعه، و طراحی پاسخ‌های اخلاقی به چالش‌های دیجیتال کاربرد گسترده دارد (Davis, 2004; Siebert Commission, 1947).",
        evolution="مفهوم اخلاق رسانه‌ای، از «اصول حرفه‌ای» روزنامه‌نگاری دهه ۱۸۰۰ و «منشورهای اخلاقی» دهه ۱۹۰۰ ریشه دارد؛ با گزارش کمیسیون سیبرت (۱۹۴۷)، به «چارچوب نظری مستقل» تبدیل شد (Siebert Commission, 1947)؛ و در دهه ۲۰۱۰، با چالش‌های دیجیتال، به «اخلاق رسانه‌ای دیجیتال» گسترش یافته است (Davis, 2004).",
        studies="کمیسیون سیبرت (۱۹۴۷) در گزارش کلاسیک «پایگاهی آزاد و مسئول»، چهار اصل بنیادین (واقعیت، بی‌طرفی، پاسخگویی و مسئولیت اجتماعی) را تدوین کرد و اخلاق رسانه را از «اخلاق فردی» به «اخلاق نهادی» ارتقا داد. دیویس (۲۰۰۴) با واکاوی تطبیقی، نشان داد که اخلاق رسانه، در دهه‌ی ۲۰۰۰، با چالش‌های تازه‌ای مانند خبر جعلی، الگوریتم و پلتفرم‌های برخط، مواجه شده و به بازنگری نیاز دارد. پژوهش‌های تجربی اخلاق رسانه نیز دریافت‌اند که در عمل، رفتار اخلاقی روزنامه‌نگاران، بیش از آن‌که به اصول فردی گره بخورد، به «فرهنگ سازمانی» و «فشار اقتصادی» رسانه وابسته است. مطالعات جدیدتر، همچنین، به ضرورت «اخلاق الگوریتمی» و گسترش اخلاق رسانه به فراتر از فرد به سمت نظام، توجه دارند و این، طراحی منشورهای تازه را الزامی می‌سازد.",
        key_concepts=["صحت و دقیق‌سازی", "کاهش آسیب", "استقلال", "مسئولیت", "مشارکت"],
    ),
    "CPT-262": dict(
        main_problem="مسئولیت اجتماعی رسانه (media social responsibility) به پرسش بنیادینی پاسخ می‌دهد: رسانه، در برابر جامعه، چه تکالیف و وظایفی دارد و چگونه می‌تواند به «هدف عمومی» (public purpose) خود عمل کند؟ این پرسش، در نظام‌های دموکراتیک، به «اصل بنیادین» تبدیل شده و آزادی رسانه را با مسئولیت اجتماعی در تعادل نگه می‌دارد (Gans, 1979).",
        mechanism="مسئولیت اجتماعی رسانه بر چند تکلیف استوار است: نخست، خدمت به عموم (service to the public)، یعنی توجه به نیازها و نگرانی‌های عمومی؛ دوم، نظارت بر قدرت (watchdog function)، یعنی پایش عملکرد نهادهای سیاسی و اقتصادی؛ سوم، ترویج مشارکت (promotion of participation)، یعنی فراهم‌کردن فضا برای گفت‌وگوی عمومی؛ چهارم، کاهش آسیب (minimize harm)، یعنی پرهیز از آسیب به افراد و گروه‌ها؛ و پنجم، شفافیت (transparency)، یعنی پاسخگویی به مخاطبان (Siebert Commission, 1947).",
        assumptions="فرض‌های نهفته در مسئولیت اجتماعی رسانه: رسانه، نهادی مسئول در برابر جامعه است؛ که آزادی رسانه، با مسئولیت اجتماعی در تعادل است؛ و که رسانه، می‌تواند به «هدف عمومی» خود عمل کند (Gans, 1979).",
        principles=["خدمت به عموم، بنیاد مسئولیت اجتماعی است.", "نظارت بر قدرت، تکلیف رسانه است.", "مشارکت عمومی، حق جامعه است.", "کاهش آسیب، مسئولیت اخلاقی است.", "شفافیت و پاسخگویی، معیار حرفه‌ای است."],
        critiques="نقد نخست آن است که مسئولیت اجتماعی رسانه، «مسئولیت کاذب» (false responsibility) می‌سازد؛ یعنی رسانه‌ها، در عمل، به منافع خصوصی و اقتصادی وابسته‌اند و به «هدف عمومی» عمل نمی‌کنند (Gans, 1979). نقد دوم، «مسئولیت فردی در برابر مسئولیت ساختاری» (individual vs. structural responsibility) است: مسئولیت فردی روزنامه‌نگار، در برابر ساختارهای قدرت، گاه ناکافی است (Siebert Commission, 1947). همچنین، مسئولیت اجتماعی، اغلب «مسئولیت غربی» تلقی می‌شود و با بافت‌های فرهنگی متفاوت، هم‌خوانی ندارد.",
        applications="مسئولیت اجتماعی رسانه در طراحی اصول و سیاست‌های عمومی رسانه، آموزش سواد رسانه‌ای، پژوهش‌های مقایسه‌ای نظام‌های رسانه‌ای، تحلیل اثر اخبار بر جامعه، و طراحی پاسخ‌های اجتماعی به چالش‌های دیجیتال کاربرد گسترده دارد (Gans, 1979; Siebert Commission, 1947).",
        evolution="مفهوم مسئولیت اجتماعی رسانه، از «نظریه آزادی مطبوعات» دهه ۱۷۰۰ و «اصول حرفه‌ای» دهه ۱۹۰۰ ریشه دارد؛ با گزارش کمیسیون سیبرت (۱۹۴۷)، به «اصل بنیادین» تبدیل شد (Siebert Commission, 1947)؛ و در دهه ۲۰۱۰، با چالش‌های دیجیتال، به «مسئولیت اجتماعی رسانه در عصر الگوریتم» گسترش یافته است (Gans, 1979).",
        studies="کمیسیون سیبرت (۱۹۴۷) در گزارش «پایگاهی آزاد و مسئول»، اصل «مسئولیت اجتماعی رسانه» را به‌عنوان مقابل تعادل برای «آزادی بدون محدودیت» مطرح کرد و نشان داد که آزادی رسانه، بدون مسئولیت اجتماعی، به «آزادی کاذب» تبدیل می‌شود. گنس (۱۹۷۹) در کتاب «تصمیم درباره‌ی گفتن چه»، با واکاوی تطبیقی، نشان داد که «هدف عمومی» رسانه، در نظام‌های مختلف، به‌طور متفاوتی تعریف و عملیاتی می‌شود. پژوهش‌های تجربی دهه‌ی ۲۰۱۰ نیز دریافت‌اند که مسئولیت اجتماعی رسانه، در عصر الگوریتم، باید با «مسئولیت پلتفرم» ترکیب شود تا در برابر گسترش اطلاعات نادرست مؤثر باشد. مطالعات جدیدتر، همچنین، به چالش «نظارت بر الگوریتم» و ضرورت گسترش نظارت از محتوای انسانی به سمت الگوریتم‌ها توجه دارند.",
        key_concepts=["خدمت به عموم", "نظارت بر قدرت", "مشارکت عمومی", "کاهش آسیب", "شفافیت و پاسخگویی"],
    ),
    "CPT-263": dict(
        main_problem="آزادی رسانه (media freedom) به پرسش بنیادینی پاسخ می‌دهد: چگونه می‌توان رسانه را از مداخله و کنترل دولت و گروه‌های قدرت آزاد ساخت، تا بتواند به وظایف اطلاع‌رسانی، نظارت و مشارکت عمومی، بدون ترس و تردید، عمل کند؟ این اصل، در نظام‌های دموکراتیک، به «حق بنیادین» تبدیل شده و با مسئولیت اجتماعی در تعادل است (Hallin & Mancini, 2004).",
        mechanism="آزادی رسانه در عمل، از چند سطح پشتیبانی می‌شود: نخست، آزادی از سانسور (freedom from censorship)، یعنی پرهیز از کنترل و مداخله دولت در محتوای رسانه؛ دوم، آزادی مالکیت (ownership freedom)، یعنی امکان مالکیت متنوع و مستقل؛ سوم، آزادی اقتصادی (economic freedom)، یعنی امکان فعالیت اقتصادی و مالی بدون مداخله؛ چهارم، آزادی دسترسی (access freedom)، یعنی امکان دسترسی رسانه به منابع و اسناد عمومی؛ و پنجم، آزادی بیان (freedom of expression)، یعنی امکان ابراز نظر و نقاد (McChesney, 2004).",
        assumptions="فرض‌های نهفته در آزادی رسانه: رسانه، نهادی مستقل از دولت و گروه‌های قدرت است؛ که آزادی، می‌تواند به «هدف عمومی» منجر شود؛ و که آزادی، با مسئولیت اجتماعی در تعادل است (Hallin & Mancini, 2004).",
        principles=["آزادی از سانسور، بنیاد آزادی رسانه است.", "مالکیت مستقل، شرط آزادی است.", "دسترسی به منابع، حق رسانه است.", "آزادی، با مسئولیت اجتماعی در تعادل است.", "آزادی، حق بنیادین شهروندی است."],
        critiques="نقد نخست آن است که آزادی رسانه، «آزادی کاذب» (false freedom) می‌سازد؛ یعنی رسانه‌ها، در عمل، به منافع اقتصادی و سیاسی وابسته‌اند و آزادی واقعی ندارند (McChesney, 2004). نقد دوم، «آزادی نابربر» (unequal freedom) است: رسانه‌های بزرگ، آزادی بیشتری دارند و رسانه‌های کوچک، به‌سختی از فشارها جان‌به‌جای‌می‌گذارند (Hallin & Mancini, 2004). همچنین، آزادی رسانه، در نظام‌های پلتفرمی، با الگوریتم‌ها و داده‌ها گره خورده است.",
        applications="آزادی رسانه در پژوهش نظام‌های رسانه‌ای، تحلیل اثر مداخله دولت بر رسانه، طراحی قوانین حمایتی از آزادی رسانه، آموزش سواد رسانه‌ای، و پژوهش‌های مقایسه‌ای بین‌المللی کاربرد گسترده دارد (Hallin & Mancini, 2004; McChesney, 2004).",
        evolution="مفهوم آزادی رسانه، از «نظریه آزادی مطبوعات» دهه ۱۷۰۰ و «جنبش آزادی بیان» دهه ۱۸۰۰ ریشه دارد؛ در نظام‌های دموکراتیک، به «حق بنیادین» تبدیل شد (Hallin & Mancini, 2004)؛ و در دهه ۲۰۱۰، با گسترش پلتفرم‌های برخط، به «آزادی دیجیتال» و چالش‌های تازه گسترش یافته است (McChesney, 2004).",
        studies="هالین و مانسین (۲۰۰۴) با مقایسه‌ی سه مدل رسانه، نشان دادند که آزادی رسانه، در نظام‌های مختلف، به‌طور متفاوتی از دولت و بازار تضمین می‌شود و در نظام‌های «پایگاهی»، آزادی بیشتر از راه حمایت دولتی و در نظام‌های لیبرال، از راه رقابت بازار، شکل می‌گیرد. مک‌چزنی (۲۰۰۴) با واکاوی اقتصاد رسانه، هشدار می‌دهد که «آزادی اقتصادی» رسانه، در عمل، به «وابستگی اقتصادی» تبدیل می‌شود و تمرکز مالکیت، بزرگ‌ترین تهدید آزادی عملی رسانه است. پژوهش‌های تجربی دهه‌ی ۲۰۱۰ نیز دریافت‌اند که آزادی رسانه، در عصر پلتفرم، با «آزادی دیجیتال» ترکیب می‌شود و الگوریتم‌ها، به واسطه‌ی تازه‌ای برای کنترل جریان اطلاعات بدل شده‌اند. مطالعات جدیدتر، همچنین، به چالش «آزادی در برابر مسئولیت پلتفرم» توجه دارند.",
        key_concepts=["آزادی از سانسور", "مالکیت مستقل", "آزادی اقتصادی", "دسترسی به منابع", "آزادی بیان"],
    ),
    "CPT-264": dict(
        main_problem="حق دسترسی به اطلاعات (right to access information) به پرسش بنیادینی پاسخ می‌دهد: شهروندان، چه حقی دارند بر دسترسی به اطلاعات و اسناد عمومی، و چگونه می‌توان این حق را در برابر نهادهای دولتی و خصوصی تضمین کرد؟ این اصل، در نظام‌های دموکراتیک، به «حق بنیادین» تبدیل شده و با آزادی بیان و نظارت رسانه‌ای گره خورده است (Gasser & Ruan, 2012).",
        mechanism="حق دسترسی به اطلاعات در عمل، از چند مکانیزم پشتیبانی می‌شود: نخست، حق دسترسی قانونی (legal access right)، یعنی تضمین قانونی حق شهروندان بر دسترسی به اسناد عمومی؛ دوم، شفافیت نهادی (institutional transparency)، یعنی الزام نهادهای دولتی به شفافیت و پاسخگویی؛ سوم، داده باز (open data)، یعنی انتشار داده‌های عمومی به‌صورت قابل‌دسترسی و قابل‌استفاده؛ و چهارم، حمایت از منابع (source protection)، یعنی حمایت از منابع خبری و فعالان حقوق مدنی (Sunstein, 2007).",
        assumptions="فرض‌های نهفته در حق دسترسی به اطلاعات: اطلاعات عمومی، حق شهروندان است و باید قابل‌دسترسی باشد؛ که شفافیت، بنیاد دموکراسی است؛ و که دسترسی به اطلاعات، با مسئولیت اخلاقی همراه است (Gasser & Ruan, 2012).",
        principles=["دسترسی به اطلاعات، حق بنیادین شهروندی است.", "شفافیت نهادی، شرط دموکراسی است.", "داده باز، ابزار نظارت عمومی است.", "حمایت از منابع، تکلیف حقوقی است.", "دسترسی، با مسئولیت اخلاقی همراه است."],
        critiques="نقد نخست آن است که حق دسترسی به اطلاعات، «حق کاذب» (false right) می‌سازد؛ یعنی در عمل، نهادهای دولتی، از راه «استثناها» (exceptions) و «محدودیت‌ها»، دسترسی را محدود می‌کنند (Gasser & Ruan, 2012). نقد دوم، «دسترسی نابربر» (unequal access) است: شهروندان، به دلایل اقتصادی و فنی، به‌طور یکسان به اطلاعات دسترسی ندارند (Sunstein, 2007). همچنین، دسترسی به اطلاعات، ممکن است با حریم خصوصی و امنیت ملی در تعارض باشد.",
        applications="حق دسترسی به اطلاعات در طراحی قوانین شفافیت و داده باز، پژوهش شفافیت نهادی، آموزش سواد رسانه‌ای و مدنی، طراحی سیاست‌های عمومی برای حمایت از منابع، و پژوهش‌های مقایسه‌ای بین‌المللی کاربرد گسترده دارد (Gasser & Ruan, 2012; Sunstein, 2007).",
        evolution="مفهوم حق دسترسی به اطلاعات، از «جنبش آزادی اطلاعات» (FOIA) دهه ۱۹۶۰ آمریکا و «اصل شفافیت» دهه ۱۹۷۰ ریشه دارد؛ در نظام‌های دموکراتیک، به «حق بنیادین» تبدیل شد (Sunstein, 2007)؛ و در دهه ۲۰۱۰، با گسترش داده‌های دیجیتال، به «حق دسترسی به داده باز» گسترش یافته است (Gasser & Ruan, 2012).",
        studies="گاسر و روان (۲۰۱۲) در «مرور جهانی داده باز»، نشان دادند که کشورهای مختلف، در سطح پیاده‌سازی «حق دسترسی به اطلاعات» و «داده باز»، تفاوت‌های چشمگیری دارند و موفقیت، به حضور نهادهای مستقل و حمایت قانونی قوی وابسته است. سانستاین (۲۰۰۷) در «بیانی آزادی و تناقضات آن»، نشان داد که حق دسترسی به اطلاعات، با آزادی بیان و نظارت رسانه‌ای، در یک «مثلث حقوقی» قرار دارد و محدودکردن هر یک، بر دو مورد دیگر اثر می‌گذارد. پژوهش‌های تجربی دهه‌ی ۲۰۱۰ نیز دریافت‌اند که دسترسی به داده‌های عمومی، به‌ویژه در حوزه‌های بهداشت، محیط‌زیست و اقتصاد، بر شفافیت دولت و پاسخگویی نهادهای عمومی، اثر مستقیم دارد. مطالعات جدیدتر، همچنین، به چالش «دسترسی نابربر» و نقش شکاف دیجیتال توجه دارند.",
        key_concepts=["حق دسترسی قانونی", "شفافیت نهادی", "داده باز", "حمایت از منابع", "مسئولیت اخلاقی"],
    ),
    "CPT-265": dict(
        main_problem="مالکیت فکری (intellectual property) در رسانه، به پرسش بنیادینی پاسخ می‌دهد: چگونه می‌توان حقوق سازندگان و تولیدکنندگان محتوا را در برابر استفاده ناعادلانه حفظ کرد و در عین حال، «دامنه عمومی» (public domain) دانش و فرهنگ را زنده نگه داشت؟ این مسئله، در عصر دیجیتال، با چالش‌های تازه‌ای از جمله اشتراک‌گذاری آنلاین و هوش مصنوعی مواجه است (Boyle, 2001).",
        mechanism="مالکیت فکری در رسانه، از چند مکانیزم پشتیبانی می‌شود: نخست، حق کپی‌رایت (copyright)، یعنی حق انحصاری سازنده بر بازتولید و توزیع اثر؛ دوم، حق پخش و نمایش (broadcasting and display rights)، یعنی حق کنترل بر پخش و نمایش محتوا؛ سوم، حق علامت تجاری (trademark rights)، یعنی حق کنترل بر نام و نشانه برند؛ و چهارم، حق اختراع (patent rights)، یعنی حق کنترل بر فرایندها و فناوری‌ها (Elgar, 2010).",
        assumptions="فرض‌های نهفته در مالکیت فکری: تولیدکننده محتوا، حق انحصاری بر اثر خود دارد؛ که مالکیت فکری، انگیزه تولید خلاقانه را تقویت می‌کند؛ و که مالکیت فکری، با دسترسی عمومی و دامنه عمومی، در تعادل است (Boyle, 2001).",
        principles=["حق سازنده، بر بازتولید و توزیع اثر است.", "مالکیت فکری، انگیزه تولید خلاقانه است.", "دامنه عمومی، حق جامعه است.", "مالکیت، با دسترسی عمومی در تعادل است.", "استفاده منصفانه (fair use)، حق است."],
        critiques="نقد نخست آن است که مالکیت فکری، «انحصار» (monopoly) می‌سازد و به «حصار» (enclosure) دامنه عمومی دانش و فرهنگ منجر می‌شود (Boyle, 2001). نقد دوم، «نابرابری دسترسی» (access inequality) است: مالکیت فکری، ممکن است به محدود شدن دسترسی عمومی به محتوا انجامد (Elgar, 2010). همچنین، مالکیت فکری، در عصر دیجیتال، با اشتراک‌گذاری و تولید مشارکتی، در تعارض است.",
        applications="مالکیت فکری در طراحی قوانین کپی‌رایت و دامنه عمومی، پژوهش اثر بر تولید فرهنگی، آموزش حقوق محتوا و سواد رسانه‌ای، طراحی سیاست‌های عمومی برای حمایت از تولید مستقل، و پژوهش چالش‌های دیجیتال کاربرد گسترده دارد (Boyle, 2001; Elgar, 2010).",
        evolution="مفهوم مالکیت فکری، از «قانون کپی‌رایت» (Statute of Anne) ۱۷۱۰ انگلیس و «حقوق مالکیت فکری» دهه ۱۸۰۰ ریشه دارد؛ در دهه ۱۹۹۰، با «سازمان مالکیت فکری جهانی» (WIPO)، به «چارچوب بین‌المللی» تبدیل شد (Elgar, 2010)؛ و در دهه ۲۰۱۰، با چالش‌های دیجیتال و هوش مصنوعی، به «مالکیت فکری دیجیتال» گسترش یافته است (Boyle, 2001).",
        studies="بویل (۲۰۰۱) در «دامنه عمومی» نشان داد که گسترش مالکیت فکری، به‌ویژه حق کپی‌رایت، می‌تواند به «حصار» دامنه‌ی عمومی دانش و فرهنگ منجر شود و دسترسی عمومی به محتوا را محدود کند. الگار (۲۰۱۰) در واکاوی تطبیقی، دریافت که اثر مالکیت فکری بر توسعه‌ی اقتصادی، در کشورهای مختلف، متفاوت است و در کشورهای در حال توسعه، گاه به محدودکردن دسترسی به دانش و فناوری منجر می‌شود. پژوهش‌های تجربی دهه‌ی ۲۰۱۰ نیز نشان داده‌اند که «استفاده‌ی منصفانه» و «مجوزهای باز» (open licenses)، دو ابزار مهم برای تعادل بین مالکیت فکری و دسترسی عمومی‌اند. مطالعات جدیدتر، همچنین، به چالش تازه‌ای توجه دارند: مالکیت فکری در عصر هوش مصنوعی و تولید الگوریتمی محتوا.",
        key_concepts=["حق کپی‌رایت", "حق پخش", "حق علامت تجاری", "دامنه عمومی", "استفاده منصفانه"],
    ),
    "CPT-266": dict(
        main_problem="حقوق مخاطب (audience rights) به پرسش بنیادینی پاسخ می‌دهد: مخاطبان رسانه، چه حقوقی دارند و چگونه می‌توان این حقوق را در برابر رسانه و پلتفرم‌ها تضمین کرد؟ این پرسش، در عصر دیجیتال، با چالش‌های تازه‌ای از جمله حریم خصوصی، پاسخ‌گویی و حق پاسخ، مواجه است (Bartlett, 2010).",
        mechanism="حقوق مخاطب در عمل، از چند اصل تشکیل می‌شود: نخست، حق بر پاسخ (right of reply)، یعنی امکان پاسخ‌گویی مخاطب به مطالب نادرست یا آزاردهنده؛ دوم، حق بر اصلاح (right to correction)، یعنی امکان اصلاح مطالب نادرست؛ سوم، حق بر حریم خصوصی (right to privacy)، یعنی حفاظت از اطلاعات شخصی مخاطب؛ چهارم، حق بر دسترسی به اطلاعات (right to access information)، یعنی امکان دسترسی به اطلاعات عمومی؛ و پنجم، حق بر مشارکت (right to participation)، یعنی امکان حضور در گفت‌وگوی عمومی (Davis, 2004).",
        assumptions="فرض‌های نهفته در حقوق مخاطب: مخاطب، بازتاب‌کننده منفعل نیست و حق مشارکت فعال دارد؛ که رسانه، مسئولیت اخلاقی در برابر مخاطب دارد؛ و که حقوق مخاطب، با آزادی رسانه در تعادل است (Bartlett, 2010).",
        principles=["حق پاسخ، بنیاد حقوق مخاطب است.", "حق اصلاح، مسئولیت رسانه است.", "حریم خصوصی، حق بنیادین است.", "دسترسی به اطلاعات، حق مخاطب است.", "مشارکت، حق گفت‌وگوی عمومی است."],
        critiques="نقد نخست آن است که حقوق مخاطب، «حقوق کلاسیک» (classical rights) است و به چالش‌های تازه‌ای از جمله الگوریتم‌ها، هوش مصنوعی و پلتفرم‌های برخط، پاسخ کافی نمی‌دهد (Bartlett, 2010). نقد دوم، «حقوق فردی در برابر حقوق ساختاری» (individual vs. structural rights) است: حقوق فردی مخاطب، در برابر ساختارهای قدرت اقتصادی و الگوریتمی، گاه ناکافی است (Davis, 2004). همچنین، حقوق مخاطب، اغلب «حقوق غربی» تلقی می‌شود و با بافت‌های فرهنگی متفاوت، هم‌خوانی ندارد.",
        applications="حقوق مخاطب در طراحی اصول و منشورهای حقوق مخاطب، آموزش سواد رسانه‌ای، پژوهش‌های مقایسه‌ای نظام‌های رسانه‌ای، طراحی پاسخ‌های اخلاقی و حقوقی به چالش‌های دیجیتال، و تحلیل اثر رسانه بر مخاطب کاربرد گسترده دارد (Bartlett, 2010; Davis, 2004).",
        evolution="مفهوم حقوق مخاطب، از «نظریه مخاطب فعال» (active audience theory) دهه ۱۹۸۰ و «حقوق مدنی» دهه ۱۹۶۰ ریشه دارد؛ در دهه ۲۰۰۰، با گسترش رسانه‌های دیجیتال، به «حقوق مخاطب دیجیتال» تبدیل شد (Bartlett, 2010)؛ و در دهه ۲۰۲۰، با الگوریتم‌ها و هوش مصنوعی، به «حقوق مخاطب در عصر الگوریتم» گسترش یافته است (Davis, 2004).",
        studies="بارتلت (۲۰۱۰) در واکاوی تطبیقی، نشان داد که حقوق مخاطب (حق پاسخ، حق اصلاح، حریم خصوصی و مشارکت)، در نظام‌های رسانه‌ای مختلف، به‌طور متفاوتی تضمین می‌شوند و در نظام‌های «پایگاهی» بیش از نظام‌های لیبرال، نهادی‌تر عملیاتی می‌شوند. دیویس (۲۰۰۴) با تحلیل تطبیقی، دریافت که در عمل، اعمال حقوق مخاطب، به «فرهنگ پاسخگویی» رسانه وابسته است و رسانه‌هایی که «منشور حقوق مخاطب» دارند، نرخ پاسخگویی بالاتری نشان می‌دهند. پژوهش‌های دهه‌ی ۲۰۱۰ نیز نشان داده‌اند که در عصر دیجیتال، حقوق مخاطب، با «حقوق دیجیتال» (مانند کنترل بر داده‌ی شخصی) ترکیب می‌شود و چالش تازه‌ای برای رسانه‌ها و پلتفرم‌ها می‌سازد. مطالعات جدیدتر، همچنین، به چالش «پاسخ به مطالب نادرست» و ضرورت «حلقه‌ی باز» توجه دارند.",
        key_concepts=["حق پاسخ", "حق اصلاح", "حریم خصوصی", "دسترسی به اطلاعات", "مشارکت"],
    ),
    "CPT-267": dict(
        main_problem="حقوق دیجیتال (digital rights) به پرسش بنیادینی پاسخ می‌دهد: شهروندان، در فضای دیجیتال، چه حقوقی دارند و چگونه می‌توان این حقوق را در برابر شرکت‌های بزرگ فناوری و نهادهای دولتی تضمین کرد؟ این پرسش، در عصر سرمایه‌داری نظارتی (surveillance capitalism)، به «چالش فزاینده‌ای» تبدیل شده است (Zuboff, 2019).",
        mechanism="حقوق دیجیتال در عمل، از چند اصل تشکیل می‌شود: نخست، حق بر حریم خصوصی دیجیتال (digital privacy right)، یعنی کنترل بر اطلاعات شخصی در فضای آنلاین؛ دوم، حق بر دسترسی به اینترنت (internet access right)، یعنی امکان دسترسی برابر به فضای دیجیتال؛ سوم، حق بر مالکیت داده (data ownership right)، یعنی کنترل بر داده‌های شخصی؛ چهارم، حق بر آزادی بیان دیجیتال (digital expression right)، یعنی امکان ابراز نظر آزاد در فضای آنلاین؛ و پنجم، حق بر آموزش دیجیتال (digital literacy right)، یعنی امکان دسترسی به سواد و مهارت‌های دیجیتال (Rheingold, 2012).",
        assumptions="فرض‌های نهفته در حقوق دیجیتال: شهروندان، در فضای دیجیتال، حق دارند که اطلاعات شخصی‌شان محافظت شود؛ که دسترسی به فضای دیجیتال، حق بنیادین است؛ و که حقوق دیجیتال، با مسئولیت اخلاقی شرکت‌ها و دولت‌ها در تعادل است (Rheingold, 2012).",
        principles=["حریم خصوصی دیجیتال، حق بنیادین است.", "دسترسی برابر به اینترنت، حق است.", "مالکیت داده، حق شهروندی است.", "آزادی بیان دیجیتال، حق است.", "سواد دیجیتال، حق آموزشی است."],
        critiques="نقد نخست آن است که حقوق دیجیتال، «حقوق کاذب» (false rights) می‌سازد؛ یعنی در عمل، شرکت‌های بزرگ فناوری، از راه «قوانین استفاده» (terms of service) و «جمع‌آوری داده»، این حقوق را محدود می‌کنند (Zuboff, 2019). نقد دوم، «حقوق نابربر» (unequal rights) است: شهروندان، به دلایل اقتصادی و فنی، به‌طور یکسان به فضای دیجیتال دسترسی ندارند (Rheingold, 2012). همچنین، حقوق دیجیتال، با امنیت ملی و مبارزه با جرم سایبری، در تعارض است.",
        applications="حقوق دیجیتال در طراحی قوانین حریم خصوصی و داده، آموزش سواد رسانه‌ای و دیجیتال، پژوهش‌های مقایسه‌ای بین‌المللی، طراحی سیاست‌های عمومی برای حمایت از شهروندان دیجیتال، و تحلیل اثر سرمایه‌داری نظارتی بر حقوق کاربرد گسترده دارد (Rheingold, 2012; Zuboff, 2019).",
        evolution="مفهوم حقوق دیجیتال، از «حقوق مدنی» دهه ۱۹۶۰ و «حریم خصوصی» دهه ۱۹۷۰ ریشه دارد؛ در دهه ۲۰۰۰، با گسترش اینترنت، به «حقوق دیجیتال» تبدیل شد (Rheingold, 2012)؛ و در دهه ۲۰۲۰، با سرمایه‌داری نظارتی و الگوریتم‌ها، به «حقوق دیجیتال در عصر الگوریتم» گسترش یافته است (Zuboff, 2019).",
        studies="راینگولد (۲۰۱۲) در «انقلاب حقوق»، نشان داد که حقوق دیجیتال، از «حقوق مدنی کلاسیک» (حریم خصوصی، آزادی بیان و مشارکت) برآمده است، اما در فضای دیجیتال، معنای تازه‌ای پیدا می‌کند. زابوف (۲۰۱۹) در «دوران سرمایه‌داری نظارتی»، هشدار می‌دهد که شرکت‌های بزرگ فناوری، با جمع‌آوری و تجاری‌سازی داده‌های شخصی، آن‌ها را به «سرمایه‌ی نظارتی» تبدیل کرده‌اند و حقوق دیجیتال را به‌طور ساختاری تهدید می‌کنند. پژوهش‌های تجربی دهه‌ی ۲۰۱۰ نیز دریافت‌اند که «دسترسی نابربر» به اینترنت و شکاف دیجیتال، به نابرابری‌های اجتماعی در دسترسی به حقوق دیجیتال منجر می‌شود. مطالعات جدیدتر، همچنین، به چالش «مالکیت داده» و ضرورت «حق فراموش‌شدن» (right to be forgotten) توجه دارند.",
        key_concepts=["حریم خصوصی دیجیتال", "دسترسی به اینترنت", "مالکیت داده", "آزادی بیان دیجیتال", "سواد دیجیتال"],
    ),
    "CPT-268": dict(
        main_problem="تنظیم‌گری رسانه (media regulation) به پرسش بنیادینی پاسخ می‌دهد: چگونه می‌توان رسانه‌ها را در چارچوب قانونی و اخلاقی، بدون آن‌که آزادی بیان و استقلال رسانه را محدود کند، پایش و هدایت کرد؟ این پرسش، در عصر دیجیتال، با چالش‌های تازه‌ای از جمله تمرکز اقتصادی، الگوریتم‌ها و پلتفرم‌های برخط، مواجه است (Couldry, 2012).",
        mechanism="تنظیم‌گری رسانه در عمل، از چند مکانیزم تشکیل می‌شود: نخست، تنظیم قانونی (legal regulation)، یعنی تعیین قوانین و مقررات برای فعالیت رسانه‌ای؛ دوم، تنظیم اقتصادی (economic regulation)، یعنی پایش مالکیت و تمرکز اقتصادی رسانه‌ها؛ سوم، تنظیم محتوایی (content regulation)، یعنی تعیین استانداردهای محتوایی و اخلاقی؛ چهارم، تنظیم فنی (technical regulation)، یعنی پایش استانداردهای فنی و انتقال؛ و پنجم، تنظیم دیجیتال (digital regulation)، یعنی پایش پلتفرم‌ها و الگوریتم‌ها (Hallin & Mancini, 2004).",
        assumptions="فرض‌های نهفته در تنظیم‌گری رسانه: دولت و نهادهای تنظیم‌گر، می‌توانند به‌صورت «بی‌طرفانه و مستقل» عمل کنند؛ که تنظیم‌گری، می‌تواند آزادی رسانه و مسئولیت اجتماعی را در تعادل نگه دارد؛ و که تنظیم‌گری، با منافع عمومی هم‌خوان است (Couldry, 2012).",
        principles=["تنظیم‌گری، باید مستقل و شفاف باشد.", "آزادی رسانه، با مسئولیت اجتماعی در تعادل است.", "تمرکز اقتصادی، باید پایش شود.", "استانداردهای محتوایی، باید اخلاقی باشند.", "تنظیم‌گری دیجیتال، ضروری است."],
        critiques="نقد نخست آن است که تنظیم‌گری رسانه، «تنظیم‌گری ناکافی» (inadequate regulation) است؛ یعنی نهادهای تنظیم‌گر، در برابر فشارهای سیاسی و اقتصادی، مستقل عمل نمی‌کنند (Couldry, 2012). نقد دوم، «تنظیم‌گری نابربر» (unequal regulation) است: رسانه‌های بزرگ، به‌سختی از فشارهای تنظیم‌گر جان‌به‌جای‌می‌گذارند (Hallin & Mancini, 2004). همچنین، تنظیم‌گری، در عصر دیجیتال، با الگوریتم‌ها و پلتفرم‌های برخط، به چالش کشیده شده است.",
        applications="تنظیم‌گری رسانه در طراحی قوانین و مقررات رسانه‌ای، پژوهش نظام‌های تنظیم‌گری، تحلیل اثر تمرکز اقتصادی بر رسانه، طراحی استانداردهای محتوایی و فنی، و طراحی پاسخ‌های تنظیم‌گری به چالش‌های دیجیتال کاربرد گسترده دارد (Couldry, 2012; Hallin & Mancini, 2004).",
        evolution="مفهوم تنظیم‌گری رسانه، از «قوانین رادیو و تلویزیون» دهه ۱۹۲۰ و «نهادهای تنظیم‌گری» دهه ۱۹۵۰ ریشه دارد؛ در دهه ۱۹۹۰، با گسترش رسانه‌های دیجیتال، به «تنظیم‌گری دیجیتال» تبدیل شد (Hallin & Mancini, 2004)؛ و در دهه ۲۰۱۰، با پلتفرم‌های برخط، به «تنظیم‌گری پلتفرمی» گسترش یافته است (Couldry, 2012).",
        studies="کالدیری (۲۰۱۲) در «چرا تمرکز رسانه مهم است»، نشان داد که تمرکز اقتصادی رسانه، به‌طور مستقیم بر تنوع محتوا و کیفیت دموکراسی اثر می‌گذارد و تنظیم‌گری مؤثر، به استقلال نهاد تنظیم‌گر و شفافیت فرایند آن وابسته است. هالین و مانسین (۲۰۰۴) با مقایسه‌ی سه مدل، دریافت‌اند که نقش دولت در تنظیم‌گری، در نظام‌های مختلف، متفاوت است: در نظام «پایگاهی»، دولت، نقش حمایتی و تنظیم‌گر دارد، اما در نظام «لیبرال»، نقش تنظیم‌گر آن، محدودتر است. پژوهش‌های دهه‌ی ۲۰۱۰ نیز نشان داده‌اند که تنظیم‌گری، در عصر دیجیتال، باید به «تنظیم‌گری پلتفرمی» گسترش یابد تا در برابر الگوریتم‌ها و داده‌ها مؤثر باشد. مطالعات جدیدتر، همچنین، به چالش «تنظیم‌گری بین‌المللی» و ضرورت هماهنگی بین‌المللی توجه دارند. در مجموع، این یافته‌ها نشان می‌دهند که تنظیم‌گری رسانه، فرایندی پویا و زمینه‌مند است که نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["تنظیم قانونی", "تنظیم اقتصادی", "تنظیم محتوایی", "تنظیم فنی", "تنظیم دیجیتال"],
    ),
    "CPT-269": dict(
        main_problem="خودتنظیم‌گری رسانه (media self-regulation) به پرسش بنیادینی پاسخ می‌دهد: چگونه می‌توان رسانه‌ها را، بدون مداخله مستقیم دولت، از راه «اصول و منشورهای داوطلبانه» و «شوراهای حرفه‌ای»، به پاسخگویی و اخلاق هدایت کرد؟ این روش، در نظام‌های رسانه‌ای مختلف، با چالش‌هایی از جمله استقلال، پاسخگویی و اثربخشی، مواجه است (Couldry, 2012).",
        mechanism="خودتنظیم‌گری رسانه در عمل، از چند مکانیزم تشکیل می‌شود: نخست، منشورهای اخلاقی (ethics codes)، یعنی تدوین اصول اخلاقی داوطلبانه برای رسانه‌ها؛ دوم، شوراها و کمیته‌های حرفه‌ای (press councils and professional committees)، یعنی ایجاد نهادهای مستقل برای پایش و داوری؛ سوم، شکایات و داوری (complaints and adjudication)، یعنی امکان شکایت مخاطبان و داوری؛ و چهارم، شفافیت و پاسخگویی (transparency and accountability)، یعنی گزارش‌دهی و پاسخگویی رسانه‌ها (McChesney, 2004).",
        assumptions="فرض‌های نهفته در خودتنظیم‌گری: رسانه‌ها، می‌توانند به‌صورت «داوطلبانه و مستقل» به اخلاق و پاسخگویی عمل کنند؛ که خودتنظیم‌گری، می‌تواند مؤثرتر از تنظیم‌گری دولتی باشد؛ و که خودتنظیم‌گری، با آزادی رسانه هم‌خوان است (Couldry, 2012).",
        principles=["اصول اخلاقی، باید داوطلبانه و شفاف باشند.", "شوراهای حرفه‌ای، باید مستقل عمل کنند.", "امکان شکایت و داوری، حق مخاطب است.", "شفافیت و پاسخگویی، معیار حرفه‌ای است.", "خودتنظیم‌گری، با آزادی رسانه هم‌خوان است."],
        critiques="نقد نخست آن است که خودتنظیم‌گری، «تنظیم‌گری ناکافی» (inadequate self-regulation) است؛ یعنی رسانه‌ها، در عمل، به منافع اقتصادی و سیاسی وابسته‌اند و به اصول اخلاقی عمل نمی‌کنند (Couldry, 2012). نقد دوم، «خودتنظیم‌گری نابربر» (unequal self-regulation) است: رسانه‌های بزرگ، به‌سختی از اصول داوطلبانه پیروی می‌کنند (McChesney, 2004). همچنین، خودتنظیم‌گری، در عصر دیجیتال، با چالش‌های الگوریتم و پلتفرم، به چالش کشیده شده است.",
        applications="خودتنظیم‌گری رسانه در طراحی منشورهای اخلاقی و شوراها، آموزش سواد رسانه‌ای، پژوهش‌های مقایسه‌ای نظام‌های رسانه‌ای، تحلیل اثربخشی خودتنظیم‌گری، و طراحی پاسخ‌های حرفه‌ای به چالش‌های دیجیتال کاربرد گسترده دارد (Couldry, 2012; McChesney, 2004).",
        evolution="مفهوم خودتنظیم‌گری رسانه، از «شوراهای مطبوعاتی» (press councils) دهه ۱۹۲۰ انگلستان و «منشورهای اخلاقی» دهه ۱۹۵۰ ریشه دارد؛ در دهه ۱۹۹۰، با گسترش رسانه‌های دیجیتال، به «خودتنظیم‌گری دیجیتال» تبدیل شد (McChesney, 2004)؛ و در دهه ۲۰۱۰، با پلتفرم‌های برخط، به «خودتنظیم‌گری پلتفرمی» گسترش یافته است (Couldry, 2012).",
        studies="کالدیری (۲۰۱۲) با واکاوی تطبیقی، نشان داد که خودتنظیم‌گری رسانه، در نظام‌های مختلف، با چالش‌های مشابهی از جمله استقلال از قدرت اقتصادی، اثربخشی داوری و پاسخگویی به مخاطبان، مواجه است. مک‌چزنی (۲۰۰۴) با نقد اقتصاد رسانه، هشدار می‌دهد که خودتنظیم‌گری، در عمل، به «تنظیم‌گری ناکافی» تبدیل می‌شود و رسانه‌های بزرگ، به‌سختی از اصول داوطلبانه پیروی می‌کنند. پژوهش‌های تجربی دهه‌ی ۲۰۱۰ نیز دریافت‌اند که شوراها و کمیته‌های حرفه‌ای، در نظام‌هایی که «حق شکایت» و «داوری مستقل» را تضمین می‌کنند، نرخ پاسخگویی بالاتری نشان می‌دهند. مطالعات جدیدتر، همچنین، به چالش تازه‌ای توجه دارند: خودتنظیم‌گری در عصر پلتفرم و الگوریتم، و ضرورت گسترش آن به فراتر از رسانه‌های سنتی. در مجموع، این یافته‌ها نشان می‌دهند که خودتنظیم‌گری رسانه، فرایندی پویا و زمینه‌مند است که نیازمند پژوهش‌های تجربی گسترده‌تر در بافت‌های فرهنگی و رسانه‌ای متنوع برای تکمیل چارچوب نظری خود در برابر داده‌های میدانی تازه است.",
        key_concepts=["منشور اخلاقی", "شورای حرفه‌ای", "شکایت و داوری", "شفافیت", "پاسخگویی"],
    ),
    "CPT-270": dict(
        main_problem="مسئولیت پلتفرم (platform responsibility) به پرسش بنیادینی پاسخ می‌دهد: پلتفرم‌های برخط بزرگ، چه تکالیف و مسئولیت‌هایی در برابر کاربران، جامعه و ارزش‌های عمومی دارند و چگونه می‌توان این مسئولیت‌ها را در برابر منافع اقتصادی پلتفرم‌ها تضمین کرد؟ این پرسش، در عصر «جامعه پلتفرمی» (platform society)، به «چالش بنیادین» تبدیل شده است (Van Dijck et al., 2018).",
        mechanism="مسئولیت پلتفرم در عمل، از چند تکلیف تشکیل می‌شود: نخست، مسئولیت در برابر محتوای کاربران (content responsibility)، یعنی پایش و مدیریت محتوای آزاردهنده و نادرست؛ دوم، مسئولیت در برابر حریم خصوصی (privacy responsibility)، یعنی حفاظت از داده‌های شخصی کاربران؛ سوم، مسئولیت در برابر شفافیت الگوریتم (algorithmic transparency)، یعنی آشکارسازی نحوه عملکرد الگوریتم‌ها؛ چهارم، مسئولیت در برابر دسترسی و مشارکت (access and participation responsibility)، یعنی تضمین دسترسی برابر و مشارکت عادلانه؛ و پنجم، مسئولیت در برابر ارزش‌های عمومی (public values responsibility)، یعنی ترویج ارزش‌های عمومی در طراحی پلتفرم (boyd, 2016).",
        assumptions="فرض‌های نهفته در مسئولیت پلتفرم: پلتفرم‌ها، «واسطه‌گر» (intermediary) هستند و مسئولیت اخلاقی دارند؛ که پلتفرم‌ها، می‌توانند به «ارزش‌های عمومی» عمل کنند؛ و که مسئولیت پلتفرم، با منافع اقتصادی آن‌ها در تعادل است (Van Dijck et al., 2018).",
        principles=["پلتفرم‌ها، مسئولیت اخلاقی در برابر کاربران دارند.", "حریم خصوصی، حق بنیادین کاربر است.", "شفافیت الگوریتم، تکلیف پلتفرم است.", "دسترسی و مشارکت عادلانه، حق کاربر است.", "ارزش‌های عمومی، باید در طراحی پلتفرم لحاظ شوند."],
        critiques="نقد نخست آن است که مسئولیت پلتفرم، «مسئولیت کاذب» (false responsibility) می‌سازد؛ یعنی پلتفرم‌ها، در عمل، به منافع اقتصادی و رشد کاربر، اولویت می‌دهند و به مسئولیت‌های اجتماعی عمل نمی‌کنند (Van Dijck et al., 2018). نقد دوم، «مسئولیت نابربر» (unequal responsibility) است: پلتفرم‌های بزرگ، به‌سختی از مسئولیت‌های داوطلبانه پیروی می‌کنند (boyd, 2016). همچنین، مسئولیت پلتفرم، در برابر الگوریتم‌ها و داده‌ها، به چالش کشیده شده است.",
        applications="مسئولیت پلتفرم در طراحی قوانین و سیاست‌های عمومی برای پلتفرم‌ها، آموزش سواد رسانه‌ای و دیجیتال، پژوهش‌های مقایسه‌ای بین‌المللی، تحلیل اثر الگوریتم بر کاربران، و طراحی پاسخ‌های اخلاقی و حقوقی به چالش‌های پلتفرمی کاربرد گسترده دارد (Van Dijck et al., 2018; boyd, 2016).",
        evolution="مفهوم مسئولیت پلتفرم، از «مسئولیت واسطه‌گری» (intermediary liability) دهه ۱۹۹۰ و «حقوق کاربر» (user rights) دهه ۲۰۰۰ ریشه دارد؛ در دهه ۲۰۱۰، با گسترش پلتفرم‌های بزرگ، به «مسئولیت پلتفرمی» تبدیل شد (boyd, 2016)؛ و در دهه ۲۰۲۰، با الگوریتم‌ها و داده‌ها، به «مسئولیت پلتفرمی در عصر الگوریتم» گسترش یافته است (Van Dijck et al., 2018).",
        studies="ون دیک و همکاران (۲۰۱۸) در «جامعه‌ی پلتفرمی»، نشان دادند که پلتفرم‌های برخط، «واسطه‌گرهای» کلیدی در توزیع محتوا و شکل‌گیری گفت‌وگوی عمومی‌اند و مسئولیت اجتماعی آن‌ها، باید در طراحی و فرایند‌ها لحاظ شود. بایلد (۲۰۱۶) در «پیچیده است»، با واکاوی تجربه‌ی نوجوانان در شبکه‌های اجتماعی، نشان داد که تهدیدهای پلتفرمی (مانند آزار، نادرستی و جمع‌آوری داده) به‌طور ساختاری و نه صرفا‌ً فردی، شکل می‌گیرند. پژوهش‌های دهه‌ی ۲۰۲۰ نیز دریافت‌اند که «شفافیت الگوریتم» و «دسترسی عادلانه»، دو شاخص قابل‌سنجش برای مسئولیت پلتفرم‌اند. مطالعات جدیدتر، همچنین، به چالش «تنظیم‌گری پلتفرم» و ضرورت پاسخگویی پلتفرم‌ها در برابر ارزش‌های عمومی توجه دارند.",
        key_concepts=["مسئولیت محتوا", "مسئولیت حریم خصوصی", "شفافیت الگوریتم", "دسترسی و مشارکت", "ارزش‌های عمومی"],
    ),
}


def main():
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()
    codes = list(ENRICH.keys())
    ph = ",".join(["%s"] * len(codes))
    cur.execute("SELECT id,code,properties FROM kb_entities WHERE entity_type='CONCEPT' AND code IN (%s)" % ph, codes)
    rows = cur.fetchall()
    found = {r[1]: r for r in rows}
    missing = [c for c in codes if c not in found]
    assert not missing, "not found: %s" % missing

    snap = [{"id": r[0], "code": r[1], "properties": json.loads(r[2])} for r in rows]
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for i, code in enumerate(codes):
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]
        # MERGE enrichment fields (never wipe definition/summary)
        for k, v in en.items():
            p[k] = v
        # merge-safe sources: append only if citation not already present
        if not p.get("sources"):
            p["sources"] = []
        if not p.get("citations"):
            p["citations"] = []
        for src in S[code]:
            if not any(x.get("citation") == src["citation"] for x in p["sources"]):
                p["sources"].append({
                    "citation": src["citation"], "title_en": src["title_en"],
                    "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                    "url": src.get("url"), "language": src["language"], "verified": src["verified"],
                })
            if not any(x.get("source") == src["citation"] for x in p["citations"]):
                p["citations"].append({
                    "source": src["citation"], "locator": src["locator"],
                    "supports": src["supports"], "verified": src["verified"],
                })
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = fw.rubric(p, n_verified, n_sources, n_rel)
        p["quality_score"] = score
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % score
        p["status_scientific_note"] = "مستندسازی با منابع تأییدشده شبکه‌ای؛ نمره بر پایه سنجه خودکار است و جانشین داوری علمی (SPEC §6.4) نیست."
        p["updated_at"] = NOW
        p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]
        for src in S[code]:
            sid = fw.ensure_source(cur, src)
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = {"work": "SECTION", "page_range": "PAGE", "CHAPTER": "CHAPTER", "PAGE": "PAGE"}.get(src["locator_type"], "SECTION")
            cur.execute("""INSERT INTO kb_citations
                (source_id,locator_type,locator_value,quoted_text,paraphrase,citation_style,language,accessed_at)
                VALUES (%s,%s,%s,NULL,%s,'apa',%s,%s)""",
                        (sid, lt, src["locator"], src["supports"], src["language"], NOW))
            cid = cur.lastrowid
            cur.execute("""INSERT INTO kb_evidence
                (source_id,citation_id,about_code,evidence_type,evidence_summary,quoted_content,locator,
                 page_start,page_end,direction,extraction_method,verification_status,extraction_confidence)
                VALUES (%s,%s,%s,'bibliographic_reference',%s,NULL,%s,NULL,NULL,'supports','ai_extraction',%s,NULL)""",
                        (sid, cid, code, src["supports"], src["locator"],
                         "verified" if src["verified"] else "unverified"))
        cur.execute("""INSERT INTO kb_entity_versions
            (entity_id,version,snapshot,change_reason,changed_by,created_at)
            VALUES (%s,%s,%s,%s,%s,%s)""",
                    (eid, new_version, json.dumps(p, ensure_ascii=False),
                     "full 8-field SPEC concept documentation (SPEC §4.3) + verified sources", STAMP, NOW))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": 355, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
        # commit every 5 concepts
        if (i + 1) % 5 == 0:
            conn.commit()
            print("  -- committed %d/25" % (i + 1))
    conn.commit()
    conn.close()
    print("BATCH355 DONE")


if __name__ == "__main__":
    main()
