import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="The Steals Brothers – Melvin & Mervin Steals Sr.",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Raleway:wght@300;400;500;600;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&display=swap');

:root {
    --gold:    #C9A84C;
    --gold2:   #E8C96C;
    --deep:    #FFFFFF;
    --warm:    #F5F0E8;
    --cream:   #2C2416;
    --muted:   #6B5C3E;
    --accent:  #8B2020;
    --blue:    #2A4A6B;
}

html, body, [data-testid="stApp"] {
    background: #FFFFFF !important;
    color: #2C2416 !important;
}

/* Sidebar hidden */
[data-testid="stSidebar"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }

/* Mobile-first container */
.main .block-container {
    padding: 1rem 1rem 3rem !important;
    max-width: 100% !important;
}

/* Responsive padding for larger screens */
@media (min-width: 640px) {
    .main .block-container {
        padding: 1.5rem 2rem 4rem !important;
        max-width: 900px !important;
    }
}

/* Mobile nav bar */
.mobile-nav {
    position: sticky;
    top: 0;
    z-index: 100;
    background: linear-gradient(135deg, #F5F0E8 0%, #EDE5D0 100%);
    border-bottom: 1px solid rgba(201,168,76,0.35);
    padding: 0.6rem 1rem;
    margin: -1rem -1rem 1.2rem -1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.mobile-nav-brand {
    font-family: 'Playfair Display', serif;
    font-size: 0.95rem;
    font-weight: 900;
    color: #C9A84C;
    line-height: 1.2;
}
.mobile-nav-sub {
    font-family: 'Cormorant Garamond', serif;
    font-size: 0.72rem;
    color: #9A8A6A;
    font-style: italic;
}

h1, h2, h3, h4 {
    font-family: 'Playfair Display', serif !important;
    color: var(--gold) !important;
}
p, li, label, span, div {
    font-family: 'Raleway', sans-serif !important;
}

.gold-hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 1.5rem 0;
}

/* Hero — mobile first */
.hero-banner {
    background: linear-gradient(135deg, #F5F0E8 0%, #EDE5D0 50%, #F5F0E8 100%);
    border: 1px solid rgba(201,168,76,0.4);
    border-radius: 4px;
    padding: 2rem 1rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 1.5rem;
}
@media (min-width: 640px) {
    .hero-banner { padding: 3.5rem 3rem; margin-bottom: 2rem; }
}
.hero-banner::before {
    content: '𝄞';
    position: absolute;
    font-size: 10rem;
    color: rgba(201,168,76,0.04);
    top: -1rem; right: -0.5rem;
    line-height: 1;
}
@media (min-width: 640px) {
    .hero-banner::before { font-size: 18rem; top: -3rem; right: -2rem; }
}
.hero-title {
    font-family: 'Playfair Display', serif !important;
    font-size: clamp(1.55rem, 7vw, 3.2rem) !important;
    font-weight: 900 !important;
    color: var(--gold) !important;
    line-height: 1.15 !important;
    margin-bottom: 0.5rem !important;
    text-shadow: 0 2px 20px rgba(201,168,76,0.3);
}
.hero-subtitle {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(0.9rem, 3.5vw, 1.35rem) !important;
    font-style: italic !important;
    color: var(--cream) !important;
    opacity: 0.85 !important;
    letter-spacing: 0.04em !important;
}
.hero-badge {
    display: inline-block;
    background: var(--accent);
    color: var(--cream) !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.62rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    padding: 0.3rem 0.75rem !important;
    border-radius: 2px;
    margin-bottom: 0.9rem;
}

/* Stat grid — 2 col on mobile, 3 on wider */
.stat-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
    margin: 1.2rem 0;
}
@media (min-width: 480px) {
    .stat-grid { grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 1.5rem 0; }
}
.stat-box {
    background: rgba(201,168,76,0.08);
    border: 1px solid rgba(201,168,76,0.25);
    border-radius: 4px;
    padding: 1.1rem 0.75rem;
    text-align: center;
}
.stat-number {
    font-family: 'Playfair Display', serif !important;
    font-size: clamp(1.5rem, 5vw, 2.4rem) !important;
    font-weight: 900 !important;
    color: var(--gold) !important;
    display: block;
    line-height: 1;
    margin-bottom: 0.35rem;
}
.stat-label {
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.65rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    color: #6B5C3E !important;
}

.pull-quote {
    border-left: 3px solid var(--gold);
    padding: 0.9rem 1.1rem;
    background: rgba(201,168,76,0.07);
    margin: 1.2rem 0;
    border-radius: 0 4px 4px 0;
}
@media (min-width: 640px) {
    .pull-quote { padding: 1.2rem 1.8rem; margin: 2rem 0; }
}
.pull-quote p {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1rem, 3.5vw, 1.3rem) !important;
    font-style: italic !important;
    color: #2C2416 !important;
    margin: 0 !important;
}

.card {
    background: rgba(201,168,76,0.05);
    border: 1px solid rgba(201,168,76,0.2);
    border-radius: 4px;
    padding: 1.1rem;
    margin-bottom: 0.85rem;
}
@media (min-width: 640px) {
    .card { padding: 1.8rem; margin-bottom: 1.2rem; }
}
.card-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.05rem !important;
    color: var(--gold) !important;
    margin-bottom: 0.5rem !important;
}

.timeline-item {
    display: flex;
    gap: 0.75rem;
    margin-bottom: 1.5rem;
    align-items: flex-start;
}
@media (min-width: 480px) {
    .timeline-item { gap: 1.5rem; margin-bottom: 2rem; }
}
.timeline-year {
    font-family: 'Playfair Display', serif !important;
    font-size: clamp(0.85rem, 3vw, 1.5rem) !important;
    font-weight: 900 !important;
    color: var(--gold) !important;
    min-width: 48px;
    text-align: right;
    padding-top: 0.15rem;
}
@media (min-width: 480px) {
    .timeline-year { min-width: 70px; }
}
.timeline-dot {
    width: 12px; height: 12px;
    background: var(--gold);
    border-radius: 50%;
    margin-top: 0.45rem;
    flex-shrink: 0;
    position: relative;
}
.timeline-dot::after {
    content: '';
    position: absolute;
    top: 12px; left: 5px;
    width: 2px; height: 55px;
    background: linear-gradient(to bottom, rgba(201,168,76,0.4), transparent);
}
.timeline-content h4 {
    font-family: 'Playfair Display', serif !important;
    color: #2C2416 !important;
    font-size: 0.98rem !important;
    margin-bottom: 0.3rem !important;
}
.timeline-content p {
    color: rgba(44,36,22,0.75) !important;
    font-size: 0.85rem !important;
    margin: 0 !important;
    line-height: 1.6 !important;
}

/* Buttons — 48px min touch target */
.stButton > button {
    background: linear-gradient(135deg, var(--gold), var(--gold2)) !important;
    color: var(--deep) !important;
    font-family: 'Raleway', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    font-size: 0.88rem !important;
    border: none !important;
    border-radius: 2px !important;
    padding: 0.75rem 1.5rem !important;
    min-height: 48px !important;
    transition: all 0.25s ease !important;
    width: 100% !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    box-shadow: 0 4px 20px rgba(201,168,76,0.4) !important;
}

.section-eyebrow {
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.63rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.25em !important;
    text-transform: uppercase !important;
    color: var(--gold) !important;
    margin-bottom: 0.3rem !important;
}

