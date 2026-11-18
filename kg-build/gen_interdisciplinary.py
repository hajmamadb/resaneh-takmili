# -*- coding: utf-8 -*-
"""Generator for kg_data_interdisciplinary.json (block: interdisciplinary).
Source: pasted-text-20261110-062125-ec35e598.txt lines 110-153 (sections 2 & 3).
"""
import json, sys

def E(id, fa, en, slug, etype, parent, abstract, description,
      hist=None, philo=None, props=None, figs=None, period=None, geo=None,
      rel=None, apps=None, strengths=None, limits=None, crits=None,
      refs=None, facets=None):
    return {
        "id": id, "title_fa": fa, "title_en": en, "slug": slug,
        "entity_type": etype, "parent_id": parent,
        "abstract": abstract, "description": description,
        "historical_background": hist, "philosophical_foundations": philo,
        "key_propositions": props, "key_figures": figs,
        "origin_period": period, "geographical_origin": geo,
        "related_disciplines": rel, "applications": apps,
        "strengths": strengths, "limitations": limits, "criticisms": crits,
        "references": refs, "status": "draft",
        "facets": facets or [{"key": "domain", "value": "communication"},
                              {"key": "approach", "value": "interdisciplinary"}],
    }

def R(src, tgt, rtype, desc, conf):
    return {"source_id": src, "target_id": tgt, "relation_type": rtype,
            "description": desc, "confidence": conf,
            "verification_status": "unverified"}

ents = []

# ================= SECTION 2: 13 interdisciplinary traditions ============
FAC = [{"key": "domain", "value": "communication"},
       {"key": "approach", "value": "interdisciplinary"},
       {"key": "theoretical_tradition", "value": "%s"}]

# 1. Marxism
ents.append(E(
    "kg-tradition-marxism", "مارکسیسم و نئومارکسیسم", "Marxism and Neo-Marxism",
    "marxism", "TRADITION", None,
    "خاندان فکری مبتنی بر نقد مادی‌تاریخی سرمایه‌داری که رسانه را زیرساخت ایدئولوژیک و ابزار تداوم روابط سلطه‌ای طبقاتی می‌بیند.",
    "مارکسیسم در تحلیل رسانه بر «عقلانی‌سازی سرمایه‌داری» (فریدمان/مارشال) و «کاراکترولوژی» (لوکاچ) تکیه دارد. نئومارکسیسم‌های آلتوسری (ایدئولوژی و دستگاه‌های ایدئولوژیک دولتی)، گرامشی‌ای (هژمونی و جبهه‌های مدنی) و مارکوزه‌ای (فرهنگ توده) رسانه را نه عین، بلکه بخشی از ایدئولوژی و کنترل اجتماعی تحلیل می‌کنند.",
    hist="ریشه‌ها: مارکس (1840s)، لنین (1900s)؛ بازخوانی‌های نئومارکسیستی 1960-80.",
    philo="مادی‌تاریخ، نظریه ایدئولوژی، نظریه ارزش اضافی و فراساختار.",
    props=["رسانه بازتولیدکننده روابط قدرت طبقاتی است",
           "ایدئولوژی از طریق بازنمایی‌های «طبیعی» تداوم می‌یابد",
           "فرهنگ و رسانه بخشی از فراساختار هستند"],
    figs=["کارل مارکس", "انتونین گرامشی", "لوئی آلتوسر", "فالتر هآرتمان", "نوربرت کرم"],
    period="1845-1980", geo="آلمان/روسیه/ایتالیا",
    rel=["اقتصاد سیاسی", "جامعه‌شناسی", "فلسفه"],
    apps=["اقتصاد سیاسی رسانه", "تحلیل ایدئولوژی رسانه", "نقد مالکیت رسانه‌ای"],
    strengths=["نقد ساختاری و کلانِ رسانه", "تطبیق با اقتصاد سیاسی"],
    limits=["تعیین‌گری ایدئولوژیک", "بازدارندگی از مطالعه عمل مخاطب"],
    crits=["کلی‌گرایی طبقاتی", "نادیده‌گرفتن آژانس مخاطب و پراکندگی معنا"],
    refs=["Marx & Engels (1845), German Ideology", "Gramsci (1971), Selections from the Prison Notebooks", "Althusser (1970), Ideology and Ideological State Apparatuses"],
    facets=FAC + [{"key": "approach", "value": "critical"}] if False else FAC))
ents[-1]["facets"] = FAC[:2] + [{"key": "theoretical_tradition", "value": "marxism"}, {"key": "approach", "value": "critical"}]

# sub: classic marxism
ents.append(E(
    "kg-approach-classical-marxism", "مارکسیسم کلاسیک", "Classical Marxism",
    "classical-marxism", "APPROACH", "kg-tradition-marxism",
    "رویکرد مبنا-فراساختاری (base-superstructure) که در آن رسانه، صنعت چاپ و نشر، زیرساخت اقتصادی را بازتاب می‌دهد.",
    "در این رویکرد رسانه عین اقتصاد است؛ مالکیت رسانه‌ای همان مالکیت ابزار تولید است و پیام‌رسانی شکل نرم‌تر تبلیغات طبقاتی تلقی می‌شود.",
    philo="مادی‌تاریخ و بنیان‌گرایی (base-superstructure).",
    props=["اقتصاد بنیاد، فرهنگ فراساختار است", "مالکیت رسانه = مالکیت ابزار تولید"],
    figs=["کارل مارکس", "فلاديمیر لنین"], period="1845-1924",
    refs=["Marx (1859), A Contribution to the Critique of Political Economy"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "critical"}, {"key": "theoretical_tradition", "value": "marxism"}]))
ents.append(E(
    "kg-approach-gramscian", "گرامشی", "Gramscianism",
    "gramscian", "APPROACH", "kg-tradition-marxism",
    "جریان نئومارکسیستی مبتنی بر نظریه هژمونی آنتونین گرامشی که سلطه را فرآیند کسب اجماع فرهنگی می‌داند.",
    "گرامشی هژمونی را فرآیندی پویا می‌داند که در آن حاکمان برای تداوم قدرت، علاوه بر زور، اجماع فرهنگی می‌سازند. در رسانه، بازنمایی‌ها مکانیزم اصلی تولید هژمونی و «جنگ موقعیت‌ها» (war of positions) است.",
    philo="مارکسیسم اصلاح‌شده با ویتورین و هگل.",
    props=["سلطه از طریق اجماع و هژمونی معناست", "بازنمایی رسانه‌ای میدان نبرد هژمونی است"],
    figs=["انتونین گرامشی"], period="1916-1935",
    rel=["فلسفه", "تاریخ", "آموزش"],
    apps=["تحلیل گفتمان هژمونیک", "مطالعات بازنمایی"],
    refs=["Gramsci (1971), Prison Notebooks"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "critical"}, {"key": "theoretical_tradition", "value": "marxism"}]))
ents.append(E(
    "kg-approach-althusser", "آلتوسر", "Althusserianism",
    "althusser", "APPROACH", "kg-tradition-marxism",
    "رویکرد ساختارگرای نئومارکسیستی مبتنی بر «دستگاه‌های ایدئولوژیک دولتی» (ISA) لوئی آلتوسر.",
    "آلتوسر دستگاه‌های ایدئولوژیک دولتی (آموزش، رسانه، دین، خانواده) را بازتولیدکننده نیروی کار در نظام سرمایه‌داری می‌داند. رسانه در این دیدگاه یکی از دستگاه‌های کلیدی ISA است که سوژه‌ها را از طریق فراخوانش (interpellation) می‌سازد.",
    philo="مارکسیسم ساختارگرای فرانسه.",
    props=["رسانه یکی از دستگاه‌های ایدئولوژیک دولتی است", "سوژه‌سازی از طریق فراخوانش ایدئولوژیک"],
    figs=["لوئی آلتوسر"], period="1960-1980",
    refs=["Althusser (1970), Ideology and Ideological State Apparatuses"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "critical"}, {"key": "theoretical_tradition", "value": "marxism"}]))

# 2. Functionalism
ents.append(E(
    "kg-tradition-functionalism", "کارکردگرایی", "Functionalism",
    "functionalism", "TRADITION", None,
    "خاندان فکری اجتماعی-فلسفی که پدیده‌های اجتماعی و رسانه را از منظر نقش و کارکردشان در حفظ تعادل اجتماعی تفسیر می‌کند.",
    "کارکردگرایی (Comte, Spencer, Durkheim, Parsons) جامعه را سیستمی از بخش‌های متقابل-وابسته می‌داند که هر بخش کارکردی برای بقای کل دارد. در رسانه، «کارکردهای اطلاعاتی، هماهنگ‌سازی‌کننده، تفریحی و بازتولید هنجار» (Lasswell, Lasswell & Lasswell) کارکردهای اصلی رسانه برای نظم اجتماعی هستند.",
    hist="1830s-1950s.",
    philo="جامعه‌محوری، نظم‌گرایی، ساختارگرایی.",
    props=["رسانه برای حفظ تعادل اجتماعی کارکرد دارد", "هر نهاد اجتماعی کارکرد مشخصی دارد"],
    figs="".join(["اوجست کونت", "هربرت اسپنسر", "امیل دورکیم", "تالت پارسونز", "هارولد لاسول"]),
    period="1830-1960", geo="فرانسه/بریتانیا/آمریکا",
    rel=["جامعه‌شناسی", "فلسفه", "روان‌شناسی اجتماعی"],
    apps=["تحلیل نقش رسانه در نظم اجتماعی", "مدل‌سازی کارکردهای رسانه"],
    strengths=["مدل‌سازی منظم پدیده‌های رسانه‌ای"],
    limits=["حفظ‌وضع‌گرایی", "نادیده‌گرفتن تضادها و تغییرات"],
    crits=["کارکردگرایی رسانه را ابزار حفظ سلطه می‌بیند", "تغییرات ساختاری را توضیح نمی‌دهد"],
    refs=["Durkheim (1897), Suicide", "Parsons (1951), The Social System", "Lasswell (1948), The Structure and Function of Communication"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "functionalism"}]))

ents.append(E(
    "kg-approach-structural-functionalism", "کارکردگرایی ساختاری", "Structural Functionalism",
    "structural-functionalism", "APPROACH", "kg-tradition-functionalism",
    "جریان نئوکارکردگرای تالت پارسونز که جامعه را به‌عنوان سیستمی از الگوهای هنجاری تحلیل می‌کند.",
    "پارسونز چهار کارکرد AGIL (همگرایی، هدف‌یابی، یکپارچگی، حفظ الگو) را برای هر جامعه تعریف می‌کند. رسانه در این دیدگاه در خدمت کارکردهای همگرایی و یکپارچگی اجتماعی است.",
    philo="نظام‌گرایی و ساختارگرایی اجتماعی.",
    props=["جامعه سیستمی از الگوهای هنجاری است", "رسانه کارکرد همگرایی اجتماعی دارد"],
    figs=["تالت پارسونز", "رابرت مerton"], period="1940-1970",
    refs=["Parsons (1951), The Social System", "Merton (1948), The Functional Perspective in Sociology"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "structural"}, {"key": "theoretical_tradition", "value": "functionalism"}]))
ents.append(E(
    "kg-approach-media-functionalist", "کارکردگرایی رسانه", "Media Functionalism",
    "media-functionalism", "APPROACH", "kg-tradition-functionalism",
    "بازخوانی کارکردگرایانه رسانه از منظر نقش‌های اطلاعاتی، هماهنگ‌سازی و تفریحی رسانه در حفظ نظم اجتماعی.",
    "در این رویکرد رسانه نه بازتولیدکننده سلطه، بلکه نهادی هماهنگ‌ساز است که سه کارکرد «اطلاع‌رسانی، هماهنگ‌سازی اجتماعی و تفریح» (Lasswell) را ایفا می‌کند.",
    philo="کارکردگرایی اجتماعی و ارتباطات.",
    props=["رسانه نهاد هماهنگ‌ساز اجتماعی است", "کارکردهای اصلی: اطلاع‌رسانی، هماهنگ‌سازی، تفریح"],
    figs=["هارولد لاسول"], period="1940-1970",
    refs=["Lasswell (1948), The Structure and Function of Communication in Society"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "functional"}, {"key": "theoretical_tradition", "value": "functionalism"}]))

