# -*- coding: utf-8 -*-
"""Build knowledge-core block: quality-ethics-tools (sections 10, 11, 12, 14).
Uses keyword arguments throughout to avoid positional-arg bugs."""
import json, io, os, datetime
from collections import Counter

OUT = r"D:\رسانامه تکمیلی\knowledge-core\data\kg_data_quality-ethics-tools.json"

def E(id, title_fa, title_en, slug, entity_type, parent_id, abstract, description,
      key_propositions=None, key_figures=None, origin_period=None,
      geographical_origin=None, related_disciplines=None, applications=None,
      strengths=None, limitations=None, criticisms=None, references=None, facets=None):
    return {
        "id": id, "title_fa": title_fa, "title_en": title_en, "slug": slug,
        "entity_type": entity_type, "parent_id": parent_id, "abstract": abstract,
        "description": description,
        "historical_background": None, "philosophical_foundations": None,
        "key_propositions": key_propositions, "key_figures": key_figures,
        "origin_period": origin_period, "geographical_origin": geographical_origin,
        "related_disciplines": related_disciplines, "applications": applications,
        "strengths": strengths, "limitations": limitations, "criticisms": criticisms,
        "references": references, "status": "draft", "facets": facets or []
    }

def R(src, tgt, rt, desc, conf=0.95):
    return {"source_id": src, "target_id": tgt, "relation_type": rt,
            "description": desc, "confidence": conf, "verification_status": "unverified"}

ents = []
rels = []

def add_e(**kw):
    ents.append(E(**kw))

def add_r(src, tgt, rt, desc, conf=0.95):
    rels.append(R(src, tgt, rt, desc, conf))

# ============ Section 10: INSTRUMENTS (10 categories) ============
add_e(id="kg-instrument-survey", title_fa="ابزارهای پیمایش", title_en="Survey Tools",
      slug="survey", entity_type="INSTRUMENT", parent_id=None,
      abstract="پلتفرم‌های الکترونیکی طراحی و توزیع پرسش‌نامه برای پژوهش‌های پیمایشی کمّی.",
      description="طبق بخش ۱۰ سند (سطر ۴۰۸) ابزار پیمایش را نمونه‌هایی چون Google Forms، Qualtrics و SurveyMonkey تشکیل می‌دهند؛ این ابزارها پرسش‌نامه را طراحی، توزیع و پاسخ‌ها را به‌صورت خودکار جمع‌آوری می‌کنند و خروجی مستقیما‌ً وارد نرم‌افزارهای آماری می‌شود.",
      key_propositions=["پیمایش کمّی با حجم نمونه بزرگ را ممکن می‌سازند","پاسخ‌ها به‌صورت ساختاریافته و مستقیم وارد فایل داده می‌شوند"],
      origin_period="1990s-2026", geographical_origin="آمریکا",
      related_disciplines=["علوم ارتباطات","روان‌شناسی"],
      applications=["پیمایش‌های آنلاین","سنجش نگرش و رضایت"],
      strengths=["مقیاس‌پذیری","جمع‌آوری خودکار","کاهش هزینه"],
      limitations=["وابستگی به دسترسی مخاطب به فناوری","ناتوانی در سنجش عمق معنا"],
      references=["Creswell & Creswell (2018), Research Design"],
      facets=[{"key":"data_type","value":"quantitative"}])

add_e(id="kg-instrument-interview", title_fa="ابزارهای مصاحبه", title_en="Interview Tools",
      slug="interview", entity_type="INSTRUMENT", parent_id=None,
      abstract="ابزارهای اجرای مصاحبه: ضبط‌کننده صوتی و نرم‌افزارهای پیاده‌سازی مصاحبه.",
      description="طبق بخش ۱۰ سند (سطر ۴۰۹) ابزار مصاحبه شامل ضبط‌کننده صوتی و نرم‌افزار پیاده‌سازی مصاحبه (ساختار مصاحبه، نوبت‌بندی و ثبت پاسخ‌ها) است؛ این ابزارها اجرای فنی مصاحبه‌های ساختاریافته تا نیمه‌ساختاریافته را ممکن می‌سازند.",
      key_propositions=["ثبت دقیق و قابل بازنمایه‌ی پاسخ مصاحبه‌شده","پشتیبانی از اجرای سیستماتیک مصاحبه"],
      origin_period="1950s-2026",
      related_disciplines=["علوم ارتباطات","جامعه‌شناسی"],
      applications=["مصاحبه عمیق","مردم‌نگاری"],
      strengths=["ثبت کامل داده"],
      limitations=["وابستگی به کیفیت تجهیزات","نیاز به رضایت آگاهانه برای ضبط"],
      facets=[{"key":"data_type","value":"qualitative"}])

add_e(id="kg-software-nvivo", title_fa="NVivo", title_en="NVivo", slug="nvivo",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار تحلیل و مدیریت داده‌های کیفی برای کدگذاری و شناسای الگوها.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۰) NVivo یکی از سه ابزار اصلی تحلیل کیفی است؛ داده‌های متن، صوت، تصویر و ویدئو را مدیریت، کدگذاری و الگوهای مضمونی را آشکار می‌سازد.",
      key_propositions=["مدیریت داده‌های کیفی چندوجهی","کدگذاری دستی و نیمه‌خودکار"],
      key_figures=["QSR International"], origin_period="2002-2026", geographical_origin="آمریکا",
      related_disciplines=["روش‌شناسی","علوم ارتباطات"],
      applications=["تحلیل مضمون","تحلیل گفتمان"],
      strengths=["رؤیت بصری الگوها","پشتیبانی چندمنبعه"],
      limitations=["هزینه","منحنی یادگیری"],
      criticisms=["محدودیت‌های کدگذاری خودکار"],
      references=["QSR International, NVivo Documentation"],
      facets=[{"key":"data_type","value":"qualitative"}])

add_e(id="kg-software-atlas-ti", title_fa="ATLAS.ti", title_en="ATLAS.ti", slug="atlas-ti",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار تحلیل داده‌های کیفی با رویکرد بصری و شبکه‌ای.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۰) ATLAS.ti از ابزارهای تحلیل کیفی است؛ با رویکرد بصری (نقشه‌های مفهومی) و امکان همکاری گروهی، فرایند کدگذاری و تحلیل کیفی را پشتیبانی می‌کند.",
      key_propositions=["تحلیل بصری روابط میان کدها","مدیریت پروژه‌های گروهی"],
      key_figures=["ATLAS.ti GmbH"], origin_period="1998-2026", geographical_origin="آلمان",
      related_disciplines=["روش‌شناسی","علوم ارتباطات"],
      applications=["تحلیل مضمون","تحلیل محتوا"],
      strengths=["نمایش بصری شبکه کدها","هماهنگی تیمی"],
      limitations=["هزینه"],
      references=["ATLAS.ti GmbH, ATLAS.ti Handbook"],
      facets=[{"key":"data_type","value":"qualitative"}])

add_e(id="kg-software-maxqda", title_fa="MAXQDA", title_en="MAXQDA", slug="maxqda",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار تحلیل داده‌های کیفی، کمّی و آمیخته.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۰) MAXQDA از ابزارهای تحلیل کیفی است و برخلاف دو هم‌خانواده‌اش، تحلیل‌های کمّی و آمیخته را نیز پشتیبانی می‌کند؛ کدگذاری، تحلیل شبکه و تحلیل پرسشنامه را در یک محیط یکپارچه می‌سازد.",
      key_propositions=["پشتیبانی هم‌زمان تحلیل کیفی و کمّی","مدیریت داده‌های آمیخته"],
      key_figures=["VERBIS","Dr. Willibald Riedel"], origin_period="1988-2026", geographical_origin="آلمان",
      related_disciplines=["روش‌شناسی","علوم ارتباطات"],
      applications=["تحلیل مضمون","تحلیل پرسشنامه‌های کیفی-کمّی"],
      strengths=["یکپارچگی داده‌های آمیخته","تحلیل شبکه کدها"],
      limitations=["هزینه"],
      references=["VERBIS, MAXQDA Reference"],
      facets=[{"key":"data_type","value":"mixed"}])

add_e(id="kg-software-spss", title_fa="SPSS", title_en="IBM SPSS Statistics", slug="spss",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار آماری برای تحلیل داده‌های کمّی (سریع و کاربرپسند).",
      description="طبق بخش ۱۰ سند (سطر ۴۱۱) SPSS یکی از سه ابزار اصلی تحلیل کمّی است؛ تحلیل‌های توصیفی، استنباطی، همبستگی، رگرسیون و معادلات ساختاری را با رابط گرافیکی انجام می‌دهد و در علوم اجتماعی به‌طور گسترده کاربرد دارد.",
      key_propositions=["تحلیل‌های استنباطی و چندمتغیره","رابط گرافیکی و دسترس‌پذیری بالا"],
      origin_period="1968-2026", geographical_origin="آمریکا",
      related_disciplines=["آمار","علوم اجتماعی"],
      applications=["پیمایش‌های کمّی","آزمون فرضیه","تحلیل رگرسیون"],
      strengths=["دسترس‌پذیری","پشتیبانی گسترده"],
      limitations=["هزینه","محدودیت در مدل‌های پیچیده محاسباتی"],
      criticisms=["محدودیت در پردازش بزرگ‌داده"],
      references=["IBM, SPSS Statistics Reference"],
      facets=[{"key":"data_type","value":"quantitative"}])

add_e(id="kg-software-stata", title_fa="Stata", title_en="Stata", slug="stata",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار آماری پیشرفته برای تحلیل داده‌های کمّی و اقتصادسنجی.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۱) Stata از ابزارهای تحلیل کمّی است و به‌ویژه در مدل‌های طولی، اقتصادسنجی و روش‌های علّی (DiD، IV) قوی است؛ رابط دستوری و گرافیکی دارد.",
      key_propositions=["تحلیل داده‌های طولی و پنل","روش‌های علّی پیشرفته"],
      key_figures=["StataCorp"], origin_period="1985-2026", geographical_origin="آمریکا",
      related_disciplines=["آمار","اقتصادسنجی"],
      applications=["تحلیل علّی","مدل‌های رشد","رگرسیون چندسطحی"],
      strengths=["قدرت محاسباتی","پشتیبانی مدل‌های پیچیده"],
      limitations=["منحنی یادگیری"],
      references=["StataCorp, Stata User's Guide"],
      facets=[{"key":"data_type","value":"quantitative"}])

add_e(id="kg-software-sas", title_fa="SAS", title_en="SAS", slug="sas",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار آماری صنعتی برای تحلیل داده‌های کمّی بزرگ‌مقیاس.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۱) SAS از ابزارهای تحلیل کمّی است و در تحلیل‌های بزرگ‌مقیاس، صنایع دارو و بهداشت و گزارش‌های رگولاتوری کاربرد دارد؛ قدرت پردازش و قابلیت اتوماسیون بالا.",
      key_propositions=["پردازش داده‌های بزرگ","اتوماسیون فرایندهای تحلیلی"],
      key_figures=["SAS Institute"], origin_period="1976-2026", geographical_origin="آمریکا",
      related_disciplines=["آمار","پزشکی"],
      applications=["تحلیل داده‌های کلان","گزارش‌های بالینی"],
      strengths=["قدرت پردازش","اتوماسیون"],
      limitations=["هزینه","پیچیدگی"],
      references=["SAS Institute, SAS Documentation"],
      facets=[{"key":"data_type","value":"quantitative"}])