/* Form inputs — large touch targets */
.stTextInput input, .stTextArea textarea {
    background: #FFFFFF !important;
    border: 1px solid rgba(201,168,76,0.4) !important;
    color: #2C2416 !important;
    border-radius: 2px !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 1rem !important;
    min-height: 44px !important;
}

/* Responsive video embed */
.video-wrapper {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%;
    height: 0;
    overflow: hidden;
    border-radius: 4px;
    margin-bottom: 1rem;
}
.video-wrapper iframe {
    position: absolute;
    top: 0; left: 0;
    width: 100% !important;
    height: 100% !important;
    border: none;
}

/* Section headings */
h1 { font-size: clamp(1.7rem, 6vw, 3rem) !important; }
h3 { font-size: clamp(1.1rem, 4vw, 1.8rem) !important; }

.site-footer {
    border-top: 1px solid rgba(201,168,76,0.2);
    padding-top: 1.5rem;
    margin-top: 3rem;
    text-align: center;
}
.site-footer p {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 0.82rem !important;
    color: var(--muted) !important;
    font-style: italic !important;
}

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #F5F0E8; }
::-webkit-scrollbar-thumb { background: rgba(201,168,76,0.45); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)




# ── Mobile top nav (compact, always visible) ─────────────────────────────────
PAGE_OPTIONS = [
    "🏠  Home",
    "👥  Meet the Twins",
    "👤  About Melvin Steals Sr.",
    "👤  About Mervin Steals Sr.",
    "🎵  With You Jesus — Purchase",
    "📖  Story of With You Jesus",
    "🎼  Legacy & Discography",
    "✉️  Contact & Booking",
]

st.markdown("""
<div style='background:linear-gradient(135deg,#F5F0E8,#EDE5D0);
            border-bottom:1px solid rgba(201,168,76,0.3);
            padding:0.6rem 0 0.2rem;margin-bottom:1rem;text-align:center;'>
    <div style='font-family:"Playfair Display",serif;font-size:1rem;
                font-weight:900;color:#C9A84C;line-height:1.2;'>
        THE STEALS BROTHERS
    </div>
    <div style='font-family:"Cormorant Garamond",serif;font-size:0.75rem;
                color:#9A8A6A;font-style:italic;'>
        Melvin · Mervin · Mystro &amp; Lyric
    </div>
</div>
""", unsafe_allow_html=True)

mobile_page = st.selectbox(
    "Navigate to",
    PAGE_OPTIONS,
    label_visibility="collapsed",
)

page = mobile_page




# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if "Home" in page:
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">Aliquippa, Pennsylvania · Est. 1946</div>
        <div class="hero-title">
            Melvin Steals Sr.
            <span style='font-family:"Cormorant Garamond",serif;font-style:italic;
                         color:rgba(201,168,76,0.6);font-size:2.5rem;margin:0 0.6rem;'>&amp;</span>
            Mervin Steals Sr.
        </div>
        <div class="hero-subtitle">
            <em>Mystro &amp; Lyric</em> — Twin brothers who gave the world a reason to fall in love
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Featured Video ──────────────────────────────────────────────────────────
    st.markdown("""
    <p class="section-eyebrow" style="text-align:center;">Featured</p>
    <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;font-size:1.6rem;
               text-align:center;margin-bottom:1.2rem;'>
        "With You Jesus" — Official Video
    </h3>
    """, unsafe_allow_html=True)

    video_url = "https://www.youtube.com/watch?v=98ajxKlR5Dk"
    video_id = video_url.split("v=")[1]

    st.components.v1.html(
        f'<div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:4px;">'
        f'<iframe src="https://www.youtube.com/embed/{video_id}" '
        f'style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;" '
        f'allow="autoplay; encrypted-media" allowfullscreen></iframe></div>',
        height=320
    )

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <p class="section-eyebrow">Welcome</p>
        <p style='font-family:"Playfair Display",serif;font-size:2.4rem;font-weight:900;
                  color:rgba(44,36,22,0.95);line-height:1.2;margin-bottom:1.2rem;'>
            Two Voices.<br>One Legendary Sound.
        </p>
        <p style='font-family:"Raleway",sans-serif;font-size:1.05rem;
                  color:rgba(44,36,22,0.88);line-height:1.8;'>
        When twins <strong style="color:#C9A84C;">Melvin</strong> and
        <strong style="color:#C9A84C;">Mervin Steals Sr.</strong> walked into Kenny Gamble and
        Leon Huff's Philadelphia offices, they were two broke 22-year-olds from a steel town
        with nothing but talent — and each other. What followed was one of the most remarkable
        songwriting partnerships in American music history.
        </p>
        <p style='font-family:"Raleway",sans-serif;font-size:1.05rem;
                  color:rgba(44,36,22,0.88);line-height:1.8;margin-top:1rem;'>
        Known in the industry as <em style="color:#C9A84C;">Mystro &amp; Lyric</em>, they crafted
        songs that defined Philadelphia Soul. Their most enduring composition,
        <strong style="color:#C9A84C;">"Could It Be I'm Falling in Love"</strong> by The Spinners,
        hit #1 on the R&amp;B chart and has been played over
        <strong style="color:#C9A84C;">4 million</strong> times on American radio.
        </p>
        <p style='font-family:"Raleway",sans-serif;font-size:1.05rem;
                  color:rgba(44,36,22,0.88);line-height:1.8;margin-top:1rem;'>
        In 2021, both brothers received <strong style="color:#C9A84C;">Grammy Awards</strong>
        as co-writers of Kaytranada's "10%" — proof that nearly 50 years in, the Steals Brothers
        are still shaping the sound of popular music. Now Melvin brings that same gift
        to gospel with his heartfelt single,
        <strong style="color:#C9A84C;">"With You Jesus."</strong>
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1rem;'>
            <div style='background:linear-gradient(160deg,rgba(201,168,76,0.10),rgba(201,168,76,0.04));
                        border:1px solid rgba(201,168,76,0.35);border-radius:4px;
                        padding:1.5rem 1rem;text-align:center;'>
                <div style='font-size:3rem;line-height:1;margin-bottom:0.7rem;'>♪</div>
                <div style='font-family:"Playfair Display",serif;font-size:1rem;
                            font-weight:900;color:#C9A84C;'>Melvin</div>
                <div style='font-family:"Cormorant Garamond",serif;font-style:italic;
                            font-size:0.78rem;color:rgba(44,36,22,0.55);margin-top:0.2rem;'>"Lyric"</div>
                <div style='font-family:"Raleway",sans-serif;font-size:0.65rem;
                            text-transform:uppercase;letter-spacing:0.12em;color:#9A8A6A;
                            margin-top:0.5rem;'>Wordsmith</div>
            </div>
            <div style='background:linear-gradient(160deg,rgba(42,74,107,0.10),rgba(42,74,107,0.03));
                        border:1px solid rgba(42,74,107,0.5);border-radius:4px;
                        padding:1.5rem 1rem;text-align:center;'>
                <div style='font-size:3rem;line-height:1;margin-bottom:0.7rem;'>♫</div>
                <div style='font-family:"Playfair Display",serif;font-size:1rem;
                            font-weight:900;color:#C9A84C;'>Mervin</div>
                <div style='font-family:"Cormorant Garamond",serif;font-style:italic;
                            font-size:0.78rem;color:rgba(44,36,22,0.55);margin-top:0.2rem;'>"Mystro"</div>
                <div style='font-family:"Raleway",sans-serif;font-size:0.65rem;
                            text-transform:uppercase;letter-spacing:0.12em;color:#9A8A6A;
                            margin-top:0.5rem;'>Melodist</div>
            </div>
        </div>
        <div style='background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.15);
                    border-radius:4px;padding:1.2rem;text-align:center;'>
            <div style='font-family:"Cormorant Garamond",serif;font-style:italic;
                        font-size:0.95rem;color:rgba(44,36,22,0.75);line-height:1.6;'>
                "Born together. Inseparable in music.<br>
                Two halves of one extraordinary gift."
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    st.markdown("""
    <div class="stat-grid">
        <div class="stat-box">
            <span class="stat-number">100+</span>
            <span class="stat-label">Songs Written &amp; Recorded</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">4M+</span>
            <span class="stat-label">Radio Spins — "Could It Be"</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">47</span>
            <span class="stat-label">Songs Still Played Worldwide</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    st.markdown("""
    <p class="section-eyebrow">Recorded by Legends</p>
    <h3 style='font-family:"Playfair Display",serif;font-size:1.5rem;color:#C9A84C;
               margin-bottom:1.2rem;'>Artists Who Recorded Steals Brothers Classics</h3>
    """, unsafe_allow_html=True)

    artists = [
        ("The Spinners", "Could It Be I'm Falling in Love"),
        ("Gloria Gaynor", "Honey Bee"),
        ("Archie Bell & The Drells", "Go For What You Know"),
        ("The Trammps", "Trusting Heart"),
        ("Blue Magic", "Steals Brothers Composition"),
        ("Harold Melvin & The Blue Notes", "Steals Brothers Composition"),
        ("Donnie Osmond", "Could It Be I'm Falling in Love (cover)"),
        ("Regina Belle", "Could It Be I'm Falling in Love (cover)"),
        ("A$AP Rocky", "Back Home (sample)"),
        ("Mary J. Blige", "Treat 'Em Right (sample)"),
        ("Kaytranada feat. Kali Uchis", "10% — 2021 Grammy Winner"),
        ("The Impressions", "Steals Brothers Composition"),
    ]
    cols = st.columns(3)
    for i, (artist, song) in enumerate(artists):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card" style="padding:1.1rem;">
                <div class="card-title" style="font-size:0.95rem;">{artist}</div>
                <div style='font-family:"Cormorant Garamond",serif;font-style:italic;
                            font-size:0.83rem;color:rgba(44,36,22,0.6);'>{song}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. &amp; Mervin Steals Sr. · The Steals Brothers · All Rights Reserved · Aliquippa, Pennsylvania</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# MEET THE TWINS
# ══════════════════════════════════════════════════════════════════════════════
elif "Meet the Twins" in page:
    st.markdown("""
    <p class="section-eyebrow">Mystro &amp; Lyric</p>
    <h1 style='font-family:"Playfair Display",serif;font-size:3rem;
               color:#C9A84C;margin-bottom:0.3rem;'>Meet the Steals Brothers</h1>
    <p style='font-family:"Cormorant Garamond",serif;font-style:italic;
              color:rgba(44,36,22,0.7);font-size:1.1rem;margin-bottom:2rem;'>
        Twin brothers. Lifelong partners. One vision divided between words and melody.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="pull-quote">
        <p>"Melvin was the wordsmith — Lyric — and Mervin crafted the melodies on piano — Mystro.
        Together they were complete."</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div style='background:linear-gradient(160deg,rgba(201,168,76,0.1),rgba(201,168,76,0.02));
                    border:1px solid rgba(201,168,76,0.35);border-radius:4px;
                    padding:2.5rem;text-align:center;margin-bottom:1rem;'>
            <div style='font-size:5rem;line-height:1;margin-bottom:1rem;'>♪</div>
            <div style='font-family:"Playfair Display",serif;font-size:2rem;
                        font-weight:900;color:#C9A84C;'>Melvin Steals Sr.</div>
            <div style='font-family:"Cormorant Garamond",serif;font-style:italic;
                        font-size:1.1rem;color:rgba(44,36,22,0.7);margin-top:0.3rem;'>
                Known as <strong style="color:#C9A84C;">"Lyric"</strong>
            </div>
            <hr style='border:none;height:1px;
                       background:linear-gradient(90deg,transparent,rgba(201,168,76,0.3),transparent);
                       margin:1.2rem 0;'>
            <div style='font-family:"Raleway",sans-serif;font-size:0.92rem;
                        color:rgba(44,36,22,0.85);line-height:1.7;'>
                The wordsmith of the duo. Melvin had an extraordinary gift for
                lyrics that felt lived-in — because they were. Every line came from
                real life: real love, real faith, real longing.
            </div>
        </div>
        """, unsafe_allow_html=True)

        for icon, fact in [
            ("✍️", "Lyricist — 'Could It Be I'm Falling in Love'"),
            ("❤️", "Inspired by childhood sweetheart Adrena, his wife"),
            ("🏫", "Educator in Aliquippa schools — separate from his music career"),
            ("🙏", "Gospel songwriter — 'With You Jesus'"),
            ("🏆", "Grammy Award Winner, 2021"),
        ]:
            st.markdown(f"""
            <div style='background:rgba(201,168,76,0.05);border:1px solid rgba(201,168,76,0.12);
                        border-radius:3px;padding:0.65rem 1rem;margin-bottom:0.5rem;
                        display:flex;gap:0.75rem;align-items:center;'>
                <span>{icon}</span>
                <span style='font-family:"Raleway",sans-serif;font-size:0.85rem;
                             color:rgba(44,36,22,0.85);'>{fact}</span>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:linear-gradient(160deg,rgba(42,74,107,0.2),rgba(42,74,107,0.04));
                    border:1px solid rgba(42,74,107,0.5);border-radius:4px;
                    padding:2.5rem;text-align:center;margin-bottom:1rem;'>
            <div style='font-size:5rem;line-height:1;margin-bottom:1rem;'>♫</div>
            <div style='font-family:"Playfair Display",serif;font-size:2rem;
                        font-weight:900;color:#C9A84C;'>Mervin Steals Sr.</div>
            <div style='font-family:"Cormorant Garamond",serif;font-style:italic;
                        font-size:1.1rem;color:rgba(44,36,22,0.7);margin-top:0.3rem;'>
                Known as <strong style="color:#C9A84C;">"Mystro"</strong>
            </div>
            <hr style='border:none;height:1px;
                       background:linear-gradient(90deg,transparent,rgba(42,74,107,0.5),transparent);
                       margin:1.2rem 0;'>
            <div style='font-family:"Raleway",sans-serif;font-size:0.92rem;
                        color:rgba(44,36,22,0.85);line-height:1.7;'>
                The melodic architect of the duo. Mervin composed on piano —
                the musical foundation that gave Melvin's words somewhere to live.
                His melodies were immediately memorable, emotional, and undeniably soulful.
            </div>
        </div>
        """, unsafe_allow_html=True)

        for icon, fact in [
            ("🎹", "Pianist & melodist — composer of the duo"),
            ("🎵", "Co-wrote all 100+ Steals Brothers songs"),
            ("🪚", "Skilled carpenter — craftsman beyond the keys"),
            ("⚒️", "Free Mason & Shriner — brotherhood, service, and philanthropy"),
            ("🤝", "Business partner of McKinley Jackson (Marvin Gaye's musical director)"),
            ("📀", "47 songs still played in the world market today"),
            ("🏆", "Grammy Award Winner, 2021"),
        ]:
            st.markdown(f"""
            <div style='background:rgba(42,74,107,0.1);border:1px solid rgba(42,74,107,0.3);
                        border-radius:3px;padding:0.65rem 1rem;margin-bottom:0.5rem;
                        display:flex;gap:0.75rem;align-items:center;'>
                <span>{icon}</span>
                <span style='font-family:"Raleway",sans-serif;font-size:0.85rem;
                             color:rgba(44,36,22,0.85);'>{fact}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    st.markdown("""
    <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;font-size:1.8rem;
               margin-bottom:1rem;text-align:center;'>The Perfect Partnership</h3>
    <p style='font-family:"Raleway",sans-serif;font-size:1rem;color:rgba(44,36,22,0.85);
              line-height:1.8;text-align:center;max-width:700px;margin:0 auto 2rem;'>
        In music, two halves rarely fit as perfectly as words and melody —
        and rarer still are cases where those two halves are literally born together.
        Melvin and Mervin were not just brothers; they were each other's creative completion.
    </p>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for col, icon, title, desc in zip(cols,
        ["🎼", "🏫", "🤝"],
        ["Born as One", "Cheyney State College", "Gamble & Huff"],
        [
            "Twin brothers from Aliquippa, sharing a dream before either had the words for it.",
            "They enrolled together at America's oldest HBCU, where a friendship with Eddie Holman opened the door to Philadelphia's music world.",
            "The legendary producing duo heard something special in the Steals Brothers and immediately put them to work — two halves greater than the sum of their parts.",
        ]
    ):
        with col:
            st.markdown(f"""
            <div class="card" style='padding:1.8rem;text-align:center;'>
                <div style='font-size:2rem;margin-bottom:0.8rem;'>{icon}</div>
                <div style='font-family:"Playfair Display",serif;font-size:1.05rem;
                            color:#C9A84C;margin-bottom:0.7rem;'>{title}</div>
                <div style='font-family:"Raleway",sans-serif;font-size:0.85rem;
                            color:rgba(44,36,22,0.75);line-height:1.6;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. &amp; Mervin Steals Sr. · All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# ABOUT MELVIN
# ══════════════════════════════════════════════════════════════════════════════
elif page == "👤  About Melvin Steals Sr.":
    st.markdown("""
    <p class="section-eyebrow">Biography</p>
    <h1 style='font-family:"Playfair Display",serif;font-size:3rem;
               color:#C9A84C;margin-bottom:0.3rem;'>Melvin Steals Sr.</h1>
    <p style='font-family:"Cormorant Garamond",serif;font-style:italic;
              color:rgba(44,36,22,0.7);font-size:1.1rem;margin-bottom:2rem;'>
        "Lyric" · Wordsmith · Educator · Gospel Songwriter · Grammy Award Winner
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="pull-quote">
            <p>"Could It Be I'm Falling in Love was inspired by my childhood sweetheart Adrena,
            whom I dated as a teenager — and later married."</p>
        </div>
        """, unsafe_allow_html=True)

        for heading, body in [
            ("Early Life in Aliquippa",
             "Melvin Steals Sr. was born and raised in Aliquippa, Pennsylvania — a Beaver County "
             "town on the Ohio River better known for producing NFL Hall of Famers than music legends. "
             "Alongside his twin brother Mervin, Melvin grew up with an innate gift for language and "
             "storytelling that would one day give The Spinners one of the most beloved songs in American R&amp;B history."),
            ("Cheyney State &amp; The Philadelphia Door",
             "After graduating high school in 1964, the twins enrolled at "
             "<strong style='color:#C9A84C;'>Cheyney State College</strong>, America's oldest HBCU, just "
             "outside Philadelphia. They met Eddie Holman and entered the orbit of Kenny Gamble and Leon "
             "Huff — the architects of the Philadelphia Sound. Melvin walked through that door as "
             "<em style='color:#C9A84C;'>Lyric</em>: every word of every Steals Brothers composition "
             "flowed from his pen. He wrote from life, and the love song that became 'Could It Be I'm "
             "Falling in Love' came directly from his romance with "
             "<strong style='color:#C9A84C;'>Adrena</strong>, his childhood sweetheart and wife."),
            ("Educator of Aliquippa",
             "Even as his songs climbed the charts, Melvin returned to Aliquippa and dedicated himself "
             "to education — a career entirely separate from his music. He taught in the local school "
             "system, pouring the same passion for words and meaning into his students that he brought "
             "to his songwriting. Students who sat in his classroom had no idea their teacher's song "
             "was playing on radio stations across the country. His work in education stands on its own "
             "as a defining part of who Melvin Steals Sr. is — a man who shaped young minds just as "
             "surely as he shaped the sound of a generation. Former students remember him decades "
             "later as a warm, gifted man — a wonderful person from their past."),
            ("From Soul to Spirit",
             "Guided by deepening faith, Melvin eventually turned his songwriting toward gospel music. "
             "His song <strong style='color:#C9A84C;'>'With You Jesus'</strong> represents the full arc "
             "of his journey — the man who wrote the anthem for falling in love, now writing about the "
             "deepest love of all."),
        ]:
            st.markdown(f"""
            <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;margin-top:2rem;'>{heading}</h3>
            <p style='font-family:"Raleway",sans-serif;line-height:1.85;
                      color:rgba(44,36,22,0.88);font-size:0.97rem;'>{body}</p>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:linear-gradient(160deg,rgba(201,168,76,0.1),rgba(201,168,76,0.02));
                    border:1px solid rgba(201,168,76,0.35);border-radius:4px;
                    padding:2rem;text-align:center;margin-bottom:1.5rem;'>
            <div style='font-size:4rem;line-height:1;margin-bottom:0.8rem;'>♪</div>
            <div style='font-family:"Playfair Display",serif;font-size:1.4rem;color:#C9A84C;'>Melvin Steals Sr.</div>
            <div style='font-family:"Cormorant Garamond",serif;font-style:italic;
                        color:rgba(44,36,22,0.6);font-size:0.85rem;margin-top:0.3rem;'>
                "Lyric" of Mystro &amp; Lyric
            </div>
        </div>
        """, unsafe_allow_html=True)
        for icon, title, sub in [
            ("🏆","Grammy Award Winner","2021 Best Dance Recording"),
            ("📚","Educator","Taught in Aliquippa Schools — a career apart from music"),
            ("✍️","Lyricist","100+ Recorded Compositions"),
            ("❤️","Love Story","Married childhood sweetheart Adrena"),
            ("🎓","Cheyney State College","America's Oldest HBCU"),
            ("🙏","Gospel Songwriter","'With You Jesus' — man of faith"),
        ]:
            st.markdown(f"""
            <div class="card" style="padding:0.85rem 1.1rem;margin-bottom:0.6rem;">
                <div style='display:flex;align-items:center;gap:0.75rem;'>
                    <span style='font-size:1.2rem;'>{icon}</span>
                    <div>
                        <div style='font-family:"Raleway",sans-serif;font-size:0.82rem;
                                    font-weight:700;color:rgba(44,36,22,0.9);'>{title}</div>
                        <div style='font-family:"Cormorant Garamond",serif;font-size:0.78rem;
                                    font-style:italic;color:#9A8A6A;'>{sub}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. &amp; Mervin Steals Sr. · All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# ABOUT MERVIN
# ══════════════════════════════════════════════════════════════════════════════
elif page == "👤  About Mervin Steals Sr.":
    st.markdown("""
    <p class="section-eyebrow">Biography</p>
    <h1 style='font-family:"Playfair Display",serif;font-size:3rem;
               color:#C9A84C;margin-bottom:0.3rem;'>Mervin Steals Sr.</h1>
    <p style='font-family:"Cormorant Garamond",serif;font-style:italic;
              color:rgba(44,36,22,0.7);font-size:1.1rem;margin-bottom:2rem;'>
        "Mystro" · Melodist &amp; Pianist · Co-writer · Grammy Award Winner · Craftsman · Free Mason &amp; Shriner
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="pull-quote">
            <p>"Mervin crafted the melodies on piano. Without the melody, the words have no home.
            He gave every song its soul."</p>
        </div>
        """, unsafe_allow_html=True)

        for heading, body in [
            ("The Architect of Sound",
             "Mervin Steals Sr. was the musical engine of the Steals Brothers. While twin brother Melvin "
             "brought the poetry of lived experience to the page, Mervin sat at the piano and found the "
             "notes that made those words soar. His melodic instincts were impeccable — the kind of ear "
             "that immediately understood what a singer needed, what a room demanded, and what would "
             "last for decades. Known in the industry as <em style='color:#C9A84C;'>'Mystro,'</em> his "
             "piano compositions were the foundation beneath every Steals Brothers classic."),
            ("Aliquippa to Philadelphia",
             "Born minutes apart from his twin in Aliquippa, Mervin's path mirrored Melvin's step for "
             "step — same house, same school, same enrollment at "
             "<strong style='color:#C9A84C;'>Cheyney State College</strong>, same walk through Gamble "
             "and Huff's door. But at the piano, Mervin was in a world entirely his own. When Thom Bell "
             "heard the brothers' songs on a scouting trip to Pittsburgh, it was the melodic architecture "
             "— Mervin's contribution — that convinced Bell he'd found something truly special."),
            ("McKinley Jackson &amp; The Grammy Years",
             "Mervin's connections in the industry ran deep. His business partnership with "
             "<strong style='color:#C9A84C;'>McKinley Jackson</strong> — Marvin Gaye's own musical "
             "director — speaks to the professional respect he commanded. That partnership paid its "
             "greatest dividend in 2021, when Mervin and Melvin, alongside Jackson, received "
             "<strong style='color:#C9A84C;'>Grammy Awards</strong> as co-writers of Kaytranada's "
             "'10%' featuring Kali Uchis — Best Dance Recording of 2020. Nearly fifty years after "
             "their first hit, the Steals Brothers were still at the very top."),
            ("Craftsman &amp; Carpenter",
             "Beyond music, Mervin Steals Sr. is a skilled carpenter — a man who builds with his hands "
             "as naturally as he composes at the piano. The same precision, patience, and craftsmanship "
             "that define his melodies are evident in his woodwork. It is a reminder that true artistry "
             "takes many forms, and that Mervin has always been a builder — of songs, of friendships, "
             "and of things that last."),
            ("Free Mason &amp; Shriner",
             "Mervin is a proud member of the <strong style='color:#C9A84C;'>Free Masons</strong>, "
             "one of the world's oldest fraternal organizations, built on the pillars of brotherhood, "
             "charity, and moral integrity. He is also a <strong style='color:#C9A84C;'>Shriner</strong> "
             "— a member of Shriners International, which is itself a part of the Free Masons. "
             "The Shriners are known widely for their philanthropic work, particularly their support "
             "of children's hospitals and medical care. Mervin's membership in both reflects the same "
             "values that have defined his life: service, community, and a deep commitment to "
             "lifting others up."),
            ("A Legacy of Melody",
             "Of the 100+ songs the Steals Brothers wrote, 47 continue to be played in the world market. "
             "Every one of those 47 carries Mervin's melodies. When a DJ drops 'Could It Be I'm Falling "
             "in Love' on a dance floor today, Mervin's piano lines are the reason the room stops and "
             "sways. That is the mark of true musicianship: melodies that outlive the moment they were born in."),
        ]:
            st.markdown(f"""
            <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;margin-top:2rem;'>{heading}</h3>
            <p style='font-family:"Raleway",sans-serif;line-height:1.85;
                      color:rgba(44,36,22,0.88);font-size:0.97rem;'>{body}</p>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:linear-gradient(160deg,rgba(42,74,107,0.2),rgba(42,74,107,0.04));
                    border:1px solid rgba(42,74,107,0.5);border-radius:4px;
                    padding:2rem;text-align:center;margin-bottom:1.5rem;'>
            <div style='font-size:4rem;line-height:1;margin-bottom:0.8rem;'>♫</div>
            <div style='font-family:"Playfair Display",serif;font-size:1.4rem;color:#C9A84C;'>Mervin Steals Sr.</div>
            <div style='font-family:"Cormorant Garamond",serif;font-style:italic;
                        color:rgba(44,36,22,0.6);font-size:0.85rem;margin-top:0.3rem;'>
                "Mystro" of Mystro &amp; Lyric
            </div>
        </div>
        """, unsafe_allow_html=True)
        for icon, title, sub in [
            ("🏆","Grammy Award Winner","2021 Best Dance Recording"),
            ("🎹","Pianist & Melodist","The musical architect of the duo"),
            ("🪚","Carpenter","Skilled craftsman — builder with hands and heart"),
            ("⚒️","Free Mason","Member of the Free Masons fraternal brotherhood"),
            ("🌙","Shriner","Shriners International — Free Masons · Children's philanthropy"),
            ("📀","Co-Composer","100+ recorded songs worldwide"),
            ("🤝","Business Partner","McKinley Jackson — Marvin Gaye's musical director"),
            ("🎓","Cheyney State College","America's Oldest HBCU"),
            ("🎵","47 Songs","Still played in the world market today"),
        ]:
            st.markdown(f"""
            <div style='background:rgba(42,74,107,0.08);border:1px solid rgba(42,74,107,0.3);
                        border-radius:3px;padding:0.85rem 1.1rem;margin-bottom:0.6rem;
                        display:flex;align-items:center;gap:0.75rem;'>
                <span style='font-size:1.2rem;'>{icon}</span>
                <div>
                    <div style='font-family:"Raleway",sans-serif;font-size:0.82rem;
                                font-weight:700;color:rgba(44,36,22,0.9);'>{title}</div>
                    <div style='font-family:"Cormorant Garamond",serif;font-size:0.78rem;
                                font-style:italic;color:#9A8A6A;'>{sub}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. &amp; Mervin Steals Sr. · All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PURCHASE
# ══════════════════════════════════════════════════════════════════════════════
elif "Purchase" in page:
    st.markdown("""
    <p class="section-eyebrow">New Release</p>
    <h1 style='font-family:"Playfair Display",serif;font-size:3rem;
               color:#C9A84C;margin-bottom:0.3rem;'>With You Jesus</h1>
    <p style='font-family:"Cormorant Garamond",serif;font-style:italic;
              color:rgba(44,36,22,0.7);font-size:1.1rem;margin-bottom:2rem;'>
        The new gospel single by Melvin Steals Sr. — co-writer of "Could It Be I'm Falling in Love"
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("""
        <div style='background:linear-gradient(135deg,#F5F0E8,#EDE5D0,#F5F0E8);
                    border:1px solid rgba(201,168,76,0.4);border-radius:6px;
                    padding:3rem 2rem;text-align:center;margin-bottom:1rem;
                    box-shadow:0 12px 50px rgba(201,168,76,0.15);'>
            <div style='font-size:5rem;line-height:1;margin-bottom:1rem;'>✝</div>
            <div style='font-family:"Playfair Display",serif;font-size:2rem;
                        font-weight:900;color:#C9A84C;line-height:1.15;'>
                With You<br>Jesus
            </div>
            <div style='font-family:"Cormorant Garamond",serif;font-size:0.95rem;
                        font-style:italic;color:rgba(44,36,22,0.6);margin-top:0.7rem;'>
                Melvin Steals Sr.
            </div>
            <div style='font-family:"Cormorant Garamond",serif;font-size:0.78rem;
                        font-style:italic;color:rgba(44,36,22,0.4);margin-top:0.3rem;'>
                of The Steals Brothers · Mystro &amp; Lyric
            </div>
            <div style='margin-top:1.5rem;padding:0.4rem 1rem;
                        border:1px solid rgba(201,168,76,0.4);border-radius:20px;
                        font-family:"Raleway",sans-serif;font-size:0.7rem;
                        font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#C9A84C;'>
                Gospel Single
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:linear-gradient(135deg,#F5F0E8,#EDE5D0);
                    border:1px solid #C9A84C;border-radius:6px;padding:2.5rem;
                    text-align:center;box-shadow:0 8px 40px rgba(201,168,76,0.12);'>
            <div style='font-family:"Raleway",sans-serif;font-size:0.68rem;
                        letter-spacing:0.25em;text-transform:uppercase;color:#9A8A6A;
                        margin-bottom:0.5rem;'>Digital Download</div>
            <div style='font-family:"Playfair Display",serif;font-size:1.8rem;
                        font-weight:900;color:#C9A84C;margin-bottom:0.3rem;'>
                "With You Jesus"
            </div>
            <div style='font-family:"Cormorant Garamond",serif;font-size:1rem;
                        font-style:italic;color:rgba(44,36,22,0.65);margin-bottom:1.5rem;'>
                by Melvin Steals Sr.
            </div>
            <div style='font-family:"Playfair Display",serif;font-size:3rem;
                        font-weight:900;color:#C9A84C;'>$1.29</div>
            <div style='font-family:"Raleway",sans-serif;font-size:0.78rem;
                        color:#9A8A6A;margin-bottom:1.8rem;'>
                MP3 · High Quality · Instant Download
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🎵  Purchase & Download — $1.29", use_container_width=True):
            st.success("Thank you! Your download link will arrive by email. God bless you! 🙏")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div style='text-align:center;margin-bottom:0.8rem;'>
            <span style='font-family:"Raleway",sans-serif;font-size:0.68rem;
                         letter-spacing:0.2em;text-transform:uppercase;color:#9A8A6A;'>
                Also Available On
            </span>
        </div>
        """, unsafe_allow_html=True)

        for icon, name, url in [
            ("🎵","Apple Music","https://music.apple.com/us/album/with-you-jesus-philly-mix-single/1874032863"),
            ("🟢","Spotify","https://open.spotify.com/album/1XoeZnbaHFVmTAqooppyIG"),
            ("▶️","YouTube Music",""),
            ("📀","Amazon Music",""),
        ]:
            if url:
                st.markdown(f"""
                <a href="{url}" target="_blank" style="text-decoration:none;">
                <div style='background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.2);
                            border-radius:4px;padding:0.7rem 1.2rem;margin-bottom:0.5rem;
                            display:flex;align-items:center;gap:0.8rem;cursor:pointer;
                            transition:background 0.2s;'>
                    <span style='font-size:1.1rem;'>{icon}</span>
                    <span style='font-family:"Raleway",sans-serif;font-size:0.88rem;
                                 font-weight:600;color:rgba(44,36,22,0.85);'>{name}</span>
                    <span style='margin-left:auto;font-family:"Raleway",sans-serif;
                                 font-size:0.75rem;color:#C9A84C;font-weight:600;'>Stream →</span>
                </div>
                </a>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style='background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.2);
                            border-radius:4px;padding:0.7rem 1.2rem;margin-bottom:0.5rem;
                            display:flex;align-items:center;gap:0.8rem;'>
                    <span style='font-size:1.1rem;'>{icon}</span>
                    <span style='font-family:"Raleway",sans-serif;font-size:0.88rem;
                                 font-weight:600;color:rgba(44,36,22,0.85);'>{name}</span>
                    <span style='margin-left:auto;font-family:"Raleway",sans-serif;
                                 font-size:0.75rem;color:#9A8A6A;'>Stream →</span>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
        <div style='margin-top:1.5rem;padding:1rem;background:rgba(201,168,76,0.06);
                    border-radius:4px;border:1px solid rgba(201,168,76,0.12);'>
            <div style='font-family:"Raleway",sans-serif;font-size:0.72rem;
                        font-weight:700;letter-spacing:0.15em;text-transform:uppercase;
                        color:#C9A84C;margin-bottom:0.5rem;'>What You Get</div>
            <div style='font-family:"Raleway",sans-serif;font-size:0.85rem;
                        color:rgba(44,36,22,0.8);line-height:1.8;'>
                ✓ High-quality MP3 (320kbps)<br>
                ✓ Instant digital delivery<br>
                ✓ Personal use license<br>
                ✓ Direct support to the artist
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    st.markdown("""
    <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;
               font-size:1.6rem;margin-bottom:1rem;'>Church &amp; Ministry Licensing</h3>
    """, unsafe_allow_html=True)

    cols = st.columns(3, gap="medium")
    for col, title, price, desc in zip(cols,
        ["Personal","Church / Small Ministry","Large Organization"],
        ["$1.29","$25","$75"],
        [
            "Single download for personal listening and devotion.",
            "Licensed for worship services, bulletins & events (up to 200 members).",
            "Broadcast rights, large congregations, conference use.",
        ]
    ):
        with col:
            st.markdown(f"""
            <div class="card" style='text-align:center;padding:1.8rem;'>
                <div style='font-family:"Raleway",sans-serif;font-size:0.68rem;
                            letter-spacing:0.2em;text-transform:uppercase;
                            color:#9A8A6A;margin-bottom:0.5rem;'>{title}</div>
                <div style='font-family:"Playfair Display",serif;font-size:2.2rem;
                            font-weight:900;color:#C9A84C;margin-bottom:0.6rem;'>{price}</div>
                <div style='font-family:"Raleway",sans-serif;font-size:0.83rem;
                            color:rgba(44,36,22,0.72);line-height:1.6;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. &amp; Mervin Steals Sr. · All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# STORY OF WITH YOU JESUS
# ══════════════════════════════════════════════════════════════════════════════
elif "Story" in page:
    st.markdown("""
    <p class="section-eyebrow">Behind the Music</p>
    <h1 style='font-family:"Playfair Display",serif;font-size:3rem;
               color:#C9A84C;margin-bottom:0.3rem;'>The Story of<br>"With You Jesus"</h1>
    <p style='font-family:"Cormorant Garamond",serif;font-style:italic;
              color:rgba(44,36,22,0.7);font-size:1.1rem;margin-bottom:2rem;'>
        From Philadelphia Soul to Gospel grace — a songwriter's final, finest truth
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="pull-quote">
        <p>"Mervin gave me the melody. God gave me the words. This song belongs to both of them."</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        for heading, body in [
            ("A Partnership That Spans Decades",
             "When Melvin and Mervin Steals wrote <em style='color:#C9A84C;'>'Could It Be I'm "
             "Falling in Love'</em> in 1972, they were drawing from the deepest wells: Melvin's "
             "words came from his real-life love for Adrena, and Mervin's melody carried them "
             "into eternity. That authenticity — writing from the depths of lived experience — "
             "became the hallmark of everything the brothers created together."),
            ("The Inspiration",
             "<strong style='color:#C9A84C;'>'With You Jesus'</strong> was born from a place of "
             "quiet reflection and profound gratitude. Decades of songwriting, chart success, and "
             "Grammy recognition — and through it all, a faith that never wavered. Melvin felt a "
             "growing call to use his pen not just to celebrate romantic love, but the transformative "
             "love he found in Jesus Christ. The same partnership that produced 'Could It Be' — "
             "words and melody, Melvin and Mervin — echoes in this gospel song."),
            ("A Legacy Fulfilled",
             "For Melvin, <em style='color:#C9A84C;'>'With You Jesus'</em> is not a departure "
             "from the Steals Brothers' legacy — it is its fulfillment. The craft that made "
             "'Could It Be I'm Falling in Love' an enduring classic is present in every measure: "
             "the hook, the heart, the honesty. For those who grew up hearing 'Could It Be' — "
             "perhaps even over the morning announcements at Aliquippa Junior High — this song "
             "offers something just as true: love in its highest form is always worth singing about."),
        ]:
            st.markdown(f"""
            <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;margin-top:1.5rem;'>{heading}</h3>
            <p style='font-family:"Raleway",sans-serif;line-height:1.85;
                      color:rgba(44,36,22,0.88);font-size:0.97rem;'>{body}</p>
            """, unsafe_allow_html=True)

    with col2:
        themes = [
            ("Faith", "Trust in God's constant presence"),
            ("Grace", "Peace found through surrender"),
            ("Gratitude", "Thankfulness for a life well-lived"),
            ("Legacy", "Leaving a spiritual inheritance"),
            ("Brotherhood", "The twins' enduring musical bond"),
            ("Love", "The highest love — divine and unconditional"),
        ]
        st.markdown("""
        <div style='background:rgba(201,168,76,0.07);border:1px solid rgba(201,168,76,0.2);
                    border-radius:4px;padding:1.8rem;margin-bottom:1.5rem;'>
            <div style='font-family:"Raleway",sans-serif;font-size:0.68rem;letter-spacing:0.2em;
                        text-transform:uppercase;color:#9A8A6A;margin-bottom:1rem;'>Song Themes</div>
        """, unsafe_allow_html=True)
        for theme, desc in themes:
            st.markdown(f"""
            <div style='border-left:2px solid #C9A84C;padding:0.6rem 1rem;margin-bottom:0.8rem;'>
                <div style='font-family:"Playfair Display",serif;font-size:0.95rem;
                            color:#C9A84C;font-weight:700;'>{theme}</div>
                <div style='font-family:"Cormorant Garamond",serif;font-size:0.82rem;
                            font-style:italic;color:rgba(44,36,22,0.65);'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style='text-align:center;padding:2rem;'>
            <div style='font-size:2.5rem;margin-bottom:0.8rem;'>✝</div>
            <div style='font-family:"Playfair Display",serif;font-size:1.3rem;
                        color:#C9A84C;font-style:italic;line-height:1.4;'>
                "With You Jesus"
            </div>
            <div style='font-family:"Cormorant Garamond",serif;font-size:0.85rem;
                        color:rgba(44,36,22,0.6);margin-top:0.5rem;font-style:italic;'>
                Melvin Steals Sr.
            </div>
            <div style='margin-top:1rem;font-family:"Cormorant Garamond",serif;
                        font-size:0.78rem;font-style:italic;color:rgba(44,36,22,0.4);'>
                Born from the same spirit that wrote<br>"Could It Be I'm Falling in Love"
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    st.markdown("""
    <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;font-size:1.6rem;
               margin-bottom:1.5rem;'>In Their Own Words</h3>
    """, unsafe_allow_html=True)

    quotes = [
        ("Melvin — On Writing", "When you write from truth, the song writes itself. I've always written from life."),
        ("Mervin — On Melody", "The melody comes first, then the words find their home. That's always been our process."),
        ("Melvin — On Faith", "Music can take you to the mountaintop, but only faith can keep you there."),
        ("Both — On Legacy", "We want people to hear these songs fifty years from now the same way they still hear 'Could It Be' today."),
    ]
    cols = st.columns(2)
    for i, (label, quote) in enumerate(quotes):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card" style='padding:1.6rem;'>
                <div style='font-family:"Raleway",sans-serif;font-size:0.65rem;
                            letter-spacing:0.2em;text-transform:uppercase;
                            color:#C9A84C;margin-bottom:0.6rem;'>{label}</div>
                <div style='font-family:"Cormorant Garamond",serif;font-size:1.1rem;
                            font-style:italic;color:rgba(44,36,22,0.88);
                            line-height:1.6;'>"{quote}"</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. &amp; Mervin Steals Sr. · All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# LEGACY & DISCOGRAPHY
# ══════════════════════════════════════════════════════════════════════════════
elif "Legacy" in page:
    st.markdown("""
    <p class="section-eyebrow">The Catalog</p>
    <h1 style='font-family:"Playfair Display",serif;font-size:3rem;
               color:#C9A84C;margin-bottom:0.3rem;'>Legacy &amp; Discography</h1>
    <p style='font-family:"Cormorant Garamond",serif;font-style:italic;
              color:rgba(44,36,22,0.7);font-size:1.1rem;margin-bottom:2rem;'>
        The Steals Brothers — five decades of music that shaped American soul, R&amp;B, and gospel
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    st.markdown("""
    <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;
               font-size:1.8rem;margin-bottom:1.5rem;'>A Shared Life in Music</h3>
    """, unsafe_allow_html=True)

    timeline = [
        ("1946", "Born in Aliquippa, PA", "Twin brothers Melvin and Mervin Steals are born on February 9, 1946 and raised in Aliquippa — a Beaver County mill town on the Ohio River."),
        ("1964", "Cheyney State College", "The twins enroll together at America's oldest HBCU. They meet Eddie Holman, who opens the door to Philadelphia's music world."),
        ("Early 70s", "Gamble & Huff Discovery", "As 22-year-old struggling songwriters, Melvin and Mervin walk through Kenny Gamble and Leon Huff's door. They are immediately put to work writing for Archie Bell & The Drells."),
        ("1972", '"I\'m Not Strong Enough"', "The brothers record their first single as The Four Perfections — a UK Northern Soul collector's item. Pristine copies now sell for up to $1,000."),
        ("1972", "Thom Bell Hears Seven Songs", "On a Pittsburgh scouting trip, Thom Bell hears seven Steals Brothers songs and agrees to find artists to record them. One is destined for history."),
        ("Dec 1972", '"Could It Be I\'m Falling in Love"', "Melvin (Lyric) writes the words; Mervin (Mystro) composes the melody. Thom Bell produces it for The Spinners at Sigma Sound Studios with MFSB. A gold record is born."),
        ("1973", "#1 R&B · #4 Billboard · Gold", "The song peaks at #1 R&B, #4 Billboard Hot 100, and sells over a million copies. The Steals Brothers — Mystro & Lyric — are legends."),
        ("1974", '"Honey Bee" — Gloria Gaynor', "Their composition becomes a successful single for future disco queen Gloria Gaynor, showing the breadth of the brothers' musical range."),
        ("70s–80s", "Prolific Catalog", "The twins write 100+ songs for Blue Magic, Harold Melvin & The Blue Notes, The Trammps, O.C. Smith, The Impressions, Eddie Kendricks, and many more."),
        ("80s–90s", "Educator, Craftsman &amp; Community", "Melvin teaches in the Aliquippa school system — a calling entirely his own, apart from the music. Mervin deepens his business partnership with McKinley Jackson, while also practicing his craft as a skilled carpenter."),
        ("2021", "Grammy Award — Best Dance Recording", "Melvin, Mervin, and McKinley Jackson receive Grammy Awards as co-writers of \"10%\" by Kaytranada feat. Kali Uchis. Nearly 50 years in — still at the top."),
        ("2020s", '"With You Jesus" — Melvin Steals Sr.', "Melvin releases his gospel single, channeling a lifetime of faith, music, and brotherhood into a song of spiritual devotion."),
    ]

    for year, title, desc in timeline:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-year">{year}</div>
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    st.markdown("""
    <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;
               font-size:1.8rem;margin-bottom:1.5rem;'>Notable Compositions</h3>
    """, unsafe_allow_html=True)

    songs = [
        ("Could It Be I'm Falling in Love", "The Spinners", "1972", "#1 R&B · #4 Billboard · Gold"),
        ("Honey Bee", "Gloria Gaynor", "1974", "Top 40 Hit"),
        ("Trusting Heart", "The Trammps", "1970s", "Philly Soul Staple"),
        ("Go For What You Know", "Archie Bell & The Drells", "Early 70s", "B-Side Hit"),
        ("I'm Not Strong Enough", "The Four Perfections", "1972", "UK Northern Soul Classic — $1,000 Collector's Copy"),
        ("10% (co-write)", "Kaytranada ft. Kali Uchis", "2020", "Grammy Award — Best Dance Recording 2021"),
        ("Back Home (sample)", "A$AP Rocky", "2010s", "Hip-Hop Sample"),
        ("Treat 'Em Right (sample)", "Mary J. Blige", "1990s", "R&B/Hip-Hop Sample"),
        ("With You Jesus", "Melvin Steals Sr.", "2020s", "Gospel Single — Available Now"),
    ]

    header_cols = st.columns([3, 3, 1, 3])
    for col, label in zip(header_cols, ["Song", "Artist", "Year", "Notes"]):
        with col:
            st.markdown(f"""<div style='font-family:"Raleway",sans-serif;font-size:0.68rem;
                letter-spacing:0.18em;text-transform:uppercase;color:#C9A84C;
                padding-bottom:0.5rem;border-bottom:1px solid rgba(201,168,76,0.3);
                display:none;'>
                {label}</div>""", unsafe_allow_html=True)

    # Mobile-friendly card layout for songs
    for song, artist, year, notes in songs:
        st.markdown(f"""
        <div style='background:rgba(201,168,76,0.04);border:1px solid rgba(201,168,76,0.18);
                    border-radius:4px;padding:0.85rem 1rem;margin-bottom:0.55rem;'>
            <div style='display:flex;justify-content:space-between;align-items:baseline;
                        gap:0.5rem;flex-wrap:wrap;margin-bottom:0.2rem;'>
                <span style='font-family:"Playfair Display",serif;font-size:0.95rem;
                             color:rgba(44,36,22,0.92);font-weight:700;'>{song}</span>
                <span style='font-family:"Raleway",sans-serif;font-size:0.78rem;
                             color:#C9A84C;font-weight:700;flex-shrink:0;'>{year}</span>
            </div>
            <div style='font-family:"Raleway",sans-serif;font-size:0.85rem;
                        color:rgba(44,36,22,0.7);margin-bottom:0.2rem;'>{artist}</div>
            <div style='font-family:"Cormorant Garamond",serif;font-size:0.82rem;
                        font-style:italic;color:rgba(44,36,22,0.55);'>{notes}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. &amp; Mervin Steals Sr. · The Steals Brothers · All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════════════════════
elif "Contact" in page:
    st.markdown("""
    <p class="section-eyebrow">Get in Touch</p>
    <h1 style='font-family:"Playfair Display",serif;font-size:3rem;
               color:#C9A84C;margin-bottom:0.3rem;'>Contact &amp; Booking</h1>
    <p style='font-family:"Cormorant Garamond",serif;font-style:italic;
              color:rgba(44,36,22,0.7);font-size:1.1rem;margin-bottom:2rem;'>
        For bookings, licensing, media inquiries, and ministry partnerships
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <h3 style='font-family:"Playfair Display",serif;color:#C9A84C;margin-bottom:1rem;'>
            Send a Message</h3>
        """, unsafe_allow_html=True)

        name = st.text_input("Full Name *", placeholder="Your name")
        email = st.text_input("Email Address *", placeholder="your@email.com")
        recipient = st.selectbox(
            "Who are you contacting? *",
            ["Select...", "Melvin Steals Sr.", "Mervin Steals Sr.", "Both / The Steals Brothers"],
        )
        subject = st.selectbox(
            "Subject *",
            ["Select a topic...", "Booking / Live Performance", "Song Licensing",
             "Media / Press Inquiry", "Ministry Partnership", "Purchase Support", "General Message"],
        )
        message = st.text_area("Your Message *", placeholder="Write your message here...", height=150)

        col_btn, _ = st.columns([1, 3])
        with col_btn:
            if st.button("Send Message →", use_container_width=True):
                if name and email and message and subject != "Select a topic..." and recipient != "Select...":
                    st.success(f"✓ Message sent to {recipient}! We'll be in touch within 2–3 business days. God bless you!")
                else:
                    st.warning("Please fill in all required fields before sending.")

    with col2:
        st.markdown("""
        <div class="card" style='padding:2rem;margin-bottom:1.2rem;'>
            <div style='font-family:"Playfair Display",serif;font-size:1.2rem;
                        color:#C9A84C;margin-bottom:1.2rem;'>Contact Details</div>
        """, unsafe_allow_html=True)

        for icon, label, val in [
            ("📍","Location","Aliquippa, Pennsylvania"),
            ("🎤","Bookings","Melvin & Mervin available for speaking engagements, gospel concerts & ministry events"),
            ("📜","Licensing","Song licensing for churches, media & commercial use"),
            ("📰","Press","Media kits and interviews available on request"),
        ]:
            st.markdown(f"""
            <div style='display:flex;gap:1rem;margin-bottom:1rem;align-items:flex-start;'>
                <span style='font-size:1.2rem;padding-top:0.1rem;'>{icon}</span>
                <div>
                    <div style='font-family:"Raleway",sans-serif;font-size:0.68rem;
                                letter-spacing:0.15em;text-transform:uppercase;color:#9A8A6A;'>{label}</div>
                    <div style='font-family:"Raleway",sans-serif;font-size:0.87rem;
                                color:rgba(44,36,22,0.85);margin-top:0.2rem;line-height:1.5;'>{val}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style='padding:1.8rem;text-align:center;'>
            <div style='font-family:"Playfair Display",serif;font-size:1.1rem;
                        color:#C9A84C;margin-bottom:0.6rem;'>
                The Steals Brothers — Speaking &amp; Ministry
            </div>
            <p style='font-family:"Raleway",sans-serif;font-size:0.85rem;
                      color:rgba(44,36,22,0.75);line-height:1.6;margin-bottom:1rem;'>
            Together and individually, Melvin and Mervin are available to share
            their remarkable story — two twins from a steel town who wrote the
            soundtrack to a generation, and never forgot where they came from.
            </p>
            <div style='font-family:"Cormorant Garamond",serif;font-style:italic;
                        color:#C9A84C;font-size:0.9rem;'>
                "Born together. Still singing together."
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. &amp; Mervin Steals Sr. · The Steals Brothers · All Rights Reserved · Aliquippa, Pennsylvania</p>
    </div>
    """, unsafe_allow_html=True)