# 3. Interactionism
ents.append(E(
    "kg-tradition-interactionism", "کنش متقابل‌گرایی", "Interactionism",
    "interactionism", "TRADITION", None,
    "خاندان فکری خاسته از جامعه‌شناسی شیکاگو که تعاملات خردروان‌شناختی و نمادین را نقطه شروع فهم جامعه می‌داند.",
    "کنش متقابل‌گرایی (Mead, Blumer, Blumer, Goffman) بر «تعامل‌گرایی نمادین» استوار است: معنا از طریق تعاملات نمادین (زبان، بدن، اشیاء) ساخته می‌شود. در رسانه، تعاملات روزمره مخاطب با رسانه (بازتولید، تفسیر، بازنمایی خودی) در مرکز تحلیل قرار می‌گیرد.",
    hist="مکتب شیکاگو 1920-1950.",
    philo="پراگماتیسم، پدیدارشناسی، جامعه‌شناسی تعاملی.",
    props=["معنا از طریق تعامل نمادین ساخته می‌شود", "خود (self) محصول تعامل اجتماعی است"],
    figs=["جورج هردیل میاد", "هربرت بلومر", "اروین گافمن"],
    period="1920-1970", geo="آمریکا (شیکاگو)",
    rel=["جامعه‌شناسی", "روان‌شناسی", "لسانیات"],
    apps=["تحلیل تعاملات روزمره رسانه", "مطالعات بازنمایی و هویت"],
    strengths=["توجه به خرد و عمل روزمره"],
    limits=["کلی‌سازی دشوار", "ضعف در تحلیل کلان"],
    crits=["کارکردگرایی کلان را نادیده می‌گیرد"],
    refs=["Mead (1934), Mind, Self and Society", "Blumer (1969), Symbolic Interactionism", "Goffman (1959), The Presentation of Self in Everyday Life"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "interactionism"}, {"key": "approach", "value": "interpretive"}]))

ents.append(E(
    "kg-approach-symbolic-interactionism", "تعامل‌گرایی نمادین", "Symbolic Interactionism",
    "symbolic-interactionism", "APPROACH", "kg-tradition-interactionism",
    "رویکرد جامعه‌شناختی-ارتباطی که بر نقش نمادها (زبان، علامت، رفتار) در ساخت معنا و خود تمرکز دارد.",
    "در تعامل‌گرایی نمادین، انسان‌ها بر اساس معنایی که چیزها برایشان دارند عمل می‌کنند؛ معنای چیزها از تعاملات اجتماعی برمی‌آید و از طریق تفسیر فرآیندی اصلاح می‌شود. رسانه و رسانه‌های دیجیتال، میدان اصلی این تعاملات نمادین امروز هستند.",
    philo="پراگماتیسم میادی و پدیدارشناسی هوزرل.",
    props=["معنا از تعاملات نمادین می‌آید", "خود محصول تعامل با دیگران است"],
    figs=["هربرت بلومر", "جورج میاد"], period="1930-1970",
    refs=["Blumer (1969), Symbolic Interactionism: Perspective and Method"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "interpretive"}, {"key": "theoretical_tradition", "value": "interactionism"}]))
ents.append(E(
    "kg-approach-social-interactionism", "کنش متقابل اجتماعی", "Social Interactionism",
    "social-interactionism", "APPROACH", "kg-tradition-interactionism",
    "رویکردی گسترده‌تر از نمادین که تعاملات را در بافت اجتماعی-مادی (نه صرفا نمادین) تحلیل می‌کند.",
    "کنش متقابل اجتماعی (Goffman, Erving Goffman, Mead, Simmel) به بافت‌های اجتماعی (غرفه‌ی نمایش، گروه، جمعیت) و الگوهای تکرارشونده تعامل توجه دارد. در رسانه، تعاملات اجتماعی در فضای دیجیتال (تعامل، پاسخ، به‌ اشتراک‌گذاری) نمونه‌های معاصر این رویکردند.",
    philo="جامعه‌شناسی خرد.",
    props=["تعامل در بافت اجتماعی-مادی رخ می‌دهد", "غرفه‌ی نمایش (front stage / back stage) الگوی کلیدی است"],
    figs=["اروین گافمن", "گئورگ زیمل"], period="1950-1980",
    refs=["Goffman (1959), The Presentation of Self in Everyday Life", "Simmel (1908), The Philosophy of Money"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "interpretive"}, {"key": "theoretical_tradition", "value": "interactionism"}]))

# 4. Phenomenology
ents.append(E(
    "kg-tradition-phenomenology", "پدیدارشناسی", "Phenomenology",
    "phenomenology", "TRADITION", None,
    "خاندان فکری فلسفی-اجتماعی که «پدیدارها را همان‌طور که ظاهر می‌شوند» بررسی می‌کند و تجربه زیسته را منبع اصلی معرفت می‌داند.",
    "پدیدارشناسی (Husserl, Heidegger, Schutz, Merleau-Ponty) از «پارانتز» (epoché) و «طرح‌به‌پشت‌گذاشتن پیش‌فرض‌ها» برای بازگشت به چیزهای خود آغاز می‌شود. در علوم اجتماعی (شوتز) تجربه زیسته، «جهان اجتماعی» و «فهم متقابل» (intersubjectivity) مبانی تحلیل رسانه به‌عنوان بخشی از جهان زیسته مخاطب می‌شوند.",
    hist="اوایل قرن بیستم، اتریش و آلمان.",
    philo="پدیدارشناسی توصیفی و انتزاعی‌سازی.",
    props=["تجربه زیسته منبع معرفت است", "پیش‌فرض‌ها باید به پس‌پا گذاشته شوند (epoché)"],
    figs=["ادموند هوزرل", "مارتین هایدگر", "البرت شوتز", "موریس مرلو-پونتی"],
    period="1900-1960", geo="اتریش/آلمان/فرانسه",
    rel=["فلسفه", "جامعه‌شناسی", "روان‌شناسی"],
    apps=["تحلیل تجربه زیسته رسانه", "پدیدارشناسی رسانه"],
    strengths=["توجه به تجربه زیسته و معنا"],
    limits=["تعمیم دشوار", "ذات‌گرایی"],
    crits=["ضعف در تبیین ساختارهای کلان"],
    refs=["Husserl (1913), Ideas I", "Heidegger (1927), Being and Time", "Schutz (1932), The Phenomenology of the Social World", "Merleau-Ponty (1945), Phenomenology of Perception"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "phenomenology"}]))

ents.append(E(
    "kg-approach-social-phenomenology", "پدیدارشناسی اجتماعی", "Social Phenomenology",
    "social-phenomenology", "APPROACH", "kg-tradition-phenomenology",
    "بازخوانی شوتز از پدیدارشناسی برای تحلیل جهان اجتماعی و فهم متقابل کنشگران.",
    "شوتز پدیدارشناسی را با جامعه‌شناسی ترکیب می‌کند: «جهان اجتماعی» از فهم متقابل کنشگران ساخته می‌شود و رسانه، یکی از ابزارهای اصلی ساخت این جهان است.",
    philo="پدیدارشناسی و جامعه‌شناسی.",
    props=["جهان اجتماعی محصول فهم متقابل است", "رسانه بخشی از جهان زیسته است"],
    figs=["البرت شوتز", "آلفرد شوتز"], period="1930-1959",
    refs=["Schutz (1932), The Phenomenology of the Social World"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "interpretive"}, {"key": "theoretical_tradition", "value": "phenomenology"}]))
ents.append(E(
    "kg-approach-hermeneutic-phenomenology", "پدیدارشناسی هرمنوتیکی", "Hermeneutic Phenomenology",
    "hermeneutic-phenomenology", "APPROACH", "kg-tradition-phenomenology",
    "ترکیب پدیدارشناسی و هرمنوتیک در «دایره هرمنوتیکی» گادامر برای فهم معنادار پدیده‌های رسانه‌ای.",
    "این رویکرد تجربه زیسته و تفسیر معنا را با هم می‌آمیزد؛ در رسانه، معنای پیام از «افق» مخاطب و «ترکیب افق‌ها» (gadamer) ساخته می‌شود.",
    philo="پدیدارشناسی هوزرل و هرمنوتیک گادامر.",
    props=["فهم در «دایره هرمنوتیکی» رخ می‌دهد", "معنا محصول ترکیب افق‌هاست"],
    figs=["هانس-گئورگ گادامر", "پاول ریکور"], period="1960-1980",
    refs=["Gadamer (1960), Truth and Method"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "interpretive"}, {"key": "theoretical_tradition", "value": "phenomenology"}]))

# 5. Hermeneutics
ents.append(E(
    "kg-tradition-hermeneutics", "هرمنوتیک", "Hermeneutics",
    "hermeneutics", "TRADITION", None,
    "خاندان فکری فلسفی-تفسیری که تفسیر (بازگویی) متون و پدیده‌های معنادار را در مرکز قرار می‌دهد.",
    "هرمنوتیک (Schleiermacher, Dilthey, Heidegger, Gadamer, Ricœur) از «هنر تفسیر» به «علم تفسیر» و سپس به «مبنای فهم انسان» تحول یافت. در رسانه، هرمنوتیک ابزار فهم تفسیری معنای متون رسانه‌ای (متن، تصویر، ویدئو) در بافت تاریخی-فرهنگی مخاطب است.",
    hist="اواسط قرن نوزدهم، آلمان.",
    philo="فلسفه تفسیر و فهم.",
    props=["فهم تفسیری است و از پیش‌فهم آغاز می‌شود", "معنا در دایره هرمنوتیکی ساخته می‌شود"],
    figs=["فرد شلایرمخر", "وایلhem دیلتای", "مارتین هایدگر", "هانس-گئورگ گادامر", "پاول ریکور"],
    period="1813-1990", geo="آلمان",
    rel=["فلسفه", "لسانیات", "ادبیات"],
    apps=["تحلیل تفسیری متن رسانه‌ای", "تحلیل روایت رسانه‌ای"],
    strengths=["عمق تفسیری", "توجه به بافت تاریخی-فرهنگی"],
    limits=["تعمیم دشوار", "ذات‌گرایی تفسیر"],
    crits=["اعتبارسنجی تفسیر دشوار است"],
    refs=["Schleiermacher (1813), Hermeneutics", "Dilthey (1883), Introduction to the Human Sciences", "Heidegger (1927), Being and Time", "Gadamer (1960), Truth and Method"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "hermeneutics"}]))

ents.append(E(
    "kg-approach-philosophical-hermeneutics", "هرمنوتیک فلسفی", "Philosophical Hermeneutics",
    "philosophical-hermeneutics", "APPROACH", "kg-tradition-hermeneutics",
    "هرمنوتیک هایدگری و گادامری که فهم را «وجودشناختی» و نه صرفا روشی می‌داند.",
    "در هرمنوتیک فلسفی، فهم «دایره هرمنوتیکی» است: پیش‌فهم، تفسیر و بازفهم. در رسانه، فهم پیام همیشه از پیش‌فهم مخاطب آغاز می‌شود.",
    philo="هستی‌شناسی هایدگر و دایره هرمنوتیکی گادامر.",
    props=["فهم در دایره هرمنوتیکی رخ می‌دهد", "پیش‌فهم پیش‌شرط فهم است"],
    figs=["مارتین هایدگر", "هانس-گئورگ گادامر"], period="1927-1960",
    refs=["Gadamer (1960), Truth and Method"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "interpretive"}, {"key": "theoretical_tradition", "value": "hermeneutics"}]))
ents.append(E(
    "kg-approach-critical-hermeneutics", "هرمنوتیک انتقادی", "Critical Hermeneutics",
    "critical-hermeneutics", "APPROACH", "kg-tradition-hermeneutics",
    "هرمنوتیک انتقادی پاول ریکور و یورگن هابرماس که تفسیر را با نقد ایدئولوژیک ترکیب می‌کند.",
    "در هرمنوتیک انتقادی، تفسیر فقط فهم نیست بلکه «آزادسازی از ایدئولوژی» است. رسانه در این دیدگاه هم میدان فهم است و هم میدان ایدئولوژی که باید نقد شود.",
    philo="هرمنوتیک و نظریه انتقادی فراکفورت.",
    props=["تفسیر فرآیند آزادسازی از ایدئولوژی است", "رسانه میدان فهم و ایدئولوژی است"],
    figs=["پاول ریکور", "یورگن هابرماس"], period="1970-1990",
    refs=["Ricoeur (1970), Freud and Philosophy", "Habermas (1968), Legitimation Crisis"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "critical"}, {"key": "theoretical_tradition", "value": "hermeneutics"}]))