add_e(id="kg-software-r", title_fa="R", title_en="R", slug="r",
      entity_type="SOFTWARE", parent_id=None,
      abstract="زبان و محیط برنامه‌نویسی آمار برای تحلیل‌های کمّی و گرافیک علمی.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۲) R یکی از ابزارهای «تحلیل آماری و برنامه‌نویسی» است؛ با هزاران بسته (ggplot2، lme4، lavaan، tidyverse) تحلیل‌های آماری از توصیفی تا مدل‌های سلسله‌مراتبی را پشتیبانی می‌کند و رایگان و متن‌باز است.",
      key_propositions=["پشتیبانی کامل تحلیل‌های آماری و بیزی","گرافیک علمی و قابل انتشار"],
      key_figures=["Robert Gentleman","Ross Ihaka"], origin_period="1993-2026", geographical_origin="نیوزیلند",
      related_disciplines=["آمار","علم داده"],
      applications=["تحلیل‌های چندسطحی","مدل‌سازی بیزی","تحلیل عاملی"],
      strengths=["رایگان و متن‌باز","جامعه بزرگ بسته‌ها","انعطاف محاسباتی"],
      limitations=["منحنی یادگیری برنامه‌نویسی"],
      references=["R Core Team, R Documentation"],
      facets=[{"key":"data_type","value":"quantitative"}])

add_e(id="kg-software-python", title_fa="Python (تحلیل داده)", title_en="Python for Data Analysis",
      slug="python", entity_type="SOFTWARE", parent_id=None,
      abstract="زبان برنامه‌نویسی چندمنظوره با کتابخانه‌های تحلیلی (pandas, scikit-learn, NLTK).",
      description="طبق بخش ۱۰ سند (سطر ۴۱۲) Python از ابزارهای «تحلیل آماری و برنامه‌نویسی» است و با کتابخانه‌هایی چون pandas، statsmodels، scikit-learn، NLTK و spaCy تحلیل داده، یادگیری ماشین، پردازش زبان طبیعی و تحلیل محاسباتی گفتمان را پشتیبانی می‌کند.",
      key_propositions=["یکپارچگی آمار، ML و NLP","پردازش متن و تحلیل محاسباتی"],
      key_figures=["Guido van Rossum"], origin_period="1991-2026", geographical_origin="هلند",
      related_disciplines=["آمار","علم داده","NLP"],
      applications=["تحلیل محاسباتی گفتمان","یادگیری ماشین","پردازش زبان طبیعی"],
      strengths=["انعطاف","یکپارچگی با اکوسیستم AI","رایگان"],
      limitations=["منحنی یادگیری","وابستگی به انتخاب کتابخانه‌ها"],
      references=["Python Software Foundation, pandas, scikit-learn Documentation"],
      facets=[{"key":"data_type","value":"mixed"}])

add_e(id="kg-software-amos", title_fa="AMOS", title_en="IBM AMOS", slug="amos",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار مدل‌سازی معادلات ساختاری (SEM) با رابط گرافیکی.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۳) AMOS یکی از سه ابزار «مدل‌سازی معادلات ساختاری» است و مدل‌های معادلات ساختاری را با نمودارهای بصری و آزمون‌های برازش (chi-square، CFI، RMSEA) اجرا می‌کند.",
      key_propositions=["رابط بصری برای مدل‌های SEM","آزمون‌های برازش استاندارد"],
      key_figures=["Arbuckle"], origin_period="1989-2026", geographical_origin="آمریکا",
      related_disciplines=["آمار","روان‌سنجی"],
      applications=["مدل‌سازی معادلات ساختاری","تحلیل عاملی تأییدی"],
      strengths=["ساده‌سازی مدل‌سازی SEM","خروجی‌های بصری"],
      limitations=["هزینه","محدودیت در مدل‌های بسیار پیچیده"],
      references=["IBM, AMOS User's Guide"],
      facets=[{"key":"data_type","value":"quantitative"}])

add_e(id="kg-software-smartpls", title_fa="SmartPLS", title_en="SmartPLS", slug="smartpls",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار مدل‌سازی معادلات ساختاری مبتنی بر متغیر (PLS-SEM).",
      description="طبق بخش ۱۰ سند (سطر ۴۱۳) SmartPLS از ابزارهای مدل‌سازی SEM است و به‌ویژه روی PLS-SEM (پارسیال اقل‌مخفی) و مدل‌سازی عاملی مبتنی بر متغیر تمرکز دارد؛ برای داده‌های کوچک و مدل‌های تفسیری مناسب است.",
      key_propositions=["PLS-SEM و مدل‌سازی تفسیری","کاربرپسند"],
      key_figures=["Rigdon"], origin_period="1996-2026", geographical_origin="آمریکا",
      related_disciplines=["آمار","بازاریابی"],
      applications=["مدل‌های SEM با داده کوچک","تحلیل عاملی مبتنی بر متغیر"],
      strengths=["ساده","انعطاف در مدل‌های تفسیری"],
      limitations=["محدودیت در مدل‌های تأییدی بزرگ"],
      criticisms=["تفاوت روشی با CB-SEM"],
      references=["Rigdon, SmartPLS User Guide"],
      facets=[{"key":"data_type","value":"quantitative"}])

add_e(id="kg-software-lavaan", title_fa="lavaan (R)", title_en="lavaan (R package)", slug="lavaan",
      entity_type="SOFTWARE", parent_id=None,
      abstract="پکیج R برای مدل‌سازی معادلات ساختاری (CB-SEM) و مدل‌های رشد.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۳) lavaan سومین ابزار «مدل‌سازی معادلات ساختاری» است و به‌صورت پکیج در R اجرا می‌شود؛ CB-SEM، مدل‌های رشد، معادلات ساختاری پنهان و مدل‌های چندگروهی را با شفافیت کد می‌کند.",
      key_propositions=["CB-SEM و مدل‌های رشد","شفافیت کد و قابل تکرار"],
      key_figures=["Yves Rosseel"], origin_period="2012-2026", geographical_origin="هولند",
      related_disciplines=["آمار"],
      applications=["مدل‌های SEM","تحلیل عاملی تأییدی","مدل‌های رشد"],
      strengths=["رایگان و متن‌باز","قابل تکرار کامل","پشتیبانی مدل‌های پیشرفته"],
      limitations=["نیاز به دانش R"],
      references=["Rosseel, lavaan User's Guide"],
      facets=[{"key":"data_type","value":"quantitative"}])

add_e(id="kg-software-gephi", title_fa="Gephi", title_en="Gephi", slug="gephi",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار تجسم و تحلیل شبکه‌های اجتماعی.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۴) Gephi یکی از سه ابزار «تحلیل شبکه» است و با تجسم بصری قوی، محاسبه شاخص‌های مرکزیت و ساختار شبکه‌های بزرگ کاربرد دارد؛ رایگان و متن‌باز است.",
      key_propositions=["تجسم بصری شبکه‌های بزرگ","محاسبه شاخص‌های مرکزیت و ساختار"],
      key_figures=["Mathieu Bastian","Stephane Jacomy"], origin_period="2008-2026", geographical_origin="فرانسه",
      related_disciplines=["علوم شبکه","شبکه‌های اجتماعی"],
      applications=["تحلیل شبکه اجتماعی","تحلیل مرکزیت","تجسم گراف"],
      strengths=["رایگان","تجسم قوی","پشتیبانی گراف‌های بزرگ"],
      limitations=["رابط پیچیده در تحلیل‌های پیشرفته"],
      references=["Bastian et al. (2009), Gephi: Open Software for Network Visualization"],
      facets=[{"key":"data_type","value":"network"}])

add_e(id="kg-software-ucinet", title_fa="UCINET", title_en="UCINET", slug="ucinet",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار تحلیل شبکه‌های اجتماعی (SNA) با ابزارهای توصیفی و استنباطی.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۴) UCINET از ابزارهای تحلیل شبکه است و مجموعه‌ای از روش‌های توصیفی (مرکزیت، تراکم) و پیشرفته (ERM، FRUIT) را در یک محیط یکپارچه می‌سازد.",
      key_propositions=["روش‌های استاندارد SNA","پشتیبانی ERM"],
      key_figures=["Wellman","Holland"], origin_period="1991-2026", geographical_origin="کانادا",
      related_disciplines=["علوم شبکه"],
      applications=["تحلیل شبکه اجتماعی","تحلیل ERM","تحلیل مرکزیت"],
      strengths=["روش‌های استاندارد"],
      limitations=["هزینه","رابط کلاسیک"],
      references=["Holland et al. (2005), UCINET for Social Network Analysis"],
      facets=[{"key":"data_type","value":"network"}])

add_e(id="kg-software-pajek", title_fa="Pajek", title_en="Pajek", slug="pajek",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار تجسم و تحلیل شبکه‌های بزرگ.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۴) Pajek از ابزارهای تحلیل شبکه است و برای شبکه‌های بسیار بزرگ (میلیون‌ها رأس) به‌دلیل الگوریتم‌های بهینه کاربرد دارد؛ رایگان است.",
      key_propositions=["پردازش شبکه‌های بسیار بزرگ","الگوریتم‌های بهینه"],
      key_figures=["Andrej Mrvar","Vladimir Batagelj"], origin_period="1996-2026", geographical_origin="اسلوونی",
      related_disciplines=["علوم شبکه"],
      applications=["تحلیل شبکه‌های بزرگ","محاسبه مرکزیت","تجزیه قطعه"],
      strengths=["پردازش گراف‌های بزرگ","رایگان"],
      limitations=["رابط ساده"],
      references=["Batagelj & Mrvar, Pajek: Systems for Large Network Analysis"],
      facets=[{"key":"data_type","value":"network"}])

add_e(id="kg-software-antconc", title_fa="AntConc", title_en="AntConc", slug="antconc",
      entity_type="SOFTWARE", parent_id=None,
      abstract="ابزار تحلیل متن (Corpus Linguistics) برای فراوانی و هم‌پیشامد واژگان.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۵) AntConc از ابزارهای «تحلیل متن» است و برای تحلیل فراوانی واژگان، هم‌پیشامد (concordance) و n-gram در متن‌های بزرگ کاربرد دارد؛ رایگان و سبک است.",
      key_propositions=["تحلیل فراوانی و هم‌پیشامد","سبکی و دسترس‌پذیری"],
      key_figures=["Laurence Anthony"], origin_period="2006-2026", geographical_origin="ژاپن",
      related_disciplines=["زبان‌شناسی","روش‌شناسی"],
      applications=["تحلیل متن","تحلیل گفتمان کمّی","تحلیل فراوانی"],
      strengths=["رایگان","سریع","خروجی‌های قابل استفاده"],
      limitations=["محدودیت در تحلیل‌های پیچیده معنایی"],
      references=["Anthony (2007), AntConc 3.0: A Corpus Linguistics Tools"],
      facets=[{"key":"data_type","value":"text"}])

add_e(id="kg-software-voyant", title_fa="Voyant Tools", title_en="Voyant Tools", slug="voyant",
      entity_type="SOFTWARE", parent_id=None,
      abstract="پلتفرم آنلاین تحلیل و تجسم متن.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۵) Voyant از ابزارهای «تحلیل متن» است و تحلیل‌های فراوانی، تجسم واژگان، ترسیم مسیر و شبکه کلمات را به‌صورت آنلاین و بدون نصب انجام می‌دهد.",
      key_propositions=["تحلیل آنلاین بدون نصب","تجیم و تحلیل هم‌زمان"],
      origin_period="2014-2026", geographical_origin="کانادا",
      related_disciplines=["زبان‌شناسی","دیجیتال‌های انسانی"],
      applications=["تحلیل متن","تجیم واژگان","تحلیل گفتمان کمّی"],
      strengths=["آنلاین","آسان"],
      limitations=["وابستگی به اینترنت","محدودیت در متن‌های بسیار بزرگ"],
      references=["Voyant Tools Documentation"],
      facets=[{"key":"data_type","value":"text"}])

add_e(id="kg-instrument-web-extraction", title_fa="ابزارهای استخراج داده دیجیتال",
      title_en="Digital Data Extraction Tools", slug="web-extraction",
      entity_type="INSTRUMENT", parent_id=None,
      abstract="ابزارهای استخراج داده از وب و API برای پژوهش‌های محاسباتی.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۶) «ابزارهای تحلیل داده دیجیتال» شامل ابزارهای استخراج وب (Web Scraping) و ابزارهای API هستند؛ این ابزارها داده‌های ساختاریافته و نیمه‌ساختاریافته را از وب، شبکه‌های اجتماعی و سرویس‌های دیجیتال جمع‌آوری می‌کنند.",
      key_propositions=["جمع‌آوری داده از منابع دیجیتال بزرگ","استخراج خودکار"],
      origin_period="2000s-2026",
      related_disciplines=["علوم داده","علوم ارتباطات دیجیتال"],
      applications=["تحلیل شبکه‌های اجتماعی","تحلیل محاسباتی گفتمان"],
      strengths=["مقیاس‌پذیری","خودکاری"],
      limitations=["وابستگی به ساختار API","محدودیت‌های اخلاقی دسترسی"],
      facets=[{"key":"data_type","value":"digital"}])

add_e(id="kg-instrument-coding-software", title_fa="نرم‌افزارهای کدگذاری و تحلیل گفتمان",
      title_en="Discourse Coding & Analysis Software", slug="discourse-coding",
      entity_type="INSTRUMENT", parent_id=None,
      abstract="نرم‌افزارهای کدگذاری و تحلیل متن برای پژوهش‌های گفتمانی.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۷) «ابزارهای تحلیل گفتمان» نرم‌افزارهای کدگذاری و تحلیل متن را شامل می‌شوند؛ این ابزارها اجرای عملی تحلیل گفتمان (مانند CDA) را با کدگذاری دستی و نیمه‌خودکار ممکن می‌سازند.",
      key_propositions=["کدگذاری ساختاریافته متن‌های گفتمانی","پشتیبانی تحلیل انتقادی"],
      origin_period="1990s-2026",
      related_disciplines=["روش‌شناسی","زبان‌شناسی"],
      applications=["تحلیل گفتمان انتقادی","تحلیل گفتمان فوکویی"],
      strengths=["ساختاردهی فرایند کدگذاری","قابلیت همکاری تیمی"],
      limitations=["وابستگی به کیفیت کدگذاری"],
      facets=[{"key":"data_type","value":"qualitative"}])

add_e(id="kg-software-zotero", title_fa="Zotero", title_en="Zotero", slug="zotero",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار مدیریت منابع و ارجاع‌دهی پژوهشی (رایگان و متن‌باز).",
      description="طبق بخش ۱۰ سند (سطر ۴۱۸) Zotero یکی از سه ابزار «مدیریت منابع» است؛ جمع‌آوری، سازمان‌بندی و ارجاع‌دهی منابع (PDF، یادداشت‌ها، داده) را با افزونه‌ها برای Word و LaTeX انجام می‌دهد و رایگان است.",
      key_propositions=["مدیریت یکپارچه منابع علمی","ارجاع‌دهی خودکار در چند سبک"],
      key_figures=["Roy Rosenzweig"], origin_period="2007-2026", geographical_origin="آمریکا",
      related_disciplines=["روش‌شناسی"],
      applications=["مدیریت منابع پژوهشی","همکاری تیمی"],
      strengths=["رایگان و متن‌باز","افزونه‌های گسترده","همکاری آنلاین"],
      limitations=["محدودیت در آرشیو بسیار بزرگ"],
      references=["Zotero Project Documentation"],
      facets=[{"key":"data_type","value":"metadata"}])

add_e(id="kg-software-endnote", title_fa="EndNote", title_en="EndNote", slug="endnote",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار مدیریت منابع و ارجاع‌دهی (رایج در علوم پزشکی).",
      description="طبق بخش ۱۰ سند (سطر ۴۱۸) EndNote از ابزارهای «مدیریت منابع» است و در علوم پزشکی و زیستی به‌طور گسترده کاربرد دارد؛ ارجاع‌دهی خودکار و مدیریت پایگاه کتابخانه‌ای قوی.",
      key_propositions=["مدیریت منابع در علوم پزشکی","هماهنگی با Word"],
      origin_period="1986-2026", geographical_origin="آمریکا",
      related_disciplines=["پزشکی","روش‌شناسی"],
      applications=["مدیریت منابع","ارجاع‌دهی خودکار"],
      strengths=["پشتیبانی گسترده در پزشکی"],
      limitations=["هزینه"],
      references=["Clarivate, EndNote User Guide"],
      facets=[{"key":"data_type","value":"metadata"}])

add_e(id="kg-software-mendeley", title_fa="Mendeley", title_en="Mendeley", slug="mendeley",
      entity_type="SOFTWARE", parent_id=None,
      abstract="نرم‌افزار رایگان مدیریت منابع و آرشیو PDF.",
      description="طبق بخش ۱۰ سند (سطر ۴۱۸) Mendeley از ابزارهای «مدیریت منابع» است و رایگان (با محدودیت فضا)؛ آرشیو PDF، ارجاع‌دهی و همکاری تیمی را پشتیبانی می‌کند.",
      key_propositions=["آرشیو رایگان PDF","همکاری تیمی"],
      origin_period="2010-2026", geographical_origin="آمریکا",
      related_disciplines=["روش‌شناسی","علوم"],
      applications=["مدیریت منابع","آرشیو PDF","هماهنگی تیمی"],
      strengths=["رایگان"],
      limitations=["محدودیت فضای رایگان","وابستگی به اکوسیستم Elsevier"],
      references=["Elsevier, Mendeley Documentation"],
      facets=[{"key":"data_type","value":"metadata"}])