# 6. Pragmatism
ents.append(E(
    "kg-tradition-pragmatism", "پراگماتیسم", "Pragmatism",
    "pragmatism", "TRADITION", None,
    "خاندان فکری آمریکایی که معنای مفاهیم را از پیامدهای عملی آن‌ها می‌سنجد و «عمل» را معیار معرفت می‌داند.",
    "پراگماتیسم (Peirce, James, Dewey) بر «عمل‌گرایی»، «ابزارگرایی» و «حل مسئله» استوار است. در رسانه، پراگماتیسم رویکردی کاربردی به تحلیل پیام‌رسانی (نقش عملی پیام در تغییر رفتار) و پژوهش‌محور (پژوهش کاربردی، حل مسئله) است.",
    hist="اواخر قرن نوزدهم، آمریکا.",
    philo="عمل‌گرایی و ابزارگرایی.",
    props=["معنا از پیامدهای عملی است", "علم ابزاری برای حل مسئله است"],
    figs=["چارلز ساندرس پیرس", "ویلیام جیمز", "جان دیویی"],
    period="1870-1940", geo="آمریکا",
    rel=["فلسفه", "آموزش", "روان‌شناسی"],
    apps=["تحلیل عملی پیام رسانه‌ای", "پژوهش کاربردی رسانه"],
    strengths=["کاربردی‌بودن", "مرونة در روش‌شناسی"],
    limits=["ضعف در تبیین کلان"],
    crits=["نسبی‌سازی ارزش‌ها", "عمل‌گرایی افراطی"],
    refs=["Peirce (1878), The Illustration of Logic", "James (1907), Pragmatism", "Dewey (1938), Logic: The Theory of Inquiry"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "pragmatism"}]))

ents.append(E(
    "kg-approach-classical-pragmatism", "پراگماتیسم کلاسیک", "Classical Pragmatism",
    "classical-pragmatism", "APPROACH", "kg-tradition-pragmatism",
    "پراگماتیسم کلاسیک پیرس، جیمز و دیویی بر اساس ابزارگرایی و عمل‌گرایی.",
    "پیرس معنای مفاهیم را «کلیه پیامدهای عملی ممکن» می‌داند؛ جیمز «عمل‌گرایی در تئوری» و دیویی «حل مسئله» و «آموزش‌محوری» را مطرح می‌کند.",
    philo="ابزارگرایی و عمل‌گرایی.",
    props=["معنا = پیامدهای عملی ممکن", "علم ابزار حل مسئله است"],
    figs=["چارلز ساندرس پیرس", "ویلیام جیمز", "جان دیویی"], period="1870-1940",
    refs=["James (1907), Pragmatism", "Dewey (1925), Experience and Nature"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "pragmatic"}, {"key": "theoretical_tradition", "value": "pragmatism"}]))
ents.append(E(
    "kg-approach-social-pragmatism", "پراگماتیسم اجتماعی", "Social Pragmatism",
    "social-pragmatism", "APPROACH", "kg-tradition-pragmatism",
    "بازخوانی اجتماعی پراگماتیسم که به پیامدهای اجتماعی-فرهنگی عمل و رسانه توجه دارد.",
    "پراگماتیسم اجتماعی (دوی، میاد، مین) عمل‌گرایی را در بافت اجتماعی‌تر می‌کشد: تعاملات اجتماعی، هویت و رسانه در «بازاندازی جهان» (world-building) نقش دارند.",
    philo="پراگماتیسم و تعامل‌گرایی نمادین.",
    props=["عمل در بافت اجتماعی معنا می‌یابد", "رسانه بخشی از بازاندازی جهان است"],
    figs=["جان دیویی", "جورج میاد", "جورج هربرت مین"], period="1930-1970",
    refs=["Dewey (1927), The Public and Its Problems", "Mead (1934), Mind, Self and Society"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "interpretive"}, {"key": "theoretical_tradition", "value": "pragmatism"}]))

# 7. Systems Theory
ents.append(E(
    "kg-tradition-systems-theory", "نظریه سیستم‌ها", "Systems Theory",
    "systems-theory", "TRADITION", None,
    "خاندان فکری بین‌رشته‌ای که پدیده‌ها را به‌عنوان سیستم‌هایی از اجزای متقابل‌وابسته و بازخوردی تحلیل می‌کند.",
    "نظریه سیستم‌ها (Bertalanffy, Shannon, Wiener, Luhmann, Bateson) در علوم ارتباطات از دو مسیر ورود کرد: (1) سیبرنتیک و تئوری اطلاعات (Shannon & Weaver 1949) و (2) نظام‌های اجتماعی (Luhmann, Merton, Parsons). در رسانه، تحلیل «سیستم ارتباطی» (فرستنده، پیام، رسانه، گیرنده، نویز، بازخورد) و «سیستم‌های خودرؤیت‌بخش» (autopoietic) از مبانی این خاندان است.",
    hist="اواسط قرن بیستم.",
    philo="سیبرنتیک و نظام‌گرایی.",
    props=["پدیده‌ها سیستم‌هایی از اجزای وابسته و بازخوردی‌اند", "معنا از رابطه اجزا و نه خود اجزا برمی‌آید"],
    figs=["لوتف ویبر", "نوربرت واینر", "کارل وایرر", "کلود شانون", "نیکلاس لومان"],
    period="1940-1990", geo="آمریکا/آلمان",
    rel=["ریاضی", "فیزیک", "جامعه‌شناسی", "بیولوژی"],
    apps=["تحلیل سیستم‌های ارتباطی", "مدل‌سازی شبکه‌های رسانه‌ای"],
    strengths=["مدل‌سازی منظم و ساختاری"],
    limits=["پیچیدگی و کاهش‌پدیدی"],
    crits=["کلی‌گرایی و فراموش‌شدن آژانس"],
    refs=["Bertalanffy (1968), General System Theory", "Shannon & Weaver (1949), The Mathematical Theory of Communication", "Luhmann (1984), Social Systems"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "systems-theory"}]))

ents.append(E(
    "kg-approach-general-systems", "سیستم‌های عمومی", "General Systems Theory",
    "general-systems", "APPROACH", "kg-tradition-systems-theory",
    "نظریه سیستم‌های عمومی لودویگ برتالنفی که الگوی منظمی برای تحلیل هر سیستمی ارائه می‌دهد.",
    "برتالنفی سیستم را مجموعه‌ای از اجزای وابسته در محیطی خاص می‌داند؛ ورودی‌ها، فرایندهای داخلی و خروجی‌ها در چارچوب بازخورد عمل می‌کنند.",
    philo="نظام‌گرایی.",
    props=["هر سیستم مجموعه‌ای از اجزای وابسته در محیطی است", "بازخورد اصل کلیدی تنظیم است"],
    figs=["لودویگ برتالنفی"], period="1940-1970",
    refs=["Bertalanffy (1968), General System Theory"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "structural"}, {"key": "theoretical_tradition", "value": "systems-theory"}]))
ents.append(E(
    "kg-approach-complex-systems", "سیستم‌های پیچیده", "Complex Systems",
    "complex-systems", "APPROACH", "kg-tradition-systems-theory",
    "رویکرد به تحلیل سیستم‌های پیچیده با ویژگی‌های ناهمگن، غیرخطی و نوسانی.",
    "سیستم‌های پیچیده ویژگی‌هایی مانند «نوسانات» (emergence)، «نقطه عطف» (tipping points) و «عدم قطعیت» دارند؛ در رسانه، انتشار اطلاعات، شکل‌گیری شایعه و الگوریتم‌های شبکه‌های اجتماعی نمونه‌های بارز این سیستم‌هاست.",
    philo="نظام‌های پیچیده و ریاضیات.",
    props=["سیستم‌های پیچیده دارای ویژگی‌های ناهمگن و غیرخطی‌اند", "نوسانات ویژگی کلیدی است"],
    figs=["استیو کاسا", "دونالد نورمان"], period="1990-2020",
    refs=["Santa Fe Institute publications", "Holland (1998), Emergence"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "computational"}, {"key": "theoretical_tradition", "value": "systems-theory"}]))
ents.append(E(
    "kg-approach-communication-systems", "نظریه ارتباطی سیستم‌ها", "Communication Systems Theory",
    "communication-systems", "APPROACH", "kg-trادition-systems-theory" if False else "kg-tradition-systems-theory",
    "بازخوانی شانون-وایبر و گرووی (Grover) از نظریه سیستم‌ها برای تحلیل فرآیندهای ارتباطی.",
    "در این رویکرد ارتباطات خود یک سیستم است: فرستنده، پیام، رسانه، گیرنده، نویز و بازخورد در یک چرخه‌ی منظم عمل می‌کنند. مدل شانون-ویبر (1949) بنیاد این رویکرد است.",
    philo="سیبرنتیک و تئوری اطلاعات.",
    props=["ارتباطات خود یک سیستم است", "بازخورد اصل تنظیم سیستم است"],
    figs=["کلود شانون", "وارن ویبر"], period="1948-1960",
    refs=["Shannon & Weaver (1949), The Mathematical Theory of Communication"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "structural"}, {"key": "theoretical_tradition", "value": "systems-theory"}]))

# 8. Action Theory
ents.append(E(
    "kg-tradition-theory-of-action", "نظریه کنش", "Action Theory",
    "theory-of-action", "TRADITION", None,
    "خاندان فکری فلسفی-جامعه‌شناختی که «کنش» (action) را واحد بنیادین تحلیل اجتماعی می‌داند.",
    "نظریه کنش (Schutz, Habermas, Giddens, Bourdieu) از پرسش «انسان چگونه در جهان عمل می‌کند؟» آغاز می‌شود. در رسانه، کنش مخاطب (انتخاب، تفسیر، بازتولید) نقطه آغاز تحلیل ارتباطات است؛ از کنش عقلانی تا کنش ارتباطی و ساختاری.",
    philo="فلسفه عمل و جامعه‌شناسی.",
    props=["کنش واحد بنیادین تحلیل اجتماعی است", "انسان موجود عمل‌گر است"],
    figs=["یورگن هابرماس", "آنتونی گیدنز", "پییر بوردیو", "البرت شوتز"],
    period="1960-2000", geo="آلمان/بریتانیا/فرانسه",
    rel=["فلسفه", "جامعه‌شناسی", "لسانیات"],
    apps=["تحلیل کنش مخاطب", "فهم فرآیندهای رسانه‌ای"],
    strengths=["تمرکز بر آژانس و عمل"],
    limits=["پیچیدگی مفهوم‌ها"],
    crits=["کلی‌گرایی"],
    refs=["Habermas (1981), Theory of Communicative Action", "Giddens (1984), The Constitution of Society", "Bourdieu (1977), Outline of a Theory of Practice"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "action-theory"}]))

ents.append(E(
    "kg-approach-rational-action", "نظریه کنش عقلانی", "Rational Action Theory",
    "rational-action", "APPROACH", "kg-tradition-theory-of-action",
    "رویکردی به کنش بر اساس انتخاب منطقی بهینه با اهداف مشخص.",
    "در کنش عقلانی (میکس)، کنشگر با هدف مشخصی عمل می‌کند و بهترین گزینه را انتخاب می‌کند. در رسانه، انتخاب رسانه، انتخاب محتوا و الگوریتم‌های پیشنهادی، نمونه‌هایی از کنش عقلانی مخاطب است.",
    philo="نظریه انتخاب و اقتصاد سیاسی.",
    props=["کنشگر با هدف مشخص عمل می‌کند", "انتخاب بهینه نتیجه عقلانی است"],
    figs=["جیمز مک‌کانتی", "رابرت اکتون"], period="1950-2000",
    refs=["Becker (1938), The Process of Socialization"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "rational"}, {"key": "theoretical_tradition", "value": "action-theory"}]))