# ============ Section 11: QUALITY CRITERIA (10 quant + 9 qual + 4 mixed) ============
# --- Quantitative (10) ---
quant_quality = [
 ("kg-quality-content-validity","روایی محتوا","Content Validity","content-validity",
  "مقداری از یک ابزار سنجش که سازه را به‌طور کامل و منطقی پوشش می‌دهد.",
  "طبق بخش ۱۱ سند (سطر ۴۲۸) «روایی محتوا» یکی از معیارهای کیفیت پژوهش کمّی است؛ یعنی گویه‌های ابزار به‌درستی و به‌طور کامل حوزه‌ی سازه را پوشش می‌دهند (بررسی تخصصی، CVI).",
  ["معیار روایی ابزار سنجش","بررسی با روش خبره‌ای (CVI)"],
  ["Nunnally (1978), Psychometric Theory"]),
 ("kg-quality-construct-validity","روایی سازه","Construct Validity","construct-validity",
  "درجه‌ای که ابزار، سازه‌ی نظری مورد نظر را واقعا‌ً اندازه می‌گیرد.",
  "طبق بخش ۱۱ سند (سطر ۴۲۹) «روایی سازه» یکی از معیارهای کمّی است؛ با بررسی ساختار عاملی (تحلیل عاملی تأییدی) و همبستگی‌های همگرا/واگرا سنجیده می‌شود.",
  ["مبنای روایی ابزار","سنجه با CFA و همبستگی"],
  ["Pettigrew & Jones (1990), The Importance of Construct Validity"]),
 ("kg-quality-criterion-validity","روایی ملاکی","Criterion-Related Validity","criterion-validity",
  "درجه‌ای که نتایج ابزار با معیار بیرونی (ملاک) همبسته است.",
  "طبق بخش ۱۱ سند (سطر ۴۳۰) «روایی ملاکی» یکی از معیارهای کمّی است و شامل روایی هم‌زمان (concurrent) و پیش‌بین (predictive) می‌شود؛ با همبستگی نتایج ابزار با معیار بیرونی سنجیده می‌شود.",
  ["مقایسه با معیار بیرونی","روایی هم‌زمان و پیش‌بین"],
  ["Cronbach & Meehl (1955), Construct Validity in Psychological Tests"]),
 ("kg-quality-convergent-validity","روایی همگرا","Convergent Validity","convergent-validity",
  "همبستگی قوی ابزار با ابزارهای معتبر سازه‌ی هم‌سان.",
  "طبق بخش ۱۱ سند (سطر ۴۳۱) «روایی همگرا» یکی از معیارهای کمّی است؛ ابزار باید با ابزارهای معتبر سازه‌ی هم‌سان همبستگی بالایی نشان دهد.",
  ["سنجه همبستگی با ابزارهای هم‌سازه","مجموعه‌ای از شواهد"],
  ["Campbell & Fiske (1959), Convergent and Discriminant Validation"]),
 ("kg-quality-divergent-validity","روایی واگرا","Discriminant (Divergent) Validity","divergent-validity",
  "همبستگی ضعیف ابزار با ابزارهای سازه‌های متفاوت.",
  "طبق بخش ۱۱ سند (سطر ۴۳۲) «روایی واگرا» یکی از معیارهای کمّی است؛ ابزار باید با ابزارهای سازه‌های متفاوت همبستگی پایینی نشان دهد تا تمایز سازه‌ها تأیید شود.",
  ["سنجه تمایز سازه‌ها","مهم در تحلیل عاملی تأییدی"],
  ["Campbell & Fiske (1959), Convergent and Discriminant Validation"]),
 ("kg-quality-test-retest-reliability","پایایی بازآزمایی","Test-Retest Reliability","test-retest-reliability",
  "ثبات نتایج ابزار در دو یا چند اندازه‌گیری در زمان‌های متفاوت.",
  "طبق بخش ۱۱ سند (سطر ۴۳۳) «پایایی بازآزمایی» یکی از معیارهای کمّی است؛ با همبستگی نتایج دو اندازه‌گیری در زمان‌های متفاوت سنجیده می‌شود.",
  ["ثبات زمانی ابزار","مهم در پژوهش‌های طولی"],
  ["Nunnally (1978), Psychometric Theory"]),
 ("kg-quality-cronbach-alpha","آلفای کرونباخ","Cronbach's Alpha","cronbach-alpha",
  "شاخص پایایی درونی (Internal Consistency) ابزار بر اساس همبستگی گویه‌ها.",
  "طبق بخش ۱۱ سند (سطر ۴۳۴) «آلفای کرونباخ» یکی از معیارهای کمّی است؛ با همبستگی میان گویه‌ها پایایی درونی ابزار را سنجیده و آستانه‌ی ۰.۷ معمولا‌ً قابل قبول شمرده می‌شود.",
  ["شایع‌ترین شاخص پایایی درونی","آستانه 0.7"],
  ["Cronbach (1951), Coefficient Alpha and the Internal Structure of Tests"]),
 ("kg-quality-mcdonald-omega","امگای مک‌دونالد","McDonald's Omega","mcdonald-omega",
  "شاخص پایایی درونی مبتنی بر تحلیل عاملی (جایگزین دقیق‌تر آلفا).",
  "طبق بخش ۱۱ سند (سطر ۴۳۵) «امگای مک‌دونالد» یکی از معیارهای کمّی است؛ با تحلیل عاملی (محتمل‌ترین) و مدل‌سازی همبستگی، جایگزین دقیق‌تر آلفای کرونباخ، به‌ویژه در مدل‌های چندعاملی.",
  ["پایایی درونی مبتنی بر مدل عاملی","دقیق‌تر از آلفا در مدل‌های چندعاملی"],
  ["McDonald (1999), Test Theory: A Unified Treatment"]),
 ("kg-quality-inter-rater-reliability","پایایی بین‌ارزیابان","Inter-Rater Reliability","inter-rater-reliability",
  "درجه‌ی توافق چند ارزیاب در کدگذاری یا امتیازدهی به داده‌ها.",
  "طبق بخش ۱۱ سند (سطر ۴۳۶) «پایایی بین‌ارزیابان» یکی از معیارهای کمّی است؛ با شاخص‌هایی چون کاپای کوئن، آلفای کرونباخ بین‌ارزیاب و همبستگی intra-class سنجیده می‌شود.",
  ["توافق چند ارزیاب","مهم در تحلیل محتوای کمّی"],
  ["Fleiss (1981), Statistical Methods for Rates and Proportions"]),
 ("kg-quality-internal-external-validity","روایی درونی و بیرونی","Internal & External Validity","internal-external-validity",
  "روایی درونی (درستی نتیجه‌گیری علّی) و روایی بیرونی (تعمیم‌پذیری).",
  "طبق بخش ۱۱ سند (سطر ۴۳۷) «اعتبار درونی و بیرونی» یکی از معیارهای کمّی است؛ درونی یعنی بدون تهدیدکننده‌های داخلی، بیرونی یعنی قابلیت تعمیم نتایج به زمینه‌های دیگر.",
  ["جفت معیار اصلی اعتبار پژوهش کمّی","درستی نتیجه‌گیری و تعمیم‌پذیری"],
  ["Campbell & Stanley (1963), Experimental and Quasi-Experimental Designs"]),
]
for (qid,tfa,ten,slug,abs_,desc_,props,refs) in quant_quality:
    add_e(id=qid, title_fa=tfa, title_en=ten, slug=slug, entity_type="QUALITY", parent_id=None,
          abstract=abs_, description=desc_, key_propositions=props, references=refs,
          related_disciplines=["روان‌سنجی","روش‌شناسی"], origin_period="1950s-2026",
          facets=[{"key":"approach","value":"quantitative"}])

# --- Qualitative (9) ---
qual_quality = [
 ("kg-quality-credibility","اعتبارپذیری (کیفی)","Credibility","credibility",
  "معادل کیفی روایی: درستی و قابل‌اعتماد بودن یافته‌های پژوهش کیفی.",
  "طبق بخش ۱۱ سند (سطر ۴۴۱) «اعتبارپذیری (Credibility)» یکی از ۹ معیار کیفیت پژوهش کیفی است؛ معادل روایی در پژوهش کیفی و با مثلث‌سازی، مشاهدات طولانی و بازگردانی به مشارکت‌کنندگان تقویت می‌شود.",
  ["معادل کیفی روایی","مهم‌ترین معیار کیفی"],
  ["Lincoln & Guba (1985), Naturalistic Inquiry"]),
 ("kg-quality-transferability","انتقال‌پذیری","Transferability","transferability",
  "درجه‌ای که یافته‌های کیفی به زمینه‌های دیگر قابل انتقال است.",
  "طبق بخش ۱۱ سند (سطر ۴۴۲) «انتقال‌پذیری (Transferability)» یکی از ۹ معیار کیفی است؛ با توصیف غنی زمینه (thick description) و مستندسازی شرایط مطالعه، قابلیت انتقال یافته‌ها به بافت‌های دیگر را افزایش می‌دهد.",
  ["معادل کیفی روایی بیرونی","مبنا بر توصیف غنی"],
  ["Lincoln & Guba (1985), Naturalistic Inquiry"]),
 ("kg-quality-dependability","اتکاپذیری","Dependability","dependability",
  "معادل کیفی پایایی: ثبات فرایند پژوهش در صورت تکرار.",
  "طبق بخش ۱۱ سند (سطر ۴۴۳) «اتکاپذیری (Dependability)» یکی از ۹ معیار کیفی است؛ معادل کیفی پایایی و با مستندسازی دقیق فرایند (audit trail) و ممیزی پژوهش سنجیده می‌شود.",
  ["معادل کیفی پایایی","مستندسازی فرایند"],
  ["Lincoln & Guba (1985), Naturalistic Inquiry"]),
 ("kg-quality-confirmability","تأییدپذیری","Confirmability","confirmability",
  "معادل کیفی بی‌طرفی: یافته‌ها محصول داده‌ها، نه پیش‌فرض پژوهشگر.",
  "طبق بخش ۱۱ سند (سطر ۴۴۴) «تأییدپذیری (Confirmability)» یکی از ۹ معیار کیفی است؛ با بازاندیشی پژوهشگر، ممیزی و شفافیت تصمیم‌گیری‌ها، بی‌طرفی و وابستگی یافته‌ها به داده‌ها را تأیید می‌کند.",
  ["معادل کیفی بی‌طرفی","مستندسازی تصمیم‌گیری"],
  ["Lincoln & Guba (1985), Naturalistic Inquiry"]),
 ("kg-quality-researcher-reflexivity","بازاندیشی پژوهشگر","Researcher Reflexivity","researcher-reflexivity",
  "آگاهی پژوهشگر از تأثیر پیش‌فرض و موضع خود بر فرایند و یافته‌ها.",
  "طبق بخش ۱۱ سند (سطر ۴۴۵) «بازاندیشی پژوهشگر» یکی از ۹ معیار کیفی است؛ پژوهشگر باید اثرات بافت، پیش‌فرض و رابطه‌اش با مشارکت‌کنندگان را مستند کند تا اعتبار یافته‌ها افزایش یابد.",
  ["آگاهی از موضع‌گیری پژوهشگر","افزایش شفافیت کیفی"],
  ["Finlay (2002), Negotiating the Triangle: Reflexivity, Ethics and Dilemma in Qualitative Research"]),
 ("kg-quality-triangulation","مثلث‌سازی","Triangulation","triangulation",
  "استفاده از چند منبع، روش، نظریه یا پژوهشگر برای تقویت اعتبار یافته‌ها.",
  "طبق بخش ۱۱ سند (سطر ۴۴۶) «مثلث‌سازی (Triangulation)» یکی از ۹ معیار کیفی است؛ با ترکیب چند منبع (داده)، چند روش (گردآوری)، چند نظریه یا چند پژوهشگر، اعتبار و روایی یافته‌ها تقویت می‌شود.",
  ["تقویت اعتبار کیفی با چند منبع","مهم‌ترین شیوه اعتباربخشی"],
  ["Denzin (1978), The Research Act"]),
 ("kg-quality-participant-checking","بررسی مشارکت‌کنندگان","Member Checking","participant-checking",
  "بازگردانی یافته‌ها به مشارکت‌کنندگان برای تأیید تفسیر.",
  "طبق بخش ۱۱ سند (سطر ۴۴۷) «بررسی مشارکت‌کنندگان (Member Checking)» یکی از ۹ معیار کیفی است؛ یافته‌ها و تفسیرها به مشارکت‌کنندگان بازمی‌گردند تا دقت تفسیر تأیید شود و اعتبارپذیری افزایش یابد.",
  ["تأیید تفسیر با مشارکت‌کنندگان","افزایش اعتبارپذیری"],
  ["Lincoln & Guba (1985), Naturalistic Inquiry"]),
 ("kg-quality-research-audit","ممیزی پژوهش","Research Audit","research-audit",
  "بازبینی مستقل فرایند پژوهش برای ارزیابی اتکاپذیری و تأییدپذیری.",
  "طبق بخش ۱۱ سند (سطر ۴۴۸) «ممیزی پژوهش (Research Audit)» یکی از ۹ معیار کیفی است؛ یک بازبین مستقل فرایند، مستندات و تحلیل‌ها را بررسی می‌کند تا اتکاپذیری و تأییدپذیری پژوهش تأیید شود.",
  ["بازبینی مستقل فرایند","تقویت اتکاپذیری و تأییدپذیری"],
  ["Lincoln & Guba (1985), Naturalistic Inquiry"]),
 ("kg-quality-thick-description","توصیف غنی","Thick Description","thick-description",
  "توصیف دقیق و بافت‌مند داده‌ها برای افزایش انتقال‌پذیری یافته‌ها.",
  "طبق بخش ۱۱ سند (سطر ۴۴۹) «توصیف غنی (Thick Description)» یکی از ۹ معیار کیفی است؛ با ارائه‌ی توصیف دقیق از بافت، باورها و کنش‌های مشارکت‌کنندگان، قابلیت انتقال یافته‌ها به بافت‌های دیگر افزایش می‌یابد.",
  ["مبنا بر بافت‌مندسازی داده","افزایش انتقال‌پذیری"],
  ["Geertz (1973), The Interpretation of Cultures"]),
]
for (qid,tfa,ten,slug,abs_,desc_,props,refs) in qual_quality:
    add_e(id=qid, title_fa=tfa, title_en=ten, slug=slug, entity_type="QUALITY", parent_id=None,
          abstract=abs_, description=desc_, key_propositions=props, references=refs,
          related_disciplines=["روش‌شناسی کیفی"], origin_period="1985-2026",
          facets=[{"key":"approach","value":"qualitative"}])

# --- Mixed (4) ---
mixed_quality = [
 ("kg-quality-mixed-design-validity","اعتبار طراحی آمیخته","Mixed Methods Design Validity","mixed-design-validity",
  "درجه‌ای که طراحی آمیخته با هدف و سؤال پژوهش هم‌راستاست.",
  "طبق بخش ۱۱ سند (سطر ۴۵۳) «اعتبار طراحی آمیخته» یکی از ۴ معیار کیفیت پژوهش آمیخته است؛ طراحی باید با سؤال پژوهش، منطق و منابع هم‌راستا باشد و ترکیب کمّی-کیفی معنادار باشد.",
  ["هم‌راستایی طراحی با سؤال پژوهش","مهم در پژوهش‌های آمیخته"],
  ["Creswell & Plano Clark (2018), Designing and Conducting Mixed Methods Research"]),
 ("kg-quality-mixed-integration-quality","کیفیت یکپارچه‌سازی داده‌ها","Mixed Methods Integration Quality","mixed-integration-quality",
  "درجه‌ای که داده‌های کمّی و کیفی به‌درستی و معنادار ترکیب شده‌اند.",
  "طبق بخش ۱۱ سند (سطر ۴۵۴) «کیفیت یکپارچه‌سازی داده‌ها» یکی از ۴ معیار آمیخته است؛ نحوه‌ی ترکیب داده‌های کمّی و کیفی (نقطه‌های اتصال، هم‌راستایی) باید معنادار و مستند باشد.",
  ["مبنا بر هم‌راستایی داده‌ها","مستندسازی نقطه‌های اتصال"],
  ["Creswell & Plano Clark (2018), Designing and Conducting Mixed Methods Research"]),
 ("kg-quality-mixed-integrated-inferences","استنتاج‌های یکپارچه","Integrated Inferences","mixed-integrated-inferences",
  "درجه‌ای که استنتاج‌های نهایی هم از داده کمّی و هم کیفی بهره می‌برند.",
  "طبق بخش ۱۱ سند (سطر ۴۵۵) «استنتاج‌های یکپارچه» یکی از ۴ معیار آمیخته است؛ یافته‌ها باید از ترکیب معنادار دو منبع داده برخاسته و هم‌راستا یا متمم هم باشند.",
  ["مبنا بر ترکیب معنادار دو منبع","هم‌راستایی یافته‌ها"],
  ["Creswell & Plano Clark (2018), Designing and Conducting Mixed Methods Research"]),
 ("kg-quality-mixed-congruence","سازگاری یافته‌های کمّی و کیفی","Quantitative-Qualitative Congruence","mixed-congruence",
  "درجه‌ی هم‌راستایی (یا تفاوت معنادار) یافته‌های کمّی و کیفی.",
  "طبق بخش ۱۱ سند (سطر ۴۵۶) «سازگاری یافته‌های کمّی و کیفی» یکی از ۴ معیار آمیخته است؛ هم‌راستایی یا تفاوت معنادار یافته‌های دو شاخه باید مستند و تفسیر شده باشد.",
  ["مبنا بر هم‌راستایی یا تفاوت معنادار","مستندسازی تحلیل تفاوت‌ها"],
  ["Creswell & Plano Clark (2018), Designing and Conducting Mixed Methods Research"]),
]
for (qid,tfa,ten,slug,abs_,desc_,props,refs) in mixed_quality:
    add_e(id=qid, title_fa=tfa, title_en=ten, slug=slug, entity_type="QUALITY", parent_id=None,
          abstract=abs_, description=desc_, key_propositions=props, references=refs,
          related_disciplines=["روش‌شناسی آمیخته"], origin_period="2000s-2026",
          facets=[{"key":"approach","value":"mixed"}])

# ============ Section 12: ETHICS (14 principles) ============
ethics = [
 ("kg-ethics-informed-consent","رضایت آگاهانه","Informed Consent","informed-consent",
  "حقوق پژوهش‌شونده برای آگاه‌شدن از هدف، ریسک و حق خروج، و اجازه‌ی خودخواسته مشارکت.",
  "طبق بخش ۱۲ سند (سطر ۴۶۰) «رضایت آگاهانه» نخستین اصل اخلاقی پژوهش است؛ پژوهش‌شونده باید پیش از مشارکت از هدف، روش‌ها، ریسک‌ها و حق خودداری آگاه شود و رضایت خود را به‌طور داوطلبانه بدهد.",
  ["پایه‌ی اصلی اخلاق پژوهش","معتبر در همه‌ی شاخه‌ها"],
  ["Belmont Report (1979), Ethical Principles and Guidelines"]),
 ("kg-ethics-confidentiality","محرمانگی","Confidentiality","confidentiality",
  "حفظ اسرار داده‌ها و اطلاعات پژوهش‌شونده در برابر اشخاص ثالث.",
  "طبق بخش ۱۲ سند (سطر ۴۶۱) «محرمانگی» یکی از ۱۴ اصل اخلاقی است؛ اطلاعات شخصی و پاسخ‌های پژوهش‌شونده باید در برابر اشخاص ثالث حفظ شود و تنها در چارچوب تعریف‌شده استفاده شوند.",
  ["حفظ اسرار داده","مبنا بر اعتماد مشارکت‌کننده"],
  ["GDPR (2018); APA Ethics Code (2017)"]),
 ("kg-ethics-anonymization","ناشناس‌سازی","Anonymization","anonymization",
  "حذف یا تغییر اطلاعات هویتی پژوهش‌شونده از داده‌ها.",
  "طبق بخش ۱۲ سند (سطر ۴۶۲) «ناشناس‌سازی» یکی از ۱۴ اصل اخلاقی است؛ با حذف یا تغییر نام، تاریخ تولد و دیگر اطلاعات هویتی، داده‌ها از هویت پژوهش‌شونده جدا می‌شوند.",
  ["حفظ حریم خصوصی","مهم در داده‌های حساس"],
  ["GDPR (2018), Article 4"]),
 ("kg-ethics-personal-data-protection","حفاظت از داده‌های شخصی","Personal Data Protection","personal-data-protection",
  "رعایت قوانین (مانند GDPR) برای حفاظت از داده‌های شخصی پژوهش‌شوندگان.",
  "طبق بخش ۱۲ سند (سطر ۴۶۳) «حفاظت از داده‌های شخصی» یکی از ۱۴ اصل اخلاقی است؛ با رعایت قوانین محلی (مانند GDPR) در جمع‌آوری، ذخیره، استفاده و حذف داده‌های شخصی.",
  ["مبنا بر قوانین محلی","مهم در پژوهش‌های دیجیتال"],
  ["GDPR (2018); California CCPA (2018)"]),
 ("kg-ethics-digital-research-ethics","اخلاق پژوهش دیجیتال","Digital Research Ethics","digital-research-ethics",
  "اصول اخلاقی پژوهش‌هایی که داده‌ها را از فضای دیجیتال جمع‌آوری می‌کنند.",
  "طبق بخش ۱۲ سند (سطر ۴۶۴) «اخلاق پژوهش دیجیتال» یکی از ۱۴ اصل اخلاقی است؛ اصول اخلاقی‌ای برای پژوهش‌هایی که داده‌ها را از فضای دیجیتال (وب، شبکه اجتماعی، لاگ) جمع‌آوری می‌کنند؛ شامل دسترسی، اجازه، حریم خصوصی و تفسیر.",
  ["مبنا بر داده‌های دیجیتال","مهم در پژوهش‌های محاسباتی"],
  ["ACM Code of Ethics (2018)"]),
 ("kg-ethics-social-media-ethics","اخلاق پژوهش در شبکه‌های اجتماعی","Social Media Research Ethics","social-media-ethics",
  "اصول اخلاقی دسترسی و استفاده از داده‌های عمومی/خصوصی در شبکه‌های اجتماعی.",
  "طبق بخش ۱۲ سند (سطر ۴۶۵) «اخلاق پژوهش در شبکه‌های اجتماعی» یکی از ۱۴ اصل اخلاقی است؛ با توجه به ماهیت «عمومی/خصوصی» داده‌ها در شبکه‌های اجتماعی، اصولی برای دسترسی، تفسیر و انتشار داده‌ها.",
  ["مبنا بر داده‌های شبکه اجتماعی","مهم در تحلیل شبکه"],
  ["ASPA Code of Ethics (2020)"]),
 ("kg-ethics-vulnerable-groups-ethics","اخلاق پژوهش با گروه‌های آسیب‌پذیر","Ethics with Vulnerable Groups","vulnerable-groups-ethics",
  "رعایت اصول اخلاقی ویژه هنگام پژوهش با کودکان، سالمندان، بیماران و…",
  "طبق بخش ۱۲ سند (سطر ۴۶۶) «اخلاق پژوهش با گروه‌های آسیب‌پذیر» یکی از ۱۴ اصل اخلاقی است؛ کودکان، سالمندان، بیماران، زندانیان و دیگر گروه‌های آسیب‌پذیر نیازمند مراقبت‌های اخلاقی بیشترند.",
  ["مبنا بر مراقبت مضاعف","مهم در پژوهش‌های اجتماعی"],
  ["Belmont Report (1979)"]),
 ("kg-ethics-conflict-of-interest","تعارض منافع","Conflict of Interest","conflict-of-interest",
  "شفاف‌سازی و مدیریت منافع مالی و غیرمالی پژوهشگر که ممکن است نتیجه را تحت تأثیر بگذارد.",
  "طبق بخش ۱۲ سند (سطر ۴۶۷) «تعارض منافع» یکی از ۱۴ اصل اخلاقی است؛ پژوهشگر باید منافع مالی، سازمانی یا شخصی که ممکن است بر نتیجه‌ی پژوهش اثر بگذارد را اعلام و مدیریت کند.",
  ["شفاف‌سازی منافع","مهم در پژوهش‌های صنعتی"],
  ["ICMJE (2016), Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work"]),
 ("kg-ethics-research-transparency","شفافیت پژوهش","Research Transparency","research-transparency",
  "مستندسازی شفاف هدف، روش، داده و محدودیت‌های پژوهش برای بازبینی.",
  "طبق بخش ۱۲ سند (سطر ۴۶۸) «شفافیت پژوهش» یکی از ۱۴ اصل اخلاقی است؛ هدف، روش‌ها، داده‌ها و محدودیت‌ها باید به‌قدری شفاف مستند شوند که پژوهش دیگر بتواند فرایند را بازبینی کند.",
  ["مبنا بر مستندسازی","مهم در بازتولیدپذیری"],
  ["Wilkinson et al. (2016), The FAIR Guiding Principles for Scientific Data Management"]),
 ("kg-ethics-pre-registration","پیش‌ثبت پژوهش","Pre-registration","pre-registration",
  "ثبت طرح پژوهش (سؤال، فرضیه، روش) پیش از گردآوری داده.",
  "طبق بخش ۱۲ سند (سطر ۴۶۹) «پیش‌ثبت پژوهش» یکی از ۱۴ اصل اخلاقی است؛ با ثبت طرح پژوهش (سؤال، فرضیه، روش) در یک ثبت‌خانه (مانند OSF) پیش از گردآوری داده، انعطاف‌پذیری و سوگیری انتخابی کاهش می‌یابد.",
  ["مبنا بر ثبت‌خانه (OSF)","کاهش HARKing"],
  ["Lakens et al. (2018), Pre-registration of Psychological Research"]),
 ("kg-ethics-open-data","دسترسی آزاد به داده","Open Data Access","open-data",
  "دسترسی آزاد به داده‌ها و روش‌ها برای بازبینی و استفاده مجدد.",
  "طبق بخش ۱۲ سند (سطر ۴۷۰) «دسترسی آزاد به داده» یکی از ۱۴ اصل اخلاقی است؛ داده‌ها و روش‌ها باید (در صورت امکان و رعایت حریم خصوصی) به‌صورت آزاد در دسترس جامعه علمی قرار گیرند.",
  ["مبنا بر FAIR","مهم در بازتولیدپذیری"],
  ["Wilkinson et al. (2016), The FAIR Guiding Principles"]),
 ("kg-ethics-reproducibility","بازتولیدپذیری","Reproducibility","reproducibility",
  "قابلیت تکرار فرایند پژوهش با داده‌ها و کدهای یکسان.",
  "طبق بخش ۱۲ سند (سطر ۴۷۱) «بازتولیدپذیری» یکی از ۱۴ اصل اخلاقی است؛ پژوهشگر دیگر باید با داده‌ها و کدهای یکسان بتواند نتیجه‌ها را بازتولید کند.",
  ["مبنا بر مستندسازی کامل","مهم در پژوهش‌های کمّی"],
  ["Baker (2016), 1,500 Scientists Lift the Lid on Replication Crisis"]),
 ("kg-ethics-replicability","تکرارپذیری","Replicability","replicability",
  "قابلیت تکرار پژوهش با داده‌های جدید و بازتولید نتیجه.",
  "طبق بخش ۱۲ سند (سطر ۴۷۲) «تکرارپذیری» یکی از ۱۴ اصل اخلاقی است؛ با تکرار پژوهش در شرایط جدید (داده‌های جدید یا مشارکت‌کنندگان دیگر) نتیجه‌ها تکرارپذیر باشند.",
  ["مبنا بر تکرار پژوهش","مهم در اعتبار علمی"],
  ["Klein et al. (2014), A Guide for Conducting Replication Studies"]),
 ("kg-ethics-data-management","مدیریت و نگهداری داده‌های پژوهش","Research Data Management","data-management",
  "طرح‌ریزی، ذخیره، مستندسازی و نگهداری داده‌ها در طول و پس از پژوهش.",
  "طبق بخش ۱۲ سند (سطر ۴۷۳) «مدیریت و نگهداری داده‌های پژوهش» آخرین اصل اخلاقی است؛ از جمع‌آوری تا انتشار و پس از پژوهش، داده‌ها باید به‌صورت منظم ذخیره، مستند و نگهداری شوند.",
  ["مبنا بر طرح مدیریت داده (DMP)","مهم در پژوهش‌های طولانی"],
  ["Wilkinson et al. (2016), The FAIR Guiding Principles"]),
]
for (eid,tfa,ten,slug,abs_,desc_,props,refs) in ethics:
    add_e(id=eid, title_fa=tfa, title_en=ten, slug=slug, entity_type="ETHICS", parent_id=None,
          abstract=abs_, description=desc_, key_propositions=props, references=refs,
          related_disciplines=["روش‌شناسی"], origin_period="2000s-2026",
          facets=[{"key":"category","value":"ethics"}])