ents.append(E(
    "kg-approach-communicative-action", "کنش ارتباطی", "Communicative Action",
    "communicative-action", "APPROACH", "kg-tradition-theory-of-action",
    "کنش ارتباطی یورگن هابرماس که توافقی‌گرایی و عقلانیت ارتباطی را در مرکز قرار می‌دهد.",
    "هابرماس کنش را دو نوع می‌داند: کنش استراتژیک (هدف‌محور) و کنش ارتباطی (توافق‌محور). در کنش ارتباطی، کنشگران برای رسیدن به «فهم مشترک» گفتگو می‌کنند. در رسانه، «میدان عمومی» و «گفتگوی عمومی» نمونه‌های بارز کنش ارتباطی است.",
    philo="نظریه عمل ارتباطی هابرماس.",
    props=["کنش ارتباطی برای فهم مشترک است", "میدان عمومی مبنای کنش ارتباطی است"],
    figs=["یورگن هابرماس"], period="1981-2000",
    refs=["Habermas (1981), Theory of Communicative Action"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "communicative"}, {"key": "theoretical_tradition", "value": "action-theory"}]))
ents.append(E(
    "kg-approach-structured-action", "نظریه کنش ساختاری", "Structured Action Theory",
    "structured-action", "APPROACH", "kg-tradition-theory-of-action",
    "رویکرد گیدنز و بوردیو که در آن کنش هم ساختار می‌سازد و هم از ساختار تأثیر می‌پذیرد.",
    "در نظریه کنش ساختاری (structured action)، کنش و ساختار در چرخه‌ای از «دوسریایی» (duality) با هم در می‌آیند: کنش هم تولیدکننده ساختار است و هم محصول آن. در رسانه، الگوریتم‌ها هم کنش مخاطب را شکل می‌دهند و هم از کنش مخاطب ساخته می‌شوند.",
    philo="دوسریایی گیدنز و نظریه میدان بوردیو.",
    props=["کنش و ساختار در چرخه‌ای دوسریایی‌اند", "ساختار هم ابزار کنش و هم نتیجه آن است"],
    figs=["آنتونی گیدنز", "پییر بوردیو"], period="1980-2000",
    refs=["Giddens (1984), The Constitution of Society", "Bourdieu (1977), Outline of a Theory of Practice"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "structural"}, {"key": "theoretical_tradition", "value": "action-theory"}]))

# 9. Feminism
ents.append(E(
    "kg-tradition-feminism", "فمینیسم", "Feminism",
    "feminism", "TRADITION", None,
    "خاندان فکری-سیاسی که نابرابری جنسیتی را در مرکز تحلیل قدرت، ایدئولوژی و رسانه قرار می‌دهد.",
    "فمینیسم (Wollstonecraft, Beauvoir, de Beauvoir, Hooks, hooks) در رسانه چهار جریان اصلی دارد: لیبرال (برابری حقوق)، رادیکال (نقد ساختار سرمایه‌داری-فرپدرنشینی)، سوسیالیستی (پیوند طبقاتی-جنسیتی) و پست‌مدرن (ساخت‌شدگی جنسیت و بازنمایی). هر جریان رویکرد متفاوتی به بازنمایی جنسیت در رسانه دارد.",
    philo="فلسفه فمینیستی و نظریه جنسیت.",
    props=["جنسیت رابطه قدرت است", "بازنمایی رسانه‌ای جنسیت ساخته‌شده است"],
    figs=["ماری الواس", "سیمون دو بوفوار", "بیل هوکس", "دوناللا هاروی"],
    period="1800-2020", geo="بریتانیا/فرانسه/آمریکا",
    rel=["فلسفه", "جامعه‌شناسی", "اقتصاد سیاسی"],
    apps=["تحلیل بازنمایی جنسیت در رسانه", "مطالعات فمینیستی رسانه"],
    strengths=["نقد ساختاری و بین‌رشته‌ای"],
    limits=["تنوع درونی و اختلاف‌نظرهای روش‌شناختی"],
    crits=["اساس‌گرایی جنسیتی", "نادیده‌گرفتن تنوع"],
    refs=["Beauvoir (1949), The Second Sex", "hooks (1981), Ain't I a Woman", "Haraway (1985), A Cyborg Manifesto"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "feminism"}]))

for sub, slug, fa, en, desc, figs, refs, appr in [
    ("liberal", "liberal-feminism", "فمینیسم لیبرال", "Liberal Feminism",
     "رویکرد فمینیستی مبتنی بر برابری حقوقی و قانونی زنان و مردان در همه‌ی عرصه‌ها.",
     ["ماری الواس", "بیتی فرفان"],
     ["Wollstonecraft (1792), A Vindication of the Rights of Woman"],
     "liberal"),
    ("radical", "radical-feminism", "فمینیسم رادیکال", "Radical Feminism",
     "نقد ساختاری فرپدرنشینی (patriarchy) به‌عنوان ریشه‌ی نابرابری جنسیتی.",
     ["کیت میلر", "سوزن فالکوس"],
     ["Daly (1978), Gyn/Ecology"],
     "radical"),
    ("socialist", "socialist-feminism", "فمینیسم سوسیالیستی", "Socialist Feminism",
     "ترکیب فمینیسم و مارکسیسم؛ بررسی هم‌زمان سلطه طبقاتی و جنسیتی.",
     ["مارتینا ویمز", "شیرلی هینز"],
     ["Daly (1978), Feminism and Marxism"],
     "socialist"),
    ("postmodern", "postmodern-feminism", "فمینیسم پست‌مدرن", "Postmodern Feminism",
     "نقد اساس‌گرایی جنسیتی و بازخوانی ساخت‌شدگی جنسیت از منظر پست‌مدرن.",
     ["جودی باتلر", "دوناللا هاروی"],
     ["Butler (1990), Gender Trouble", "Haraway (1985), A Cyborg Manifesto"],
     "postmodern"),
    ("intersectional", "intersectional-feminism", "فمینیسم بین‌بخشی", "Intersectional Feminism",
     "تحلیل هم‌زمان نژاد، طبقه، جنسیت و قدرت به سبک کینبیرا کروپ و کربن کروپ.",
     ["کینبیرا کروپ", "پاملا هاروی"],
     ["Crenshaw (1989), Demarginalizing the Intersection of Race and Sex"],
     "intersectional"),
]:
    ents.append(E(
        "kg-approach-" + slug, fa, en, slug, "APPROACH", "kg-tradition-feminism",
        "رویکرد " + fa[1:] + " در تحلیل بازنمایی و نابرابری جنسیت در رسانه.",
        desc,
        philo="فلسفه فمینیستی.",
        props=["جنسیت رابطه قدرت است", "بازنمایی رسانه‌ای جنسیت ساخته‌شده است"],
        figs=figs, period="1970-2000",
        refs=refs,
        facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": appr},
                {"key": "theoretical_tradition", "value": "feminism"}]))

# 10. Postcolonialism
ents.append(E(
    "kg-tradition-postcolonialism", "پسااستعمارگرایی", "Postcolonialism",
    "postcolonialism", "TRADITION", None,
    "خاندان فکری بین‌رشته‌ای که میراث استعمار را در بازنمایی، ایدئولوژی و رسانه تحلیل می‌کند.",
    "پسااستعمارگرایی (Said, Spivak, Bhabha, Hall, Mignolo) بر سه محور استوار است: (1) نقد «شرق‌شناسی» و بازنمایی استعماری (Said 1978)، (2) نقد «صداهای قابل درک‌پذیر» و حاشیه‌نشینی (Spivak 1988) و (3) «فضای میانی» و آمایگمه (Bhabha 1994). در رسانه، بازنمایی جنوب، جریان‌های رسانه‌ای شمال-جنوب و نظریه امپریالیسم فرهنگی در مرکز تحلیل قرار می‌گیرند.",
    philo="پسااستعمارگرایی و پساساختارگرایی.",
    props=["بازنمایی استعماری در زبان و رسانه بازتولید می‌شود", "مغز و حاشیه ساختارهای قدرت هستند"],
    figs=["ادوارد سعید", "گایاتری اسپویاک", "هوم‌بهاب‌ها", "استیو هال", "انریکه مِگنونلو"],
    period="1970-2020", geo="بریتانیا/آمریکا/جنوب جهانی",
    rel=["ادبیات", "تاریخ", "لسانیات", "مطالعات فرهنگی"],
    apps=["تحلیل بازنمایی جنوب در رسانه", "نقد جریان رسانه‌ای شمال-جنوب"],
    strengths=["بین‌رشته‌ای و بین‌فرهنگی"],
    limits=["کلی‌سازی «جنوب»", "ضعف روش‌شناختی"],
    crits=["اساس‌گرایی هویت"],
    refs=["Said (1978), Orientalism", "Spivak (1988), Can the Subaltern Speak?", "Bhabha (1994), The Location of Culture", "Hall (1992), The West and the Rest"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "postcolonialism"}, {"key": "approach", "value": "critical"}]))

ents.append(E(
    "kg-approach-postcolonial-studies", "مطالعات پسااستعماری", "Postcolonial Studies",
    "postcolonial-studies", "APPROACH", "kg-tradition-postcolonialism",
    "مطالعات پسااستعماری به‌عنوان رشته‌ی مستقل بین‌رشته‌ای (Said, Spivak, Bhabha).",
    "مطالعات پسااستعماری به میراث استعمار در زبان، بازنمایی، هویت و رسانه می‌پردازد. در رسانه، «جریان شمال-جنوب»، «مغز و حاشیه» و «بازنمایی جنوب» موضوعات کلیدی این رشته‌اند.",
    philo="پسااستعمارگرایی.",
    props=["استعمار در بازنمایی رسانه‌ای بازتولید می‌شود", "مغز و حاشیه ساختار قدرت رسانه‌ای است"],
    figs=["ادوارد سعید", "گایاتری اسپویاک", "هوم‌بهاب‌ها"], period="1978-2020",
    refs=["Said (1978), Orientalism"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "critical"}, {"key": "theoretical_tradition", "value": "postcolonialism"}]))
ents.append(E(
    "kg-approach-decolonization", "نظریه استعمارزدایی", "Decolonial Theory",
    "decolonization", "APPROACH", "kg-tradition-postcolonialism",
    "نظریه استعمارزدایی که فراتر از «پسااستعمار» به «پساکلونیالیسم» و «پساستعمار» می‌پردازد.",
    "در نظریه استعمارزدایی (Mignolo, Quijano, Maldonado-Torres)، ساختارهای قدرت استعماری در «متافیزیک کلاسیک» و «زبان و رسانه» بازتولید می‌شوند. رسانه در این دیدگاه ابزار کلیدی «پساکلونیالیسم» است.",
    philo="پساکلونیالیسم و جنوب جهانی.",
    props=["استعمار در زبان و رسانه بازتولید می‌شود", "دانش کلاسیک ابزار سلطه است"],
    figs=["انریکه مِگنونلو", "انخل کویانو", "ماندونالدو تورس"], period="1990-2020",
    refs=["Mignolo (2011), The Darker Side of Western Modernity", "Quijano (2000), Coloniality of Power"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "critical"}, {"key": "theoretical_tradition", "value": "postcolonialism"}]))
ents.append(E(
    "kg-approach-orientalism", "شرق‌شناسی", "Orientalism",
    "orientalism", "APPROACH", "kg-tradition-postcolonialism",
    "نقد ادوارد سعید از بازنمایی استعماری شرق در زبان، رسانه و فرهنگ غرب.",
    "سعید (1978) نشان می‌دهد «شرق» یک ساختار بازنمایی است، نه واقعیت جغرافیایی؛ در رسانه، بازنمایی‌های «شرق‌ی مرموز، خرافاتی و عقب‌مانده» نمونه‌های بارز شرق‌شناسی رسانه‌ای است.",
    philo="پسااستعمارگرایی و ساختارگرایی.",
    props=["«شرق» ساختار بازنمایی است", "رسانه ابزار بازتولید بازنمایی استعماری است"],
    figs=["ادوارد سعید"], period="1978-2000",
    refs=["Said (1978), Orientalism"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "critical"}, {"key": "theoretical_tradition", "value": "postcolonialism"}]))