# ============ Section 14: SPECIALIZED TECHNIQUES (10 domains) ============
specialized = [
 ("kg-technique-news-research","پژوهش روزنامه‌نگاری","News & Journalism Research","news-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی روزنامه‌نگاری (تحلیل خبر، منابع خبری، قاب خبری).",
  "طبق بخش ۱۴ سند (سطر ۵۵۲) حوزه‌ی «پژوهش روزنامه‌نگاری» شامل روش‌های تخصصی تحلیل محتوای خبر، تحلیل منابع خبری و تحلیل قاب خبری است.",
  ["تحلیل محتوای خبر","تحلیل منابع خبری","تحلیل قاب خبری"]),
 ("kg-technique-advertising-research","پژوهش تبلیغات","Advertising Research","advertising-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی تبلیغات (اثربخشی، پیام، یادآوری برند).",
  "طبق بخش ۱۴ سند (سطر ۵۵۳) حوزه‌ی «پژوهش تبلیغات» شامل آزمایش اثربخشی تبلیغ، تحلیل پیام تبلیغاتی و سنجش یادآوری برند است.",
  ["آزمایش اثربخشی تبلیغ","تحلیل پیام تبلیغاتی","سنجش یادآوری برند"]),
 ("kg-technique-pr-research","پژوهش روابط عمومی","Public Relations Research","pr-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی روابط عمومی (ممیزی ارتباطات، ذی‌نفعان، اعتبار).",
  "طبق بخش ۱۴ سند (سطر ۵۵۴) حوزه‌ی «پژوهش روابط عمومی» شامل ممیزی ارتباطات، تحلیل ذی‌نفعان و سنجش اعتبار سازمانی است.",
  ["ممیزی ارتباطات","تحلیل ذی‌نفعان","سنجش اعتبار سازمانی"]),
 ("kg-technique-audience-research","پژوهش مخاطب","Audience Research","audience-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی مخاطب (مصرف رسانه، تجربه کاربر، قوم‌نگاری مخاطب).",
  "طبق بخش ۱۴ سند (سطر ۵۵۵) حوزه‌ی «پژوهش مخاطب» شامل تحلیل مصرف رسانه، سنجش تجربه کاربر و قوم‌نگاری مخاطب است.",
  ["تحلیل مصرف رسانه","سنجش تجربه کاربر","قوم‌نگاری مخاطب"]),
 ("kg-technique-social-media-research","پژوهش شبکه‌های اجتماعی","Social Media Research","social-media-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی شبکه‌های اجتماعی (تحلیل شبکه، تعامل، انتشار).",
  "طبق بخش ۱۴ سند (سطر ۵۵۶) حوزه‌ی «پژوهش شبکه‌های اجتماعی» شامل تحلیل شبکه، تحلیل تعامل و تحلیل انتشار محتوا است.",
  ["تحلیل شبکه","تحلیل تعامل","تحلیل انتشار محتوا"]),
 ("kg-technique-digital-media-research","پژوهش رسانه‌های دیجیتال","Digital Media Research","digital-media-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی رسانه‌های دیجیتال (ردپای دیجیتال، تجربه کاربر، الگوریتم).",
  "طبق بخش ۱۴ سند (سطر ۵۵۷) حوزه‌ی «پژوهش رسانه‌های دیجیتال» شامل تحلیل ردپای دیجیتال، تحلیل تجربه کاربر و تحلیل الگوریتمی است.",
  ["تحلیل ردپای دیجیتال","تحلیل تجربه کاربر","تحلیل الگوریتمی"]),
 ("kg-technique-political-communication-research","پژوهش ارتباطات سیاسی","Political Communication Research","political-communication-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی ارتباطات سیاسی (کمپین، گفتمان، تبلیغات).",
  "طبق بخش ۱۴ سند (سطر ۵۵۸) حوزه‌ی «پژوهش ارتباطات سیاسی» شامل تحلیل کمپین، تحلیل گفتمان سیاسی و تحلیل تبلیغات سیاسی است.",
  ["تحلیل کمپین","تحلیل گفتمان سیاسی","تحلیل تبلیغات سیاسی"]),
 ("kg-technique-crisis-communication-research","پژوهش ارتباطات بحران","Crisis Communication Research","crisis-communication-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی ارتباطات بحران (پیام‌های بحران، اعتماد، ریسک).",
  "طبق بخش ۱۴ سند (سطر ۵۵۹) حوزه‌ی «پژوهش ارتباطات بحران» شامل تحلیل پیام‌های بحران، تحلیل اعتماد و تحلیل ارتباطات ریسک است.",
  ["تحلیل پیام‌های بحران","تحلیل اعتماد","تحلیل ارتباطات ریسک"]),
 ("kg-technique-film-tv-research","پژوهش سینما و تلویزیون","Film & Television Research","film-tv-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی سینما و تلویزیون (روایت، ژانر، بصری-نشانه‌شناختی).",
  "طبق بخش ۱۴ سند (سطر ۵۶۰) حوزه‌ی «پژوهش سینما و تلویزیون» شامل تحلیل روایت، تحلیل ژانر و تحلیل بصری و نشانه‌شناختی است.",
  ["تحلیل روایت","تحلیل ژانر","تحلیل بصری و نشانه‌شناختی"]),
 ("kg-technique-development-communication-research","پژوهش ارتباطات توسعه","Development Communication Research","development-communication-research",
  "روش‌های تخصصی پژوهش در حوزه‌ی ارتباطات توسعه (مشارکتی، تغییر رفتار، شبکه ذی‌نفعان).",
  "طبق بخش ۱۴ سند (سطر ۵۶۱) حوزه‌ی «پژوهش ارتباطات توسعه» شامل ارزیابی مشارکتی، تحلیل تغییر رفتار و تحلیل شبکه ذی‌نفعان است.",
  ["ارزیابی مشارکتی","تحلیل تغییر رفتار","تحلیل شبکه ذی‌نفعان"]),
]
for (tid,tfa,ten,slug,abs_,desc_,props) in specialized:
    add_e(id=tid, title_fa=tfa, title_en=ten, slug=slug, entity_type="TECHNIQUE", parent_id=None,
          abstract=abs_, description=desc_, key_propositions=props,
          related_disciplines=["علوم ارتباطات"], origin_period="1970s-2026",
          facets=[{"key":"domain","value":"communication"},{"key":"category","value":"specialized"}])

# ============ RELATIONS ============
# --- INSTRUMENTS -> techniques (APPLIES_TO) ---
add_r("kg-instrument-survey","kg-technique-questionnaire","APPLIES_TO","ابزارهای پیمایش برای اجرای پرسشنامه استفاده می‌شوند")
add_r("kg-instrument-survey","kg-technique-online-survey","APPLIES_TO","ابزارهای پیمایش برای نظرسنجی آنلاین استفاده می‌شوند")
add_r("kg-instrument-survey","kg-technique-delfi","APPLIES_TO","ابزارهای پیمایش می‌توانند برای اجرای دلفی الکترونیکی استفاده شوند",0.7)

for t in ["kg-technique-structured-interview","kg-technique-semistructured-interview",
          "kg-technique-in-depth-interview","kg-technique-group-interview","kg-technique-focus-group"]:
    add_r("kg-instrument-interview", t, "APPLIES_TO","ابزارهای مصاحبه برای اجرای این فن‌های مصاحبه استفاده می‌شوند")

for s in ["kg-software-nvivo","kg-software-atlas-ti","kg-software-maxqda"]:
    for a in ["kg-framework-qual-thematic-analysis","kg-framework-qual-content-analysis",
              "kg-framework-qual-discourse-analysis","kg-framework-qual-narrative-analysis"]:
        add_r(s, a, "APPLIES_TO","این نرم‌افزار برای پشتیبانی از اجرای این روش تحلیل کیفی استفاده می‌شود")

for s in ["kg-software-spss","kg-software-stata","kg-software-sas"]:
    for a in ["kg-analysis-t-test","kg-analysis-anova","kg-analysis-linear-regression",
              "kg-analysis-chi-square","kg-analysis-factor-analysis"]:
        add_r(s, a, "APPLIES_TO","این نرم‌افزار برای اجرای این تحلیل آماری استفاده می‌شود")

add_r("kg-software-r","kg-framework-structural-modeling","APPLIES_TO","R (با lavaan) برای مدل‌سازی ساختاری استفاده می‌شود")
add_r("kg-software-python","kg-analysis-causal-inference","APPLIES_TO","Python برای تحلیل‌های علّی و محاسباتی استفاده می‌شود",0.8)

for s in ["kg-software-amos","kg-software-smartpls","kg-software-lavaan"]:
    add_r(s,"kg-analysis-sem","APPLIES_TO","این نرم‌افزار برای اجرای معادلات ساختاری استفاده می‌شود")
    add_r(s,"kg-framework-structural-modeling","APPLIES_TO","این نرم‌افزار برای مدل‌سازی ساختاری استفاده می‌شود")

for s in ["kg-software-gephi","kg-software-ucinet","kg-software-pajek"]:
    add_r(s,"kg-technique-social-media-data","APPLIES_TO","این نرم‌افزار برای تحلیل شبکه‌های اجتماعی استفاده می‌شود",0.8)

for s in ["kg-software-antconc","kg-software-voyant"]:
    add_r(s,"kg-technique-text-analysis","APPLIES_TO","این ابزار برای تحلیل متن استفاده می‌شود")
    add_r(s,"kg-framework-qual-content-analysis","APPLIES_TO","این ابزار می‌تواند برای تحلیل محتوای کمّی استفاده شود",0.7)

add_r("kg-instrument-web-extraction","kg-technique-web-scraping","APPLIES_TO","ابزارهای استخراج وب برای استخراج داده از وب استفاده می‌شوند")
add_r("kg-instrument-web-extraction","kg-technique-api-extraction","APPLIES_TO","ابزارهای استخراج برای استخراج داده از API استفاده می‌شوند")
add_r("kg-instrument-web-extraction","kg-technique-social-media-data","APPLIES_TO","ابزارهای دیجیتال برای جمع‌آوری داده از شبکه‌های اجتماعی استفاده می‌شوند",0.8)

add_r("kg-instrument-coding-software","kg-framework-qual-discourse-analysis","APPLIES_TO","نرم‌افزارهای کدگذاری برای اجرای تحلیل گفتمان استفاده می‌شوند")
add_r("kg-instrument-coding-software","kg-analysis-qual-discourse-critical","APPLIES_TO","نرم‌افزارهای کدگذاری برای اجرای تحلیل گفتمان انتقادی استفاده می‌شوند",0.8)

# --- SOFTWARE -> QUALITY (MEASURES) ---
for s in ["kg-software-amos","kg-software-lavaan"]:
    add_r(s,"kg-quality-construct-validity","MEASURES","این نرم‌افزار با تحلیل عاملی تأییدی، روایی سازه را سنجش می‌کند")
for s in ["kg-software-spss","kg-software-stata","kg-software-sas"]:
    add_r(s,"kg-quality-cronbach-alpha","MEASURES","این نرم‌افزار آلفای کرونباخ را محاسبه می‌کند")
    add_r(s,"kg-quality-test-retest-reliability","MEASURES","این نرم‌افزار پایایی بازآزمایی را محاسبه می‌کند",0.85)
add_r("kg-software-r","kg-quality-mcdonald-omega","MEASURES","R (با pomec) برای سنجش امگای مک‌دونالد استفاده می‌شود")

# --- QUALITY -> APPROACH (APPLIES_TO) ---
for q in ["kg-quality-content-validity","kg-quality-construct-validity","kg-quality-criterion-validity",
          "kg-quality-convergent-validity","kg-quality-divergent-validity","kg-quality-test-retest-reliability",
          "kg-quality-cronbach-alpha","kg-quality-mcdonald-omega","kg-quality-inter-rater-reliability",
          "kg-quality-internal-external-validity"]:
    add_r(q,"kg-approach-quantitative","APPLIES_TO","این معیار در پژوهش‌های کمّی به‌کار می‌رود")
for q in ["kg-quality-credibility","kg-quality-transferability","kg-quality-dependability",
          "kg-quality-confirmability","kg-quality-researcher-reflexivity","kg-quality-triangulation",
          "kg-quality-participant-checking","kg-quality-research-audit","kg-quality-thick-description"]:
    add_r(q,"kg-approach-qualitative","APPLIES_TO","این معیار در پژوهش‌های کیفی به‌کار می‌رود")
for q in ["kg-quality-mixed-design-validity","kg-quality-mixed-integration-quality",
          "kg-quality-mixed-integrated-inferences","kg-quality-mixed-congruence"]:
    add_r(q,"kg-approach-mixed-methods","APPLIES_TO","این معیار در پژوهش‌های آمیخته به‌کار می‌رود")

# --- ETHICS -> APPROACH (APPLIES_TO) ---
for e_id in ["kg-ethics-informed-consent","kg-ethics-confidentiality","kg-ethics-anonymization",
             "kg-ethics-personal-data-protection","kg-ethics-digital-research-ethics",
             "kg-ethics-social-media-ethics","kg-ethics-vulnerable-groups-ethics",
             "kg-ethics-conflict-of-interest","kg-ethics-research-transparency",
             "kg-ethics-pre-registration","kg-ethics-open-data","kg-ethics-reproducibility",
             "kg-ethics-replicability","kg-ethics-data-management"]:
    for ap in ["kg-approach-quantitative","kg-approach-qualitative","kg-approach-mixed-methods"]:
        add_r(e_id, ap, "APPLIES_TO","این اصل اخلاقی در این رویکرد به‌کار می‌رود")

add_r("kg-ethics-digital-research-ethics","kg-technique-web-scraping","APPLIES_TO","اخلاق پژوهش دیجیتال در استخراج داده از وب به‌کار می‌رود")
add_r("kg-ethics-digital-research-ethics","kg-technique-api-extraction","APPLIES_TO","اخلاق پژوهش دیجیتال در استخراج داده از API به‌کار می‌رود")
add_r("kg-ethics-social-media-ethics","kg-technique-social-media-data","APPLIES_TO","اخلاق پژوهش در شبکه‌های اجتماعی در جمع‌آوری داده از شبکه‌های اجتماعی به‌کار می‌رود")
add_r("kg-instrument-web-extraction","kg-ethics-digital-research-ethics","APPLIES_TO","ابزارهای استخراج داده دیجیتال باید با اخلاق پژوهش دیجیتال همراه باشند",0.85)

# --- QUALITY internal relations ---
add_r("kg-quality-triangulation","kg-quality-participant-checking","USES","مثلث‌سازی می‌تواند از بررسی مشارکت‌کنندگان به‌عنوان یکی از منابع استفاده کند",0.8)
add_r("kg-quality-research-audit","kg-quality-confirmability","MEASURES","ممیزی پژوهش تأییدپذیری را سنجش می‌کند",0.85)
add_r("kg-quality-research-audit","kg-quality-dependability","MEASURES","ممیزی پژوهش اتکاپذیری را سنجش می‌کند",0.85)
add_r("kg-quality-participant-checking","kg-quality-credibility","MEASURES","بررسی مشارکت‌کنندگان اعتبارپذیری را سنجش می‌کند",0.85)
add_r("kg-quality-researcher-reflexivity","kg-quality-confirmability","MEASURES","بازاندیشی پژوهشگر تأییدپذیری را سنجش می‌کند",0.8)
add_r("kg-quality-thick-description","kg-quality-transferability","MEASURES","توصیف غنی انتقال‌پذیری را سنجش و تقویت می‌کند",0.85)
add_r("kg-quality-triangulation","kg-quality-credibility","MEASURES","مثلث‌سازی اعتبارپذیری را سنجش و تقویت می‌کند",0.85)
add_r("kg-quality-convergent-validity","kg-quality-construct-validity","PART_OF","روایی همگرا یکی از مؤلفه‌های روایی سازه است",0.9)
add_r("kg-quality-divergent-validity","kg-quality-construct-validity","PART_OF","روایی واگرا یکی از مؤلفه‌های روایی سازه است",0.9)
add_r("kg-quality-criterion-validity","kg-quality-construct-validity","RELATED_TO","روایی ملاکی و روایی سازه مکمل یکدیگرند",0.8)

# --- ETHICS internal relations ---
add_r("kg-ethics-anonymization","kg-ethics-confidentiality","RELATED_TO","ناشناس‌سازی و محرمانگی با هم برای حفظ حریم خصوصی استفاده می‌شوند",0.9)
add_r("kg-ethics-personal-data-protection","kg-ethics-confidentiality","EXTENDS","حفاظت از داده‌های شخصی، محرمانگی را در سطح قانونی گسترش می‌دهد",0.85)
add_r("kg-ethics-reproducibility","kg-ethics-replicability","RELATED_TO","بازتولیدپذیری و تکرارپذیری مکمل یکدیگرند",0.9)
add_r("kg-ethics-open-data","kg-ethics-reproducibility","RELATED_TO","دسترسی آزاد به داده، بازتولیدپذیری را تسهیل می‌کند",0.85)
add_r("kg-ethics-data-management","kg-ethics-open-data","RELATED_TO","مدیریت داده و دسترسی آزاد به داده مرتبط‌اند",0.8)
add_r("kg-ethics-pre-registration","kg-ethics-research-transparency","RELATED_TO","پیش‌ثبت و شفافیت پژوهش مرتبط‌اند",0.85)
add_r("kg-ethics-digital-research-ethics","kg-ethics-social-media-ethics","RELATED_TO","اخلاق دیجیتال و اخلاق شبکه‌های اجتماعی با هم مرتبط‌اند",0.85)