# 11. Critical Studies
ents.append(E(
    "kg-tradition-critical-studies", "مطالعات انتقادی", "Critical Studies",
    "critical-studies", "TRADITION", None,
    "خاندان فکری بین‌رشته‌ای که قدرت، سلطه، نابرابری و ایدئولوژی را در مرکز تحلیل قرار می‌دهد.",
    "مطالعات انتقادی (Fraser, Freire, Habermas, Giroux, Apple) از نظریه انتقادی فراکفورت و نظریه انتقادی نسل جدید (Bustos) گرفته تا مطالعات نژاد (Critical Race Theory)، جنسیت (Critical Gender Studies) و طبقه (Critical Class Studies) را در بر می‌گیرد. در رسانه، تحلیل انتقادی ایدئولوژی، بازنمایی و مالکیت رسانه محور اصلی است.",
    philo="نظریه انتقادی و فلسفه سیاسی.",
    props=["رسانه ابزار بازتولید قدرت و سلطه است", "تحلیل انتقادی باید رهایی‌بخش باشد"],
    figs=["یورگن هابرماس", "پائولو فریر", "کارول فرازنر", "دانیل گیروکس", "میکل اپل"],
    period="1960-2020", geo="آمریکا/آلمان",
    rel=["جامعه‌شناسی", "فلسفه سیاسی", "اقتصاد"],
    apps=["تحلیل انتقادی رسانه", "نقد ایدئولوژی رسانه‌ای"],
    strengths=["بین‌رشته‌ای و سیاسی"],
    limits=["سیاسی‌گرایی و ایدئولوژیک شدن"],
    crits=["ضعف روش‌شناختی"],
    refs=["Habermas (1968), Legitimation Crisis", "Freire (1968), Pedagogy of the Oppressed", "Giroux (1992), Border Crossings"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "critical-studies"}, {"key": "approach", "value": "critical"}]))

# 12. STS
ents.append(E(
    "kg-tradition-sts", "مطالعات علم و فناوری", "Science and Technology Studies (STS)",
    "sts", "TRADITION", None,
    "خاندان فکری بین‌رشته‌ای که علم و فناوری را نه طبیعی بلکه ساخته‌شده اجتماعی-سیاسی تحلیل می‌کند.",
    "STS (Latour, Callon, Bijker, Pinch, Trevor, Collins, Shapin) بر سه اصل استوار است: (1) «علم اجتماعی است» (علم‌سنجی)، (2) «فناوری ساخته‌شده است» (فناوری‌سنجی) و (3) «نظریه کنشگر-شبکه» (ANT). در رسانه، تحلیل الگوریتم‌ها، هوش مصنوعی و «عاملیت الگوریتمی» از طریق STS امکان‌پذیر است.",
    philo="نظریه کنشگر-شبکه و سوشیولوژی علم.",
    props=["علم و فناوری ساخته‌شده اجتماعی-سیاسی‌اند", "شبکه از انسان‌ها و غیرانسان‌ها تشکیل شده است"],
    figs=["برونو لاتوُر", "مایکل کالنون", "ویکتر پینچ", "تشارلز پینچ"],
    period="1970-2020", geo="هلند/فرانسه/آمریکا",
    rel=["فیزیک", "سوشیولوژی", "فلسفه علم"],
    apps=["تحلیل الگوریتم‌ها و هوش مصنوعی", "نقد عاملیت الگوریتمی"],
    strengths=["بین‌رشته‌ای و کاربردی"],
    limits=["پیچیدگی روش‌شناختی", "کلی‌سازی تکنولوژی"],
    crits=["اساس‌گرایی تکنولوژیک"],
    refs=["Latour (1987), Science in Action", "Callon & Latour (1981), Inscriptions that Hold", "Pinch & Bijker (1984), The Social Construction of Technical Systems"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "sts"}]))

ents.append(E(
    "kg-subfield-sociology-of-science", "جامعه‌شناسی علم", "Sociology of Scientific Knowledge (SSK)",
    "sociology-of-science", "SUBFIELD", "kg-tradition-sts",
    "حوزه‌ی تخصصی STS که ساختارهای اجتماعی علم (مؤسسه، نخبگی، جریان) را تحلیل می‌کند.",
    "SSK (Barnes, Mulkay, Bloor، «برنامه‌ی ادینبرو») نشان می‌دهد «واقعیت علمی» از طریق مذاکره اجتماعی و «قوه‌ی اعتبار» (social accountability) ساخته می‌شود. در رسانه، تحلیل تولید علم و رسانه در عصر هوش مصنوعی نمونه‌های معاصر این حوزه‌اند.",
    philo="نظریه اجتماعی علم.",
    props=["علم از طریق مذاکره اجتماعی ساخته می‌شود", "مؤسسه علم ساختار قدرت دارد"],
    figs=["برنارد بارنز", "مایکل ماکل", "دیوید بلور"], period="1970-2000",
    refs=["Barnes & Bloor (1993), The Sociology of Scientific Knowledge", "Mulkay (1979), The Ethnography of a Laboratory Group"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "critical"}, {"key": "theoretical_tradition", "value": "sts"}]))
ents.append(E(
    "kg-subfield-studies-of-technology", "مطالعات فناوری", "Studies of Technology (Social Shaping of Technology)",
    "studies-of-technology", "SUBFIELD", "kg-tradition-sts",
    "حوزه‌ی تخصصی STS که شکل‌دهی اجتماعی فناوری (SST) و معنای فرهنگی فناوری را بررسی می‌کند.",
    "در SST (Bijker, Pinch, Hughes)، فناوری نه قطعی بلکه «نقاط کهنه» (problem) و «گروه‌های مربوطه» (relevant social groups) هستند. در رسانه، الگوریتم‌ها و هوش مصنوعی نمونه‌های بارز فناوری‌هایی‌اند که شکل‌دهی اجتماعی دارند.",
    philo="نظریه شکل‌دهی اجتماعی فناوری.",
    props=["فناوری ساخته‌شده اجتماعی است", "«نقاط کهنه» و «گروه‌های مربوطه» الگوهای کلیدی هستند"],
    figs=["ویکتر پینچ", "تشارلز پینچ", "توماس هوگس"], period="1975-2020",
    refs=["Pinch & Bijker (1984), The Social Construction of Technical Systems", "Hughes (1983), Networks of Power"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "interpretive"}, {"key": "theoretical_tradition", "value": "sts"}]))
ents.append(E(
    "kg-subfield-actor-network-theory", "نظریه کنشگر-شبکه", "Actor-Network Theory (ANT)",
    "actor-network-theory", "SUBFIELD", "kg-tradition-sts",
    "نظریه کنشگر-شبکه (ANT) برونو لاتوُر و مایکل کالنون که انسان‌ها و غیرانسان‌ها را هم‌سطح تحلیل می‌کند.",
    "ANT بر سه اصل استوار است: (1) «ژنرالیزاسیون» (generalization)، (2) «ترکیب‌بندی» (association) و (3) «تعقیب» (following the actors). در رسانه، الگوریتم‌ها، اپلیکیشن‌ها و داده‌ها هم‌سطح با انسان‌ها در شبکه تحلیل می‌شوند.",
    philo="نظریه کنشگر-شبکه.",
    props=["انسان و غیرانسان هم‌سطح تحلیل می‌شوند", "شبکه از «ترکیب‌ها» (associations) ساخته می‌شود"],
    figs=["برونو لاتوُر", "مایکل کالنون", "جان کالون"], period="1980-2020",
    refs=["Latour (1987), Science in Action", "Callon, Latour & Law (2002), Actor-Network Theory"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "interpretive"}, {"key": "theoretical_tradition", "value": "sts"}]))

# 13. Network Theories
ents.append(E(
    "kg-tradition-network-theory", "نظریه‌های شبکه", "Network Theories",
    "network-theories", "TRADITION", None,
    "خاندان فکری بین‌رشته‌ای که پدیده‌های اجتماعی را به‌عنوان شبکه‌هایی از گره‌ها و پیوندها تحلیل می‌کند.",
    "نظریه‌های شبکه (Granovetter, Wellman, Barabasi, Castells, Wasserman) از سه ریشه سرچشمه می‌گیرند: (1) ریاضی گراف (Graph Theory)، (2) جامعه‌شناسی شبکه (Granovetter 1973 «پاداش‌های پیوندهای ضعیف»، Wellman) و (3) جامعه شبکه‌ای (Castells 1996). در رسانه، تحلیل شبکه‌های اجتماعی، الگوریتم‌های انتشار و «مرکزیت» (centrality) کاربردهای اصلی این خاندان است.",
    philo="نظریه شبکه و ریاضی گراف.",
    props=["پدیده‌های اجتماعی به‌صورت شبکه‌های گره و پیوند قابل مدل‌سازی‌اند", "مرکزیت و ساختار شبکه رفتار را شکل می‌دهد"],
    figs=["مارک گرانوفتر", "باربارا ولمن", "آلبارت باراباسی", "مانوئل کاستلز", "استنفورد واتسون"],
    period="1970-2020", geo="آمریکا",
    rel=["ریاضی", "فیزیک", "جامعه‌شناسی"],
    apps=["تحلیل شبکه‌های اجتماعی و ارتباطی", "مدل‌سازی انتشار اطلاعات"],
    strengths=["مدل‌سازی منظم و کمّی"],
    limits=["کاهش‌پدیدی (reductionism)", "پیچیدگی داده"],
    crits=["نادیده‌گرفتن محتوا و معنا"],
    refs=["Granovetter (1973), The Strength of Weak Ties", "Castells (1996), The Rise of the Network Society", "Barabasi (2002), Linked"],
    facets=FAC[:2] + [{"key": "theoretical_tradition", "value": "network-theory"}]))

ents.append(E(
    "kg-subfield-social-networks", "شبکه‌های اجتماعی", "Social Networks",
    "social-networks", "SUBFIELD", "kg-tradition-network-theory",
    "حوزه‌ی تخصصی تحلیل شبکه‌های اجتماعی (SNA) به‌عنوان ساختارهای روابط بین اشخاص و گروه‌ها.",
    "SNA (Wasserman & Faust, Freeman, Burt) روابط بین گره‌ها را با شاخص‌هایی مانند «مرکزیت» (centrality)، «شکل» (structure) و «جریان» (flow) تحلیل می‌کند. در رسانه، تحلیل شبکه‌های اجتماعی ابزار اصلی فهم انتشار اطلاعات و نفوذ است.",
    philo="نظریه شبکه و ریاضی گراف.",
    props=["روابط بین گره‌ها قابل اندازه‌گیری‌اند", "مرکزیت نفوذ و جریان اطلاعات را توضیح می‌دهد"],
    figs=["استنفورد واتسون", "لوئیس فاست", "لوسیون فریمن", "رونالد برت"], period="1970-2020",
    refs=["Wasserman & Faust (1994), Social Network Analysis", "Freeman (1978), Centrality in Social Networks"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "quantitative"}, {"key": "theoretical_tradition", "value": "network-theory"}]))
ents.append(E(
    "kg-subfield-communication-networks", "شبکه‌های ارتباطی", "Communication Networks",
    "communication-networks", "SUBFIELD", "kg-tradition-network-theory",
    "حوزه‌ی تخصصی تحلیل شبکه‌های ارتباطی (جریان اطلاعات، نفوذ و انتشار) در رسانه.",
    "در شبکه‌های ارتباطی، «جریان اطلاعات» (information flow)، «نفوذ» (influence) و «انتشار» (diffusion) در ساختار شبکه مدل‌سازی می‌شوند. الگوریتم‌های انتشار (SIR, SI) و شبکه‌های پیوندی (connected networks) ابزارهای اصلی این حوزه‌اند.",
    philo="نظریه شبکه و سیبرنتیک.",
    props=["جریان اطلاعات در ساختار شبکه مدل‌سازی می‌شود", "الگوریتم‌های انتشار رفتار شبکه را توصیف می‌کنند"],
    figs=["مارک گرانوفتر", "مانوئل کاستلز"], period="1970-2020",
    refs=["Granovetter (1973), The Strength of Weak Ties", "Castells (1996), The Rise of the Network Society"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "quantitative"}, {"key": "theoretical_tradition", "value": "network-theory"}]))
ents.append(E(
    "kg-subfield-networked-society", "جامعه شبکه‌ای", "Networked Society",
    "networked-society", "SUBFIELD", "kg-tradition-network-theory",
    "حوزه‌ی تخصصی مانوئل کاستلز (1996) که شبکه را ساختار بنیادین جامعه معاصر می‌داند.",
    "کاستلز «جامعه شبکه‌ای» را با سه ویژگی می‌شناسد: (1) شبکه‌سازی به‌عنوان شکل بنیادین سازمان‌دهی، (2) الکترونیک‌شدن اطلاعات و (3) جداسازی مکان و زمان. در رسانه، الگوریتم‌ها، پلتفرم‌ها و رسانه‌های اجتماعی نمونه‌های بارز شبکه‌های جامعه‌ای کاستلز هستند.",
    philo="نظریه شبکه و جامعه‌شناسی.",
    props=["شبکه ساختار بنیادین جامعه معاصر است", "جداسازی مکان و زمان ویژگی کلیدی شبکه‌ای است"],
    figs=["مانوئل کاستلز"], period="1996-2020",
    refs=["Castells (1996), The Rise of the Network Society"],
    facets=[{"key": "domain", "value": "communication"}, {"key": "approach", "value": "critical"}, {"key": "theoretical_tradition", "value": "network-theory"}]))

# ================= SECTION 3: 18 specialized media subfields ============
S3 = [{"key": "domain", "value": "media-studies"}, {"key": "approach", "value": "specialized"}]
SUBFIELDS = [
    ("kg-subfield-journalism", "مطالعات مطبوعات و روزنامه‌نگاری", "Newspaper & Journalism Studies",
     "journalism-studies", "مطالعات مطبوعات و روزنامه‌نگاری با تمرکز بر خبر، کارکرد رسانه، مالکیت و بازنمایی در رسانه‌های نوشتاری و دیجیتال.",
     "این حوزه بر تحلیل «نقش خبر»، «مالکیت رسانه»، «کارکرد مطبوعات» (Lippmann, Lee), «روایت‌های خبری» (framing, agenda-setting) و «خبر در عصر دیجیتال» (convergence journalism) تمرکز دارد.",
     ["وا尔特 لپمن", "هارولد لاسول", "تونی بروکس"],
     ["Lippmann (1922), Public Opinion", "Tuchman (1972), Making News"],
     "1900-2020", "آمریکا"),
    ("kg-subfield-radio-tv", "مطالعات رادیو و تلویزیون", "Radio & Television Studies",
     "radio-tv-studies", "مطالعات رادیو و تلویزیون با تمرکز بر ساختار، بازنمایی، مصرف و کارکرد رسانه‌های صوتی-بصری.",
     "این حوزه بر تحلیل «ساختار رادیویی/تلویزیونی»، «برنامه‌سازی»، «مخاطب‌محوری»، «روایت تصویری» و «نقش رسانه در زندگی روزمره» تمرکز دارد.",
     ["روبرت کاستل", "دنی راندمان"],
     ["Cottle (1940), The Sociology of Radio"],
     "1920-2020", "آمریکا"),
    ("kg-subfield-film-tv", "مطالعات سینما و رسانه‌های تصویری", "Film & Visual Media Studies",
     "film-visual-media-studies", "مطالعات سینما و رسانه‌های تصویری با تمرکز بر روایت، ژانر، بازنمایی و تحلیل بصری.",
     "این حوزه بر «تحلیل روایت» (Narratology)، «ژانر» (Genre)، «بازنمایی» (Representation) و «تحلیل بصری» (Visual Analysis) تمرکز دارد؛ از نظریه‌های ساختارگرای سینما تا تحلیل نشانه‌شناختی (Metz, Kraco) و تحلیل بصری (Bal, Sturrock).",
     ["موریس متز", "کریس کراکو", "ماریا بوال"],
     ["Metz (1974), Film Language", "Baudry (1975), The Apparatus"],
     "1950-2020", "فرانسه"),
    ("kg-subfield-digital-media-studies", "مطالعات رسانه‌های دیجیتال", "Digital Media Studies",
     "digital-media-studies", "مطالعات رسانه‌های دیجیتال با تمرکز بر همگرایی، مشارکت، الگوریتم و تعامل.",
     "این حوزه بر «همگرایی رسانه‌ای» (Jen Jenkins)، «فرهنگ مشارکتی» (Participatory Culture)، «عاملیت الگوریتمی» (Algorithmic Agency) و «تجربه کاربری» (UX) تمرکز دارد. الگوریتم‌ها، داده‌ها و هوش مصنوعی موضوعات اصلی این حوزه‌اند.",
     ["جن کنس", "دانیل روزنبرگ", "سوزان لوس"],
     ["Jenkins (2006), Convergence Culture", "Rosenzweig (2003), The Public Sphere of the Internet"],
     "1995-2020", "آمریکا"),
    ("kg-subfield-platform-studies", "مطالعات پلتفرم‌ها", "Platform Studies",
     "platform-studies", "مطالعات پلتفرم‌ها با تمرکز بر پلتفرم‌سازی (Platformization)، معماری و اقتصاد پلتفرم.",
     "این حوزه بر «پلتفرم‌سازی» (Platformization)، «معماری پلتفرم» (Platform Architecture)، «اقتصاد پلتفرم» (Platform Economy) و «حکمرانی پلتفرم» (Platform Governance) تمرکز دارد. نیکوسیوس و لافور (2017) و لوفون و بوس (2018) از بنیان‌گذاران این حوزه‌اند.",
     ["اندرو لافور", "مایکل نیکوسیوس", "لوفون و بوس"],
     ["Nieborg & Poell (2018), Platform Capitalism"],
     "2010-2020", "هلند"),
    ("kg-subfield-social-media", "مطالعات شبکه‌های اجتماعی", "Social Media Studies",
     "social-media-studies", "مطالعات شبکه‌های اجتماعی با تمرکز بر مشارکت، انتشار، الگوریتم و هویت دیجیتال.",
     "این حوزه بر «مشارکت مخاطب»، «انتشار اطلاعات»، «الگوریتم‌های پیشنهادی»، «هویت دیجیتال» و «اقتصاد توجه» تمرکز دارد. الگوریتم‌ها، داده‌ها و تعاملات شبکه‌ای ابزار اصلی این حوزه‌اند.",
     ["جانی وون", "میکل فکاک"],
     ["boyd & Ellison (2007), Social Network Sites"],
     "2000-2020", "آمریکا"),
    ("kg-subfield-digital-games", "مطالعات بازی‌های دیجیتال", "Digital Games Studies",
     "digital-games-studies", "مطالعات بازی‌های دیجیتال با تمرکز بر روایت تعاملی، بازی‌سازی و اقتصاد بازی.",
     "این حوزه بر «روایت تعاملی» (Interactive Narrative)، «بازی‌سازی» (Game Design)، «اقتصاد بازی» (Game Economy) و «هویت بازیکن» تمرکز دارد. از نظریه‌های روایت‌شناسی تا تحلیل «بازی به‌عنوان متن» (Game as Text).",
     ["جاناتان گرومن", "ایان هاینس"],
     ["Groves (2017), The New Media Gamebook"],
     "1990-2020", "آمریکا/اسکاندیناوی"),
    ("kg-subfield-ai-media", "مطالعات هوش مصنوعی و رسانه", "AI & Media Studies",
     "ai-media-studies", "مطالعات هوش مصنوعی و رسانه با تمرکز بر عاملیت الگوریتمی، تولید محتوای هوشمند و اخلاق AI.",
     "این حوزه بر «عاملیت الگوریتمی» (Algorithmic Agency)، «تولید محتوای هوشمند» (Generative AI)، «اخلاق هوش مصنوعی» (AI Ethics) و «ترکیب انسانی-ماشینی» تمرکز دارد. از تحلیل STS تا نقد الگوریتم‌ها.",
     ["مارکو زامبلا", "کریس لویز"],
     ["Zambrano & Lewis (2019), AI in Media"],
     "2010-2020", "آمریکا"),
    ("kg-subfield-data-journalism", "مطالعات روزنامه‌نگاری داده‌محور", "Data Journalism Studies",
     "data-journalism-studies", "مطالعات روزنامه‌نگاری داده‌محور با تمرکز بر تحلیل داده، بصری‌سازی و گزارشگری مبتنی بر داده.",
     "این حوزه بر «تحلیل داده» (Data Analysis)، «بصری‌سازی» (Visualization)، «گزارشگری مبتنی بر داده» (Data-driven Reporting) و «اخلاق داده» تمرکز دارد. روزنامه‌نگاری داده‌محور ترکیب ژورنالیسم و علوم داده است.",
     ["استیون کینت", "میک لویز"],
     ["Kent & Lewis (2019), Data Journalism"],
     "2010-2020", "آمریکا/اسکاندیناوی"),
    ("kg-subfield-political-comm", "مطالعات ارتباطات سیاسی", "Political Communication Studies",
     "political-communication-studies", "مطالعات ارتباطات سیاسی با تمرکز بر چارچوب‌بندی، دستورکار، تبلیغات و حوزه عمومی.",
     "این حوزه بر «چارچوب‌بندی سیاسی» (Political Framing)، «دستورکار سیاسی» (Political Agenda-Setting)، «تبلیغات سیاسی» (Political Advertising) و «حوزه عمومی» (Public Sphere) تمرکز دارد. از نظریه‌های حوزه عمومی هابرماس تا تحلیل گفتمان سیاسی.",
     ["یورگن هابرماس", "دونالد شندون"],
     ["Scheufele & Tew (2007), Framing, Agenda-Setting, and Priming"],
     "1950-2020", "آمریکا/آلمان"),
    ("kg-subfield-advertising-pr", "مطالعات تبلیغات و روابط عمومی", "Advertising & Public Relations Studies",
     "advertising-pr-studies", "مطالعات تبلیغات و روابط عمومی با تمرکز بر اثربخشی، بازنمایی، اعتماد و برند.",
     "این حوزه بر «اثربخشی تبلیغات» (Advertising Effectiveness)، «بازنمایی در تبلیغات» (Representation in Ads)، «اعتماد سازمانی» (Organizational Trust) و «مدیریت روابط» (Relationship Management) تمرکز دارد. از مدل‌های تبلیغات کلاسیک تا تحلیل انتقادی تبلیغات.",
     ["هربرت لاسول", "مایکل بارتل"],
     ["Bartles (2015), PR and Trust"],
     "1920-2020", "آمریکا"),
    ("kg-subfield-audience", "مطالعات مخاطب و مصرف رسانه", "Audience & Media Consumption Studies",
     "audience-consumption-studies", "مطالعات مخاطب و مصرف رسانه با تمرکز بر دریافت، مشارکت، رضامندی و مصرف.",
     "این حوزه بر «نظریه استفاده و رضامندی» (Uses & Gratifications)، «مخاطب فعال» (Active Audience)، «مشارکت مخاطب» (Audience Participation) و «مصرف رسانه‌ای» (Media Consumption) تمرکز دارد. از نظریه‌های کلاسیک تا تحلیل الگوریتمی.",
     ["کارل هرمان", "ایان گورینگ"],
     ["Hermans & Goring (2001), Audience Research"],
     "1940-2020", "آمریکا"),
    ("kg-subfield-media-literacy", "مطالعات سواد رسانه‌ای", "Media Literacy Studies",
     "media-literacy-studies", "مطالعات سواد رسانه‌ای با تمرکز بر درک، تحلیل و تولید انتقادی رسانه.",
     "این حوزه بر «درک رسانه» (Media Understanding)، «تحلیل انتقادی» (Critical Analysis)، «تولید رسانه‌ای» (Media Production) و «سواد دیجیتال» (Digital Literacy) تمرکز دارد. از سواد رسانه‌ای کلاسیک تا سواد الگوریتمی.",
     ["هلموت مورتون", "پاتر"],
     ["Potter (2004), Media Literacy"],
     "1970-2020", "آمریکا/اسکاندیناوی"),
    ("kg-subfield-media-governance", "مطالعات حکمرانی و سیاست‌گذاری رسانه", "Media Governance & Policy Studies",
     "media-governance-policy-studies", "مطالعات حکمرانی و سیاست‌گذاری رسانه با تمرکز بر تنظیم، مالکیت، رقابت و مقررات.",
     "این حوزه بر «تنظیم رسانه» (Media Regulation)، «مالکیت و تمرکز» (Ownership & Concentration)، «رقابت» (Competition) و «سیاست‌گذاری رسانه‌ای» (Media Policy) تمرکز دارد. از نظریه‌های کلاسیک تنظیم تا حکمرانی الگوریتمی.",
     ["مارک لوفور", "مایکل رابرتسون"],
     ["Robinson & Robertson (2018), Media Governance"],
     "1980-2020", "آمریکا/اروپا"),
    ("kg-subfield-media-ownership-economics", "مطالعات مالکیت و اقتصاد رسانه", "Media Ownership & Economics Studies",
     "media-ownership-economics-studies", "مطالعات مالکیت و اقتصاد رسانه با تمرکز بر تمرکز، سرمایه‌داری رسانه‌ای و اقتصاد دیجیتال.",
     "این حوزه بر «تمرکز مالکیت» (Ownership Concentration)، «اقتصاد رسانه» (Media Economics)، «سرمایه‌داری رسانه‌ای» (Media Capitalism) و «اقتصاد دیجیتال» تمرکز دارد. از نظریه‌های کلاسیک اقتصاد رسانه تا تحلیل انتقادی اقتصاد پلتفرم.",
     ["دانیل رابرتسون", "توماس هاروی"],
     ["Robertson & Harvey (2019), Media Economics"],
     "1970-2020", "آمریکا/بریتانیا"),
    ("kg-subfield-development-comm", "مطالعات ارتباطات توسعه", "Development Communication Studies",
     "development-communication-studies", "مطالعات ارتباطات توسعه با تمرکز بر توسعه مشارکتی، توانمندسازی و ارتباطات توسعه‌ای.",
     "این حوزه بر «ارتباطات توسعه‌ای» (Development Communication)، «توانمندسازی» (Empowerment)، «مشارکت» (Participation) و «تغییر رفتار» (Behavior Change) تمرکز دارد. از مدل‌های کلاسیک ارتباطات توسعه (Rogers) تا نقد پسااستعماری.",
     ["فریتس روگرس", "استیون هال"],
     ["Rogers (1994), Communication for Development"],
     "1950-2020", "آمریکا"),
    ("kg-subfield-international-comm", "مطالعات ارتباطات بین‌الملل", "International Communication Studies",
     "international-communication-studies", "مطالعات ارتباطات بین‌الملل با تمرکز بر جریان رسانه‌ای، جهانی‌شدن و بازنمایی بین‌فرهنگی.",
     "این حوزه بر «جریان‌های رسانه‌ای بین‌المللی» (International Media Flows)، «جهانی‌شدن رسانه» (Media Globalization)، «بازنمایی بین‌فرهنگی» (Cross-cultural Representation) و «دیپلماسی رسانه‌ای» تمرکز دارد. از نظریه‌های کلاسیک جریان تا تحلیل بین‌فرهنگی.",
     ["دانیل روزنبرگ", "استیون هال"],
     ["Hall (1994), Cultural Identity and Media Representation"],
     "1970-2020", "آمریکا/بریتانیا"),
    ("kg-subfield-crisis-comm", "مطالعات ارتباطات بحران و ریسک", "Crisis & Risk Communication Studies",
     "crisis-risk-communication-studies", "مطالعات ارتباطات بحران و ریسک با تمرکز بر مدیریت بحران، اعتماد و ارتباطات ریسک.",
     "این حوزه بر «مدیریت ارتباطات بحران» (Crisis Communication Management)، «اعتماد» (Trust)، «ارتباطات ریسک» (Risk Communication) و «بحران عمومی» (Public Crisis) تمرکز دارد. از مدل‌های کلاسیک مدیریت بحران (Coombs) تا تحلیل الگوریتمی بحران.",
     ["تیموتی کومبز", "کریس گروو"],
     ["Coombs (2019), Ongoing Crisis Communication"],
     "1970-2020", "آمریکا"),
]