# --- TECHNIQUE (specialized) -> THEORY (TESTS) ---
add_r("kg-technique-news-research","kg-theory-framing","TESTS","پژوهش روزنامه‌نگاری (تحلیل قاب خبری) نظریه چارچوب‌سازی را آزمون می‌کند")
add_r("kg-technique-news-research","kg-theory-agenda-setting","TESTS","پژوهش روزنامه‌نگاری (تحلیل محتوای خبر) نظریه برجسته‌سازی را آزمون می‌کند")
add_r("kg-technique-advertising-research","kg-theory-uses-and-gratifications","TESTS","پژوهش تبلیغات (سنجش یادآوری برند) می‌تواند نظریه استفاده و رضامندی را آزمون کند",0.8)
add_r("kg-technique-political-communication-research","kg-theory-spiral-silence","TESTS","پژوهش ارتباطات سیاسی (تحلیل گفتمان سیاسی) می‌تواند نظریه مارپیچ سکوت را آزمون کند",0.8)
add_r("kg-technique-political-communication-research","kg-theory-framing","TESTS","پژوهش ارتباطات سیاسی (تحلیل تبلیغات سیاسی) نظریه چارچوب‌بندی سیاسی را آزمون می‌کند")
add_r("kg-technique-audience-research","kg-theory-encoding-decoding","TESTS","پژوهش مخاطب (قوم‌نگاری مخاطب) می‌تواند نظریه رمزگذاری و رمزگشایی را آزمون کند",0.8)
add_r("kg-technique-audience-research","kg-theory-uses-and-gratifications","TESTS","پژوهش مخاطب (تحلیل مصرف رسانه) نظریه استفاده و رضامندی را آزمون می‌کند")
add_r("kg-technique-development-communication-research","kg-theory-dependence","TESTS","پژوهش ارتباطات توسعه (تحلیل تغییر رفتار) می‌تواند نظریه وابستگی به رسانه را آزمون کند",0.7)
add_r("kg-technique-social-media-research","kg-theory-networked-communication","TESTS","پژوهش شبکه‌های اجتماعی (تحلیل شبکه) نظریه ارتباطات شبکه‌ای را آزمون می‌کند",0.8)
add_r("kg-technique-digital-media-research","kg-theory-algorithmic-agency","TESTS","پژوهش رسانه‌های دیجیتال (تحلیل الگوریتمی) نظریه عاملیت الگوریتمی را آزمون می‌کند",0.8)
add_r("kg-technique-digital-media-research","kg-theory-attention-economy","TESTS","پژوهش رسانه‌های دیجیتال (تحلیل ردپای دیجیتال) می‌تواند نظریه اقتصاد توجه را آزمون کند",0.7)
add_r("kg-technique-pr-research","kg-theory-communication-management","TESTS","پژوهش روابط عمومی (سنجش اعتبار سازمانی) می‌تواند نظریه مدیریت ارتباطات را آزمون کند",0.8)
add_r("kg-technique-film-tv-research","kg-framework-qual-semiotic-analysis","TESTS","پژوهش سینما و تلویزیون (تحلیل بصری-نشانه‌شناختی) از روش‌های نشانه‌شناختی استفاده می‌کند",0.8)

# --- TECHNIQUE (specialized) -> core TECHNIQUE (USES) ---
add_r("kg-technique-news-research","kg-technique-media-content-analysis","USES","پژوهش روزنامه‌نگاری از تحلیل محتوای رسانه‌ای استفاده می‌کند",0.9)
add_r("kg-technique-advertising-research","kg-technique-questionnaire","USES","پژوهش تبلیغات از پرسشنامه برای سنجش یادآوری برند استفاده می‌کند",0.85)
add_r("kg-technique-audience-research","kg-technique-digital-ethnography","USES","پژوهش مخاطب از مردم‌نگاری دیجیتال استفاده می‌کند",0.8)
add_r("kg-technique-social-media-research","kg-technique-social-media-data","USES","پژوهش شبکه‌های اجتماعی از جمع‌آوری داده شبکه‌های اجتماعی استفاده می‌کند",0.9)
add_r("kg-technique-digital-media-research","kg-technique-digital-footprint-analysis","USES","پژوهش رسانه‌های دیجیتال از تحلیل ردپای دیجیتال استفاده می‌کند",0.9)
add_r("kg-technique-political-communication-research","kg-technique-official-document-analysis","USES","پژوهش ارتباطات سیاسی از تحلیل اسناد رسمی استفاده می‌کند",0.8)
add_r("kg-technique-film-tv-research","kg-technique-video-analysis","USES","پژوهش سینما و تلویزیون از تحلیل ویدئو استفاده می‌کند",0.9)
add_r("kg-technique-development-communication-research","kg-technique-participant-observation","USES","پژوهش ارتباطات توسعه از مشاهده مشارکتی استفاده می‌کند",0.85)
add_r("kg-technique-pr-research","kg-technique-document-review","USES","پژوهش روابط عمومی از بررسی اسناد استفاده می‌کند",0.85)
add_r("kg-technique-crisis-communication-research","kg-technique-document-review","USES","پژوهش ارتباطات بحران از بررسی اسناد و تحلیل محتوا استفاده می‌کند",0.8)

# --- TECHNIQUE (specialized) -> SUBFIELD (APPLIES_TO) ---
add_r("kg-technique-news-research","kg-subfield-media-effects","APPLIES_TO","این روش تخصصی در حوزه‌ی پژوهش اثرات رسانه به‌کار می‌رود",0.85)
add_r("kg-technique-audience-research","kg-subfield-audience-reception","APPLIES_TO","این روش تخصصی در حوزه‌ی مطالعات مخاطب و دریافت به‌کار می‌رود",0.85)
add_r("kg-technique-political-communication-research","kg-subfield-political","APPLIES_TO","این روش تخصصی در حوزه‌ی ارتباطات سیاسی به‌کار می‌رود",0.9)
add_r("kg-technique-digital-media-research","kg-subfield-digital-media","APPLIES_TO","این روش تخصصی در حوزه‌ی رسانه‌های دیجیتال به‌کار می‌رود",0.9)
add_r("kg-technique-social-media-research","kg-subfield-digital-media","APPLIES_TO","این روش تخصصی در حوزه‌ی رسانه‌های دیجیتال به‌کار می‌رود",0.85)

# --- INSTRUMENT -> PARADIGM (INFLUENCED_BY) ---
for s in ["kg-instrument-survey","kg-software-spss","kg-software-stata","kg-software-sas"]:
    add_r(s,"kg-paradigm-positivism","INFLUENCED_BY","این ابزار از مبانی فلسفی اثبات‌گرایی (واقعیت عینی، اندازه‌گیری) تأثیر پذیرفته",0.8)

# --- QUALITY -> PARADIGM (INFLUENCED_BY) ---
for q in ["kg-quality-content-validity","kg-quality-construct-validity","kg-quality-cronbach-alpha",
          "kg-quality-internal-external-validity"]:
    add_r(q,"kg-paradigm-positivism","INFLUENCED_BY","این معیار از مبانی اثبات‌گرایی (اعتبارسنجی عینی) تأثیر پذیرفته",0.8)
for q in ["kg-quality-credibility","kg-quality-triangulation","kg-quality-thick-description"]:
    add_r(q,"kg-paradigm-interpretivism","INFLUENCED_BY","این معیار از مبانی تفسیرگرایی (فهم معنایی، بافت) تأثیر پذیرفته",0.8)

# ============ VALIDATION ============
valid_types = {"SCHOOL","TRADITION","PARADIGM","APPROACH","THEORY","MODEL","FRAMEWORK",
               "HYPOTHESIS","LAW","CONCEPT","METHODOLOGY","METHOD","DESIGN","STRATEGY",
               "TECHNIQUE","INSTRUMENT","SAMPLING","ANALYSIS","QUALITY","ETHICS","SOFTWARE",
               "DISCIPLINE","SUBFIELD"}
valid_rels = {"IS_A","PART_OF","BELONGS_TO","INFLUENCED_BY","INFLUENCED","CRITICIZES","EXTENDS",
              "CONTRADICTS","RELATED_TO","APPLIES_TO","USES","MEASURES","ANALYZES","COLLECTS",
              "DEVELOPED_BY","PROPOSED_BY","OPERATIONALIZES","TESTS","DERIVED_FROM","COMPARED_WITH"}

ids = {e["id"] for e in ents}
bad_type = [e["id"] for e in ents if e["entity_type"] not in valid_types]
bad_rel = [r for r in rels if r["relation_type"] not in valid_rels]
# External targets allowed (from other blocks)
external_targets = {
    "kg-approach-quantitative","kg-approach-qualitative","kg-approach-mixed-methods",
    "kg-technique-questionnaire","kg-technique-online-survey","kg-technique-delfi",
    "kg-technique-structured-interview","kg-technique-semistructured-interview",
    "kg-technique-in-depth-interview","kg-technique-group-interview","kg-technique-focus-group",
    "kg-framework-qual-thematic-analysis","kg-framework-qual-content-analysis",
    "kg-framework-qual-discourse-analysis","kg-framework-qual-narrative-analysis",
    "kg-framework-qual-semiotic-analysis","kg-analysis-qual-discourse-critical",
    "kg-analysis-t-test","kg-analysis-anova","kg-analysis-linear-regression",
    "kg-analysis-chi-square","kg-analysis-factor-analysis","kg-analysis-causal-inference",
    "kg-framework-structural-modeling","kg-analysis-sem",
    "kg-technique-social-media-data","kg-technique-text-analysis","kg-technique-web-scraping",
    "kg-technique-api-extraction","kg-technique-media-content-analysis",
    "kg-technique-digital-ethnography","kg-technique-digital-footprint-analysis",
    "kg-technique-official-document-analysis","kg-technique-video-analysis",
    "kg-technique-participant-observation","kg-technique-document-review",
    "kg-theory-framing","kg-theory-agenda-setting","kg-theory-uses-and-gratifications",
    "kg-theory-spiral-silence","kg-theory-encoding-decoding","kg-theory-dependence",
    "kg-theory-networked-communication","kg-theory-algorithmic-agency",
    "kg-theory-attention-economy","kg-theory-communication-management",
    "kg-subfield-media-effects","kg-subfield-audience-reception","kg-subfield-political",
    "kg-subfield-digital-media","kg-paradigm-positivism","kg-paradigm-interpretivism",
}
missing_target = [r for r in rels
                  if r["target_id"] not in ids and r["target_id"] not in external_targets]
missing_source = [r for r in rels if r["source_id"] not in ids]
dup = [i for i in ids if sum(1 for e in ents if e["id"]==i) > 1]

print(f"Entities: {len(ents)}")
print(f"Relations: {len(rels)}")
print(f"Bad entity types: {bad_type}")
print(f"Bad relation types: {len(bad_rel)}")
for r in bad_rel:
    print("  BAD REL:", r["source_id"], r["relation_type"], r["target_id"])
print(f"Missing target ids (not in block and not known external): {len(missing_target)}")
for r in missing_target:
    print("  MISSING TARGET:", r["target_id"])
print(f"Missing source ids: {len(missing_source)}")
for r in missing_source:
    print("  MISSING SOURCE:", r["source_id"])
print(f"Duplicate ids: {dup}")
print("Entity type breakdown:", dict(Counter(e["entity_type"] for e in ents)))
print("Relation type breakdown:", dict(Counter(r["relation_type"] for r in rels)))

out = {
    "blockId": "quality-ethics-tools",
    "generated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "source_document": "pasted-text-20261110-062125-ec35e598.txt",
    "source_sections": [10, 11, 12, 14],
    "entities": ents,
    "relations": rels,
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with io.open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("Saved to:", OUT)
print("File size:", os.path.getsize(OUT), "bytes")