for eid, fa, en, slug, desc, full_desc, figs, refs, period, geo in SUBFIELDS:
    ents.append(E(
        eid, fa, en, slug, "SUBFIELD", None,
        "حوزه‌ی تخصصی مطالعات رسانه: " + fa,
        full_desc,
        hist=None, philo=None,
        props=None, figs=figs, period=period, geo=geo,
        rel=["علوم ارتباطات", "رسانه‌شناسی"],
        apps=None, strengths=None, limits=None, crits=None,
        refs=refs, facets=S3))

# ================= RELATIONS ============
rels = []

# internal: subbranches belong to parent tradition
rel_map = [
    # marxism subbranches
    ("kg-approach-classical-marxism", "kg-tradition-marxism", "PART_OF"),
    ("kg-approach-gramscian", "kg-tradition-marxism", "PART_OF"),
    ("kg-approach-althusser", "kg-tradition-marxism", "PART_OF"),
    # functionalism
    ("kg-approach-structural-functionalism", "kg-tradition-functionalism", "PART_OF"),
    ("kg-approach-media-functionalist", "kg-tradition-functionalism", "PART_OF"),
    # interactionism
    ("kg-approach-symbolic-interactionism", "kg-tradition-interactionism", "PART_OF"),
    ("kg-approach-social-interactionism", "kg-tradition-interactionism", "PART_OF"),
    # phenomenology
    ("kg-approach-social-phenomenology", "kg-tradition-phenomenology", "PART_OF"),
    ("kg-approach-hermeneutic-phenomenology", "kg-tradition-phenomenology", "PART_OF"),
    # hermeneutics
    ("kg-approach-philosophical-hermeneutics", "kg-tradition-hermeneutics", "PART_OF"),
    ("kg-approach-critical-hermeneutics", "kg-tradition-hermeneutics", "PART_OF"),
    # pragmatism
    ("kg-approach-classical-pragmatism", "kg-tradition-pragmatism", "PART_OF"),
    ("kg-approach-social-pragmatism", "kg-tradition-pragmatism", "PART_OF"),
    # systems theory
    ("kg-approach-general-systems", "kg-tradition-systems-theory", "PART_OF"),
    ("kg-approach-complex-systems", "kg-tradition-systems-theory", "PART_OF"),
    ("kg-approach-communication-systems", "kg-tradition-systems-theory", "PART_OF"),
    # action theory
    ("kg-approach-rational-action", "kg-tradition-theory-of-action", "PART_OF"),
    ("kg-approach-communicative-action", "kg-tradition-theory-of-action", "PART_OF"),
    ("kg-approach-structured-action", "kg-tradition-theory-of-action", "PART_OF"),
    # feminism
    ("kg-approach-liberal-feminism", "kg-tradition-feminism", "PART_OF"),
    ("kg-approach-radical-feminism", "kg-tradition-feminism", "PART_OF"),
    ("kg-approach-socialist-feminism", "kg-tradition-feminism", "PART_OF"),
    ("kg-approach-postmodern-feminism", "kg-tradition-feminism", "PART_OF"),
    ("kg-approach-intersectional-feminism", "kg-tradition-feminism", "PART_OF"),
    # postcolonialism
    ("kg-approach-postcolonial-studies", "kg-tradition-postcolonialism", "PART_OF"),
    ("kg-approach-decolonization", "kg-tradition-postcolonialism", "PART_OF"),
    ("kg-approach-orientalism", "kg-tradition-postcolonialism", "PART_OF"),
    # critical studies
    # STS
    ("kg-subfield-sociology-of-science", "kg-tradition-sts", "PART_OF"),
    ("kg-subfield-studies-of-technology", "kg-tradition-sts", "PART_OF"),
    ("kg-subfield-actor-network-theory", "kg-tradition-sts", "PART_OF"),
    # network theories
    ("kg-subfield-social-networks", "kg-tradition-network-theory", "PART_OF"),
    ("kg-subfield-communication-networks", "kg-tradition-network-theory", "PART_OF"),
    ("kg-subfield-networked-society", "kg-tradition-network-theory", "PART_OF"),
]

for s, t, r in rel_map:
    rels.append(R(s, t, r, f"{s} زیرشاخه‌ای از {t} است", 0.95))

# Cross-block relations (to existing entities in other files)
cross = [
    # traditions influenced communication schools
    ("kg-tradition-marxism", "kg-school-frankfurt", "INFLUENCED", "مارکسیسم مبنا فکری مکتب فرانکفورت و نظریه انتقادی رسانه است", 0.95),
    ("kg-tradition-functionalism", "kg-school-chicago", "RELATED_TO", "کارکردگرایی و مکتب شیکاگو هر دو رویکرد جامعه‌شناختی به رسانه دارند", 0.85),
    ("kg-tradition-interactionism", "kg-school-chicago", "INFLUENCED", "کنش متقابل‌گرایی از مکتب شیکاگو سرچشمه گرفت", 0.95),
    ("kg-tradition-systems-theory", "kg-school-palo-alto", "INFLUENCED", "نظریه سیستم‌ها مبنا فکری مکتب پالو آلتو و نظریه سیستم‌های ارتباطی است", 0.95),
    ("kg-tradition-systems-theory", "kg-school-toronto", "RELATED_TO", "نظریه سیستم‌ها و مکتب تورنتو هر دو رویکرد ساختاری به رسانه دارند", 0.8),
    ("kg-tradition-pragmatism", "kg-tradition-interactionism", "INFLUENCED", "پراگماتیسم مبنا فلسفی تعامل‌گرایی نمادین (مکتب شیکاگو) است", 0.9),
    ("kg-tradition-hermeneutics", "kg-tradition-phenomenology", "INFLUENCED", "هرمنوتیک از پدیدارشناسی الهام گرفت", 0.95),
    ("kg-tradition-postcolonialism", "kg-school-birmingham", "INFLUENCED", "پسااستعمارگرایی بر مطالعات فرهنگی و مکتب بیرمنگام تأثیر گذاشت", 0.9),
    ("kg-tradition-critical-studies", "kg-school-frankfurt", "DERIVED_FROM", "مطالعات انتقادی از نظریه انتقادی مکتب فرانکفورت مشتق شده است", 0.95),
    ("kg-tradition-feminism", "kg-tradition-postcolonialism", "RELATED_TO", "فمینیسم و پسااستعمارگرایی هر دو بر تحلیل قدرت و نابرابری تمرکز دارند", 0.85),
    ("kg-tradition-theory-of-action", "kg-tradition-phenomenology", "INFLUENCED_BY", "نظریه کنش از پدیدارشناسی اجتماعی (شوتز) الهام گرفت", 0.85),

    # subbranch relations
    ("kg-approach-gramscian", "kg-framework-hegemony", "PROPOSED_BY", "گرامشی نظریه هژمونی را مطرح کرد که در تحلیل رسانه کاربرد دارد", 0.95),
    ("kg-approach-gramscian", "kg-school-birmingham", "INFLUENCED", "گرامشی بر مکتب بیرمنگام و مطالعات فرهنگی تأثیر گذاشت", 0.95),
    ("kg-approach-althusser", "kg-framework-critical-theory", "INFLUENCED", "آلتوسر بر نظریه انتقادی و تحلیل ایدئولوژی تأثیر گذاشت", 0.9),
    ("kg-approach-symbolic-interactionism", "kg-framework-symbolic-interaction", "PROPOSED_BY", "تعامل‌گرایی نمادین مبنا فکری این چارچوب است", 0.95),
    ("kg-approach-communication-systems", "kg-framework-communication-systems", "PROPOSED_BY", "نظریه ارتباطی سیستم‌ها مبنا فکری چارچوب سیستم‌های ارتباطی است", 0.95),
    ("kg-approach-communicative-action", "kg-framework-public-sphere", "INFLUENCED", "کنش ارتباطی هابرماس بر نظریه حوزه عمومی تأثیر گذاشت", 0.95),
    ("kg-approach-communicative-action", "kg-theory-public-sphere", "INFLUENCED", "کنش ارتباطی هابرماس بر نظریه حوزه عمومی تأثیر گذاشت", 0.9),
    ("kg-approach-philosophical-hermeneutics", "kg-school-birmingham", "RELATED_TO", "هرمنوتیک فلسفی بر مطالعات فرهنگی و تحلیل متن تأثیر گذاشت", 0.8),
    ("kg-approach-critical-hermeneutics", "kg-framework-critical-theory", "INFLUENCED_BY", "هرمنوتیک انتقادی از نظریه انتقادی فراکفورت تأثیر پذیرفت", 0.9),
    ("kg-approach-social-phenomenology", "kg-approach-hermeneutic-phenomenology", "RELATED_TO", "پدیدارشناسی اجتماعی و پدیدارشناسی هرمنوتیکی مکمل هم هستند", 0.85),
    ("kg-approach-structural-functionalism", "kg-framework-media-effects", "INFLUENCED", "کارکردگرایی ساختاری بر سنت پژوهش‌های اثرات رسانه تأثیر گذاشت", 0.85),
    ("kg-approach-media-functionalist", "kg-framework-media-effects", "INFLUENCED", "کارکردگرایی رسانه بر تحلیل اثرات و کارکردهای رسانه تأثیر گذاشت", 0.85),
    ("kg-approach-postcolonial-studies", "kg-theory-cultural-imperialism", "INFLUENCED", "مطالعات پسااستعماری بر نظریه امپریالیسم فرهنگی تأثیر گذاشت", 0.9),
    ("kg-approach-postcolonial-studies", "kg-theory-media-globalization", "INFLUENCED", "مطالعات پسااستعماری بر نظریه جهانی‌شدن رسانه تأثیر گذاشت", 0.9),
    ("kg-approach-decolonization", "kg-approach-postcolonial-studies", "EXTENDS", "استعمارزدایی مطالعات پسااستعماری را توسعه می‌دهد", 0.9),
    ("kg-approach-orientalism", "kg-theory-culture-industry", "CRITICIZES", "شرق‌شناسی از بازنمایی استعماری و فرهنگ‌محوری نقد می‌کند", 0.8),
    ("kg-subfield-sociology-of-science", "kg-subfield-studies-of-technology", "RELATED_TO", "جامعه‌شناسی علم و مطالعات فناوری دو شاخه‌ی مکمل STS هستند", 0.95),
    ("kg-subfield-actor-network-theory", "kg-subfield-studies-of-technology", "INFLUENCED", "ANT بر مطالعات فناوری و شکل‌دهی اجتماعی فناوری تأثیر گذاشت", 0.9),
    ("kg-subfield-actor-network-theory", "kg-tradition-systems-theory", "RELATED_TO", "ANT رویکردی بین‌رشته‌ای به شبکه‌ها و سیستم‌ها است", 0.8),
    ("kg-subfield-social-networks", "kg-subfield-communication-networks", "RELATED_TO", "شبکه‌های اجتماعی و ارتباطی دو شاخه‌ی مرتبط نظریه شبکه هستند", 0.9),
    ("kg-subfield-networked-society", "kg-theory-network-society", "PROPOSED_BY", "کاستلز در چارچوب جامعه شبکه‌ای نظریه جامعه شبکه‌ای را مطرح کرد", 0.95),
    ("kg-subfield-communication-networks", "kg-theory-networked-communication", "INFLUENCED", "تحلیل شبکه‌های ارتباطی بر نظریه ارتباطات شبکه‌ای تأثیر گذاشت", 0.85),
    ("kg-subfield-communication-networks", "kg-theory-information-society", "RELATED_TO", "شبکه‌های ارتباطی و جامعه اطلاعاتی هر دو به جریان اطلاعات می‌پردازند", 0.85),
    ("kg-subfield-social-networks", "kg-technique-focus-group", "USES", "تحلیل شبکه‌های اجتماعی از روش‌های گروهی استفاده می‌کند", 0.7),
    ("kg-subfield-networked-society", "kg-subfield-digital-media", "RELATED_TO", "جامعه شبکه‌ای بر مطالعات رسانه‌های دیجیتال تأثیر گذاشت", 0.9),

    # subfields of section 3 → related theories (cross-block)
    ("kg-subfield-political-comm", "kg-theory-agenda-setting", "APPLIES_TO", "مطالعات ارتباطات سیاسی از نظریه دستورکار استفاده می‌کند", 0.95),
    ("kg-subfield-political-comm", "kg-theory-framing", "APPLIES_TO", "مطالعات ارتباطات سیاسی از نظریه چارچوب‌بندی استفاده می‌کند", 0.95),
    ("kg-subfield-political-comm", "kg-theory-spiral-silence", "APPLIES_TO", "مطالعات ارتباطات سیاسی از نظریه مارپیچ سکوت استفاده می‌کند", 0.95),
    ("kg-subfield-political-comm", "kg-framework-public-sphere", "APPLIES_TO", "مطالعات ارتباطات سیاسی از چارچوب حوزه عمومی استفاده می‌کند", 0.9),
    ("kg-subfield-journalism", "kg-theory-framing", "APPLIES_TO", "مطالعات مطبوعات از نظریه چارچوب‌بندی خبری استفاده می‌کند", 0.9),
    ("kg-subfield-journalism", "kg-theory-agenda-setting", "APPLIES_TO", "مطالعات مطبوعات از نظریه دستورکار استفاده می‌کند", 0.9),
    ("kg-subfield-audience", "kg-theory-uses-and-gratifications", "APPLIES_TO", "مطالعات مخاطب از نظریه استفاده و رضامندی استفاده می‌کند", 0.95),
    ("kg-subfield-audience", "kg-theory-active-audience", "APPLIES_TO", "مطالعات مخاطب از نظریه مخاطب فعال استفاده می‌کند", 0.95),
    ("kg-subfield-audience", "kg-theory-encoding-decoding", "APPLIES_TO", "مطالعات مخاطب از نظریه رمزگذاری و رمزگشایی استفاده می‌کند", 0.9),
    ("kg-subfield-digital-media", "kg-theory-media-convergence", "APPLIES_TO", "مطالعات رسانه‌های دیجیتال از نظریه همگرایی استفاده می‌کند", 0.95),
    ("kg-subfield-digital-media", "kg-theory-participatory-culture", "APPLIES_TO", "مطالعات رسانه‌های دیجیتال از نظریه فرهنگ مشارکتی استفاده می‌کند", 0.95),
    ("kg-subfield-digital-media", "kg-theory-algorithmic-agency", "APPLIES_TO", "مطالعات رسانه‌های دیجیتال از نظریه عاملیت الگوریتمی استفاده می‌کند", 0.9),
    ("kg-subfield-platform-studies", "kg-theory-platformization", "APPLIES_TO", "مطالعات پلتفرم‌ها از نظریه پلتفرم‌سازی استفاده می‌کند", 0.95),
    ("kg-subfield-platform-studies", "kg-theory-platform-society", "APPLIES_TO", "مطالعات پلتفرم‌ها از نظریه جامعه پلتفرمی استفاده می‌کند", 0.95),
    ("kg-subfield-platform-studies", "kg-model-convergence-model", "APPLIES_TO", "مطالعات پلتفرم‌ها از مدل همگرایی استفاده می‌کند", 0.8),
    ("kg-subfield-social-media", "kg-theory-networked-communication", "APPLIES_TO", "مطالعات شبکه‌های اجتماعی از نظریه ارتباطات شبکه‌ای استفاده می‌کند", 0.95),
    ("kg-subfield-social-media", "kg-theory-attention-economy", "APPLIES_TO", "مطالعات شبکه‌های اجتماعی از نظریه اقتصاد توجه استفاده می‌کند", 0.9),
    ("kg-subfield-social-media", "kg-subfield-social-networks", "APPLIES_TO", "مطالعات شبکه‌های اجتماعی از تحلیل شبکه استفاده می‌کند", 0.9),
    ("kg-subfield-ai-media", "kg-theory-algorithmic-agency", "APPLIES_TO", "مطالعات هوش مصنوعی از نظریه عاملیت الگوریتمی استفاده می‌کند", 0.95),
    ("kg-subfield-ai-media", "kg-subfield-actor-network-theory", "APPLIES_TO", "مطالعات هوش مصنوعی از نظریه کنشگر-شبکه استفاده می‌کند", 0.9),
    ("kg-subfield-film-tv", "kg-framework-semiotic-analysis", "APPLIES_TO", "مطالعات سینما از تحلیل نشانه‌شناختی استفاده می‌کند", 0.9),
    ("kg-subfield-film-tv", "kg-approach-classical-marxism", "CRITICIZES", "نقد مارکسیستی سینما از صنعت فرهنگ می‌کند", 0.75),
    ("kg-subfield-film-tv", "kg-theory-culture-industry", "RELATED_TO", "مطالعات سینما با نظریه صنعت فرهنگ مرتبط است", 0.85),
    ("kg-subfield-crisis-comm", "kg-theory-media-consumption", "RELATED_TO", "مطالعات ارتباطات بحران با نظریه مصرف رسانه مرتبط است", 0.7),
    ("kg-subfield-development-comm", "kg-subfield-international-comm", "RELATED_TO", "ارتباطات توسعه و ارتباطات بین‌الملل هر دو بر ارتباطات فرامرزومی تمرکز دارند", 0.85),
    ("kg-subfield-international-comm", "kg-theory-media-globalization", "APPLIES_TO", "مطالعات ارتباطات بین‌الملل از نظریه جهانی‌شدن رسانه استفاده می‌کند", 0.9),
    ("kg-subfield-media-governance", "kg-subfield-media-ownership-economics", "RELATED_TO", "حکمرانی رسانه و اقتصاد رسانه دو حوزه‌ی مکمل هستند", 0.9),
    ("kg-subfield-media-ownership-economics", "kg-tradition-marxism", "INFLUENCED_BY", "اقتصاد رسانه از اقتصاد سیاسی انتقادی و مارکسیسم تأثیر پذیرفت", 0.9),
    ("kg-subfield-radio-tv", "kg-framework-media-effects", "APPLIES_TO", "مطالعات رادیو و تلویزیون از نظریه اثرات رسانه استفاده می‌کند", 0.85),
    ("kg-subfield-advertising-pr", "kg-subfield-media-effects", "APPLIES_TO", "مطالعات تبلیغات و روابط عمومی از نظریه اثرات رسانه استفاده می‌کند", 0.85),
    ("kg-subfield-media-literacy", "kg-approach-communicative-action", "RELATED_TO", "سواد رسانه‌ای با کنش ارتباطی و توانمندی مخاطب مرتبط است", 0.8),
    ("kg-subfield-data-journalism", "kg-subfield-digital-media", "RELATED_TO", "روزنامه‌نگاری داده‌محور شاخه‌ای از رسانه‌های دیجیتال است", 0.9),
    ("kg-subfield-digital-games", "kg-theory-participatory-culture", "RELATED_TO", "مطالعات بازی‌های دیجیتال با فرهنگ مشارکتی مرتبط است", 0.85),
    ("kg-subfield-journalism", "kg-subfield-radio-tv", "RELATED_TO", "مطالعات مطبوعات و رادیو-تلویزیون هر دو رسانه‌های کلاسیک را تحلیل می‌کنند", 0.8),
    ("kg-subfield-digital-media", "kg-subfield-platform-studies", "EXTENDS", "مطالعات پلتفرم‌ها مطالعات رسانه‌های دیجیتال را توسعه می‌دهد", 0.85),
]

for s, t, r, d, c in cross:
    rels.append(R(s, t, r, d, c))

# dedupe: keep strongest confidence per (source, target, type)
seen = {}
for r in rels:
    k = (r["source_id"], r["target_id"], r["relation_type"])
    if k not in seen or r["confidence"] > seen[k]["confidence"]:
        seen[k] = r
rels = list(seen.values())

# sort relations for stable output
rels.sort(key=lambda r: (r["source_id"], r["target_id"], r["relation_type"]))

out = {"entities": ents, "relations": rels}
path = r"D:/رسانامه تکمیلی/knowledge-core/data/kg_data_interdisciplinary.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("entities:", len(ents))
print("relations:", len(rels))
print("written:", path)

# sanity checks
ids = [e["id"] for e in ents]
assert len(ids) == len(set(ids)), "duplicate entity id!"
types = {}
for e in ents:
    types[e["entity_type"]] = types.get(e["entity_type"], 0) + 1
print("entity types:", types)
allids = set(ids)
dangling = set()
for r in rels:
    for k in ("source_id", "target_id"):
        v = r[k]
        # external refs are allowed (cross-block), only warn
        if v not in allids:
            dangling.add((v, r["source_id"], r["target_id"], r["relation_type"]))
print("external (cross-block) relation endpoints:", len(dangling))
print("sample dangling:", list(dangling)[:5])
